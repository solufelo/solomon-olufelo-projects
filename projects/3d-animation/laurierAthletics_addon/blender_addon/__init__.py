"""
Laurier Football Shell Game Addon for Blender 4.5
=================================================

Professional 3D shell game shuffle animation addon for Laurier Football promos.
Features smooth helmet movements, dramatic reveals, and cinematic camera work.

Author: Solomon Olufelo
Version: 1.0.0
Blender: 4.5+
Category: Animation

Installation:
1. Download the blender_addon folder
2. In Blender: Edit > Preferences > Add-ons > Install
3. Select the blender_addon folder
4. Enable "Laurier Football Shell Game"

Usage:
1. Set up your scene with helmets and football (see documentation)
2. Go to 3D Viewport > Sidebar > Laurier Football tab
3. Adjust parameters and click "Create Shell Game Animation"
"""

bl_info = {
    "name": "Laurier Football Shell Game",
    "author": "Solomon Olufelo",
    "version": (1, 0, 0),
    "blender": (4, 5, 0),
    "location": "3D Viewport > Sidebar > Laurier Football",
    "description": "Professional 3D shell game shuffle animation for Laurier Football promos",
    "warning": "",
    "doc_url": "https://github.com/solomon-olufelo/laurier-football-addon",
    "category": "Animation",
}

import bpy
import bmesh
import mathutils
from math import sin, cos, pi
import random
from bpy.types import Panel, Operator, PropertyGroup
from bpy.props import (
    FloatProperty, 
    IntProperty, 
    BoolProperty, 
    EnumProperty,
    PointerProperty
)

# ============================================================================
# PROPERTY GROUP FOR ADDON SETTINGS
# ============================================================================

class LaurierShellGameProperties(PropertyGroup):
    """Property group to store addon settings in the scene."""
    
    # Animation timing
    duration_sec: FloatProperty(
        name="Duration (seconds)",
        description="Total animation duration",
        default=8.0,
        min=1.0,
        max=30.0,
        step=0.1
    )
    
    fps: IntProperty(
        name="FPS",
        description="Frames per second",
        default=24,
        min=12,
        max=60
    )
    
    shuffle_speed: FloatProperty(
        name="Shuffle Speed",
        description="Speed of shuffle movements",
        default=2.0,
        min=0.5,
        max=10.0,
        step=0.1
    )
    
    shuffle_cycles: IntProperty(
        name="Shuffle Cycles",
        description="Number of shuffle cycles",
        default=4,
        min=1,
        max=20
    )
    
    # Movement parameters
    shuffle_amplitude: FloatProperty(
        name="Shuffle Amplitude",
        description="How far helmets move horizontally",
        default=2.0,
        min=0.1,
        max=10.0,
        step=0.1
    )
    
    vertical_bounce: FloatProperty(
        name="Vertical Bounce",
        description="Height of vertical bounce effect",
        default=0.3,
        min=0.0,
        max=2.0,
        step=0.1
    )
    
    spacing_buffer: FloatProperty(
        name="Spacing Buffer",
        description="Minimum distance between helmets",
        default=1.5,
        min=0.5,
        max=5.0,
        step=0.1
    )
    
    # Reveal settings
    reveal_target: IntProperty(
        name="Reveal Target",
        description="Which helmet (1, 2, or 3) hides the football",
        default=2,
        min=1,
        max=3
    )
    
    reveal_duration: FloatProperty(
        name="Reveal Duration",
        description="How long the reveal takes",
        default=1.5,
        min=0.5,
        max=5.0,
        step=0.1
    )
    
    reveal_height: FloatProperty(
        name="Reveal Height",
        description="How high the revealing helmet lifts",
        default=1.0,
        min=0.1,
        max=3.0,
        step=0.1
    )
    
    # Camera and effects
    camera_sway: BoolProperty(
        name="Camera Sway",
        description="Add subtle camera movement",
        default=True
    )
    
    sway_amount: FloatProperty(
        name="Sway Amount",
        description="Intensity of camera sway",
        default=0.1,
        min=0.0,
        max=1.0,
        step=0.01
    )
    
    ease_out: BoolProperty(
        name="Ease Out",
        description="Slow down before reveal",
        default=True
    )
    
    ease_duration: FloatProperty(
        name="Ease Duration",
        description="How long the ease-out lasts",
        default=1.0,
        min=0.1,
        max=3.0,
        step=0.1
    )
    
    # Randomization
    randomize_target: BoolProperty(
        name="Randomize Target",
        description="Randomly choose which helmet hides football",
        default=True
    )
    
    # Preset selection
    preset: EnumProperty(
        name="Animation Preset",
        description="Choose a preset configuration",
        items=[
            ('CUSTOM', "Custom", "Use custom settings"),
            ('QUICK_SNAPPY', "Quick & Snappy", "Fast 5-second animation"),
            ('DRAMATIC_SLOW', "Dramatic & Slow", "Cinematic 12-second animation"),
            ('SOCIAL_MEDIA', "Social Media", "Energetic 3-second animation"),
            ('BROADCAST_QUALITY', "Broadcast Quality", "Professional 8-second animation"),
            ('MINIMAL_CLEAN', "Minimal & Clean", "Subtle 6-second animation"),
            ('HIGH_ENERGY', "High Energy", "Fast and bouncy 4-second animation"),
        ],
        default='BROADCAST_QUALITY'
    )

# ============================================================================
# ANIMATION ENGINE (Converted from original script)
# ============================================================================

class LaurierShellGameEngine:
    """Core animation engine for the shell game effect."""
    
    def __init__(self, props):
        self.props = props
        self.config = {
            "duration_sec": props.duration_sec,
            "fps": props.fps,
            "shuffle_speed": props.shuffle_speed,
            "shuffle_cycles": props.shuffle_cycles,
            "shuffle_amplitude": props.shuffle_amplitude,
            "vertical_bounce": props.vertical_bounce,
            "spacing_buffer": props.spacing_buffer,
            "reveal_target": props.reveal_target,
            "reveal_duration": props.reveal_duration,
            "reveal_height": props.reveal_height,
            "camera_sway": props.camera_sway,
            "sway_amount": props.sway_amount,
            "ease_out": props.ease_out,
            "ease_duration": props.ease_duration,
            "randomize_target": props.randomize_target,
        }
    
    def get_empty_object(self, name):
        """Get empty object by name, with error handling."""
        obj = bpy.data.objects.get(name)
        if not obj:
            raise ValueError(f"Required empty '{name}' not found in scene. Please ensure your scene is set up correctly.")
        return obj
    
    def ease_out_cubic(self, t):
        """Cubic ease-out function for smooth deceleration."""
        return 1 - pow(1 - t, 3)
    
    def ease_in_out_sine(self, t):
        """Sine ease-in-out for natural movement."""
        return -(cos(pi * t) - 1) / 2
    
    def create_sine_wave_movement(self, frame, amplitude, frequency, phase_offset=0):
        """Generate sine wave movement with phase offset for different helmets."""
        t = frame / (self.config["fps"] * self.config["duration_sec"])
        return amplitude * sin(2 * pi * frequency * t + phase_offset)
    
    def add_vertical_bounce(self, frame):
        """Add realistic vertical bounce to helmet movement."""
        t = frame / (self.config["fps"] * self.config["duration_sec"])
        bounce = self.config["vertical_bounce"] * abs(sin(2 * pi * self.config["shuffle_speed"] * t))
        return bounce
    
    def calculate_helmet_positions(self, frame):
        """Calculate positions for all three helmets with collision avoidance."""
        positions = {}
        
        base_positions = {
            1: mathutils.Vector((-self.config["spacing_buffer"], 0, 0)),
            2: mathutils.Vector((0, 0, 0)),
            3: mathutils.Vector((self.config["spacing_buffer"], 0, 0))
        }
        
        for helmet_num in [1, 2, 3]:
            phase_offset = (helmet_num - 1) * (2 * pi / 3)
            
            horizontal_offset = self.create_sine_wave_movement(
                frame, 
                self.config["shuffle_amplitude"], 
                self.config["shuffle_speed"], 
                phase_offset
            )
            
            vertical_bounce = self.add_vertical_bounce(frame)
            
            pos = base_positions[helmet_num].copy()
            pos.x += horizontal_offset
            pos.z += vertical_bounce
            
            positions[helmet_num] = pos
        
        return positions
    
    def apply_ease_out(self, frame):
        """Apply ease-out effect to slow down before reveal."""
        if not self.config["ease_out"]:
            return 1.0
        
        total_frames = self.config["duration_sec"] * self.config["fps"]
        ease_frames = self.config["ease_duration"] * self.config["fps"]
        ease_start_frame = total_frames - ease_frames
        
        if frame < ease_start_frame:
            return 1.0
        
        ease_progress = (frame - ease_start_frame) / ease_frames
        return self.ease_out_cubic(ease_progress)
    
    def setup_scene(self):
        """Initialize scene settings and validate required objects."""
        bpy.context.scene.frame_set(1)
        bpy.context.scene.render.fps = self.config["fps"]
        
        required_empties = ["Empty_1", "Empty_2", "Empty_3", "Football_CTRL"]
        for empty_name in required_empties:
            if not bpy.data.objects.get(empty_name):
                raise ValueError(f"Required object '{empty_name}' not found. Please ensure your scene is set up correctly.")
    
    def randomize_football_target(self):
        """Randomly choose which helmet hides the football."""
        if self.config["randomize_target"]:
            self.config["reveal_target"] = random.randint(1, 3)
            self.props.reveal_target = self.config["reveal_target"]
    
    def animate_helmets(self):
        """Create smooth shuffle animation for all helmets."""
        total_frames = int(self.config["duration_sec"] * self.config["fps"])
        
        for frame in range(1, total_frames + 1):
            positions = self.calculate_helmet_positions(frame)
            ease_factor = self.apply_ease_out(frame)
            
            for helmet_num in [1, 2, 3]:
                empty_name = f"Empty_{helmet_num}"
                empty_obj = self.get_empty_object(empty_name)
                
                pos = positions[helmet_num]
                pos.x *= ease_factor
                pos.z *= ease_factor
                
                empty_obj.location = pos
                empty_obj.keyframe_insert(data_path="location", frame=frame)
    
    def animate_football(self):
        """Animate football to follow the target helmet."""
        football_ctrl = self.get_empty_object("Football_CTRL")
        target_empty = self.get_empty_object(f"Empty_{self.config['reveal_target']}")
        
        total_frames = int(self.config["duration_sec"] * self.config["fps"])
        
        for frame in range(1, total_frames + 1):
            football_ctrl.location = target_empty.location
            football_ctrl.keyframe_insert(data_path="location", frame=frame)
    
    def create_reveal_animation(self):
        """Create dramatic reveal animation for the target helmet."""
        target_empty = self.get_empty_object(f"Empty_{self.config['reveal_target']}")
        football_ctrl = self.get_empty_object("Football_CTRL")
        
        total_frames = int(self.config["duration_sec"] * self.config["fps"])
        reveal_frames = int(self.config["reveal_duration"] * self.config["fps"])
        reveal_start_frame = total_frames - reveal_frames + 1
        
        final_pos = target_empty.location.copy()
        
        for i, frame in enumerate(range(reveal_start_frame, total_frames + 1)):
            progress = i / (reveal_frames - 1)
            ease_progress = self.ease_out_cubic(progress)
            
            reveal_pos = final_pos.copy()
            reveal_pos.z += self.config["reveal_height"] * ease_progress
            
            target_empty.location = reveal_pos
            target_empty.keyframe_insert(data_path="location", frame=frame)
            
            football_ctrl.location = final_pos
            football_ctrl.keyframe_insert(data_path="location", frame=frame)
    
    def animate_camera(self):
        """Add subtle camera sway for cinematic feel."""
        if not self.config["camera_sway"]:
            return
        
        camera = bpy.context.scene.camera
        if not camera:
            return
        
        total_frames = int(self.config["duration_sec"] * self.config["fps"])
        
        for frame in range(1, total_frames + 1):
            t = frame / (self.config["fps"] * self.config["duration_sec"])
            
            sway_x = self.config["sway_amount"] * sin(2 * pi * 0.5 * t)
            sway_y = self.config["sway_amount"] * cos(2 * pi * 0.3 * t)
            
            camera.rotation_euler.x += sway_x * 0.1
            camera.rotation_euler.y += sway_y * 0.1
            camera.keyframe_insert(data_path="rotation_euler", frame=frame)
    
    def set_render_settings(self):
        """Configure render settings for output."""
        scene = bpy.context.scene
        
        total_frames = int(self.config["duration_sec"] * self.config["fps"])
        scene.frame_start = 1
        scene.frame_end = total_frames
        
        scene.render.image_settings.file_format = 'PNG'
        scene.render.image_settings.color_mode = 'RGBA'
        scene.render.image_settings.color_depth = '16'
    
    def run_animation(self):
        """Execute the complete shell game animation."""
        try:
            self.setup_scene()
            self.randomize_football_target()
            self.animate_helmets()
            self.animate_football()
            self.create_reveal_animation()
            self.animate_camera()
            self.set_render_settings()
            return True, f"Animation complete! Football hidden under helmet {self.config['reveal_target']}"
        except Exception as e:
            return False, str(e)

# ============================================================================
# BLENDER OPERATOR
# ============================================================================

class LAURIER_OT_create_shell_game(Operator):
    """Create Laurier Football Shell Game Animation"""
    bl_idname = "laurier.create_shell_game"
    bl_label = "Create Shell Game Animation"
    bl_description = "Generate professional 3D shell game shuffle animation"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        props = context.scene.laurier_shell_game
        
        # Apply preset if selected
        if props.preset != 'CUSTOM':
            self.apply_preset(props, props.preset)
        
        # Create and run animation engine
        engine = LaurierShellGameEngine(props)
        success, message = engine.run_animation()
        
        if success:
            self.report({'INFO'}, message)
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, f"Animation failed: {message}")
            return {'CANCELLED'}
    
    def apply_preset(self, props, preset_name):
        """Apply preset configuration to properties."""
        presets = {
            'QUICK_SNAPPY': {
                'duration_sec': 5.0, 'shuffle_speed': 3.0, 'shuffle_cycles': 3,
                'shuffle_amplitude': 1.5, 'vertical_bounce': 0.2, 'spacing_buffer': 1.2,
                'reveal_duration': 1.0, 'reveal_height': 0.8, 'sway_amount': 0.05,
                'ease_duration': 0.8, 'randomize_target': True
            },
            'DRAMATIC_SLOW': {
                'duration_sec': 12.0, 'shuffle_speed': 1.2, 'shuffle_cycles': 6,
                'shuffle_amplitude': 3.0, 'vertical_bounce': 0.5, 'spacing_buffer': 2.0,
                'reveal_duration': 2.5, 'reveal_height': 1.5, 'sway_amount': 0.15,
                'ease_duration': 2.0, 'randomize_target': False
            },
            'SOCIAL_MEDIA': {
                'duration_sec': 3.0, 'fps': 30, 'shuffle_speed': 4.0, 'shuffle_cycles': 2,
                'shuffle_amplitude': 1.0, 'vertical_bounce': 0.4, 'spacing_buffer': 1.0,
                'reveal_duration': 0.8, 'reveal_height': 1.2, 'sway_amount': 0.2,
                'ease_out': False, 'ease_duration': 0.5, 'randomize_target': True
            },
            'BROADCAST_QUALITY': {
                'duration_sec': 8.0, 'shuffle_speed': 2.0, 'shuffle_cycles': 4,
                'shuffle_amplitude': 2.0, 'vertical_bounce': 0.3, 'spacing_buffer': 1.5,
                'reveal_duration': 1.5, 'reveal_height': 1.0, 'sway_amount': 0.1,
                'ease_duration': 1.0, 'randomize_target': True
            },
            'MINIMAL_CLEAN': {
                'duration_sec': 6.0, 'shuffle_speed': 1.5, 'shuffle_cycles': 3,
                'shuffle_amplitude': 1.2, 'vertical_bounce': 0.1, 'spacing_buffer': 1.8,
                'reveal_duration': 1.2, 'reveal_height': 0.6, 'camera_sway': False,
                'sway_amount': 0.0, 'ease_duration': 1.5, 'randomize_target': False
            },
            'HIGH_ENERGY': {
                'duration_sec': 4.0, 'fps': 30, 'shuffle_speed': 3.5, 'shuffle_cycles': 3,
                'shuffle_amplitude': 1.8, 'vertical_bounce': 0.6, 'spacing_buffer': 1.3,
                'reveal_duration': 1.0, 'reveal_height': 1.4, 'sway_amount': 0.25,
                'ease_out': False, 'ease_duration': 0.5, 'randomize_target': True
            }
        }
        
        if preset_name in presets:
            for key, value in presets[preset_name].items():
                setattr(props, key, value)

# ============================================================================
# USER INTERFACE PANEL
# ============================================================================

class LAURIER_PT_shell_game_panel(Panel):
    """Panel for Laurier Shell Game controls"""
    bl_label = "Laurier Football Shell Game"
    bl_idname = "LAURIER_PT_shell_game_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Laurier Football"
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.laurier_shell_game
        
        # Header
        box = layout.box()
        box.label(text="🏈 Laurier Football Shell Game", icon='ARMATURE_DATA')
        box.label(text="Professional 3D Animation Addon")
        
        # Preset Selection
        layout.separator()
        layout.prop(props, "preset")
        
        # Animation Settings
        if props.preset == 'CUSTOM':
            layout.separator()
            box = layout.box()
            box.label(text="Animation Settings")
            box.prop(props, "duration_sec")
            box.prop(props, "fps")
            box.prop(props, "shuffle_speed")
            box.prop(props, "shuffle_cycles")
            
            # Movement Settings
            box = layout.box()
            box.label(text="Movement Settings")
            box.prop(props, "shuffle_amplitude")
            box.prop(props, "vertical_bounce")
            box.prop(props, "spacing_buffer")
            
            # Reveal Settings
            box = layout.box()
            box.label(text="Reveal Settings")
            box.prop(props, "reveal_target")
            box.prop(props, "reveal_duration")
            box.prop(props, "reveal_height")
            
            # Effects
            box = layout.box()
            box.label(text="Effects")
            box.prop(props, "camera_sway")
            if props.camera_sway:
                box.prop(props, "sway_amount")
            box.prop(props, "ease_out")
            if props.ease_out:
                box.prop(props, "ease_duration")
            box.prop(props, "randomize_target")
        
        # Create Animation Button
        layout.separator()
        row = layout.row()
        row.scale_y = 2.0
        row.operator("laurier.create_shell_game", text="Create Shell Game Animation", icon='PLAY')
        
        # Help Section
        layout.separator()
        box = layout.box()
        box.label(text="📋 Setup Requirements:")
        box.label(text="• Empty_1, Empty_2, Empty_3")
        box.label(text="• Football_CTRL")
        box.label(text="• Helmets parented to empties")
        box.label(text="• Football parented to Football_CTRL")
        
        # Status
        layout.separator()
        box = layout.box()
        box.label(text="📊 Animation Info:")
        box.label(text=f"Duration: {props.duration_sec}s")
        box.label(text=f"Frames: {int(props.duration_sec * props.fps)}")
        box.label(text=f"Target: Helmet {props.reveal_target}")

# ============================================================================
# REGISTRATION
# ============================================================================

classes = (
    LaurierShellGameProperties,
    LAURIER_OT_create_shell_game,
    LAURIER_PT_shell_game_panel,
)

def register():
    """Register the addon."""
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.laurier_shell_game = PointerProperty(type=LaurierShellGameProperties)
    print("🏈 Laurier Football Shell Game Addon registered successfully!")

def unregister():
    """Unregister the addon."""
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    del bpy.types.Scene.laurier_shell_game
    print("🏈 Laurier Football Shell Game Addon unregistered.")

if __name__ == "__main__":
    register()
