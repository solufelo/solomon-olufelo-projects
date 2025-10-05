# Add-on Preset Manager - Integration Guide & UI Mockup

## 🎨 Visual UI Layout Preview

Here's how the preset manager panel will appear in Blender's Preferences:

```
┌─ Blender Preferences ──────────────────────────────────────┐
│ File █ Edit █ Render █ Window █ Help                      │
├────────────────────────────────────────────────────────────┤
│ Add-ons                                                   │
│ ├─ Categories                                            │
│ │  ├─ All Add-ons                                        │
│ │  ├─ Import-Export                                      │
│ │  └─ Your Category                                      │
│ │                                                         │
│ ├─ Your Add-on Name                                      │
│ │  ☑ Enable                                              │
│ │                                                         │
│ │  ┌─ Add-on Preset Manager ─────────────┐                │
│ │  │ Preset: [Select Preset        ▼]    │                │
│ │  │                                     │                │
│ │  │ ┌─ Save Current as Preset ─────────┐ │                │
│ │  │ └──────────────────────────────────┘ │                │
│ │  │                                     │                │
│ │  │ ┌─ Apply Preset ────────────────────┐ │                │
│ │  │ └──────────────────────────────────┘ │                │
│ │  │                                     │                │
│ │  │ ┌─ Revert to Previous State ───────┐ │                │
│ │  │ └──────────────────────────────────┘ │                │
│ │  │                                     │                │
│ │  │ ┌─ Rename ─┐ ┌─ Delete ─┐           │                │
│ │  │ └──────────┘ └──────────┘           │                │
│ │  │                                     │                │
│ │  │ ┌─ Refresh List ────────────────────┐ │                │
│ │  │ └──────────────────────────────────┘ │                │
│ │  │                                     │                │
│ │  │ ┌─ Preset Info ─────────────────────┐ │                │
│ │  │ │ ℹ️ Preset Info:                   │ │                │
│ │  │ │ • Modeling Setup: 3 add-ons      │ │                │
│ │  │ │ • Animation Setup: 2 add-ons     │ │                │
│ │  │ │ • Rendering Setup: 3 add-ons     │ │                │
│ │  │ └──────────────────────────────────┘ │                │
│ │  │                                     │                │
│ │  │ ┌─ ⚠️ Warning ──────────────────────┐ │                │
│ │  │ │ ⚠️ Warning: Applying a preset     │ │                │
│ │  │ │ will change your current          │ │                │
│ │  │ │ add-on configuration!             │ │                │
│ │  │ └──────────────────────────────────┘ │                │
│ │  └─────────────────────────────────────┘                │
│ └─────────────────────────────────────────────────────────┤
└────────────────────────────────────────────────────────────┘
```

## 🚀 Step-by-Step Integration

### Step 1: File Integration
```python
# Option A: Direct Integration (Recommended)
# Copy the entire addon_preset_manager.py content into your main add-on file

# Option B: Modular Integration
# Keep as separate file and import it
from . import addon_preset_manager
```

### Step 2: Update Your Register Function
```python
def register():
    # Your existing registration code...
    bpy.utils.register_class(YourExistingClass)
    
    # Add preset manager registration
    register_preset_manager()
    
    print("Your Add-on: Registered successfully")
```

### Step 3: Update Your Unregister Function
```python
def unregister():
    # Your existing unregistration code...
    bpy.utils.unregister_class(YourExistingClass)
    
    # Add preset manager unregistration
    unregister_preset_manager()
    
    print("Your Add-on: Unregistered")
```

### Step 4: Update Your Classes List
```python
# Your existing classes
your_classes = [
    YourExistingClass,
    AnotherClass,
    # ... other classes
]

# Add preset manager classes
classes = your_classes + preset_manager_classes

# Or use the spread operator
classes = [
    *your_classes,
    *preset_manager_classes,
]
```

### Step 5: Customize the Panel (Optional)
```python
# In ADDON_PT_preset_manager class, modify:
class ADDON_PT_preset_manager(Panel):
    bl_label = "Add-on Preset Manager"  # Change this title
    bl_parent_id = "ADDON_PT_your_main_panel"  # Set to your main panel ID
    
    # Or remove bl_parent_id to make it standalone:
    # bl_parent_id = ""  # Remove this line for standalone panel
```

## 🎯 Usage Workflow

### Creating Your First Preset:
1. Enable the add-ons you want for a specific workflow (e.g., modeling)
2. Go to `Edit > Preferences > Add-ons`
3. Find your add-on and locate the "Add-on Preset Manager" panel
4. Click "Save Current as Preset"
5. Enter a name like "Modeling Workflow"
6. Click OK

### Applying a Preset:
1. Select a preset from the dropdown
2. Click "Apply Preset"
3. All add-ons will be disabled, then only preset add-ons enabled
4. Check console for any warnings about missing add-ons

### Managing Presets:
- **Rename**: Select preset → Click "Rename" → Enter new name
- **Delete**: Select preset → Click "Delete" → Confirm deletion
- **Revert**: Click "Revert to Previous State" to undo last preset application

## 📁 File Structure After Integration

```
your_addon/
├── __init__.py                 # Main add-on file (includes preset manager)
├── your_addon.py              # Your existing add-on code
├── addon_presets.json         # Auto-created preset storage file
└── README.md                  # Your documentation
```

## 🔧 Advanced Customization Options

### Custom Preset Storage Location
```python
def get_presets_file_path():
    # Store in user's config directory instead of add-on directory
    config_dir = user_resource('CONFIG')
    return os.path.join(config_dir, "your_addon_presets.json")
    
    # Or store in a specific folder
    # return os.path.join(os.path.expanduser("~"), "BlenderPresets", "your_presets.json")
```

### Custom Panel Layout
```python
def draw(self, context):
    layout = self.layout
    props = context.scene.addon_preset_props
    
    # Custom header
    box = layout.box()
    box.label(text="🎯 Quick Preset Switching", icon='GAME')
    
    # Horizontal preset selection
    row = layout.row(align=True)
    row.prop(props, "selected_preset", text="")
    row.operator("addon.apply_preset", text="Apply", icon='PLAY')
    
    # Compact management buttons
    row = layout.row(align=True)
    row.operator("addon.save_current_as_preset", text="Save", icon='FILE_TICK')
    row.operator("addon.refresh_presets", text="", icon='FILE_REFRESH')
```

### Add Hotkey Support (Future Enhancement)
```python
# In your add-on's register function:
addon_keymaps = []

def register():
    # ... existing code ...
    
    # Register hotkey for quick preset switching
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')
        kmi = km.keymap_items.new("addon.apply_preset", 'P', 'PRESS', ctrl=True, shift=True)
        addon_keymaps.append((km, kmi))

def unregister():
    # ... existing code ...
    
    # Remove hotkey
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
```

## 🐛 Troubleshooting

### Common Issues:

1. **Panel Not Appearing**
   - Check that `bl_parent_id` matches your main panel ID
   - Verify the panel is registered in your classes list

2. **Presets Not Saving**
   - Check file permissions in your add-on directory
   - Verify JSON file creation in console output

3. **Add-ons Not Enabling**
   - Check console for error messages
   - Some add-ons may require specific conditions to enable

4. **Previous State Not Working**
   - Ensure you apply a preset first to save the previous state
   - Check that the JSON string is being saved correctly

### Debug Mode:
Add this to see detailed console output:
```python
# In any operator's execute method:
print(f"Debug: Current add-ons: {get_current_addon_state()}")
print(f"Debug: Preset add-ons: {preset_addons}")
```

## 🎉 Ready to Use!

The preset manager is now fully integrated and ready to use. Users can:
- Save their current add-on configuration as named presets
- Quickly switch between different workflows
- Revert changes if needed
- Manage their preset library

This will significantly improve the user experience by allowing quick setup changes for different types of work in Blender!
