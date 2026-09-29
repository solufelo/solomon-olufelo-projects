# Antigravity & AI Agent Master Rules: Laurier Athletics Broadcast Production

## 1. Zero-Clipping & Geometric Collision Mandate (NON-NEGOTIABLE)
Under NO circumstances may any render, graphic, or 3D asset exhibit mesh clipping, geometry interpenetration, or floating props ("glitch under a plane"). This is a permanent, non-negotiable studio standard:

### A. Mathematical Grounding & Bounding-Box Alignment
- Every object (helmet, football, goalpost, pylon, maquette plinth, player model) must have its exact lowest world-space vertex computed before rendering:
  ```python
  # Mandatory grounding calculation for all prop placement:
  bbox_world = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]
  z_min = min(v.z for v in bbox_world)
  # Adjust object so its lowest point sits precisely on the supporting surface:
  obj.location.z += (surface_z - z_min) + 0.0008  # Micro-clearance prevents z-fighting and plane slicing
  ```
- **Zero Interpenetration**: Props placed near each other (e.g., football resting against or adjacent to a helmet) must have confirmed non-intersecting collision boundaries. Never place props so that the facemask, chin strap, or outer shell cuts into adjacent geometry.
- **Support Pedestals & Slicing Planes**: Support pedestals, plinths, and tables must be modeled with real-world low-profile proportions, beveled top edges, and proper scale. A pedestal must NEVER occlude, bisect, or slice through the props it supports.

### B. Rigid Body & Physics Collision Protocols
- **Collision Shapes**: Use `CONVEX_HULL` or evaluated `MESH` for all contoured athletic assets. Never use default unscaled box collision on curved objects (helmets, footballs).
- **Collision Margins**: Set collision margins explicitly (`margin = 0.002m` / 2mm) to prevent physics tunneling or visual mesh sinking.
- **Solver Fidelity**: When baking physics simulations (e.g., helmet shuffle, bin drops), configure minimum `substeps_per_frame = 20` and `solver_iterations = 30` to guarantee zero high-speed penetration.

### C. Metric Scale Consistency
- All assets in the scene must be verified to real-world metric dimensions:
  - **Riddell SpeedFlex Helmet**: ~0.30m width x 0.32m height x 0.28m depth.
  - **Official Wilson CFL/Collegiate Football**: ~0.28m length x 0.17m diameter.
  - **Collegiate Goalpost**: Crossbar 3.05m (10ft), uprights 6.1m (20ft).
- Props must never be scaled arbitrarily without counter-scaling collision bounds and origins.

---

## 2. Official Brand Typography Mandate
All generated graphics, render overlays, title cards, lower thirds, jumbotron animations, and broadcast frames MUST use the official brand font stack:
- **Primary Display & Title Font**: **Radwave** (`C:\Windows\Fonts\RadwaveFont-Demo.otf` / `Radwave Demo 400.otf`) for high-octane, aggressive sports headlines, hero match titles, and hype text.
- **Athletic Technical & Numbers Font**: **Agency FB** (`C:\Windows\Fonts\AGENCYB.TTF`, `Agency FB Black Wide.ttf`, `agencyfb_bold.ttf`) for player numbers, scores, technical coordinates, dates, HUD elements, and game stats.
- **Secondary Display / Subheads**: **Railroad** / **Agency FB Bold**.
- **STRICT PROHIBITION**: NEVER use generic default fonts (e.g., Arial, Times New Roman, generic Calibri/Segoe) for display headlines.
- **No Missing Font Glyphs**: Never use Unicode special characters (e.g., `★`, `⚡`, `▲`) unless verified that the font file supports the glyph. Missing glyphs render as ugly `□` tofu rectangles and ruin broadcast deliverables. Use clean ASCII delimiters (`//`, `•`, `-`, `|`).

---

## 3. "Stylized Maxxed" Aesthetic Mandate
Always max out visual energy, collegiate athletic impact, and cinematic polish.
- **Lighting**: High-contrast, multi-point athletic lighting (intense rim/edge lights, tungsten pin-spotlights, stadium beam volumetric sweeps, metallic specular highlights).
- **Materials**: Rich, tangible textures-automotive pearlescent purple flake clearcoat, official Wilson leather grain with white lacing, brushed gold, architectural foam board, and mixed-media grit.
- **Color Palette**: 
  - Official Laurier Purple: `#3D1152`
  - Laurier Athletic Gold: `#F2A900`
  - Metallic Gold Accent: `#FFB81C`
  - Deep Charcoal/Void: `#0D0A12`
  - Pure White: `#FFFFFF`
- **Zero Generic Work**: Every graphic must look like it belongs on ESPN, Nike Football, or the Big Ten Network. Never produce flat, corporate, or lifeless designs.

---

## 4. Zero-Glitch Quality Control (Mandatory Inspection)
- **Mandatory `view_file` Visual Audit**: Every still, render, or graphic MUST be visually inspected and verified with `view_file` BEFORE presenting to the user.
- **Contact Shadow Inspection**: Verify that every object makes clean, grounded contact with its shadow caster, with zero gap ("floating") and zero penetration ("sinking").
- **No Raw Faceted Meshes**: All curved surfaces (pedestals, cylinders, helmet shells) MUST have smooth shading (`use_smooth = True`) and appropriate bevel/subdivision modifiers.
