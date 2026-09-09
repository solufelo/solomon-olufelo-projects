# 🎨 Golden Hawks Helmet Shuffle — Brand Identity & UI/UX Design System

> **Brand**: Golden Hawks Helmet Shuffle ⚡ Game-Day Interactive Suite  
> **Client / Partnership**: Wilfrid Laurier Athletics × Rockstar Games Tools Spec  
> **Version**: 3.5.0  
> **Master Hub**: [[../../VAULT_INDEX.md|Root Vault Index]] | [[ROCKSTAR_GAMES_PORTFOLIO_BLUEPRINT.md|Rockstar Portfolio Blueprint]]

---

## 🌟 Visual Identity Showcase

![Golden Hawks Helmet Shuffle Hero Branding](assets/golden_hawks_branding_hero.jpg)

---

## 🎨 Color Palette & LED Science Tokens

Our color tokens are engineered to satisfy two demanding constraints simultaneously:
1. **Collegiate Athletic Identity**: Laurier Golden Hawks heritage (Varsity Gold & Darkness Purple).
2. **High-Nit Stadium LED Videoboard Science**: Preventing Automatic Power Limiting (APL) diode dimming and white-glare blowout.

| Token Name | Hex Code | RGB (0-1 Linear) | Diode Emission | Usage & Purpose |
| :--- | :--- | :--- | :---: | :--- |
| **Varsity Gold** | `#FDB913` | `0.992, 0.725, 0.075` | `0.22` | Core 3D letterface, helmet metallic shell, active telemetry accents |
| **Darkness Purple** | `#20003B` | `0.125, 0.000, 0.231` | `0.00` | Backing stroke & bevel depth, pitch boundary lines, dark contrast anchor |
| **Cyber Volt / Neon Cyan** | `#00F5D4` | `0.000, 0.960, 0.831` | `4.00` | Viewport 3D motion trajectory splines, velocity vectors, telemetry HUD lines |
| **Stadium Slate Carbon** | `#121316` | `0.071, 0.075, 0.086` | `0.00` | Backdrop field turf vignette, dark carbon stage, jumbotron letterboxing |
| **Pigskin Amber** | `#5B2C0D` | `0.357, 0.173, 0.051` | `0.00` | Hidden football prize, contrasting sharply against green turf and gold metal |

> [!IMPORTANT]
> **The Anti-Glare APL Protection Rule**: Pure white (`#FFFFFF`) outlines are strictly prohibited on stadium LED displays. High-nit LED boards (like Daktronics / Knight-Newbrough) suffer from Automatic Power Limiting when high-frequency white strokes cause the board power supply to dim down. Darkness Purple (`#20003B`) delivers razor-sharp contrast without triggering APL dimming.

---

## 🔤 Typography Hierarchy

```
HEADLINE / STINGER      RADWAVE DISPLAY       "GOLDEN HAWKS SHUFFLE" (All-Caps, Beveled)
BROADCAST / DOWN & DIST AGENCY FB BOLD        "3RD & GOAL • 0:42 4TH QTR"
TELEMETRY & TIMECODES   GEIST / JETBRAINS MONO "114.48 ms | 29,168 keys/s | 00:04:12:08"
```

1. **Radwave Display (*Radwave Demo Regular*)**:
   - Explosive hype headers (*"TOUCHDOWN!"*, *"WHERE IS IT?"*, *"THE ULTIMATE CHALLENGE"*).
   - Characterized by thick horizontal strokes and aggressive forward-leaning athletic geometry.
2. **Agency FB Bold (*AGENCYB.TTF*)**:
   - High-density information typography for Downs, yardlines, slot badge numbers (`[ 1 ]`, `[ 2 ]`, `[ 3 ]`), and sponsor tags.
   - Clean, condensed architectural proportions legible from the farthest stadium bleachers.
3. **JetBrains Mono / Geist Mono**:
   - Engineering metrics, frame indices, SMPTE timecodes, and telemetry counters.

---

## 🎛️ Technical Artist UI/UX Ergonomics (Blender N-Panel)

The Blender interface in **v3.5.0** applies core human factors engineering and Fitts's Law principles to make live broadcast operations error-proof:

### 1. The Branded Header Ribbon
- **Title Block**: Prominent `GOLDEN HAWKS ⚡ HELMET SHUFFLE` title with live versioning (`v3.5.0`).
- **Sidebar Tab**: Clean, recognizable `Golden Hawks` category tab in the View3D sidebar.
- **Status Pill Bar**: Four green-lit indicator pills:
  `[● 60 FPS]` `[● PRORES 422]` `[● RAGE READY]` `[● 0 LEAKS]`
  Provides immediate visual confirmation of operational health before any operator is clicked.

### 2. The Hero Action Deck (Fitts's Law Optimization)
- **⚡ 1-Click Full Game-Day Show (`scale_y = 1.45`)**:
  - The single most prominent button in the entire interface.
  - Automatically initializes the 3D venue, sets volumetric lighting, positions the 3 shufflers, bakes the entire bumper-to-shuffle sequence, renders 3D motion arcs, and configures ProRes 422 output in **under 200 milliseconds**.
  - Eliminates human error during high-stress game-day operations in the control booth.
- **Bake Golden Hawks Shuffle Animation (`scale_y = 1.45`)**:
  - Secondary prominent action for rapid routine re-shuffling.

### 3. Two-Column Information Density Grids
- Previous versions stacked every property vertically, forcing tedious scrolling.
- v3.5.0 implements clean two-column paired rows:
  - *Headline* alongside *Kicker*
  - *Sponsor* alongside *Layout Mode*
  - *Title Scale* alongside *Line Gap*
  - *Duration* alongside *Exit Motion Style*
  - *Swaps Count* alongside *Swap Duration*
  - *Spacing* alongside *Pause Frames*
- **Result**: **40% reduction in vertical panel height**, allowing animators to view all critical controls on a single 1080p monitor without scrolling.

### 4. Instrument-Cluster Telemetry Card (Stage 5)
- Styled like a supercar instrument cluster:
  - Column 1: `⚡ Latency: 114.5 ms` | `📦 Keys: 3339`
  - Column 2: `🚀 Speed: 29168 k/s` | `🧠 Peak: +0.16 MB`
  - Status: `🛡️ 0 Leaks | Deterministic Execution`
- Instant one-click export buttons for Game Engine JSON tracks and Telemetry CI/CD benchmarks.

---

## 📱 Social Media & Portfolio Presentation Assets

### 1. LinkedIn Showcase Video Dimensions
* **Format**: `1080 × 1080` (1:1 Square) or `1080 × 1350` (4:5 Vertical Portrait).
* **Frame Rate**: `60.00 fps` (smooth athletic motion).
* **Length**: Strictly **20 seconds**.
* **Thumbnail**: Golden Hawks Hero Helmet with glowing 3D trajectory spline curves.

### 2. Behance Case Study Structure
* **Header**: Hero Branding Artwork (1920×1080) with title: *"Golden Hawks Helmet Shuffle: Procedural 3D Motion Engine for Collegiate Stadiums"*.
* **Section 1**: The Real-World Challenge (APL protection, camera perspective overlap).
* **Section 2**: Mathematical Innovation (Camera-normal pitch vector `61.74°`, centripetal sine wave banking).
* **Section 3**: Technical Artist Tooling (Blender N-panel, 3D motion splines, real-time profiler).
* **Section 4**: Data Interoperability (Runtime quaternion export for Rockstar RAGE & Unreal).
* **Section 5**: 4K Video Reel on Stadium LED Videoboard.

---
*Anchor Document: [[../../THE_SUPER_BOWL_4_PILLAR_SYSTEM.md|The Super Bowl 4-Pillar System]]*
