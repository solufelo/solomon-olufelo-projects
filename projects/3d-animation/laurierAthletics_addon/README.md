# 🏈 Laurier Athletics Videoboard & Wolfpack Shuffle 3D Suite (v3.4.0)

> **Master Vault Hub**: [[../../VAULT_INDEX.md|Root Vault Index]] | [[PROJECT_STATUS.md|Active Status]]  
> **Timesheet & LORIS Log**: [[LAURIER_TIMESHEET_LOG.md|LAURIER_TIMESHEET_LOG.md]]  
> **Production Blueprint & Behance Case Study**: [[PRODUCTION_SET_DESIGN_BLUEPRINT.md|Set Design Blueprint]]  
> **Changelog**: [[CHANGELOG.md|Release History]]  
> **Latest Release Archive**: `laurier_wolfpack_shuffle_v3.4.0.zip`

A professional broadcast-grade 3D motion graphics suite and Blender 5.2+ addon engineered for Wilfrid Laurier University Athletics (Laurier Golden Hawks / Wolfpack Glory). Automates stadium jumbotron animations, helmet shell game shuffles, scoring stingers, and sponsor integrations for live collegiate football productions at University Stadium.

---

## ✨ What's New in v3.4.0 (Broadcast Production Release)

### 🥪 1. Broadcast Sandwich Layout (Camera Overlap Fixed)
* **Problem**: In standard perspective camera views, titles, kickers, and sponsor tags collapsed onto the same visual plane, creating messy polygon collisions and illegible text overlaps.
* **Solution**: Three-tiered vertical stratum pitched directly along the camera sightline vector (`61.74°`):
  * **Top Eyebrow Kicker**: `"THE ULTIMATE CHALLENGE"` (`+Y = +0.58m`, scale `0.46`).
  * **Center Hero**: `"GOLDEN HAWKS SHUFFLE"` (`Y = 0.00m`, scale `0.68`).
  * **Bottom Sponsor**: `"PRESENTED BY WILFRID LAURIER ATHLETICS"` (`-Y = -0.58m`, scale `0.38`).
* **Result**: Clean `0.26+` screen-height air gaps with zero overlap across all focal lengths.

### 🎯 2. Symmetrical Centered Text Exits
* Replaced asymmetric rightward drift with 4 broadcast-grade centered exit animations:
  * `BURST_FORWARD`: Hero text surges dynamically toward camera with smooth dissolve.
  * `CENTER_IMPLODE`: Kinetic inward scale collapse to zero.
  * `DROP_DOWN`: Heavy gravitational drop through turf plane.
  * `LIFT_UP`: Majestic skyward ascent off the top frame.
* Strictly locked horizontal translation (`X = 0.0`) and rotation (`rot_z = 0.0°`).

### 🎛️ 3. Modular 5-Stage UI Panel Architecture
Reorganized the 2,357-line production script into 5 intuitive workflow tabs in the Blender N-Panel:
1. `All Sections`: Complete master console.
2. `1. Presentation`: Entry bumpers, 3D titles, stadium slogans, and scoring stingers.
3. `2. Arena & Lights`: Turf shader, floodlights, volumetric scattering, and sky dome.
4. `3. Shuffle & Game`: Helmet rigging, continuous non-linear orbital math, and game logic.
5. `4. Render & Sync`: 1-click Apple ProRes 422 / H.264 exports and SMPTE cue sheet generation.

### 💡 4. Volumetric Lighting & Atmospheric Moods
* **4 Curated Mood Presets**:
  * `Night Game Volumetric`: Crisp 5800K halogen floodlight banks, high-angle Gold & Deep Purple rim kickers.
  * `Golden Sunset`: Warm 3200K low-angle sunburst with long turf shadows.
  * `Halftime Blackout`: Cyber violet/magenta flood wash with laser gold rims.
  * `Clean Studio`: Neutral, balanced commercial presentation.
* **Procedural Volumetric Scattering**: $36\text{m} \times 36\text{m} \times 15\text{m}$ Principled Volume domain delivering visible stadium floodlight beams and god rays.

### 🚀 5. Pure Blender 1-Click Broadcast Render Pipeline
* Directly render broadcast deliverables without risking After Effects crashes or corruption:
  * **Apple ProRes 422 QuickTime (`.mov`)**: Ready for direct playback on Daktronics / Click Effects / Ross XPression stadium control systems.
  * **Apple ProRes 4444 RGBA (`.mov`)**: Transparent alpha channel for live camera overlays.
  * **H.264 Lossless MP4 (`.mp4`)**: Web and mobile review copies.

---

## 📦 Installation & Setup

### Method 1: Automatic Pre-Installation (Installed in Environment)
The addon is already pre-installed and activated in Blender 5.2.1 LTS user preferences:
```
%APPDATA%\Blender Foundation\Blender\5.2\scripts\addons\wolfpack_shuffle\
```

### Method 2: Install from Zip File
1. Locate `laurier_wolfpack_shuffle_v3.4.0.zip` (available in this repository folder, or on Desktop/Downloads).
2. Open Blender 5.2+.
3. Open `Edit > Preferences > Add-ons`.
4. Click the arrow in the top right > `Install from Disk...`.
5. Select `laurier_wolfpack_shuffle_v3.4.0.zip`.
6. Enable the checkbox for **"Laurier Athletics - Wolfpack Shuffle 3D Suite"**.
7. Press `N` in the 3D Viewport to open the sidebar and navigate to the **Laurier Football** tab.

---

## 🧪 Automated Testing & Validation

Run the headless verification suite to confirm all 18 production checks pass:
```powershell
& "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" -b --python "projects\3d-animation\laurierAthletics_addon\test_addon.py"
```

---

## ⏱️ Employment & Timesheet Reference
* **Student Video Assistant**: Solomon Olufelo (`ST1086-01`, Position `H00209`)
* **Department**: Athletics and Recreation, Wilfrid Laurier University
* **Supervisor**: Hailey Tripodi (`Tripodi, Hailey R.`)
* **Hourly Wage**: **CA$19.030000 / hour**
* **Work Cap**: **40.00 hours/week maximum** (Authorized by Hailey Tripodi)
* **Full Hours Audit & LORIS Breakdown**: [[LAURIER_TIMESHEET_LOG.md|LAURIER_TIMESHEET_LOG.md]]
