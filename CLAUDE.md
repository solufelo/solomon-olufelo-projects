# Claude Code Assistant Guidelines - Solomon Olufelo Vault

## 🧠 System Orientation & Master Framework
- **Master Strategic Framework**: Read `THE_SUPER_BOWL_4_PILLAR_SYSTEM.md` for Solomon's 4-pillar system:
  1. **The Body**: WLU gym before 8:30 AM, $0 Moses Springer lot, high energy.
  2. **The Degree**: 12 hrs/week budget, 10 courses left (Aug 2027), protect SAS GPA.
  3. **The Code**: C++ WASM in `light-years-game`, ImGui tool, Python/Blender AAA tool.
  4. **The Radar**: Connect with Rockstar Oakville Tools Leads, 20s build clips on LinkedIn, US Dual Citizen.
- **Single Source of Truth**: Consult `VAULT_INDEX.md` and `PROJECT_STATUS.md`.
- **Active Node**: Laurier Athletics & Rockstar Spec 3D Suite (Blender 5.2.1 LTS Addon `v3.5.0`) in `projects/3d-animation/laurierAthletics_addon/`.
- **Employment Context**: Video Assistant (`ST1086-01`, `H00209`) at Wilfrid Laurier University Athletics, **CA$19.03/hr** with **40h/week cap** from Hailey Tripodi ($1,522.40 gross bi-weekly).

---

## 🛠️ Common Build & Test Commands

### Blender 5.2.1 Addon Testing & Headless Batch Execution
```powershell
# Run the automated 8-test validation suite inside Blender headless:
& "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" -b --python "projects\3d-animation\laurierAthletics_addon\test_addon.py"

# Run the headless studio batch runner:
& "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" -b --python "projects\3d-animation\laurierAthletics_addon\pipeline_batch_runner.py" -- --swaps 5 --preset NIGHT_GAME_FLOODLIGHT --outcome SLOT_2 --export-tracks --benchmark
```

### Git Operations
```powershell
git add <files>
git commit -m "feat(studio-tools): description"
git push origin main
```

---

## 📐 Architecture & Key Design Rules (Rockstar Spec)
1. **Game Engine Animation Track Serialization**: Extracts per-frame unit quaternions $[w, x, y, z]$, velocity vectors, and gameplay event markers to `wolfpack_anim_tracks.json` with coordinate swizzling.
2. **Microsecond Telemetry Profiling**: Measures bake time in milliseconds ($<120\,\text{ms}$), keyframe throughput ($>25,000\,\text{keys/s}$), and memory delta ($<0.2\,\text{MB}$) with zero leaks.
3. **3D Motion Trajectory Arcs**: Viewport splines with color-coded emission materials for Technical Artists.
4. **Broadcast Sandwich Layout**: 3-tier typography pitched at `61.74°` along active camera normal with zero perspective overlap.
5. **Centered Exits**: All exits locked to $X = 0.0$ and $\text{rot}_z = 0.0^\circ$.
