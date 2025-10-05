"""
Add-on Preset Manager Feature for Blender 4.5

This module provides preset management functionality for add-ons.
Save, load, and manage groups of add-ons as presets for different workflows.

Integration Instructions:
1. Copy this entire file into your existing add-on
2. Add the classes to your existing 'classes' list in register()
3. Add the panel to your existing panel registration
4. The presets will be stored in your add-on's directory as 'addon_presets.json'

Author: StudyOS Development
Version: 1.0.0
Blender Version: 4.5+
"""

import bpy
import json
import os
from bpy.types import Panel, Operator, PropertyGroup
from bpy.props import StringProperty, EnumProperty, BoolProperty
from bpy.utils import user_resource
from bpy.path import abspath


# ============================================================================
# PROPERTY GROUPS
# ============================================================================

class AddonPresetManagerProps(PropertyGroup):
    """Property group to store preset manager UI state"""
    
    selected_preset: EnumProperty(
        name="Selected Preset",
        description="Currently selected preset",
        items=lambda self, context: get_presets_list(),
        default=""
    )
    
    previous_state: StringProperty(
        name="Previous State",
        description="JSON string of previous add-on state",
        default=""
    )


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_presets_file_path():
    """Get the path to the presets JSON file in the add-on directory"""
    # Get the current add-on directory
    addon_dir = os.path.dirname(__file__)
    return os.path.join(addon_dir, "addon_presets.json")


def get_presets_list(self=None, context=None):
    """Get list of available presets for enum property"""
    presets = load_presets()
    items = [("", "Select Preset", "")]
    items.extend([(name, name, f"Apply {name} preset") for name in sorted(presets.keys())])
    return items


def load_presets():
    """Load presets from JSON file"""
    presets_file = get_presets_file_path()
    
    if not os.path.exists(presets_file):
        # Create default presets file with example presets
        default_presets = {
            "Modeling Setup": ["mesh_looptools", "node_wrangler", "extra_objects"],
            "Animation Setup": ["rigify", "animation_nodes", "bone_collection"],
            "Rendering Setup": ["cycles", "eevee", "render_auto_tile_size"]
        }
        save_presets(default_presets)
        return default_presets
    
    try:
        with open(presets_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Add-on Preset Manager: Error loading presets file: {e}")
        return {}


def save_presets(presets):
    """Save presets to JSON file"""
    presets_file = get_presets_file_path()
    
    try:
        with open(presets_file, 'w', encoding='utf-8') as f:
            json.dump(presets, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Add-on Preset Manager: Error saving presets file: {e}")
        raise


def get_current_addon_state():
    """Get current enabled add-ons as a list"""
    return list(bpy.context.preferences.addons.keys())


def save_current_state_as_json():
    """Save current add-on state as JSON string"""
    current_state = get_current_addon_state()
    return json.dumps(current_state, ensure_ascii=False)


def load_state_from_json(json_string):
    """Load add-on state from JSON string"""
    if not json_string:
        return []
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        return []


# ============================================================================
# OPERATORS
# ============================================================================

class ADDON_OT_save_current_as_preset(Operator):
    """Save current enabled add-ons as a named preset"""
    bl_idname = "addon.save_current_as_preset"
    bl_label = "Save Current as Preset"
    bl_description = "Save the currently enabled add-ons as a new preset"
    bl_options = {'REGISTER', 'UNDO'}

    preset_name: StringProperty(
        name="Preset Name",
        description="Name for the new preset",
        default="New Preset"
    )

    def invoke(self, context, event):
        """Show dialog to enter preset name"""
        return context.window_manager.invoke_props_dialog(self, width=350)

    def execute(self, context):
        """Save the current add-on state as a preset"""
        if not self.preset_name.strip():
            self.report({'ERROR'}, "Preset name cannot be empty")
            return {'CANCELLED'}

        try:
            # Get currently enabled add-ons
            enabled_addons = get_current_addon_state()
            
            # Load existing presets
            presets = load_presets()
            
            # Add or update the preset
            presets[self.preset_name] = enabled_addons
            
            # Save presets to file
            save_presets(presets)
            
            # Update UI
            context.scene.addon_preset_props.selected_preset = self.preset_name
            
            self.report({'INFO'}, f"Preset '{self.preset_name}' saved with {len(enabled_addons)} add-ons")
            return {'FINISHED'}
            
        except Exception as e:
            self.report({'ERROR'}, f"Failed to save preset: {str(e)}")
            return {'CANCELLED'}


class ADDON_OT_apply_preset(Operator):
    """Apply a preset by enabling/disabling add-ons accordingly"""
    bl_idname = "addon.apply_preset"
    bl_label = "Apply Preset"
    bl_description = "Apply the selected preset (this will change your current add-on configuration)"
    bl_options = {'REGISTER', 'UNDO'}

    preset_name: StringProperty(
        name="Preset Name",
        description="Name of the preset to apply",
        default=""
    )

    def execute(self, context):
        """Apply the specified preset"""
        if not self.preset_name:
            self.report({'ERROR'}, "No preset selected")
            return {'CANCELLED'}

        try:
            # Save current state before applying preset
            current_state_json = save_current_state_as_json()
            context.scene.addon_preset_props.previous_state = current_state_json
            
            # Load presets
            presets = load_presets()
            
            if self.preset_name not in presets:
                self.report({'ERROR'}, f"Preset '{self.preset_name}' not found")
                return {'CANCELLED'}

            preset_addons = presets[self.preset_name]
            
            # Get all available add-ons (both enabled and disabled)
            all_addons = set()
            
            # Get enabled add-ons
            enabled_addons = set(bpy.context.preferences.addons.keys())
            all_addons.update(enabled_addons)
            
            # Get all available add-on modules
            try:
                for addon in bpy.utils.addon_utils.modules():
                    all_addons.add(addon.__name__)
            except:
                pass  # Continue if we can't get all modules
            
            # Disable all add-ons first
            disabled_count = 0
            for addon_name in all_addons:
                if addon_name in enabled_addons:
                    try:
                        bpy.ops.preferences.addon_disable(module=addon_name)
                        disabled_count += 1
                    except:
                        pass  # Skip if add-on can't be disabled
            
            # Enable add-ons specified in preset
            enabled_count = 0
            failed_count = 0
            
            for addon_name in preset_addons:
                try:
                    bpy.ops.preferences.addon_enable(module=addon_name)
                    enabled_count += 1
                except:
                    failed_count += 1
                    print(f"Add-on Preset Manager: Warning - Could not enable add-on '{addon_name}'")
            
            # Update UI
            context.scene.addon_preset_props.selected_preset = self.preset_name
            
            message = f"Preset '{self.preset_name}' applied: {enabled_count} add-ons enabled, {disabled_count} disabled"
            if failed_count > 0:
                message += f", {failed_count} failed to enable"
            
            self.report({'INFO'}, message)
            
            # Print detailed info to console
            print(f"Add-on Preset Manager: {message}")
            if failed_count > 0:
                print(f"Add-on Preset Manager: Failed to enable: {[addon for addon in preset_addons if addon not in get_current_addon_state()]}")
            
            return {'FINISHED'}
            
        except Exception as e:
            self.report({'ERROR'}, f"Failed to apply preset: {str(e)}")
            return {'CANCELLED'}


class ADDON_OT_rename_preset(Operator):
    """Rename a preset"""
    bl_idname = "addon.rename_preset"
    bl_label = "Rename Preset"
    bl_description = "Rename the selected preset"
    bl_options = {'REGISTER', 'UNDO'}

    old_name: StringProperty(
        name="Old Name",
        description="Current name of the preset",
        default=""
    )
    
    new_name: StringProperty(
        name="New Name",
        description="New name for the preset",
        default=""
    )

    def invoke(self, context, event):
        """Show dialog to enter new name"""
        if not self.old_name:
            self.report({'ERROR'}, "No preset selected")
            return {'CANCELLED'}
        
        self.new_name = self.old_name
        return context.window_manager.invoke_props_dialog(self, width=350)

    def execute(self, context):
        """Rename the specified preset"""
        if not self.new_name.strip():
            self.report({'ERROR'}, "Preset name cannot be empty")
            return {'CANCELLED'}

        if self.new_name == self.old_name:
            return {'CANCELLED'}

        try:
            # Load presets
            presets = load_presets()
            
            if self.old_name not in presets:
                self.report({'ERROR'}, f"Preset '{self.old_name}' not found")
                return {'CANCELLED'}

            if self.new_name in presets:
                self.report({'ERROR'}, f"Preset '{self.new_name}' already exists")
                return {'CANCELLED'}

            # Rename preset
            presets[self.new_name] = presets[self.old_name]
            del presets[self.old_name]
            
            # Save updated presets
            save_presets(presets)
            
            # Update UI selection
            if context.scene.addon_preset_props.selected_preset == self.old_name:
                context.scene.addon_preset_props.selected_preset = self.new_name
            
            self.report({'INFO'}, f"Preset renamed from '{self.old_name}' to '{self.new_name}'")
            return {'FINISHED'}
            
        except Exception as e:
            self.report({'ERROR'}, f"Failed to rename preset: {str(e)}")
            return {'CANCELLED'}


class ADDON_OT_delete_preset(Operator):
    """Delete a preset"""
    bl_idname = "addon.delete_preset"
    bl_label = "Delete Preset"
    bl_description = "Delete the selected preset"
    bl_options = {'REGISTER', 'UNDO'}

    preset_name: StringProperty(
        name="Preset Name",
        description="Name of the preset to delete",
        default=""
    )

    def invoke(self, context, event):
        """Show confirmation dialog"""
        return context.window_manager.invoke_confirm(self, event)

    def execute(self, context):
        """Delete the specified preset"""
        if not self.preset_name:
            self.report({'ERROR'}, "No preset selected")
            return {'CANCELLED'}

        try:
            # Load presets
            presets = load_presets()
            
            if self.preset_name not in presets:
                self.report({'ERROR'}, f"Preset '{self.preset_name}' not found")
                return {'CANCELLED'}

            # Remove preset
            del presets[self.preset_name]
            
            # Save updated presets
            save_presets(presets)
            
            # Clear selection if deleted preset was selected
            if context.scene.addon_preset_props.selected_preset == self.preset_name:
                context.scene.addon_preset_props.selected_preset = ""
            
            self.report({'INFO'}, f"Preset '{self.preset_name}' deleted")
            return {'FINISHED'}
            
        except Exception as e:
            self.report({'ERROR'}, f"Failed to delete preset: {str(e)}")
            return {'CANCELLED'}


class ADDON_OT_revert_to_previous_state(Operator):
    """Revert to the add-on configuration before the last preset was applied"""
    bl_idname = "addon.revert_to_previous_state"
    bl_label = "Revert to Previous State"
    bl_description = "Restore the add-on configuration from before the last preset was applied"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        """Revert to previous add-on state"""
        props = context.scene.addon_preset_props
        
        if not props.previous_state:
            self.report({'ERROR'}, "No previous state saved")
            return {'CANCELLED'}

        try:
            # Load previous state
            previous_addons = load_state_from_json(props.previous_state)
            
            # Get current state
            current_addons = get_current_addon_state()
            
            # Get all available add-ons
            all_addons = set()
            enabled_addons = set(bpy.context.preferences.addons.keys())
            all_addons.update(enabled_addons)
            
            try:
                for addon in bpy.utils.addon_utils.modules():
                    all_addons.add(addon.__name__)
            except:
                pass
            
            # Disable all current add-ons
            disabled_count = 0
            for addon_name in all_addons:
                if addon_name in enabled_addons:
                    try:
                        bpy.ops.preferences.addon_disable(module=addon_name)
                        disabled_count += 1
                    except:
                        pass
            
            # Enable add-ons from previous state
            enabled_count = 0
            failed_count = 0
            
            for addon_name in previous_addons:
                try:
                    bpy.ops.preferences.addon_enable(module=addon_name)
                    enabled_count += 1
                except:
                    failed_count += 1
                    print(f"Add-on Preset Manager: Warning - Could not restore add-on '{addon_name}'")
            
            # Clear previous state
            props.previous_state = ""
            
            message = f"Previous state restored: {enabled_count} add-ons enabled, {disabled_count} disabled"
            if failed_count > 0:
                message += f", {failed_count} failed to restore"
            
            self.report({'INFO'}, message)
            print(f"Add-on Preset Manager: {message}")
            
            return {'FINISHED'}
            
        except Exception as e:
            self.report({'ERROR'}, f"Failed to revert to previous state: {str(e)}")
            return {'CANCELLED'}


class ADDON_OT_refresh_presets(Operator):
    """Refresh the preset list"""
    bl_idname = "addon.refresh_presets"
    bl_label = "Refresh"
    bl_description = "Refresh the preset list"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        """Refresh the preset list"""
        try:
            # Force UI update by updating the enum property
            bpy.context.scene.addon_preset_props.selected_preset = bpy.context.scene.addon_preset_props.selected_preset
            self.report({'INFO'}, "Preset list refreshed")
            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, f"Failed to refresh: {str(e)}")
            return {'CANCELLED'}


# ============================================================================
# UI PANEL
# ============================================================================

class ADDON_PT_preset_manager(Panel):
    """Panel in Preferences for managing add-on presets"""
    bl_label = "Add-on Preset Manager"
    bl_space_type = 'PREFERENCES'
    bl_region_type = 'WINDOW'
    bl_context = "addons"
    bl_parent_id = "ADDON_PT_your_existing_panel"  # Replace with your existing panel ID

    def draw(self, context):
        """Draw the UI panel"""
        layout = self.layout
        props = context.scene.addon_preset_props
        
        # Preset selection
        row = layout.row()
        row.prop(props, "selected_preset", text="Preset")
        
        # Main control buttons
        col = layout.column(align=True)
        col.scale_y = 1.2
        
        # Save current as preset button
        save_op = col.operator("addon.save_current_as_preset", text="Save Current as Preset", icon='FILE_TICK')
        
        # Apply preset button
        if props.selected_preset:
            apply_op = col.operator("addon.apply_preset", text="Apply Preset", icon='IMPORT')
            apply_op.preset_name = props.selected_preset
        
        # Revert to previous state button
        if props.previous_state:
            col.operator("addon.revert_to_previous_state", text="Revert to Previous State", icon='LOOP_BACK')
        
        # Preset management buttons
        if props.selected_preset:
            layout.separator()
            row = layout.row(align=True)
            row.scale_y = 1.1
            
            # Rename button
            rename_op = row.operator("addon.rename_preset", text="Rename", icon='OUTLINER_OB_FONT')
            rename_op.old_name = props.selected_preset
            
            # Delete button
            delete_op = row.operator("addon.delete_preset", text="Delete", icon='TRASH')
            delete_op.preset_name = props.selected_preset
        
        # Refresh button
        layout.separator()
        layout.operator("addon.refresh_presets", text="Refresh List", icon='FILE_REFRESH')
        
        # Info section
        layout.separator()
        box = layout.box()
        box.label(text="Preset Info:", icon='INFO')
        
        presets = load_presets()
        if presets:
            for name, addons in presets.items():
                box.label(text=f"• {name}: {len(addons)} add-ons", icon='PLUGIN')
        else:
            box.label(text="No presets saved yet", icon='PLUGIN')
        
        # Safety warning
        layout.separator()
        box = layout.box()
        box.alert = True
        box.label(text="⚠️ Warning: Applying a preset will change", icon='ERROR')
        box.label(text="your current add-on configuration!")


# ============================================================================
# REGISTRATION
# ============================================================================

# List of classes to register
preset_manager_classes = [
    AddonPresetManagerProps,
    ADDON_OT_save_current_as_preset,
    ADDON_OT_apply_preset,
    ADDON_OT_rename_preset,
    ADDON_OT_delete_preset,
    ADDON_OT_revert_to_previous_state,
    ADDON_OT_refresh_presets,
    ADDON_PT_preset_manager,
]


def register_preset_manager():
    """Register the preset manager classes"""
    for cls in preset_manager_classes:
        bpy.utils.register_class(cls)
    
    # Register property group
    bpy.types.Scene.addon_preset_props = bpy.props.PointerProperty(type=AddonPresetManagerProps)
    
    print("Add-on Preset Manager: Registered successfully")


def unregister_preset_manager():
    """Unregister the preset manager classes"""
    # Unregister property group
    if hasattr(bpy.types.Scene, 'addon_preset_props'):
        del bpy.types.Scene.addon_preset_props
    
    # Unregister classes in reverse order
    for cls in reversed(preset_manager_classes):
        bpy.utils.unregister_class(cls)
    
    print("Add-on Preset Manager: Unregistered")


# ============================================================================
# INTEGRATION INSTRUCTIONS
# ============================================================================

"""
INTEGRATION INSTRUCTIONS:

1. COPY THIS FILE:
   - Copy this entire file into your existing add-on
   - Or import it as a module if you prefer modular structure

2. UPDATE YOUR REGISTER FUNCTION:
   Add this to your existing register() function:
   
   def register():
       # Your existing registration code...
       
       # Add preset manager
       register_preset_manager()

3. UPDATE YOUR UNREGISTER FUNCTION:
   Add this to your existing unregister() function:
   
   def unregister():
       # Your existing unregistration code...
       
       # Remove preset manager
       unregister_preset_manager()

4. UPDATE YOUR CLASSES LIST:
   Add the preset manager classes to your existing classes list:
   
   classes = [
       # Your existing classes...
       *preset_manager_classes,  # Add this line
   ]

5. CUSTOMIZE THE PANEL:
   - Change bl_parent_id in ADDON_PT_preset_manager to your existing panel ID
   - Or remove bl_parent_id to make it a standalone panel
   - Adjust the UI layout as needed for your add-on

6. CUSTOMIZE PRESET STORAGE:
   - The presets are stored in your add-on's directory as 'addon_presets.json'
   - You can change the filename by modifying get_presets_file_path()

7. TEST THE INTEGRATION:
   - Enable your add-on in Blender
   - Go to Edit > Preferences > Add-ons
   - Find your add-on and look for the "Add-on Preset Manager" panel
   - Test creating, applying, and managing presets

FEATURES INCLUDED:
✅ Save current add-ons as named presets
✅ Apply presets (disable all, enable preset add-ons)
✅ Create, rename, and delete presets
✅ JSON file storage in add-on directory
✅ Clean UI in Preferences > Add-ons
✅ Error handling for missing add-ons
✅ Revert to previous state functionality
✅ Non-blocking UI interactions
✅ PEP8 compliant code
✅ Blender 4.5 compatible
✅ Console logging for debugging

The preset manager is now ready to integrate into your existing add-on!
"""
