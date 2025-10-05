# 🏈 Installation Guide - Laurier Football Shell Game Addon

Complete step-by-step installation guide for the Laurier Football Shell Game Blender addon.

## 📋 System Requirements

### Software Requirements
- **Blender 4.5+** (tested on 4.5.0)
- **Windows 10/11, macOS 10.15+, or Linux** (Ubuntu 20.04+ recommended)
- **4GB RAM minimum** (8GB recommended for complex scenes)
- **2GB free disk space** for addon and temporary files

### Hardware Requirements
- **Graphics Card** - OpenGL 3.3 compatible
- **CPU** - Multi-core processor recommended
- **Monitor** - 1920x1080 minimum resolution

## 🚀 Installation Methods

### Method 1: Install from Folder (Recommended)

#### Step 1: Download the Addon
1. Download or clone the `blender_addon` folder
2. Ensure the folder contains `__init__.py` file
3. Keep the folder structure intact

#### Step 2: Install in Blender
1. **Open Blender 4.5+**
2. **Go to Edit > Preferences** (or press `Ctrl+Alt+U` / `Cmd+Opt+U`)
3. **Click on "Add-ons" tab** in the left sidebar
4. **Click "Install..." button** at the top
5. **Navigate to and select the `blender_addon` folder**
6. **Click "Install Add-on"**
7. **Find "Laurier Football Shell Game" in the list**
8. **Check the checkbox to enable the addon**
9. **Close Preferences**

#### Step 3: Verify Installation
1. **Open 3D Viewport**
2. **Press `N` to open sidebar** (or View > Sidebar)
3. **Look for "Laurier Football" tab** in the sidebar
4. **If visible, installation successful!**

### Method 2: Manual Installation

#### Windows Installation
1. **Navigate to addons directory:**
   ```
   %APPDATA%\Blender Foundation\Blender\4.5\scripts\addons\
   ```

2. **Copy the `blender_addon` folder** to this directory

3. **Restart Blender**

4. **Enable addon in Preferences > Add-ons**

#### macOS Installation
1. **Navigate to addons directory:**
   ```
   ~/Library/Application Support/Blender Foundation/Blender/4.5/scripts/addons/
   ```

2. **Copy the `blender_addon` folder** to this directory

3. **Restart Blender**

4. **Enable addon in Preferences > Add-ons**

#### Linux Installation
1. **Navigate to addons directory:**
   ```
   ~/.config/blender/4.5/scripts/addons/
   ```

2. **Copy the `blender_addon` folder** to this directory

3. **Restart Blender**

4. **Enable addon in Preferences > Add-ons**

## ✅ Post-Installation Setup

### 1. Scene Preparation Checklist
Before using the addon, ensure your scene has:

```
Required Objects:
□ Empty_1 (for left helmet)
□ Empty_2 (for center helmet)
□ Empty_3 (for right helmet)
□ Football_CTRL (for football)
□ Camera (positioned appropriately)
□ Lighting setup

Parenting Relationships:
□ Helmet 1 parented to Empty_1
□ Helmet 2 parented to Empty_2
□ Helmet 3 parented to Empty_3
□ Football parented to Football_CTRL

Scene Setup:
□ Objects positioned side-by-side
□ Proper spacing between helmets
□ Camera framing configured
□ Materials and textures applied
```

### 2. First Use Test
1. **Open the Laurier Football panel** in 3D Viewport sidebar
2. **Select "Broadcast Quality" preset**
3. **Click "Create Shell Game Animation"**
4. **Check for error messages** in the UI panel
5. **Preview animation** in viewport

## 🔧 Troubleshooting Installation

### Addon Not Appearing in List
**Problem:** Addon doesn't show up in Preferences > Add-ons

**Solutions:**
1. **Check folder structure** - Ensure `__init__.py` is in the root of the addon folder
2. **Verify Blender version** - Must be 4.5 or higher
3. **Restart Blender** completely
4. **Check file permissions** - Ensure Blender can read the addon files
5. **Try manual installation** method instead

### Addon Enabled But Panel Not Visible
**Problem:** Addon is enabled but "Laurier Football" tab doesn't appear

**Solutions:**
1. **Check sidebar is open** - Press `N` or go to View > Sidebar
2. **Switch to 3D Viewport** - Panel only appears in 3D Viewport
3. **Scroll through tabs** - Tab might be hidden if sidebar is narrow
4. **Restart Blender** and re-enable addon
5. **Check for error messages** in Blender's console

### Python Errors on Installation
**Problem:** Python errors when enabling addon

**Solutions:**
1. **Update Blender** to latest 4.5.x version
2. **Check Python compatibility** - Addon requires Python 3.10+
3. **Clear Blender cache** - Delete temp files and restart
4. **Check file corruption** - Re-download addon files
5. **Run Blender as administrator** (Windows) or with sudo (Linux/macOS)

### Performance Issues
**Problem:** Addon works but causes Blender to lag

**Solutions:**
1. **Reduce animation duration** for testing
2. **Lower FPS setting** in addon panel
3. **Simplify scene geometry** if using complex models
4. **Close other applications** to free up RAM
5. **Update graphics drivers**

## 📞 Getting Help

### Before Asking for Help
1. **Check this installation guide** thoroughly
2. **Verify all requirements** are met
3. **Test with a simple scene** first
4. **Check Blender's console** for error messages
5. **Try different presets** to isolate issues

### When Reporting Issues
Include the following information:
- **Blender version** (Help > About Blender)
- **Operating system** and version
- **Installation method** used
- **Error messages** (if any)
- **Scene setup** (objects, parenting, etc.)
- **Steps to reproduce** the problem

### Contact Information
- **Email:** oluf9170@mylaurier.ca
- **Subject:** "Laurier Football Addon - [Issue Description]"

## 🔄 Updating the Addon

### Updating to New Version
1. **Disable current addon** in Preferences > Add-ons
2. **Remove old addon files** from addons directory
3. **Install new version** using Method 1 or 2 above
4. **Enable updated addon**
5. **Test functionality** with existing scenes

### Backup Your Settings
Before updating, consider backing up:
- **Custom presets** (if any)
- **Scene files** with addon-generated animations
- **Render settings** and output configurations

## 🎯 Next Steps

After successful installation:

1. **Read the main README.md** for usage instructions
2. **Set up a test scene** with required objects
3. **Try different presets** to understand options
4. **Experiment with custom settings**
5. **Create your first Laurier Football animation!**

---

**Installation complete? Time to create some magic! 🏈✨**

Head over to the main README.md for detailed usage instructions and start creating professional football animations.
