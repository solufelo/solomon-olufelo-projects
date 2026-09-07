# Laurier Golden Hawks / Wolfpack Glory Jumbotron Shuffle
## Production Blueprint, Set Design & Behance Case Study Master Plan

> **Project Goal**: Transform the Wilfrid Laurier University in-game helmet shuffle into an ESPN/Fox Sports-grade motion graphics case study for your graduation art/design portfolio and Behance showcase.
> **Date**: September 7, 2026  
> **Client / Identity**: Wilfrid Laurier Athletics (Laurier Golden Hawks / Wolfpack Glory)  
> **Format**: 16:9 4K Stadium Broadcast Video + Vertical Reel/TikTok Cut + Behance Process Deck  

---

## 1. Creative Direction & Brand System

### 1.1 Brand Identity Matrix & LED Videoboard Science
| Element | Specification | Visual Purpose & LED Science |
| :--- | :--- | :--- |
| **Primary Color** | Laurier Gold (`#FDB913` / RGB: `0.992, 0.725, 0.075`) | Front lettering core face, light flares, metallic chrome luster (0.22 diode emission) |
| **Secondary Color** | Laurier Darkness Purple (`#20003B` / RGB: `0.125, 0.000, 0.231`) | Backing stroke & bevels, helmet shell base, pitch boundary lines |
| **LED Contrast Rule** | **Zero Pure White Borders** (APL Protection) | High-nit stadium LED boards dim down under high-APL white. Deep Purple replaces white outlines. |
| **Neutral Low** | Stadium Carbon Slate (`#121316` to `#1E1F24`) | Dark turf perimeter, jumbotron vignette |
| **Prize Accent** | Authentic Pigskin Leather (`#5B2C0D` with pebble bump) | Contrasts sharply against green/purple turf and gold metals |
| **Hype Typography** | **Radwave Display** (*Radwave Demo Regular*) | **Hailey's Spec**: Explosive headlines ("WATCH CLOSELY!", "WHERE IS IT?", "TOUCHDOWN!", "INTERCEPTION!") |
| **Broadcast Typography** | **Agency FB Bold** (*AGENCYB.TTF* / *agencyfb_bold.ttf*) | **Hailey's Spec**: Geometric condensed sports typography for Downs ("1ST DOWN", "3RD & SHORT"), yard lines, clock, and slot numbers |

### 1.2 Two-Tone Varsity Athletic Lockup (Anti-Glare Dual Mesh)
To ensure maximum readability from any angle in University Stadium without blowing out the LED diodes:
* **Front Core (3D Curve)**: Golden Hawks Gold (`#FDB913`), Extrude: `0.045m`, Bevel Depth: `0.008m`, Subtle emission strength `0.22`.
* **Backing Outline (Parented 3D Curve)**: Laurier Deep Purple (`#20003B`), Extrude: `0.040m`, Bevel Depth: `0.024m` (forms a thick, crisp athletic border around the gold letters).
* **Result**: Razor-sharp edge separation, rich contrast against floodlit grass, and 100% compliance with stadium videoboard hardware limits.

---

## 2. Environmental Set Designs & Themed Variations

To make your Behance project look like a comprehensive university athletics campaign, we define **3 distinct seasonal themes**:

```
                                  THEMED SET DESIGNS
                                          │
        ┌─────────────────────────────────┼────────────────────────────────┐
        ▼                                 ▼                                ▼
[ Theme A: Prime-Time Football ]   [ Theme B: Homecoming Gold Out ]  [ Theme C: Frozen Frostbite (Winter) ]
 • Night stadium with floodlights   • Gold particle pyro fountains    • Sub-zero ice rink / winter dome
 • Dew-glossed artificial turf      • Golden reflective dancefloor    • Frosted visor helmet shaders
 • Purple & gold stadium stands     • Laser beam sweeps               • Breath vapor & volumetric fog
```

### Theme A: "Prime-Time Friday Night Lights" (Hero / Baseline Set)
* **Floor / Pitch**: High-detail artificial field turf with subtle dew gloss (`Roughness: 0.35`, micro-displacement normal map) and painted purple yard line boundary.
* **Backdrop**: University Stadium stands plunged in low evening blue-purple ambient tone with blurred stadium crowd billboards and LED ribbon board.
* **Lighting Rig**:
  * **4x Corner Stadium Floodlights**: High-intensity spot lights (`Power: 5000W`, color temperature `5600K`) with volumetric cone haze (`Volume Scatter: Density 0.015`).
  * **Key Fill**: Soft overhead gold broadcast dome (`Warm 3200K`).
  * **Edge / Rim Lights**: Two crisp cyan/purple rim lights behind helmets to carve out silhouette edges against the dark background.

### Theme B: "Homecoming Gold-Out" (Hype & Championship Theme)
* **Floor**: Mirror-gloss dark carbon stage reflecting golden overhead trusses and scoreboards.
* **Lighting & FX**: Golden spark pyro particles firing up on the outro reveal, laser sweeps, and dynamic jumbotron LED panels flashing.

### Theme C: "Winter Frost / Golden Hawk Blizzard" (Playoff Edition)
* **Floor**: Frosted hockey-rink ice surface with skate cut scratches and sub-surface scattering.
* **Helmets**: Chrome gold shell with frost condensation shader and tinted mirrored iridescent visors.

---

## 3. Shot-by-Shot Storyboard & Broadcast Timeline

**Total Runtime**: 12 to 14 Seconds (360 to 420 frames @ 30 FPS)

```mermaid
timeline
    title 14-Second Broadcast Storyboard Timeline
    00:00 - 01:50 : [Phase 1: The Intro Hook] : Wide camera dolly in : Gold banner pops "WATCH CLOSELY!" : Winning helmet lifts to display football
    01:50 - 07:50 : [Phase 2: The Orbital Frenzy] : Dynamic camera tracking : Banners switch to "KEEP YOUR EYES ON THE BALL!" : 8-10 high-speed orbital passes with banking roll
    07:50 - 10:00 : [Phase 3: The Suspense Beat] : Helmets freeze in final slots : "WHERE IS IT? PICK 1, 2 OR 3!" : Jumbotron crowd audio tension build
    10:00 - 13:50 : [Phase 4: The Golden Reveal] : Winning helmet lifts with slow-motion tilt : Gold confetti / strobe burst : "HELMET 2 WINS!"
```

### Detailed Shot Breakdown

#### Shot 1: The Intro Hook (Frames 1 – 50 / 0.0s – 1.6s)
* **Visual**: Camera dollys in from wide angle. The 3 helmets are resting at Slots 1, 2, and 3.
* **Action**: 3D Banner slams in: *"WATCH CLOSELY!"*. The winning helmet (e.g., Helmet 2) smoothly lifts `1.8m` and tilts forward 20°, clearly showing the spinning football underneath.
* **Broadcast Element**: Lower-third chyron badge: *"LAURIER ATHLETICS // HALFTIME SHUFFLE"*.

#### Shot 2: The Drop & Lock (Frames 50 – 70 / 1.6s – 2.3s)
* **Visual**: Helmet drops firmly back over the ball with a subtle ground impact dust puff.
* **Action**: Camera pulls into locked 65° broadcast tracking angle.

#### Shot 3: The Frenzy (Frames 70 – 260 / 2.3s – 8.6s)
* **Visual**: 8 to 10 rapid, continuous orbital swaps.
* **Dynamics**:
  * Front passes swing $+Y$, back passes swing $-Y$ (Zero clipping).
  * Centripetal roll of $12^\circ$ banks helmets into corners.
  * Motion blur (`Shutter: 0.5`) adds speed sensation.
* **On-Screen Graphic**: Banner switches to pulsing gold: *"TRACK THE HELMET!"*.

#### Shot 4: The Dramatic Suspense Pause (Frames 260 – 310 / 8.6s – 10.3s)
* **Visual**: Helmets come to an abrupt, synchronized stop in their final slots.
* **Action**: Everything goes dead still.
* **Graphic**: Massive animated 3D sign pops into the foreground: *"WHERE IS IT? PICK A HELMET!"*.
* **Audience Engagement**: Screen shows numbers `[ 1 ]`, `[ 2 ]`, `[ 3 ]` pulsing over each helmet.

#### Shot 5: The Golden Reveal & Climax (Frames 310 – 380 / 10.3s – 12.6s)
* **Visual**: Spotlight isolates the winning helmet.
* **Action**: Helmet lifts smoothly upward into the air with an athletic 28° forward tilt. The football spins proudly underneath.
* **Graphics**: Golden light bursts, confetti particles, and banner updates to *"HELMET 2 WINS! CLAIM YOUR PRIZE"*.

---

## 4. Environmental Asset Checklist & Starter Kit

Everything needed to build the complete broadcast environment:

### A. 3D Model Assets
- [x] **Procedural Helmet Stand-ins**: Built and verified in addon.
- [ ] **Hero Football Helmet Mesh**: Low/Mid-poly athletic helmet with separable visor, inner padding, chinstrap, and facemask cage.
- [ ] **Prize Assets**:
  - Wilson Leather Football (Hero).
  - Laurier Gold Coin / Championship Ring (Alternative prize variant).
  - Hockey Puck (for Laurier Golden Hawk Ice Hockey variant).
- [ ] **Stadium Prop Elements**:
  - Yard line marker pylons (Orange padded pylons at side boundaries).
  - Background goalposts (Yellow galvanized steel uprights in depth of field).
  - Truss lighting rig (Aluminum triangular truss above frame).

### B. Shaders & Material Palette (Blender EEVEE Next / Cycles)
- [ ] **Laurier Purple Pearlescent**: `Metallic: 0.4`, `Roughness: 0.2`, clearcoat sheen with subtle metallic purple flake.
- [ ] **Laurier Gold Chrome / Satin**: `Base Color: #FDB913`, `Metallic: 0.92`, `Roughness: 0.18`.
- [ ] **Pebbled Leather Pigskin**: Leather brown with Voronoi bump and white painted laces.
- [ ] **Turf Shader**: Hair particle grass or high-frequency normal map with specular highlights simulating stadium floodlight reflections.
- [ ] **Emissive Stadium Ribbon Boards**: Scrolling digital LED texture with Bloom/Glow.

### C. Audio Design & SFX (Crucial for Behance Reel)
- [ ] **Intro**: Whoosh riser + referee stadium whistle.
- [ ] **Shuffle Loop**: Fast rhythmic sliding whooshes (`whir-whir-whir`) synced to pair crossing frames.
- [ ] **Suspense Beat**: Deep bass drone / heartbeat pulse with crowd murmur.
- [ ] **Reveal**: Loud stadium buzzer / horn, crowd roar, and celebratory chime.

---

## 5. "Start Today" Action Plan & Step-by-Step Schedule

### Phase 1: Today (Day 1) — Studio Lighting & Set Dressing Setup
1. **Scene File Architecture**:
   - Create a master file: `laurier_shuffle_studio.blend`.
   - Link the Wolfpack addon to drive the animation.
2. **Build the Pitch Stage**:
   - Add a $12\text{m} \times 8\text{m}$ ground plane with turf material and white boundary yard lines.
   - Place two orange boundary pylons on the left and right edges.
3. **Setup Broadcast 3-Point Stadium Lighting**:
   - Add 2 spot lights angled from top-left and top-right aimed at the center slot.
   - Add a subtle purple/blue rim light behind the helmets.
   - Enable **Depth of Field** on the camera with target set to `Helmet_2` (`F-Stop: 2.8` for cinematic focal blur).

### Phase 2: Day 2 — Model Polishing & Shaders
1. Import or refine hero Laurier helmets with university logos/decals.
2. Apply high-spec gold and deep purple gloss materials.
3. Use the addon's **"Auto-Assign 3 Selected"** button to bind the new models in one click.

### Phase 3: Day 3 — Camera Moves & Render Passes
1. Add subtle camera punch-in on the final reveal lift.
2. Render out **Cycles / EEVEE Next** 4K passes:
   - Beauty Pass
   - Cryptomatte / Ambient Occlusion
   - Mist / Depth Pass
3. Export vertical 9:16 crop for social reels.

### Phase 4: Day 4 — Behance Case Study Packaging
1. **Case Study Header**: "Wilfrid Laurier Athletics: In-Game Jumbotron Motion Identity & Interactive Shell Game".
2. **Breakdown Sections**:
   - *The Challenge*: Eliminating 1D planar collisions, maintaining center-of-mass camera framing, and engaging stadium crowds.
   - *The Algorithm*: Parametric orbital swap paths with continuous depth variation ($+Y/-Y$) and centripetal banking.
   - *Design System*: Colors, typography, helmet 3D topology wireframes.
   - *Final Animation*: Video embed + looped GIFs of key moments.

---

## 6. The 3 Deterministic Outcome Variants (Game-Day Production System)

To prevent fans in University Stadium from predicting identical results across multiple games or quarters, the system includes 3 deterministic variants alongside random live generation:

```
                            GAME-DAY OUTCOME ROTATION
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        ▼                              ▼                              ▼
 [ Variant A: Slot 1 / Left ]   [ Variant B: Slot 2 / Center ] [ Variant C: Slot 3 / Right ]
  • Target X = -2.40m            • Target X = 0.00m             • Target X = +2.40m
  • Q1 / Homecoming Halftime     • Q2 / Rivalry Matchup         • Q3 / Playoff Climax
  • Output: shuffle_varA.mp4     • Output: shuffle_varB.mp4     • Output: shuffle_varC.mp4
```

* **Mathematical Enforcement**: After $N$ procedural random swaps, the routine verifies if `item_slot[ball_holder] == desired_slot`. If not, a single mathematically collision-free swap between current slot and target slot is executed, guaranteeing 100% precision.
* **Control Room Delivery**: Export 3 pre-rendered 4K Apple ProRes / H.264 clips for the videoboard switcher, allowing the game director to rotate variants dynamically based on crowd interaction.

---

## 7. Modular In-Game Videoboard Stingers Suite

Generated dynamically via the addon using Hailey's exact typography pairings and anti-glare shader lockups:

| Stinger Event | Headline Font | Subtitle Font | Colorway & LED FX | Duration |
| :--- | :--- | :--- | :--- | :--- |
| **TOUCHDOWN** | **Radwave Display** | **Agency FB Bold** | Gold Core (`#FDB913`) + Purple Bevel (`#20003B`) + Kinetic Overshoot Slam | 65 Frames (2.1s) |
| **INTERCEPTION** | **Radwave Display** | **Agency FB Bold** | Alternating Purple/Gold Siren Alert + Strobe Settle | 60 Frames (2.0s) |
| **1ST DOWN** | **Agency FB Bold** | **Agency FB Bold** | Broadcast Chevron Slide-In + "MOVE THE CHAINS" Yardage Marker | 55 Frames (1.8s) |
| **2ND DOWN** | **Agency FB Bold** | **Agency FB Bold** | Offense Rhythm Graphic + Down Counter | 50 Frames (1.6s) |
| **3RD & SHORT** | **Agency FB Bold** | **Agency FB Bold** | Red Zone Tension Pulse + "GET ON YOUR FEET!" | 55 Frames (1.8s) |
| **3RD & LONG** | **Agency FB Bold** | **Agency FB Bold** | Stadium Crowd Rally + "DEFENSE // STAND UP!" | 60 Frames (2.0s) |

