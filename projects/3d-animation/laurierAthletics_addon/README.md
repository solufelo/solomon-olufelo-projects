# 🏈 Laurier Football Shell Game - Blender Addon

A professional Blender 4.5+ addon for creating stunning 3D shell game shuffle animations for Laurier Football promos. Features smooth helmet movements, dramatic reveals, and cinematic camera work with an intuitive user interface.

## ✨ Features

- **🎛️ Intuitive UI Panel** - Easy-to-use controls in Blender's 3D Viewport sidebar
- **⚡ Preset Configurations** - Quick setup with professional presets
- **🎬 Cinematic Quality** - Smooth sine-wave movements with realistic bounce
- **📹 Camera Integration** - Automatic camera sway for dynamic shots
- **🎲 Smart Randomization** - Randomize football location for variety
- **⚙️ Full Customization** - Fine-tune every aspect of the animation
- **🎯 Scene Validation** - Built-in error checking and helpful feedback

## 📦 Installation

### Method 1: Install from Zip File (Recommended)
1. Download `laurier_football_shell_game_v1.0.0.zip`
2. Open Blender 4.5+
3. Go to `Edit > Preferences > Add-ons`
4. Click `Install...` and select the zip file
5. Enable "Laurier Football Shell Game" in the add-on list
6. The addon will appear in the 3D Viewport sidebar under "Laurier Football"

### Method 2: Install from Folder
1. Download the `blender_addon` folder
2. Open Blender 4.5+
3. Go to `Edit > Preferences > Add-ons`
4. Click `Install...` and select the `blender_addon` folder
5. Enable "Laurier Football Shell Game" in the add-on list
6. The addon will appear in the 3D Viewport sidebar under "Laurier Football"

### Method 3: Manual Installation
1. Copy the `blender_addon` folder to your Blender add-ons directory:
   - **Windows**: `%APPDATA%\Blender Foundation\Blender\4.5\scripts\addons\`
   - **macOS**: `~/Library/Application Support/Blender Foundation/Blender/4.5/scripts/addons/`
   - **Linux**: `~/.config/blender/4.5/scripts/addons/`
2. Restart Blender
3. Enable the addon in `Edit > Preferences > Add-ons`

## 🚀 Quick Start

### 1. Scene Setup
Before using the addon, set up your Blender scene:

```
Required Objects:
├── Empty_1 (for left helmet)
├── Empty_2 (for center helmet)  
├── Empty_3 (for right helmet)
└── Football_CTRL (for football)

Setup Steps:
1. Import your helmet and football models
2. Create the four empty objects listed above
3. Parent each helmet to its corresponding empty
4. Parent the football to Football_CTRL
5. Position the empties side-by-side
6. Set up camera and lighting
```

### 2. Using the Addon
1. Open the 3D Viewport
2. Press `N` to open the sidebar (or go to `View > Sidebar`)
3. Click the "Laurier Football" tab
4. Choose a preset or customize settings
5. Click "Create Shell Game Animation"
6. Preview your animation!

## 🎛️ User Interface

### Main Panel
The addon creates a dedicated panel in the 3D Viewport sidebar with:

- **🏈 Header** - Addon branding and version info
- **📋 Preset Selection** - Choose from 6 professional presets
- **⚙️ Custom Controls** - Fine-tune settings when "Custom" is selected
- **▶️ Create Button** - Generate the animation
- **📊 Info Display** - Show current settings and frame count

### Available Presets

| Preset | Duration | Best For | Characteristics |
|--------|----------|----------|-----------------|
| **Quick & Snappy** | 5s | Fast content | High speed, tight movements |
| **Dramatic & Slow** | 12s | Cinematic | Slow, dramatic movements |
| **Social Media** | 3s | Instagram/TikTok | High energy, quick cuts |
| **Broadcast Quality** | 8s | TV/Web | Balanced, professional |
| **Minimal & Clean** | 6s | Subtle effects | Clean, minimal movement |
| **High Energy** | 4s | Exciting content | Fast, bouncy movements |

## ⚙️ Custom Settings

When "Custom" preset is selected, you can adjust:

### Animation Settings
- **Duration** - Total animation length (1-30 seconds)
- **FPS** - Frame rate (12-60 fps)
- **Shuffle Speed** - Movement speed (0.5-10.0)
- **Shuffle Cycles** - Number of shuffle patterns (1-20)

### Movement Settings
- **Shuffle Amplitude** - Horizontal movement range (0.1-10.0)
- **Vertical Bounce** - Bounce height (0.0-2.0)
- **Spacing Buffer** - Distance between helmets (0.5-5.0)

### Reveal Settings
- **Reveal Target** - Which helmet hides football (1, 2, or 3)
- **Reveal Duration** - How long reveal takes (0.5-5.0s)
- **Reveal Height** - How high helmet lifts (0.1-3.0)

### Effects
- **Camera Sway** - Add subtle camera movement
- **Sway Amount** - Intensity of camera movement (0.0-1.0)
- **Ease Out** - Slow down before reveal
- **Ease Duration** - How long ease-out lasts (0.1-3.0s)
- **Randomize Target** - Randomly choose football location

## 🎬 Workflow

### 1. Pre-Production
```
Scene Preparation:
├── Import helmet and football models
├── Create required empty objects
├── Set up parenting relationships
├── Position objects appropriately
├── Configure lighting setup
└── Set camera framing
```

### 2. Animation Creation
```
Using the Addon:
├── Open 3D Viewport sidebar
├── Navigate to "Laurier Football" tab
├── Choose preset or customize settings
├── Click "Create Shell Game Animation"
├── Preview in viewport
└── Adjust settings if needed
```

### 3. Post-Production
```
Rendering & Compositing:
├── Set render output directory
├── Configure render settings
├── Render PNG sequence with alpha
├── Import into After Effects
├── Add motion blur and color grading
├── Add titles and graphics
└── Export final video
```

## 🛠️ Technical Details

### Requirements
- **Blender 4.5+** (tested on 4.5.0)
- **Python 3.10+** (included with Blender)
- **Scene Setup** - Proper object naming and parenting

### Architecture
The addon is built with:
- **Property Groups** - Store settings in scene data
- **Operator Classes** - Handle animation creation
- **Panel Classes** - Create user interface
- **Animation Engine** - Core animation logic

### Performance
- **Optimized** - Efficient keyframe generation
- **Memory Safe** - Proper cleanup and error handling
- **Scalable** - Works with complex scenes

## 🐛 Troubleshooting

### Common Issues

**"Required object not found"**
- Ensure empty objects exist with exact names
- Check that objects are not hidden or in different collections
- Verify parenting relationships are correct

**Animation not working**
- Check that helmets are properly parented to empties
- Ensure football is parented to Football_CTRL
- Verify scene has proper lighting and camera

**Poor performance**
- Reduce animation duration for testing
- Lower FPS for faster preview
- Simplify scene geometry if needed

**UI Panel not visible**
- Ensure addon is enabled in Preferences
- Check that sidebar is open (press N)
- Look for "Laurier Football" tab in sidebar

### Getting Help
1. Check the setup requirements in the UI panel
2. Verify all required objects exist in your scene
3. Try different presets to isolate issues
4. Check Blender's console for error messages

## 📁 File Structure

```
laurierAthletics_addon/
├── blender_addon/
│   └── __init__.py          # Main addon file
├── README.md                # This documentation
├── INSTALLATION.md          # Detailed installation guide
└── examples/
    ├── sample_scene.blend   # Example scene setup
    └── presets_demo.blend   # Preset demonstrations
```

## 🔮 Future Updates

### Version 1.1 (Planned)
- **Particle Effects** - Dust clouds on impacts
- **Sound Integration** - Audio cues and timing
- **Multiple Cameras** - Automatic camera switching
- **Export Options** - Direct video export

### Version 1.2 (Planned)
- **Advanced Easing** - More motion curve options
- **Batch Processing** - Multiple animation variants
- **Template System** - Save/load custom presets
- **Real-time Preview** - Live animation preview

## 👨‍💻 Author & Support

**Solomon Olufelo**  
Student ID: 210729170  
Email: oluf9170@mylaurier.ca  
SASP Program - Laurier University

### Support
- 📧 Email: oluf9170@mylaurier.ca
- 🐛 Issues: Report bugs via email
- 💡 Features: Request new features via email

## 📝 License

This addon is created for Laurier Athletics promotional use. All rights reserved.

---

**Ready to create professional football animations? 🏈✨**

Install the addon and start creating stunning Laurier Football promos with just a few clicks!
