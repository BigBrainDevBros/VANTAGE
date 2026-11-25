"""Check tracked repository files and repair unambiguous Markdown issues."""

import argparse
import os
from pathlib import Path
import posixpath
import re
import subprocess
import sys
from urllib.parse import quote, unquote, urlsplit


SUBJECT = re.compile(r"[a-z]+: [a-z0-9]+ [a-z0-9]+ [a-z0-9]+")
FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.+)")
INLINE_CODE = re.compile(r"(`+).*?\1")
EMOJI = re.compile(r"[\U0001f1e6-\U0001f1ff\U0001f300-\U0001faff\u2600-\u27bf\ufe0f]|"
                   r"(?<![\w:/]):[a-z0-9_+-]+:(?![\w/])")
LINK = re.compile(r"(\]\(\s*<?|^\s{0,3}\[[^\]]+\]:\s*<?|<(?=https?://)"
                  r"|(?<![\w/<])(?=https?://))([^\s<>()]+)")
BINARY = re.compile(r"\.(?:dmg|pkg|zip|tar\.gz|app|exe|msi|apk|deb|rpm|bin|iso|7z|tgz)$", re.I)
REQUIRED = {
    ".gitignore", "readme.md", "changelog.md", "security.md", "license",
    ".github/ISSUE_TEMPLATE/bug_report.md", ".github/pull_request_template.md",
}


def git(*args):
    return subprocess.check_output(["git", *args])


def check_markdown(path, paths, folded, fix):
    original = Path(path).read_bytes()
    source = original.decode("utf-8")
    if "\0" in source:
        return [f"{path}: expected a UTF-8 Markdown text file"]
    lines = source.splitlines(keepends=True)
    problems = []
    fence = ""
    previous = ""
    frontmatter = (
        bool(lines) and lines[0].strip() == "---"
        and any(line.strip() in ("---", "...") for line in lines[1:])
    )
    for number, line in enumerate(lines, 1):
        if frontmatter:
            if number > 1 and line.strip() in ("---", "..."):
                frontmatter = False
            continue
        marker = FENCE.match(line)
        if marker:
            delimiter = marker[1]
            if not fence:
                fence = delimiter
            elif (delimiter.startswith(fence)
                  and not line[marker.end():].strip()):
                fence = ""
            previous = ""
            continue
        if fence or line.startswith(("    ", "\t")):
            previous = ""
            continue

        def report(message):
            problems.append(f"{path}:{number}: {message}")

        prose = INLINE_CODE.sub(lambda match: " " * len(match[0]), line)
        if EMOJI.search(prose):
            report("remove emoji from Markdown prose")
        heading = HEADING.match(prose)
        title = heading[1] if heading else ""
        if previous and re.fullmatch(r"\s{0,3}(?:=+|-+)\s*", prose):
            title = previous
        if re.search(r"\b[a-z][a-z]+\b", title):
            report("use Title Case in the heading")
        previous = prose.strip()

        replacements = []
        for match in LINK.finditer(prose):
            target = match[2]
            if not match[1] or match[1] == "<":
                target = target.rstrip(".,;")
            try:
                url = urlsplit(target)
            except ValueError:
                report(f"invalid link: {target}")
                continue
            pathname = unquote(url.path)
            if url.scheme == "file" or (not url.scheme and not url.netloc and pathname.startswith("/")):
                report(f"use a repository-relative link: {target}")
            if BINARY.search(pathname):
                report(f"use a release page for binary downloads: {target}")
            if url.scheme or url.netloc or not pathname or pathname.startswith("/"):
                continue
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(path), pathname))
            if resolved in paths:
                continue
            matches = folded.get(resolved.casefold(), [])
            if fix and len(matches) == 1:
                relative = posixpath.relpath(matches[0], posixpath.dirname(path) or ".")
                encoded = quote(relative, safe="/-._~")
                if pathname.endswith("/"):
                    encoded += "/"
                replacements.append((match.start(2), match.start(2) + len(url.path), encoded))
            else:
                report(f"missing or incorrectly cased link target: {target}")
        for start, end, replacement in reversed(replacements):
            line = line[:start] + replacement + line[end:]
        lines[number - 1] = line

    updated = "".join(lines)
    if updated and not updated.endswith("\n"):
        if fix:
            updated += "\r\n" if "\r\n" in updated else "\n"
        else:
            problems.append(f"{path}: add a final newline")
    if fix and updated != source:
        Path(path).write_bytes(updated.encode("utf-8"))
    return problems


def check_files(fix):
    entries = git("ls-files", "--stage", "-z").split(b"\0")
    tracked = {}
    for entry in filter(None, entries):
        metadata, name = entry.split(b"\t", 1)
        tracked[os.fsdecode(name)] = metadata.split()[0]

    paths = set(tracked)
    for name in tracked:
        paths.update(str(parent) for parent in Path(name).parents)
    folded = {}
    for name in paths:
        folded.setdefault(name.casefold(), []).append(name)

    problems = [f"missing required file: {name}" for name in sorted(REQUIRED - tracked.keys())]
    for path in sorted(tracked):
        name = path.removeprefix(".github/ISSUE_TEMPLATE/")
        if any(not re.fullmatch(r"[a-z0-9._-]+", part) for part in name.split("/")):
            problems.append(f"{path}: use lowercase path components")
        if len(folded[path.casefold()]) > 1:
            problems.append(f"{path}: tracked paths collide on case-insensitive filesystems")
        if not path.lower().endswith(".md"):
            continue
        if tracked[path] not in (b"100644", b"100755") or Path(path).is_symlink():
            problems.append(f"{path}: Markdown must be a regular tracked file")
            continue
        try:
            problems.extend(check_markdown(path, paths, folded, fix))
        except (OSError, UnicodeError) as error:
            problems.append(f"{path}: {error}")
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fix", action="store_true", help="repair safe Markdown issues")
    parser.add_argument("--base", help="check commit subjects after this Git revision")
    args = parser.parse_args()
    os.chdir(os.fsdecode(git("rev-parse", "--show-toplevel").rstrip(b"\n")))
    problems = check_files(args.fix)
    if args.base:
        base = git("rev-parse", "--verify", "--end-of-options", f"{args.base}^{{commit}}").strip().decode()
        commits = git("log", "--format=%h%x00%s", f"{base}..HEAD").decode()
        for commit in commits.splitlines():
            sha, subject = commit.split("\0", 1)
            if not SUBJECT.fullmatch(subject):
                problems.append(f"{sha}: invalid commit subject: {subject}")
    for problem in problems:
        # Keep contributor text from being interpreted as a workflow command.
        print(f"Compliance: {problem}", file=sys.stderr)
    return bool(problems) and not args.fix


if __name__ == "__main__":
    sys.exit(main())
