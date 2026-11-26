# Changelog

All notable changes to VANTAGE are documented here.

## [Unreleased]

### Added

- Added street furniture across the playable city: street lamps, traffic lights, parked cars that work as cover, benches, bins, hydrants and rooftop antennas.
- Added rooftop props on tall buildings: water tanks, AC units and stair penthouses.
- Added a graphics quality setting with four levels, trading shadow resolution and render scale.
- Added a time of day option on the main menu, with noon and dusk lighting.
- Added a subtle screen vignette and baked contact shadows around each block into the ground texture.
- Added a night lighting mode on the main menu: moonlit sky, warm pools under the street lamps,
  and a share of the windows lit up.
- Added a build version label to the settings panel header.
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

### Fixed

- Pointer lock failures in iframes and unfocused windows no longer surface as console errors.
- The render scale follows the active graphics quality when the window moves to a display with a different pixel ratio.
- The far horizon no longer shows a seam where the ground plane ended.
- Brighten the night menu backdrop so the city is visible behind the menu.
