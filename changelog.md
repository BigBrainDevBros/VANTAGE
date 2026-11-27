# Changelog

All notable changes to VANTAGE are documented here.

## [Unreleased]

### Added

- Published linked contributor guides in English and Simplified Chinese.
- Added a Simplified Chinese project guide and bilingual feedback templates.
- Added an in-place rematch: the end screen's restart button resets the round without reloading the
  page, and online matches reset on both sides together.

### Fixed

- Setback towers on tall buildings now have collision. The upper tier had none, so players could
  walk through it from the roof and bullets and grapple rays passed straight through.
- Restarting after a disconnect now reconnects in place and returns to the lobby instead of reloading
  the page.

## [0.2.0] - 2026-11-27

### Added

- Added street furniture across the playable city: street lamps, traffic lights, parked cars that work as cover, benches, bins, hydrants and rooftop antennas.
- Added rooftop props on tall buildings: water tanks, AC units and stair penthouses.
- Added a graphics quality setting with four levels, trading shadow resolution and render scale.
- Added a time of day option on the main menu, with noon and dusk lighting.
- Added a subtle screen vignette and baked contact shadows around each block into the ground texture.
- Added a night lighting mode on the main menu: moonlit sky, warm pools under the street lamps,
  and a share of the windows lit up.
- Added a build version label to the settings panel header and a version badge to the HUD; both read one
  semantic version constant that is kept in step with this changelog.
- Added a heartbeat watchdog to online matches: when a peer stops answering, the match ends cleanly and
  their model is removed instead of freezing in place.
- Added streets outside the playable walls: a tiled road texture with lane markings and crosswalks, plus parked cars and street lamps.
- Added third-person body animations: jumping, landing, hit reactions, reload and inspect poses, and head tracking, plus a landing dust burst.
- Added an in-game "Report a bug" button that prefills the issue form with build information.
- Added a thanks section to the README for the repository setup.
- Added automated repository compliance checks and safe Markdown repairs.
- Added contributor templates, a security policy, and a consolidated license notice.

### Changed

- Brought the distribution documentation and tracked paths into line with the organisation's conventions.
- Defaults keep the previous look: graphics quality Medium and lighting Noon.
- The training panel's ESP overlay is now off by default; it can be switched on with the right Shift panel.
- Viewmodel materials use Phong shading with a slightly lifted base colour, textures use 16x anisotropy,
  and the sky gradient is dithered to remove banding.
- Keyboard focus is now visible in menus and panels.

### Fixed

- Pointer lock failures in iframes and unfocused windows no longer surface as console errors.
- The render scale follows the active graphics quality when the window moves to a display with a different pixel ratio.
- The far horizon no longer shows a seam where the ground plane ended.
- Brighten the night menu backdrop so the city is visible behind the menu.
- Losing the connection now ends a match as "Connection lost" instead of "Defeat", and the opponent's
  model is removed right away.
