# 素材来源

## 音效（sfx/）

全部来自 **TeamForbiddenLLC/warfork-free-soundpacks** 的 `cc0/` 目录，**CC0 1.0（公共领域）**，可自由使用、修改、商用，无需署名。这里仍然列出以表尊重。

| 文件 | 用途 |
|---|---|
| machinegun_fire.ogg | 冲锋枪开火 |
| instagun_strong.ogg | 狙击枪开火 |
| bladegun_strong_fire.ogg | 手枪开火 |
| blade_strike1/2.ogg | 挥刀（随机二选一） |
| blade_hitflsh1.ogg | 刀砍中人 |
| weapon_noammo.ogg | 空仓 |
| weapon_switch.ogg | 切枪 |

仓库：https://github.com/TeamForbiddenLLC/warfork-free-soundpacks

## 代码

- Three.js r170（vendor/three/，本地化，MIT）
- PeerJS 1.5.4（vendor/peerjs/peerjs.min.js，MIT，https://peerjs.com）—— 联机单挑的 WebRTC 信令与数据通道；
  它自己打包了 eventemitter3 / peerjs-js-binarypack / webrtc-adapter / sdp，许可证全文见官方仓库
- 其余游戏逻辑为本项目自写

## 参考（只看了思路，没抄代码）

- Krunker 官方 wiki 的武器数值表
- DustIII（浏览器版 CS）的刀数值与挥砍曲线
- CS:GO / VALORANT / 三角洲行动的瞄具与手感常识

## 3D 模型（models/）

### 第一人称枪模与士兵：已删除（2026-11-25）

原来这里放着 GitHub **cktang88/3d-fps** 的 mp5a5.glb / vss.glb / m1911.glb / soldier.glb。
那个仓库**没有 LICENSE**（GitHub API 返回 `license: null`，等于保留所有权利），不能随包发。
2026-11-25 按要求把四个文件全部删除，连带同来源的 `assets_unused/scarl.glb`。

现在枪、玩家身体、人机身体、大部分近战道具都是 `js/main.js` 里用方块现搭的
（`buildVM` / `makeBlockBody` / `makeBot`），**不依赖任何外部模型文件**。

以后要换回真模型：只接受 **MIT / CC0 / 有明确书面授权** 的文件，
按原路径放回 `models/mp5a5.glb`、`models/vss.glb`、`models/m1911.glb`、`models/soldier.glb`，
再把 `js/main.js` 里的 `GLB_ART` 改成 `true`。换之前先更新本文件和 ASSET_REPORT.md。

grapple（钩索枪）本来就是方块搭的。

### 场景道具（models/props/）

全部是 **Kenney** 的 CC0 模型（公共领域，可商用、可修改、无需署名），
通过 **Hidencod/tge-assets** 的 GLB 整理版下载（原包为 Kenney 的 3D kits）：

| 文件 | 来源包 | 用途 |
|---|---|---|
| building-a / building-c / building-skyscraper-a / low-detail-building-a | city-kit-commercial | ~~围墙外的城市天际线~~ 已不用（v4 换成程序化远景楼群），文件移到 `assets_unused/`，不打包进单文件 |
| brick-wall | graveyard-kit | ~~场内矮墙~~ 旧地图用的，v4 城市地图不再摆放 |
| crate | prototype-kit | 旧地图叠箱（v4 不再使用，Props 表里保留以便以后摆） |
| barrel | platformer-kit | 场地摆件 |
| dumpster / construction-barrier / construction-cone | city-kit-roads | 场地摆件（v4 备用） |
| tree-large / tree-small | castle-kit | 街角行道树 + 墙外树冠 |
| rock-largea / rock-smalla / plant-bushlarge / grass | nature-kit | 角落点缀 |

整理仓库：https://github.com/Hidencod/tge-assets
原始作者：https://kenney.nl（CC0 1.0）

### 刀（models/knives/）

| 文件 | 名称 | 来源 | 授权 |
|---|---|---|---|
| katana.glb | 武士刀（圆镡、缠绳柄、带弧度刀身；刀尖 +Z，全长 1.047 m） | 3dassets.dev「Swords, Shields and Melee Arms — Katana」<br>https://3dassets.dev/assets/swords-shields-and-melee-arms-katana-dc914408 | **CC0 1.0**（该包标注由 AI 生成，作者 3D Assets） |

（11-24 深夜：蝴蝶刀 balisong.glb 和猎刀 hunting.glb 已经删掉，连带它们那两套开合 / 摆位代码。
近战槽现在是「拳头（内置方块手）」和「武士刀」两种。）

武士刀是静态模型（没有骨骼和动画）。游戏里的检视动作是程序驱动的旋转。
武士刀用 KHR_mesh_quantization（three r170 原生支持），材质没有贴图，靠 knifeEnv 那张环境贴图出金属感。

道具只负责外观：碰撞、寻路、命中判定仍然走原来 addBox 生成的方块，模型加载失败时自动回落到方块。

## 大地图（v4，200 米街区城市）

整张地图是**代码生成的**（`js/main.js` 里「大地图：程序化街区城市」那一段），
不包含任何外部地图文件：建筑体块、街道、地面贴图、窗户 / 幕墙 / 店面 / 瓦楞板纹理
全部是运行时用 canvas 画出来或者直接生成的几何体。因此没有第三方地图授权问题。

试过但**没有采用**、也没有把文件留在仓库里的：Khronos glTF 样例 VirtualCity（3DRT，仅测试授权，
而且是个带穹顶的广场不是关卡）、Sponza（CryEngine 协议，45 MB）。
