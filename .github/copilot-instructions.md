# VANTAGE Repository Instructions

- VANTAGE distributes a single static game in `index.html`. The editable game source is maintained separately. Preserve embedded third-party notices and the contributor attribution in `credits.md`.
- Follow the BigBrainDevBros [Template](https://github.com/BigBrainDevBros/.github/blob/main/template.md) and [Checklist](https://github.com/BigBrainDevBros/.github/blob/main/check.md).
- Use lowercase tracked paths. GitHub's issue template directory is `.github/ISSUE_TEMPLATE/`.
- Use Title Case headings, plain text statuses, and repository-relative links. Keep Markdown emoji-free and link to release pages for downloads.
- Use a lowercase commit prefix and exactly three lowercase alphanumeric words after the colon. Example: `docs: update gameplay guide`.
- Run `python3 scripts/check-repository.py` before submitting changes. Smoke-test gameplay changes in a desktop browser. Keep existing commits and authors intact.
