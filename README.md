# VANTAGE

A browser first-person shooter that ships as one static HTML file. No build step, no server, works offline.

- 200 × 200 m procedural city with three presets (downtown, low-rise, towers)
- Up to 100 bots with flow-field pathfinding; endless solo mode
- SMG, sniper, pistol, katana, grappling hook
- 1v1 duels and co-op vs bots over LAN or room codes (WebRTC)
- MIT / CC0 assets only, no unlicensed models

![VANTAGE](screenshot.jpg)

## Play

- **Offline:** download `index.html` and open it in a browser. That is all it takes.
- **Online:** <https://bigbraindevbros.github.io/VANTAGE/> — the same file, served by GitHub Pages.
- **Language:** the UI defaults to English. Settings → Language switches to 中文.

## Controls

| Key | Action |
|---|---|
| Left mouse | Fire / melee |
| 1 / Q / 2 / 3 / 4 | SMG / sniper / pistol / melee / grappling hook |
| E | Aim down sights (sniper and pistol) |
| C | First / third person |
| Right Shift | Training aids panel (aim assist, ESP, wallbang; local only) |
| R / Y | Reload / inspect weapon |
| Shift / Space | Crouch / jump (jump is disabled in tactical mode) |
| M / Esc | Mute / settings |

Pick a map on the home screen. "Start game" is endless solo; "Create / join room" is multiplayer.

## What is in it

- **City:** a 4 × 4 block grid with 14 m streets, generated at startup — courtyard blocks, towers, a freight yard, a plaza. Fire escapes lead to the roofs, and bots will climb them to follow you.
- **Bots:** a 1 m navigation grid plus one flow field (BFS) shared by every bot, so they path around blocks and through alleys instead of sliding along walls. When you stand on a roof, their target becomes that building's fire-escape landing.
- **Collision, raycasts, hit detection:** all against the axis-aligned boxes created by `addBox`, accelerated with an 8 m spatial hash. Bullets use a 2D DDA plus slab test against those boxes.
- **Multiplayer:** 1v1 first-to-N, or co-op against bots. LAN through `server.py`, or room codes over WebRTC (PeerJS only exchanges SDP). Client-authoritative, no anti-cheat; play with friends.

## Tech

Three.js r170 for rendering, WebAudio for sound, PeerJS for WebRTC. Everything is bundled into a single HTML file: engine, game code, models (base64) and sounds. The city, textures, UI, AI, netcode and the block-built weapons and characters were written for this project.

## Assets and licenses

Everything in this build is MIT or CC0:

| Asset | License |
|---|---|
| Three.js r170 | MIT |
| PeerJS 1.5.4 | MIT |
| Kenney props (trees, barrels, planters, barriers) | CC0 1.0 |
| warfork-free-soundpacks | CC0 1.0 |
| Katana model | CC0 1.0 (3dassets.dev) |
| Maps, textures, UI, AI, netcode, block models, half the sound effects | Original |

See [CREDITS.md](CREDITS.md) for details. Weapon numbers are tuned against the Krunker wiki and DustIII tables; the code is original.

## About this repo

`index.html` is the single-file build output. The source lives outside this repo; this is the distribution build.