"""
Enhanced Add-on Preset Manager for Blender 4.5

This is an enhanced version with additional features:
- Export/Import presets as external files
- Preset validation and cleanup
- Batch operations
- Enhanced UI with icons and better layout
- Backup/restore functionality

Integration Instructions:
1. Replace the basic preset manager with this enhanced version
2. All integration steps remain the same as the basic version
3. Additional features are automatically available

Author: StudyOS Development
Version: 2.0.0
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
# ENHANCED PROPERTY GROUPS
# ============================================================================

class AddonPresetManagerProps(PropertyGroup):
    """Enhanced property group with additional features"""
    
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
    
    show_advanced: BoolProperty(
        name="Show Advanced",
        description="Show advanced options",
        default=False
    )
    
    auto_backup: BoolProperty(
        name="Auto Backup",
        description="Automatically backup before applying presets",
        default=True
    )


# ============================================================================
# ENHANCED UTILITY FUNCTIONS
# ============================================================================

def get_presets_file_path():
    """Get the path to the presets JSON file in the add-on directory"""
    addon_dir = os.path.dirname(__file__)
    return os.path.join(addon_dir, "addon_presets.json")


def get_backup_file_path():
    """Get the path to the backup file"""
    addon_dir = os.path.dirname(__file__)
    return os.path.join(addon_dir, "addon_presets_backup.json")


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
        default_presets = {
            "Modeling Setup": ["mesh_looptools", "node_wrangler", "extra_objects"],
            "Animation Setup": ["rigify", "animation_nodes", "bone_collection"],
            "Rendering Setup": ["cycles", "eevee", "render_auto_tile_size"],
            "Clean Setup": []  # Empty preset for minimal configuration
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
    """Save presets to JSON file with backup"""
    presets_file = get_presets_file_path()
    backup_file = get_backup_file_path()
    
    # Create backup if file exists
    if os.path.exists(presets_file):
        try:
            import shutil
            shutil.copy2(presets_file, backup_file)
        except:
            pass  # Continue if backup fails
    
    try:
        with open(presets_file, 'w', encoding='utf-8') as f:
            json.dump(presets, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Add-on Preset Manager: Error saving presets file: {e}")
        raise


def get_current_addon_state():
    """Get current enabled add-ons as a list"""
    return list(bpy.context.preferences.addons.keys())


def validate_preset(preset_name, preset_addons):
    """Validate a preset and return info about missing add-ons"""
    available_addons = set()
    
    # Get all available add-on modules
    try:
        for addon in bpy.utils.addon_utils.modules():
            available_addons.add(addon.__name__)
    except:
        pass
    
    missing_addons = [addon for addon in preset_addons if addon not in available_addons]
    valid_addons = [addon for addon in preset_addons if addon in available_addons]
    
    return {
        'valid': valid_addons,
        'missing': missing_addons,
        'total': len(preset_addons),
        'valid_count': len(valid_addons),
        'missing_count': len(missing_addons)
    }


# ============================================================================
# ENHANCED OPERATORS
# ============================================================================

class ADDON_OT_save_current_as_preset(Operator):
    """Enhanced save preset with validation"""
    bl_idname = "addon.save_current_as_preset"
    bl_label = "Save Current as Preset"
    bl_description = "Save the currently enabled add-ons as a new preset"
    bl_options = {'REGISTER', 'UNDO'}

    preset_name: StringProperty(
        name="Preset Name",
        description="Name for the new preset",
        default="New Preset"
    )
    
    overwrite_existing: BoolProperty(
        name="Overwrite Existing",
        description="Overwrite if preset already exists",
        default=False
    )

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=400)

    def execute(self, context):
        if not self.preset_name.strip():
            self.report({'ERROR'}, "Preset name cannot be empty")
            return {'CANCELLED'}

        try:
            enabled_addons = get_current_addon_state()
            presets = load_presets()
            
            # Check if preset exists
            if self.preset_name in presets and not self.overwrite_existing:
                self.report({'ERROR'}, f"Preset '{self.preset_name}' already exists. Enable 'Overwrite Existing' to replace it.")
                return {'CANCELLED'}
            
            presets[self.preset_name] = enabled_addons
            save_presets(presets)
            
            context.scene.addon_preset_props.selected_preset = self.preset_name
            
            self.report({'INFO'}, f"Preset '{self.preset_name}' saved with {len(enabled_addons)} add-ons")
            return {'FINISHED'}
            
        except Exception as e:
            self.report({'ERROR'}, f"Failed to save preset: {str(e)}")
            return {'CANCELLED'}


class ADDON_OT_apply_preset(Operator):
    """Enhanced apply preset with validation and backup"""
    bl_idname = "addon.apply_preset"
    bl_label = "Apply Preset"
    bl_description = "Apply the selected preset with validation and backup"
    bl_options = {'REGISTER', 'UNDO'}

    preset_name: StringProperty(
        name="Preset Name",
        description="Name of the preset to apply",
        default=""
    )

    def execute(self, context):
        if not self.preset_name:
            self.report({'ERROR'}, "No preset selected")
            return {'CANCELLED'}

        try:
            props = context.scene.addon_preset_props
            
            # Auto backup if enabled
            if props.auto_backup:
                current_state_json = save_current_state_as_json()
                props.previous_state = current_state_json
            
            presets = load_presets()
            
            if self.preset_name not in presets:
                self.report({'ERROR'}, f"Preset '{self.preset_name}' not found")
                return {'CANCELLED'}

            preset_addons = presets[self.preset_name]
            
            # Validate preset
            validation = validate_preset(self.preset_name, preset_addons)
            
            # Get all available add-ons
            all_addons = set()
            enabled_addons = set(bpy.context.preferences.addons.keys())
            all_addons.update(enabled_addons)
            
            try:
                for addon in bpy.utils.addon_utils.modules():
                    all_addons.add(addon.__name__)
            except:
                pass
            
            # Disable all add-ons first
            disabled_count = 0
            for addon_name in all_addons:
                if addon_name in enabled_addons:
                    try:
                        bpy.ops.preferences.addon_disable(module=addon_name)
                        disabled_count += 1
                    except:
                        pass
            
            # Enable valid add-ons from preset
            enabled_count = 0
            for addon_name in validation['valid']:
                try:
                    bpy.ops.preferences.addon_enable(module=addon_name)
                    enabled_count += 1
                except:
                    pass
            
            context.scene.addon_preset_props.selected_preset = self.preset_name
            
            message = f"Preset '{self.preset_name}' applied: {enabled_count} enabled, {disabled_count} disabled"
            if validation['missing_count'] > 0:
                message += f", {validation['missing_count']} missing add-ons skipped"
                self.report({'WARNING'}, message)
            else:
                self.report({'INFO'}, message)
            
            print(f"Add-on Preset Manager: {message}")
            if validation['missing']:
                print(f"Add-on Preset Manager: Missing add-ons: {validation['missing']}")
            
            return {'FINISHED'}
            
        except Exception as e:
            self.report({'ERROR'}, f"Failed to apply preset: {str(e)}")
            return {'CANCELLED'}


class ADDON_OT_export_preset(Operator):
    """Export a preset to an external JSON file"""
    bl_idname = "addon.export_preset"
    bl_label = "Export Preset"
    bl_description = "Export the selected preset to an external file"
    bl_options = {'REGISTER', 'UNDO'}

    preset_name: StringProperty(
        name="Preset Name",
        description="Name of the preset to export",
        default=""
    )
    
    filepath: StringProperty(
        name="File Path",
        description="Path to save the exported preset",
        subtype='FILE_PATH',
        default=""
    )

    def invoke(self, context, event):
        if not self.preset_name:
            self.report({'ERROR'}, "No preset selected")
            return {'CANCELLED'}
        
        # Set default filename
        self.filepath = f"{self.preset_name.replace(' ', '_')}_preset.json"
        
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        try:
            presets = load_presets()
            
            if self.preset_name not in presets:
                self.report({'ERROR'}, f"Preset '{self.preset_name}' not found")
                return {'CANCELLED'}

            # Create export data
            export_data = {
                "preset_name": self.preset_name,
                "addons": presets[self.preset_name],
                "export_info": {
                    "blender_version": bpy.app.version_string,
                    "export_date": bpy.context.scene.frame_current,
                    "total_addons": len(presets[self.preset_name])
                }
            }
            
            # Save to file
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            
            self.report({'INFO'}, f"Preset '{self.preset_name}' exported to {self.filepath}")
            return {'FINISHED'}
            
        except Exception as e:
            self.report({'ERROR'}, f"Failed to export preset: {str(e)}")
            return {'CANCELLED'}


class ADDON_OT_import_preset(Operator):
    """Import a preset from an external JSON file"""
    bl_idname = "addon.import_preset"
    bl_label = "Import Preset"
    bl_description = "Import a preset from an external file"
    bl_options = {'REGISTER', 'UNDO'}

    filepath: StringProperty(
        name="File Path",
        description="Path to the preset file to import",
        subtype='FILE_PATH',
        default=""
    )

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                import_data = json.load(f)
            
            # Validate import data
            if "preset_name" not in import_data or "addons" not in import_data:
                self.report({'ERROR'}, "Invalid preset file format")
                return {'CANCELLED'}
            
            preset_name = import_data["preset_name"]
            preset_addons = import_data["addons"]
            
            # Load existing presets
            presets = load_presets()
            
            # Check for conflicts
            if preset_name in presets:
                # You could add a confirmation dialog here
                self.report({'WARNING'}, f"Preset '{preset_name}' already exists and will be overwritten")
            
            # Add/update preset
            presets[preset_name] = preset_addons
            save_presets(presets)
            
            self.report({'INFO'}, f"Preset '{preset_name}' imported with {len(preset_addons)} add-ons")
            return {'FINISHED'}
            
        except Exception as e:
            self.report({'ERROR'}, f"Failed to import preset: {str(e)}")
            return {'CANCELLED'}


class ADDON_OT_cleanup_presets(Operator):
    """Clean up presets by removing invalid add-ons"""
    bl_idname = "addon.cleanup_presets"
    bl_label = "Cleanup Presets"
    bl_description = "Remove invalid add-ons from all presets"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        try:
            presets = load_presets()
            cleaned_count = 0
            
            # Get all available add-ons
            available_addons = set()
            try:
                for addon in bpy.utils.addon_utils.modules():
                    available_addons.add(addon.__name__)
            except:
                pass
            
            # Clean each preset
            for preset_name, preset_addons in presets.items():
                original_count = len(preset_addons)
                valid_addons = [addon for addon in preset_addons if addon in available_addons]
                
                if len(valid_addons) != original_count:
                    presets[preset_name] = valid_addons
                    cleaned_count += (original_count - len(valid_addons))
            
            if cleaned_count > 0:
                save_presets(presets)
                self.report({'INFO'}, f"Cleanup complete: Removed {cleaned_count} invalid add-ons")
            else:
                self.report({'INFO'}, "No invalid add-ons found")
            
            return {'FINISHED'}
            
        except Exception as e:
            self.report({'ERROR'}, f"Failed to cleanup presets: {str(e)}")
            return {'CANCELLED'}


# Include all the other operators from the basic version...
# (Rename, Delete, Revert, Refresh - same as before)

class ADDON_OT_rename_preset(Operator):
    """Rename a preset"""
    bl_idname = "addon.rename_preset"
    bl_label = "Rename Preset"
    bl_description = "Rename the selected preset"
    bl_options = {'REGISTER', 'UNDO'}

    old_name: StringProperty(name="Old Name", default="")
    new_name: StringProperty(name="New Name", default="")

    def invoke(self, context, event):
        if not self.old_name:
            self.report({'ERROR'}, "No preset selected")
            return {'CANCELLED'}
        self.new_name = self.old_name
        return context.window_manager.invoke_props_dialog(self, width=350)

    def execute(self, context):
        if not self.new_name.strip():
            self.report({'ERROR'}, "Preset name cannot be empty")
            return {'CANCELLED'}

        try:
            presets = load_presets()
            
            if self.old_name not in presets:
                self.report({'ERROR'}, f"Preset '{self.old_name}' not found")
                return {'CANCELLED'}

            if self.new_name in presets:
                self.report({'ERROR'}, f"Preset '{self.new_name}' already exists")
                return {'CANCELLED'}

            presets[self.new_name] = presets[self.old_name]
            del presets[self.old_name]
            save_presets(presets)
            
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

    preset_name: StringProperty(name="Preset Name", default="")

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

    def execute(self, context):
        if not self.preset_name:
            self.report({'ERROR'}, "No preset selected")
            return {'CANCELLED'}

        try:
            presets = load_presets()
            
            if self.preset_name not in presets:
                self.report({'ERROR'}, f"Preset '{self.preset_name}' not found")
                return {'CANCELLED'}

            del presets[self.preset_name]
            save_presets(presets)
            
            if context.scene.addon_preset_props.selected_preset == self.preset_name:
                context.scene.addon_preset_props.selected_preset = ""
            
            self.report({'INFO'}, f"Preset '{self.preset_name}' deleted")
            return {'FINISHED'}
            
        except Exception as e:
            self.report({'ERROR'}, f"Failed to delete preset: {str(e)}")
            return {'CANCELLED'}


class ADDON_OT_revert_to_previous_state(Operator):
    """Revert to previous state"""
    bl_idname = "addon.revert_to_previous_state"
    bl_label = "Revert to Previous State"
    bl_description = "Restore the add-on configuration from before the last preset was applied"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.addon_preset_props
        
        if not props.previous_state:
            self.report({'ERROR'}, "No previous state saved")
            return {'CANCELLED'}

        try:
            previous_addons = json.loads(props.previous_state)
            current_addons = get_current_addon_state()
            
            all_addons = set()
            enabled_addons = set(bpy.context.preferences.addons.keys())
            all_addons.update(enabled_addons)
            
            try:
                for addon in bpy.utils.addon_utils.modules():
                    all_addons.add(addon.__name__)
            except:
                pass
            
            disabled_count = 0
            for addon_name in all_addons:
                if addon_name in enabled_addons:
                    try:
                        bpy.ops.preferences.addon_disable(module=addon_name)
                        disabled_count += 1
                    except:
                        pass
            
            enabled_count = 0
            failed_count = 0
            
            for addon_name in previous_addons:
                try:
                    bpy.ops.preferences.addon_enable(module=addon_name)
                    enabled_count += 1
                except:
                    failed_count += 1
            
            props.previous_state = ""
            
            message = f"Previous state restored: {enabled_count} enabled, {disabled_count} disabled"
            if failed_count > 0:
                message += f", {failed_count} failed to restore"
            
            self.report({'INFO'}, message)
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
        try:
            bpy.context.scene.addon_preset_props.selected_preset = bpy.context.scene.addon_preset_props.selected_preset
            self.report({'INFO'}, "Preset list refreshed")
            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, f"Failed to refresh: {str(e)}")
            return {'CANCELLED'}


# ============================================================================
# ENHANCED UI PANEL
# ============================================================================

class ADDON_PT_preset_manager(Panel):
    """Enhanced preset manager panel with better layout"""
    bl_label = "🎯 Add-on Preset Manager"
    bl_space_type = 'PREFERENCES'
    bl_region_type = 'WINDOW'
    bl_context = "addons"
    bl_parent_id = "ADDON_PT_your_existing_panel"  # Replace with your panel ID

    def draw(self, context):
        layout = self.layout
        props = context.scene.addon_preset_props
        
        # Header with preset selection
        box = layout.box()
        row = box.row(align=True)
        row.prop(props, "selected_preset", text="")
        row.operator("addon.refresh_presets", text="", icon='FILE_REFRESH')
        
        # Main action buttons
        col = layout.column(align=True)
        col.scale_y = 1.2
        
        # Save and Apply buttons (primary actions)
        row = col.row(align=True)
        save_op = row.operator("addon.save_current_as_preset", text="Save", icon='FILE_TICK')
        if props.selected_preset:
            apply_op = row.operator("addon.apply_preset", text="Apply", icon='PLAY')
            apply_op.preset_name = props.selected_preset
        
        # Revert button (if previous state exists)
        if props.previous_state:
            col.operator("addon.revert_to_previous_state", text="Revert to Previous", icon='LOOP_BACK')
        
        # Management buttons
        if props.selected_preset:
            layout.separator()
            row = layout.row(align=True)
            row.scale_y = 1.1
            
            rename_op = row.operator("addon.rename_preset", text="Rename", icon='OUTLINER_OB_FONT')
            rename_op.old_name = props.selected_preset
            
            delete_op = row.operator("addon.delete_preset", text="Delete", icon='TRASH')
            delete_op.preset_name = props.selected_preset
        
        # Advanced options toggle
        layout.separator()
        row = layout.row()
        row.prop(props, "show_advanced", text="Advanced Options", icon='SETTINGS')
        
        if props.show_advanced:
            box = layout.box()
            box.label(text="Advanced Options:", icon='TOOL_SETTINGS')
            
            # Auto backup setting
            box.prop(props, "auto_backup", text="Auto Backup Before Apply")
            
            # Import/Export buttons
            if props.selected_preset:
                row = box.row(align=True)
                export_op = row.operator("addon.export_preset", text="Export", icon='EXPORT')
                export_op.preset_name = props.selected_preset
                
                row.operator("addon.import_preset", text="Import", icon='IMPORT')
            
            # Cleanup button
            box.operator("addon.cleanup_presets", text="Cleanup Invalid Add-ons", icon='BRUSH_DATA')
        
        # Info section
        layout.separator()
        box = layout.box()
        box.label(text="Preset Information:", icon='INFO')
        
        presets = load_presets()
        if presets:
            for name, addons in presets.items():
                validation = validate_preset(name, addons)
                icon = 'CHECKMARK' if validation['missing_count'] == 0 else 'ERROR'
                box.label(text=f"• {name}: {validation['valid_count']}/{validation['total']} add-ons", icon=icon)
        else:
            box.label(text="No presets saved yet", icon='PLUGIN')
        
        # Safety warning
        layout.separator()
        box = layout.box()
        box.alert = True
        box.label(text="⚠️ Warning: Applying presets will change", icon='ERROR')
        box.label(text="your current add-on configuration!")


# ============================================================================
# REGISTRATION
# ============================================================================

enhanced_preset_manager_classes = [
    AddonPresetManagerProps,
    ADDON_OT_save_current_as_preset,
    ADDON_OT_apply_preset,
    ADDON_OT_export_preset,
    ADDON_OT_import_preset,
    ADDON_OT_cleanup_presets,
    ADDON_OT_rename_preset,
    ADDON_OT_delete_preset,
    ADDON_OT_revert_to_previous_state,
    ADDON_OT_refresh_presets,
    ADDON_PT_preset_manager,
]


def register_preset_manager():
    """Register the enhanced preset manager classes"""
    for cls in enhanced_preset_manager_classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.addon_preset_props = bpy.props.PointerProperty(type=AddonPresetManagerProps)
    
    print("Enhanced Add-on Preset Manager: Registered successfully")


def unregister_preset_manager():
    """Unregister the enhanced preset manager classes"""
    if hasattr(bpy.types.Scene, 'addon_preset_props'):
        del bpy.types.Scene.addon_preset_props
    
    for cls in reversed(enhanced_preset_manager_classes):
        bpy.utils.unregister_class(cls)
    
    print("Enhanced Add-on Preset Manager: Unregistered")


# ============================================================================
# INTEGRATION INSTRUCTIONS
# ============================================================================

"""
ENHANCED VERSION INTEGRATION:

1. REPLACE the basic preset manager with this enhanced version
2. Use 'enhanced_preset_manager_classes' instead of 'preset_manager_classes'
3. Call 'register_preset_manager()' and 'unregister_preset_manager()' as before

NEW FEATURES:
✅ Export/Import presets as external JSON files
✅ Preset validation and cleanup of invalid add-ons
✅ Auto backup before applying presets
✅ Enhanced UI with better layout and icons
✅ Advanced options panel
✅ Better error handling and user feedback
✅ Preset information with validation status

USAGE:
- Export presets to share with others
- Import presets from other users
- Cleanup removes add-ons that no longer exist
- Auto backup saves state before changes
- Advanced options provide more control

This enhanced version provides a more professional and feature-rich experience!
"""
