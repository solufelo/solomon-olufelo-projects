"""
Laurier Football Shell Game Animation Addon
===========================================

Automated 3D shell game shuffle animation for Laurier Football promos.
Creates smooth, professional helmet shuffle with hidden football reveal.

Author: Solomon Olufelo
Created: 2024
Compatible: Blender 4.x

Setup Requirements:
- Three helmets parented to Empty_1, Empty_2, Empty_3
- Football parented to Football_CTRL empty
- Scene configured with proper lighting and camera

Usage:
1. Install as Blender addon
2. Find "Laurier Tools" in 3D Viewport sidebar
3. Adjust parameters and click "Create Shell Game Animation"
"""

import bpy
import bmesh
import mathutils
from math import sin, cos, pi
import random
from bpy.types import Operator, Panel
from bpy.props import FloatProperty, IntProperty, BoolProperty

# ============================================================================
# CONFIGURATION PARAMETERS - Adjust these values as needed
# ============================================================================

CONFIG = {
    # Animation timing
    "duration_sec": 8.0,           # Total animation duration
    "fps": 24,                     # Frames per second
    "shuffle_speed": 3.5,          # Speed of shuffle movements (higher = faster)
    "shuffle_cycles": 4,           # Number of shuffle cycles
    
    # Movement parameters
    "shuffle_amplitude": 12.0,     # How far helmets move horizontally (scaled up for large objects)
    "vertical_bounce": 2.0,        # Vertical bounce height (scaled up)
    "spacing_buffer": 8.0,         # Minimum distance between helmets (scaled up)
    
    # Reveal settings
    "reveal_target": 2,            # Which helmet (1, 2, or 3) hides the football
    "reveal_duration": 1.5,        # How long the reveal takes
    "reveal_height": 4.0,          # How high the revealing helmet lifts (scaled up)
    
    # Camera and effects
    "camera_sway": True,           # Add subtle camera movement
    "sway_amount": 0.1,            # Intensity of camera sway
    "ease_out": True,              # Slow down before reveal
    "ease_duration": 1.0,          # How long the ease-out lasts
    
    # Randomization
    "randomize_target": True,      # Randomly choose which helmet hides football
    "add_dust_effects": False,     # Add particle effects (v2 feature)
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_empty_object(name):
    """Get empty object by name, with error handling."""
    obj = bpy.data.objects.get(name)
    if not obj:
        raise ValueError(f"Required empty '{name}' not found in scene. Please ensure your scene is set up correctly.")
    return obj

def ease_out_cubic(t):
    """Cubic ease-out function for smooth deceleration."""
    return 1 - pow(1 - t, 3)

def ease_in_out_sine(t):
    """Sine ease-in-out for natural movement."""
    return -(cos(pi * t) - 1) / 2

def create_sine_wave_movement(frame, amplitude, frequency, phase_offset=0):
    """Generate sine wave movement with phase offset for different helmets."""
    t = frame / (CONFIG["fps"] * CONFIG["duration_sec"])
    return amplitude * sin(2 * pi * frequency * t + phase_offset)

def add_vertical_bounce(frame):
    """Add realistic vertical bounce to helmet movement."""
    t = frame / (CONFIG["fps"] * CONFIG["duration_sec"])
    # Create bounce pattern that peaks during shuffle movements
    bounce = CONFIG["vertical_bounce"] * abs(sin(2 * pi * CONFIG["shuffle_speed"] * t))
    return bounce

def calculate_helmet_positions(frame):
    """Calculate positions for all three helmets with collision avoidance."""
    positions = {}
    
    # Base positions for helmets (side by side) - wider spacing
    base_positions = {
        1: mathutils.Vector((-CONFIG["spacing_buffer"], 0, 0)),
        2: mathutils.Vector((0, 0, 0)),
        3: mathutils.Vector((CONFIG["spacing_buffer"], 0, 0))
    }
    
    # Calculate sine wave movements for each helmet
    for helmet_num in [1, 2, 3]:
        # Phase offset ensures helmets move in different patterns
        # Use different phase offsets to create more dramatic movement
        phase_offset = (helmet_num - 1) * (2 * pi / 3) + (frame * 0.1)
        
        # Calculate horizontal movement with more dramatic amplitude
        horizontal_offset = create_sine_wave_movement(
            frame, 
            CONFIG["shuffle_amplitude"], 
            CONFIG["shuffle_speed"], 
            phase_offset
        )
        
        # Add secondary wave for more complex movement
        secondary_offset = create_sine_wave_movement(
            frame,
            CONFIG["shuffle_amplitude"] * 0.5,
            CONFIG["shuffle_speed"] * 1.5,
            phase_offset + pi/2
        )
        
        # Calculate vertical bounce
        vertical_bounce = add_vertical_bounce(frame)
        
        # Get base position and apply offsets
        pos = base_positions[helmet_num].copy()
        pos.x += horizontal_offset + secondary_offset
        pos.z += vertical_bounce
        
        positions[helmet_num] = pos
    
    return positions

def apply_ease_out(frame):
    """Apply ease-out effect to slow down before reveal."""
    if not CONFIG["ease_out"]:
        return 1.0
    
    # Calculate progress through ease-out period
    total_frames = CONFIG["duration_sec"] * CONFIG["fps"]
    ease_frames = CONFIG["ease_duration"] * CONFIG["fps"]
    ease_start_frame = total_frames - ease_frames
    
    if frame < ease_start_frame:
        return 1.0
    
    # Apply ease-out to the last portion of animation
    # But don't let it go below 0.3 to maintain some movement
    ease_progress = (frame - ease_start_frame) / ease_frames
    eased_value = ease_out_cubic(ease_progress)
    return max(0.3, eased_value)  # Minimum 30% movement to keep shuffle visible

# ============================================================================
# MAIN ANIMATION FUNCTIONS
# ============================================================================

def setup_scene():
    """Initialize scene settings and validate required objects."""
    print("Setting up Laurier Shell Game animation...")
    
    # Set scene frame rate
    bpy.context.scene.frame_set(1)
    bpy.context.scene.render.fps = CONFIG["fps"]
    
    # Validate required objects exist
    required_empties = ["Empty_1", "Empty_2", "Empty_3", "Football_CTRL"]
    for empty_name in required_empties:
        if not bpy.data.objects.get(empty_name):
            raise ValueError(f"Required object '{empty_name}' not found. Please ensure your scene is set up correctly.")
    
    print("✓ Scene setup complete")

def randomize_football_target():
    """Randomly choose which helmet hides the football."""
    if CONFIG["randomize_target"]:
        CONFIG["reveal_target"] = random.randint(1, 3)
        print(f"🎲 Randomly selected helmet {CONFIG['reveal_target']} to hide the football")

def animate_helmets():
    """Create smooth shuffle animation for all helmets."""
    print("Animating helmet shuffle...")
    
    total_frames = int(CONFIG["duration_sec"] * CONFIG["fps"])
    
    for frame in range(1, total_frames + 1):
        # Calculate positions for this frame
        positions = calculate_helmet_positions(frame)
        
        # Apply ease-out effect
        ease_factor = apply_ease_out(frame)
        
        # Animate each helmet
        for helmet_num in [1, 2, 3]:
            empty_name = f"Empty_{helmet_num}"
            empty_obj = get_empty_object(empty_name)
            
            # Get calculated position
            pos = positions[helmet_num]
            
            # Apply easing only to the movement offset, not the base position
            # This ensures helmets still move but slow down before reveal
            base_pos = mathutils.Vector((-CONFIG["spacing_buffer"], 0, 0)) if helmet_num == 1 else \
                      mathutils.Vector((0, 0, 0)) if helmet_num == 2 else \
                      mathutils.Vector((CONFIG["spacing_buffer"], 0, 0))
            
            # Calculate movement offset and apply easing
            movement_offset = pos - base_pos
            movement_offset.x *= ease_factor
            movement_offset.z *= ease_factor
            
            # Final position = base + eased movement
            final_pos = base_pos + movement_offset
            
            # Set keyframe
            empty_obj.location = final_pos
            empty_obj.keyframe_insert(data_path="location", frame=frame)
    
    print("✓ Helmet animation complete")

def animate_football():
    """Animate football to follow the target helmet."""
    print("Animating football...")
    
    football_ctrl = get_empty_object("Football_CTRL")
    target_empty = get_empty_object(f"Empty_{CONFIG['reveal_target']}")
    
    total_frames = int(CONFIG["duration_sec"] * CONFIG["fps"])
    
    for frame in range(1, total_frames + 1):
        # Follow target helmet position
        football_ctrl.location = target_empty.location
        football_ctrl.keyframe_insert(data_path="location", frame=frame)
    
    print("✓ Football animation complete")

def create_reveal_animation():
    """Create dramatic reveal animation for the target helmet."""
    print("Creating reveal animation...")
    
    target_empty = get_empty_object(f"Empty_{CONFIG['reveal_target']}")
    football_ctrl = get_empty_object("Football_CTRL")
    
    # Calculate reveal timing
    total_frames = int(CONFIG["duration_sec"] * CONFIG["fps"])
    reveal_frames = int(CONFIG["reveal_duration"] * CONFIG["fps"])
    reveal_start_frame = total_frames - reveal_frames + 1
    
    # Get final position before reveal
    final_pos = target_empty.location.copy()
    
    # Create reveal lift animation
    for i, frame in enumerate(range(reveal_start_frame, total_frames + 1)):
        progress = i / (reveal_frames - 1)
        ease_progress = ease_out_cubic(progress)
        
        # Lift helmet up
        reveal_pos = final_pos.copy()
        reveal_pos.z += CONFIG["reveal_height"] * ease_progress
        
        # Update helmet position
        target_empty.location = reveal_pos
        target_empty.keyframe_insert(data_path="location", frame=frame)
        
        # Keep football at original position (now revealed)
        football_ctrl.location = final_pos
        football_ctrl.keyframe_insert(data_path="location", frame=frame)
    
    print("✓ Reveal animation complete")

def animate_camera():
    """Add subtle camera sway for cinematic feel."""
    if not CONFIG["camera_sway"]:
        return
    
    print("Adding camera sway...")
    
    camera = bpy.context.scene.camera
    if not camera:
        print("⚠️  No camera found in scene, skipping camera animation")
        return
    
    total_frames = int(CONFIG["duration_sec"] * CONFIG["fps"])
    
    for frame in range(1, total_frames + 1):
        t = frame / (CONFIG["fps"] * CONFIG["duration_sec"])
        
        # Create gentle sway motion
        sway_x = CONFIG["sway_amount"] * sin(2 * pi * 0.5 * t)
        sway_y = CONFIG["sway_amount"] * cos(2 * pi * 0.3 * t)
        
        # Apply to camera rotation
        camera.rotation_euler.x += sway_x * 0.1
        camera.rotation_euler.y += sway_y * 0.1
        camera.keyframe_insert(data_path="rotation_euler", frame=frame)
    
    print("✓ Camera sway complete")

def create_dust_effects():
    """Add particle effects for shuffle impacts (v2 feature)."""
    if not CONFIG["add_dust_effects"]:
        return
    
    print("Creating dust effects...")
    # TODO: Implement particle system for dust effects
    # This would involve creating particle systems on helmet impacts
    print("⚠️  Dust effects not yet implemented (v2 feature)")

def set_render_settings():
    """Configure render settings for output."""
    print("Configuring render settings...")
    
    scene = bpy.context.scene
    
    # Set frame range
    total_frames = int(CONFIG["duration_sec"] * CONFIG["fps"])
    scene.frame_start = 1
    scene.frame_end = total_frames
    
    # Set output settings for After Effects
    scene.render.image_settings.file_format = 'PNG'
    scene.render.image_settings.color_mode = 'RGBA'
    scene.render.image_settings.color_depth = '16'
    
    print("✓ Render settings configured")
    print(f"  Frame range: 1-{total_frames}")
    print(f"  Output format: PNG sequence with alpha")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main function to run the complete shell game animation."""
    try:
        print("🏈 Starting Laurier Football Shell Game Animation")
        print("=" * 50)
        
        # Initialize scene
        setup_scene()
        
        # Randomize target if enabled
        randomize_football_target()
        
        # Create animations
        animate_helmets()
        animate_football()
        create_reveal_animation()
        animate_camera()
        create_dust_effects()
        
        # Configure output
        set_render_settings()
        
        print("=" * 50)
        print("🎉 Animation complete!")
        print(f"🏆 Football is hidden under helmet {CONFIG['reveal_target']}")
        print("📹 Ready for rendering and After Effects compositing")
        print("\nNext steps:")
        print("1. Preview animation in viewport")
        print("2. Render PNG sequence")
        print("3. Import into After Effects for final compositing")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Ensure all required empty objects exist:")
        print("   - Empty_1, Empty_2, Empty_3 (for helmets)")
        print("   - Football_CTRL (for football)")
        print("2. Check that helmets are parented to empties")
        print("3. Verify scene has proper lighting and camera setup")

# ============================================================================
# BLENDER ADDON CLASSES
# ============================================================================

class LaurierShellGameOperator(Operator):
    """Operator to create the shell game animation."""
    bl_idname = "laurier.shell_game_animation"
    bl_label = "Create Shell Game Animation"
    bl_description = "Generate automated 3D shell game shuffle animation"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        """Execute the shell game animation creation."""
        try:
            # Update CONFIG with current scene settings
            main()
            self.report({'INFO'}, "Shell game animation created successfully!")
            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, f"Error: {str(e)}")
            return {'CANCELLED'}

class LaurierShellGamePanel(Panel):
    """Panel for Laurier Shell Game tools."""
    bl_label = "Laurier Shell Game"
    bl_idname = "LAURIER_PT_shell_game"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Laurier Tools"

    def draw(self, context):
        """Draw the panel UI."""
        layout = self.layout
        
        # Header
        layout.label(text="🏈 Football Shell Game Animation", icon='MESH_MONKEY')
        
        # Configuration section
        box = layout.box()
        box.label(text="Animation Settings:", icon='SETTINGS')
        
        # Duration
        row = box.row()
        row.label(text="Duration:")
        row.prop(context.scene, "laurier_duration", text="")
        
        # Shuffle speed
        row = box.row()
        row.label(text="Shuffle Speed:")
        row.prop(context.scene, "laurier_shuffle_speed", text="")
        
        # Movement amplitude
        row = box.row()
        row.label(text="Movement Size:")
        row.prop(context.scene, "laurier_amplitude", text="")
        
        # Reveal settings
        box = layout.box()
        box.label(text="Reveal Settings:", icon='HIDE_OFF')
        
        row = box.row()
        row.label(text="Target Helmet:")
        row.prop(context.scene, "laurier_reveal_target", text="")
        
        row = box.row()
        row.label(text="Random Target:")
        row.prop(context.scene, "laurier_random_target", text="")
        
        # Execute button
        layout.separator()
        layout.operator("laurier.shell_game_animation", 
                       text="🎬 Create Animation", 
                       icon='PLAY')

# Add properties to scene
def register_properties():
    """Register custom properties."""
    bpy.types.Scene.laurier_duration = FloatProperty(
        name="Duration",
        description="Animation duration in seconds",
        default=8.0,
        min=1.0,
        max=30.0
    )
    
    bpy.types.Scene.laurier_shuffle_speed = FloatProperty(
        name="Shuffle Speed",
        description="Speed of shuffle movements",
        default=3.5,
        min=0.5,
        max=10.0
    )
    
    bpy.types.Scene.laurier_amplitude = FloatProperty(
        name="Movement Amplitude",
        description="How far helmets move horizontally",
        default=12.0,
        min=1.0,
        max=50.0
    )
    
    bpy.types.Scene.laurier_reveal_target = IntProperty(
        name="Reveal Target",
        description="Which helmet hides the football (1, 2, or 3)",
        default=2,
        min=1,
        max=3
    )
    
    bpy.types.Scene.laurier_random_target = BoolProperty(
        name="Random Target",
        description="Randomly choose which helmet hides the football",
        default=True
    )

def unregister_properties():
    """Unregister custom properties."""
    del bpy.types.Scene.laurier_duration
    del bpy.types.Scene.laurier_shuffle_speed
    del bpy.types.Scene.laurier_amplitude
    del bpy.types.Scene.laurier_reveal_target
    del bpy.types.Scene.laurier_random_target

# Run the animation
if __name__ == "__main__":
    main()
