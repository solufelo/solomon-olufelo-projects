# Claude Code Assistant Guidelines - Solomon Olufelo Vault

## 🧠 System Orientation & Master Vault Linkage
- **Primary Source of Truth**: Consult `VAULT_INDEX.md` and `PROJECT_STATUS.md` at the repository root before making changes.
- **Active Node**: Laurier Athletics Videoboard & Wolfpack Shuffle 3D Suite (Blender 5.2.1 LTS Addon `v3.4.0`) located in `projects/3d-animation/laurierAthletics_addon/`.
- **Employment Context**: Solomon Olufelo is employed as a Student Video Assistant (`ST1086-01`, `H00209`) at Wilfrid Laurier University Athletics & Recreation, earning **CA$19.03/hr** with an authorized **40 hours/week cap** from supervisor Hailey Tripodi ($1,522.40 gross bi-weekly).
- **Academic Context**: Fall 2026 undergraduate classes begin **Thursday, September 10, 2026**. Sept 8-9 are O-Week/orientation (no classes).
- **Game Kickoff**: First Laurier home football game is this coming weekend (September 12–13, 2026).

---

## 🛠️ Common Build & Test Commands

### Blender 5.2.1 Addon Testing & Verification
```powershell
# Run the automated validation test suite inside Blender headless:
& "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" -b --python "projects\3d-animation\laurierAthletics_addon\test_addon.py"

# Test addon installation from release zip:
& "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" -b --python-expr "import bpy; bpy.ops.preferences.addon_install(filepath=r'projects\3d-animation\laurierAthletics_addon\laurier_wolfpack_shuffle_v3.4.0.zip'); bpy.ops.preferences.addon_enable(module='wolfpack_shuffle'); print('Addon enabled:', 'wolfpack_shuffle' in bpy.context.preferences.addons)"
```

### Git Repository Operations
```powershell
# Check status
git status

# Commit changes following project conventions:
git add <files>
git commit -m "feat(3d-addon): description of change"
git push origin main
```

---

## 📐 Architecture & Key Design Rules

### 1. Broadcast Sandwich Layout (Wolfpack Shuffle Addon v3.4.0)
- **Problem Solved**: Standard camera perspective views collapsed 3D title text onto the same plane as the hero text, causing overlap and visual collision.
- **Solution**: The Broadcast Sandwich:
  - **Eyebrow Kicker**: `"THE ULTIMATE CHALLENGE"` positioned at local `+Y = +0.58m`, scale `0.46`.
  - **Center Hero**: `"GOLDEN HAWKS SHUFFLE"` centered at `Y = 0.00m`, scale `0.68`.
  - **Sponsor Anchor**: `"PRESENTED BY WILFRID LAURIER ATHLETICS"` anchored at `-Y = -0.58m`, scale `0.38`.
  - **Camera Normal Pitch**: Rotated base text container `61.74°` to squarely face the `Shuffle_Camera` sightline vector, eliminating perspective distortion and maintaining clean vertical air gaps.

### 2. Symmetrical Centered Text Exits
- Four broadcast styles: `BURST_FORWARD` (hero forward punch), `CENTER_IMPLODE` (scale collapse), `DROP_DOWN` (gravity slam), and `LIFT_UP` (celestial float).
- Always lock `X = 0.0` and `rot_z = 0.0°`. Never introduce asymmetric rightward tilt.

### 3. Modular 5-Stage UI Panel System
- The Blender N-Panel is tabbed into 5 workflows:
  1. `All Sections`
  2. `1. Presentation` (Titles, Slogans, Scoreboard Stingers)
  3. `2. Arena & Lights` (Turf, Floodlights, Volumetrics)
  4. `3. Shuffle & Game` (Helmets, Swapping speed, Hat tricks)
  5. `4. Render & Sync` (ProRes 422, H.264, SMPTE cue sheets)

### 4. Timesheet & Documentation Hygiene
- Ensure all work hours are recorded in `projects/3d-animation/laurierAthletics_addon/LAURIER_TIMESHEET_LOG.md`.
- Keep bidirectional links between documents (`[[VAULT_INDEX.md]]`).
- Preserve all existing comments and documentation.
