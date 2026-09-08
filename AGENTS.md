# Universal AI Agent Specification (AGENTS.md)

This file instructs all AI coding agents operating within Solomon Olufelo's engineering vault (`solomon-olufelo-projects`).

---

## 🧭 System Orientation & State Synchronization

Whenever an agent begins a task in this workspace:
1. **Source of Truth**: Read [[VAULT_INDEX.md|VAULT_INDEX.md]] first.
2. **Tactical Board**: Read [[PROJECT_STATUS.md|PROJECT_STATUS.md]] for current sprint blockers, deliverables, and test criteria.
3. **Active Project**: **Laurier Athletics Videoboard & Wolfpack Shuffle 3D Suite (v3.4.0)** in `projects/3d-animation/laurierAthletics_addon/`.
4. **Current Environment**:
   - OS: Windows 11
   - Blender: 5.2.1 LTS (`C:\Program Files\Blender Foundation\Blender 5.2\blender.exe`)
   - Addon path: `%APPDATA%\Blender Foundation\Blender\5.2\scripts\addons\wolfpack_shuffle\`
   - Active Git Branch: `main`

---

## 💼 Employment & Payroll Protocol

- **Institution**: Wilfrid Laurier University, Waterloo, Ontario.
- **Position**: Video Assistant (`ST1086-01`, Position `H00209`), Department of Athletics and Recreation.
- **Supervisor**: Hailey Tripodi (`Tripodi, Hailey R.`).
- **Approved Pay Rate**: **CA$19.030000 / hour**.
- **Student Work Cap**: **40.00 hours per week maximum** (Approved by Hailey Tripodi: *"your student cap is 40, so don't go over that, please. If it rolls into next pay, that's fine"*).
- **Target Gross Pay**: $761.20 / week → **$1,522.40 gross per bi-weekly pay cycle**.
- **LORIS Timesheet Submission Protocol**:
  - Log entries daily in LORIS Employee Self-Service.
  - Maintain audit trail in [[projects/3d-animation/laurierAthletics_addon/LAURIER_TIMESHEET_LOG.md|LAURIER_TIMESHEET_LOG.md]].
  - Submission hard deadline for Pay Period 1 (08/23 - 09/05): **Wednesday, September 9, 2026, 11:59 PM**.

---

## 🎓 Academic Schedule Context

- Wilfrid Laurier University Fall 2026 term starts **Thursday, September 10, 2026**.
- September 8–9 are Orientation / O-Week. No classes are held.
- Transportation: Solomon's car is out of commission; avoid unnecessary campus commuting prior to Thursday to conserve travel costs.

---

## 📐 Engineering & 3D Motion Graphics Standards

1. **Broadcast Sandwich Layout**:
   - Never place title and subtitle texts on identical coordinates or let them overlap in camera perspective.
   - Use the camera-normal pitch angle (`61.74°` for camera at `Z = 4.0m, Y = -8.0m`) with 3 vertical tiers:
     - Upper Kicker (`+Y = +0.58m`)
     - Center Hero (`Y = 0.00m`)
     - Lower Sponsor (`-Y = -0.58m`)
2. **Symmetrical Centered Exits**:
   - Avoid rightward skewing exit animations. Keep exits centered with `X = 0.0` and `rot_z = 0.0°`.
3. **Modular Addon Organization**:
   - Maintain the 5-stage UI workflow: Presentation, Arena & Lights, Shuffle & Game, Render & Sync.
4. **Color Calibration**:
   - Golden Hawks Gold: `#FDB913`
   - Deep Purple: `#20003B`
   - APL Protection: Do not use pure white strokes on LED stadium videoboards.
