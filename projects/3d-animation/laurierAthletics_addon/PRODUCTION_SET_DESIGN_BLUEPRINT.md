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
| **FIELD_GOAL_GOOD** | **Radwave Display** | **Agency FB Bold** | *"IT'S GOOD!"* + Gold Flare Burst + Cam Punch through Uprights | 65 Frames (2.1s) |
| **FIELD_GOAL_ATTEMPT** | **Radwave Display** | **Agency FB Bold** | *"FIELD GOAL"* + *"45 YARDS // 4TH DOWN"* Countdown Tension | 55 Frames (1.8s) |
| **FIELD_GOAL_BLOCKED** | **Radwave Display** | **Agency FB Bold** | *"BLOCKED!"* + *"TURNOVER ON DOWNS"* + Siren Pulse | 60 Frames (2.0s) |
| **INTERCEPTION** | **Radwave Display** | **Agency FB Bold** | Alternating Purple/Gold Siren Alert + Strobe Settle | 60 Frames (2.0s) |
| **1ST DOWN** | **Agency FB Bold** | **Agency FB Bold** | Broadcast Chevron Slide-In + "MOVE THE CHAINS" Yardage Marker | 55 Frames (1.8s) |
| **2ND DOWN** | **Agency FB Bold** | **Agency FB Bold** | Offense Rhythm Graphic + Down Counter | 50 Frames (1.6s) |
| **3RD & SHORT** | **Agency FB Bold** | **Agency FB Bold** | Red Zone Tension Pulse + "GET ON YOUR FEET!" | 55 Frames (1.8s) |
| **3RD & LONG** | **Agency FB Bold** | **Agency FB Bold** | Stadium Crowd Rally + "DEFENSE // STAND UP!" | 60 Frames (2.0s) |

---

## 8. Procedural 3D Collegiate Upright Goalposts

Authentic NCAA/U SPORTS collegiate goalposts spawned in the background ($Y = +11.5\text{m}$) to anchor the stadium environment and frame all scoring stingers:

* **Gooseneck Support Base**: Angled heavy-gauge steel post rising $3.2\text{m}$ ($10\text{ft}$) with stadium optic yellow powder coat finish.
* **Horizontal Crossbar**: $5.64\text{m}$ ($18.5\text{ft}$) wide cylinder spanning the target window.
* **Dual Vertical Uprights**: $9.14\text{m}$ ($30\text{ft}$) tall uprights at $X = \pm 2.82\text{m}$ rising into the clouds.
* **Wind Streamers**: Dynamic fluttering Laurier purple ribbons (`Mat_Goalpost_Streamer`) parented to the tips of both uprights to indicate stadium wind direction and add atmospheric micro-motion.

---

## 9. The Compositor's Eye: Sky Atmosphere & Optical Lens Rig

```
                        BLENDER 5.2 COMPOSITOR GRAPH
                                     │
   ┌─────────────────────────────────┼─────────────────────────────────┐
   ▼                                 ▼                                 ▼
[ Render Layers (3D) ] ──► [ Fog Glow Glare ] ──► [ Lens Distortion & Dispersion ] ──► [ Output ]
 • 3D Helmets & Ball       • Optical Bloom (0.68) • Anamorphic Squeeze (0.012)        • Direct
 • Sky Dome & Clouds       • Metallic Halation    • Chromatic Fringe (0.006)            Broadcast
 • Stadium Turf & Lines    • Stadium Spot Glow    • Analog 35mm / Arri Aesthetic        Frame
```

### 1. Procedural Twilight Sky Dome (`Sky_Dome_Atmosphere`)
- $45\text{m}$ radius inverted geodesic sphere with a custom gradient emission shader.
- Gradient shifts from deep twilight purple (`#110022`) at zenith, through rich royal indigo (`#1D0B38`), into a fiery amber sunburst horizon (`#E68A00` / `#FDB913`).
- Procedural cloud noise texture layer ($2.8$ scale, $4.5$ detail, $0.65$ roughness) generating rolling game-day storm clouds backlit by setting sun rays.

### 2. High-Angle Rim/Kicker Backlights
- **Amber Sun Flare Kicker (`Atmosphere_Rim_L`)**: $(-6.0, 7.5, 5.0)$ at $2200\text{W}$, casting intense warm golden rim highlights across helmet crowns.
- **Deep Purple Kicker (`Atmosphere_Rim_R`)**: $(+6.0, 7.5, 5.0)$ at $2200\text{W}$, casting cool collegiate purple fill on the opposite rim.
- **Visual Result**: Razor-sharp edge separation that makes 3D elements jump off the cloudy background.

### 3. Procedural Turf Yardlines
- Authentic Knight-Newbrough Field turf green (`#08280D`) with repeating painted white/gold chalk yardlines every $2.8\text{m}$ with subtle specularity and dewy sheen.

---

## 10. The Multi-Hyphenate Creative Director Blueprint (Album Art & Streetwear Lookbooks)

> *"If somebody sees this on the jumbotron, I want them to see it and be like, 'Yo, the person who animated this was a compositor.' I'd like them to do my clothing brand. I'd like them to make my album art. I want them to be curious about the creator. Nobody is limiting me. The sky is."* — Solomon Olufelo

This motion graphics system is not just an in-game sports utility; it is a **high-fashion creative direction portfolio piece**. Here is how to package and present this work on Behance, Instagram, and your creative portfolio to land high-paying streetwear brand campaigns, music album art commissions, and commercial motion direction:

### A. Three Framing Formulas (Crop & Perspective Strategy)

| Format / Crop | Camera Lens & Angle | Aesthetic Reference | Target Client / Industry |
| :--- | :--- | :--- | :--- |
| **1:1 Square (Album Cover)** | $85\text{mm}$ Telephoto, centered straight-on macro, tight crop on golden chrome helmet with dark storm clouds behind, high-contrast typography stamp. | Travis Scott *Cactus Jack*, Kanye West *Yeezus*, Playboi Carti, NikeLab | Record Labels, Indie Musicians, Vinyl Collectors |
| **9:16 Vertical (Reel / Lookbook)** | $20\text{mm}$ Ultra-Wide, low-angle worm's-eye heroic view looking up through golden goalposts against dramatic clouds, anamorphic horizontal lens flare. | Off-White *Virgil Abloh*, Fear of God Athletics, Balenciaga Sports | Streetwear Brands, Fashion Lookbooks, Social Hype Campaigns |
| **16:9 Landscape (Stadium / Reel)** | $50\text{mm}$ Broadcast Prime, kinetic camera tracking with depth of field ($f/2.8$) focused on Helmet 2 with field yardlines extending into infinity. | ESPN Sunday Night Football, Fox Sports NFL, FIFA World Cup TV Package | Broadcasters, Collegiate Athletic Departments, Esports Leagues |

### B. The 4 High-Fashion Material Palettes

1. **Liquid Gold Chrome (The Winner's Grail)**:
   - Base Color: `#FDB913`, Metallic: $1.0$, Roughness: $0.08$.
   - Reflects the procedural twilight clouds with liquid mirror fidelity; blooms with Fog Glow in the compositor.
2. **Obsidian Matte Carbon (The Away Stealth Edition)**:
   - Base Color: `#0A0A0D`, Metallic: $0.2$, Roughness: $0.45$, Subtle carbon weave normal map.
   - High-end technical apparel aesthetic (A-COLD-WALL* / Arc'teryx Veilance).
3. **Pearlescent Iridescent Purple (The Heritage Shift)**:
   - Dual-tone Fresnel shader shifting between Deep Darkness Purple (`#20003B`) at grazing angles and Molten Gold (`#FFCC00`) at direct view.
4. **Distressed Varsity Enamel**:
   - High-gloss athletic lacquer with subtle scuffs and procedural metallic flecks for authentic game-worn grit.

### C. Behance Case Study Storyboard Structure

When publishing this on Behance upon graduation, structure your case study as follows:
1. **The Hero Video**: 4K 60fps render with dynamic sound design (air whooshes, dramatic heartbeat countdown, brass fanfare).
2. **The Creative Philosophy**: *"Bridging Collegiate Athletic Excitement with High-Fashion Motion Compositing"*.
3. **The Design System**: Typography lockup card (**Radwave Display** x **Agency FB Bold**), color swatches with LED power limiting science.
4. **The Engineering**: Wireframe turnarounds, ShufflePlan collision-free orbital math diagrams, and the After Effects SMPTE cue sheet bridge.
5. **Brand Extensions**: Mockups of the helmet emblem on streetwear hoodies, vinyl record sleeves, and oversized museum gallery prints.


