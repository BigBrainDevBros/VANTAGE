# Credits And Asset Licenses

## Sound Effects

All from the **TeamForbiddenLLC/warfork-free-soundpacks** `cc0/` folder, **CC0 1.0 (public domain)**:
free to use, modify and sell, no attribution required. Listed here anyway, out of respect.

| File | Used for |
|---|---|
| machinegun_fire.ogg | SMG fire |
| instagun_strong.ogg | Sniper fire |
| bladegun_strong_fire.ogg | Pistol fire |
| blade_strike1/2.ogg | Melee swing (picked at random) |
| blade_hitflsh1.ogg | Melee hit |
| weapon_noammo.ogg | Dry fire |
| weapon_switch.ogg | Weapon switch |

Repository: https://github.com/TeamForbiddenLLC/warfork-free-soundpacks

## Code

- Three.js r170 (`vendor/three/`, vendored locally, MIT)
- PeerJS 1.5.4 (`vendor/peerjs/peerjs.min.js`, MIT, https://peerjs.com) — WebRTC signaling and data channel
  for room-code multiplayer. It bundles eventemitter3 / peerjs-js-binarypack / webrtc-adapter / sdp;
  their license texts are in the official repository.
- All other game logic was written for this project.

## 3D Models

### Removed First-Person Guns And Soldier (2026-11-25)

This folder used to contain **cktang88/3d-fps** `mp5a5.glb`, `vss.glb`, `m1911.glb` and `soldier.glb`.
That repository has **no LICENSE** (GitHub reports `license: null`, i.e. all rights reserved),
so they could not be redistributed. All four were deleted on 2026-11-25, along with
`assets_unused/scarl.glb` from the same source.

Guns, the player body, bots and most melee props are now built out of boxes in `js/main.js`
(`buildVM` / `makeBlockBody` / `makeBot`); the game does **not depend on any external model file**.

To bring real models back: only accept **MIT / CC0 / explicitly licensed** files, put them back at
`models/mp5a5.glb`, `models/vss.glb`, `models/m1911.glb` and `models/soldier.glb`,
then set `GLB_ART = true` in `js/main.js`. Update this file and ASSET_REPORT.md first.

The grappling hook was always built out of boxes.

### Props

All **Kenney** CC0 models (public domain; commercial use, modification and redistribution allowed,
no attribution required), downloaded as GLB conversions from **Hidencod/tge-assets**:

| File | Source kit | Use |
|---|---|---|
| building-a / building-c / building-skyscraper-a / low-detail-building-a | city-kit-commercial | ~~distant skyline~~ no longer used (v4 generates the skyline procedurally); moved to `assets_unused/`, not bundled |
| brick-wall | graveyard-kit | ~~low walls~~ only used by the old map; not placed in the v4 city |
| crate | prototype-kit | old map crates (unused in v4, kept in the prop table) |
| barrel | platformer-kit | street prop |
| dumpster / construction-barrier / construction-cone | city-kit-roads | street props (v4 spare) |
| tree-large / tree-small | castle-kit | street trees and trees outside the walls |
| rock-largea / rock-smalla / plant-bushlarge / grass | nature-kit | corner decoration |

Conversion repository: https://github.com/Hidencod/tge-assets
Original author: https://kenney.nl (CC0 1.0)

### Knife

| File | Name | Source | License |
|---|---|---|---|
| katana.glb | Katana (round tsuba, wrapped handle, curved blade; tip at +Z, 1.047 m long) | 3dassets.dev "Swords, Shields and Melee Arms — Katana"<br>https://3dassets.dev/assets/swords-shields-and-melee-arms-katana-dc914408 | **CC0 1.0** (the pack is marked AI-generated, author 3D Assets) |

(The balisong and hunting knife models, plus their open/close and placement code, were removed on
2026-11-24. The melee slot now has two choices: fists (built-in box hand) and katana.)

The katana is a static mesh (no skeleton or animation); the inspect animation is a scripted rotation.
It uses KHR_mesh_quantization (native in three r170) and has no textures; the metal look comes from
the environment map baked into `knifeEnv`.

Props are visual only: collision, pathfinding and hit detection still use the boxes created by `addBox`,
and everything falls back to boxes if a model fails to load.

## Procedural City Map

The whole map is **generated in code** (the "大地图：程序化街区城市" section of `js/main.js`).
There is no external map file: building volumes, streets, the ground texture and the window / curtain-wall /
storefront / corrugated textures are all painted on canvas or built as geometry at runtime.
So there is no third-party map license involved.

Tried but **not used**, and no files kept in the repo: the Khronos glTF sample VirtualCity
(3DRT, evaluation-only license, and it is a dome-covered plaza rather than a level) and Sponza
(CryEngine license, 45 MB).
