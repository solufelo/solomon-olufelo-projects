bl_info = {
    "name": "Wolfpack Glory Helmet Shuffle",
    "author": "Solomon Olufelo / Wolfpack Glory",
    "version": (2, 0, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Wolfpack Shuffle",
    "description": "Collision-free parametric helmet shuffle generator for jumbotron promos",
    "category": "Animation",
}

import bpy
import math
import random
from typing import List, Tuple, Dict, Optional

# ============================================================================
# VECTOR & MATH UTILITIES (Clean & Independent)
# ============================================================================

class Vector3:
    __slots__ = ('x', 'y', 'z')
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def distance_to(self, other) -> float:
        return (self - other).length()

    def copy(self):
        return Vector3(self.x, self.y, self.z)

    def as_tuple(self) -> Tuple[float, float, float]:
        return (self.x, self.y, self.z)


class MoveStep:
    """Represents a discrete swap or carousel move in the shuffle."""
    def __init__(self, move_type: str, slots: List[int], start_frame: int, end_frame: int, y_depth: float, bounce_height: float, style: str = 'SMOOTH'):
        self.move_type = move_type      # 'PAIR_SWAP' or 'CAROUSEL'
        self.slots = slots              # Slot indices participating
        self.start_frame = start_frame
        self.end_frame = end_frame
        self.y_depth = y_depth
        self.bounce_height = bounce_height
        self.style = style


def ease_smoothstep(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return t * t * (3.0 - 2.0 * t)


def ease_whip(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return t * t * t * (t * (t * 6.0 - 15.0) + 10.0)


def ease_bouncy(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return (1.0 - math.cos(math.pi * t)) / 2.0


# ============================================================================
# SHUFFLE ENGINE (Collision-Free Parametric Mechanics)
# ============================================================================

class ShufflePlan:
    """
    Manages discrete slots, movement scheduling, and calculates frame-by-frame
    collision-free trajectories with fixed center-of-mass preservation.
    """
    def __init__(
        self,
        num_items: int = 3,
        slot_spacing: float = 2.4,
        y_depth_base: float = 1.35,
        bounce_height: float = 0.25,
        fps: int = 30
    ):
        self.num_items = num_items
        self.slot_spacing = slot_spacing
        self.y_depth_base = y_depth_base
        self.bounce_height = bounce_height
        self.fps = fps
        
        # Center of mass is pinned strictly at X = 0, Y = 0, Z = 0
        offset = (num_items - 1) * slot_spacing / 2.0
        self.slot_centers = [
            Vector3(i * slot_spacing - offset, 0.0, 0.0)
            for i in range(num_items)
        ]
        
        self.slot_occupant = list(range(num_items))
        self.item_slot = list(range(num_items))
        
        self.moves: List[MoveStep] = []
        self.total_frames = 0
        self.ball_holder_item_id = 1
        self.reveal_item_id = 1

    def get_slot_center(self, slot_idx: int) -> Vector3:
        return self.slot_centers[slot_idx].copy()

    def generate_routine(
        self,
        num_swaps: int = 8,
        swap_duration_frames: int = 24,
        pause_frames: int = 4,
        target_item: Optional[int] = None,
        style: str = 'SMOOTH'
    ):
        self.moves.clear()
        self.slot_occupant = list(range(self.num_items))
        self.item_slot = list(range(self.num_items))
        
        if target_item is not None and 0 <= target_item < self.num_items:
            self.ball_holder_item_id = target_item
        else:
            self.ball_holder_item_id = random.randint(0, self.num_items - 1)
        
        current_frame = 30  # Intro cushion
        last_swapped_pair = None
        
        for i in range(num_swaps):
            possible_pairs = [(0, 1), (1, 2), (0, 2)] if self.num_items == 3 else [
                (a, b) for a in range(self.num_items) for b in range(a + 1, self.num_items)
            ]
            candidates = [p for p in possible_pairs if p != last_swapped_pair]
            s1, s2 = random.choice(candidates)
            last_swapped_pair = (s1, s2)
            
            dist_factor = abs(s1 - s2)
            y_depth = self.y_depth_base * (1.0 + (dist_factor - 1) * 0.35)
            
            move = MoveStep(
                move_type='PAIR_SWAP',
                slots=[s1, s2],
                start_frame=current_frame,
                end_frame=current_frame + swap_duration_frames,
                y_depth=y_depth,
                bounce_height=self.bounce_height,
                style=style
            )
            self.moves.append(move)
            current_frame = move.end_frame + pause_frames
            
            occ1, occ2 = self.slot_occupant[s1], self.slot_occupant[s2]
            self.slot_occupant[s1], self.slot_occupant[s2] = occ2, occ1
            self.item_slot[occ1] = s2
            self.item_slot[occ2] = s1
        
        self.reveal_item_id = self.ball_holder_item_id
        self.total_frames = current_frame + 50  # Outro / reveal buffer

    def evaluate_at_frame(self, frame: int) -> Dict[int, Tuple[Vector3, Vector3]]:
        slot_occ = list(range(self.num_items))
        item_to_slot = list(range(self.num_items))
        current_move: Optional[MoveStep] = None
        
        for move in self.moves:
            if frame < move.start_frame:
                break
            elif move.start_frame <= frame <= move.end_frame:
                current_move = move
                break
            else:
                s1, s2 = move.slots
                it1, it2 = slot_occ[s1], slot_occ[s2]
                slot_occ[s1], slot_occ[s2] = it2, it1
                item_to_slot[it1], item_to_slot[it2] = s2, s1

        results = {}
        if not current_move:
            for item_id in range(self.num_items):
                slot_idx = item_to_slot[item_id]
                pos = self.get_slot_center(slot_idx)
                rot = Vector3(0.0, 0.0, 0.0)
                results[item_id] = (pos, rot)
            return results

        progress = (frame - current_move.start_frame) / max(1, (current_move.end_frame - current_move.start_frame))
        
        if current_move.style == 'WHIP':
            t_eval = ease_whip(progress)
        elif current_move.style == 'BOUNCY':
            t_eval = ease_bouncy(progress)
        else:
            t_eval = ease_smoothstep(progress)
            
        bounce_t = math.sin(progress * math.pi)
        vertical_offset = current_move.bounce_height * bounce_t

        s1, s2 = current_move.slots
        it1, it2 = slot_occ[s1], slot_occ[s2]
        p1, p2 = self.get_slot_center(s1), self.get_slot_center(s2)
        
        x_mid = (p1.x + p2.x) / 2.0
        x_radius = abs(p2.x - p1.x) / 2.0
        theta = t_eval * math.pi
        sign = 1.0 if p1.x < p2.x else -1.0
        
        # Orbit paths with guaranteed passing depth
        pos_it1 = Vector3(
            x=x_mid - sign * x_radius * math.cos(theta),
            y=+current_move.y_depth * math.sin(theta),
            z=p1.z + vertical_offset
        )
        bank_it1 = math.radians(-14.0) * math.sin(theta) * sign
        
        pos_it2 = Vector3(
            x=x_mid + sign * x_radius * math.cos(theta),
            y=-current_move.y_depth * math.sin(theta),
            z=p2.z + vertical_offset
        )
        bank_it2 = math.radians(14.0) * math.sin(theta) * sign
        
        results[it1] = (pos_it1, Vector3(0.0, bank_it1, 0.0))
        results[it2] = (pos_it2, Vector3(0.0, bank_it2, 0.0))
        
        for item_id in range(self.num_items):
            if item_id not in (it1, it2):
                slot_idx = item_to_slot[item_id]
                results[item_id] = (self.get_slot_center(slot_idx), Vector3(0.0, 0.0, 0.0))
                
        return results

    def verify_no_collisions(self, min_safe_distance: float = 1.0) -> Tuple[bool, float, Optional[Tuple[int, int, int]]]:
        min_dist_found = float('inf')
        worst_case = None
        for frame in range(0, self.total_frames + 1):
            evals = self.evaluate_at_frame(frame)
            for i in range(self.num_items):
                for j in range(i + 1, self.num_items):
                    pos_i, _ = evals[i]
                    pos_j, _ = evals[j]
                    dist = pos_i.distance_to(pos_j)
                    if dist < min_dist_found:
                        min_dist_found = dist
                        worst_case = (frame, i, j)
        passed = (min_dist_found >= min_safe_distance)
        return passed, min_dist_found, worst_case


# ============================================================================
# BLENDER INTEGRATION & DEMO SCENE BUILDER
# ============================================================================

def setup_demo_scene_if_needed(slot_spacing: float = 2.4):
    """
    Creates standard Empty controllers and visually distinct stand-in helmets + football
    if the user hasn't already defined them in their blend file.
    """
    scene = bpy.context.scene
    required_empties = ["Helmet_1", "Helmet_2", "Helmet_3", "Football_CTRL"]
    existing = [name for name in required_empties if bpy.data.objects.get(name)]
    
    if len(existing) == len(required_empties):
        return  # Everything already exists
    
    # Create Wolfpack collection
    coll_name = "Wolfpack_Shuffle"
    if coll_name in bpy.data.collections:
        coll = bpy.data.collections[coll_name]
    else:
        coll = bpy.data.collections.new(coll_name)
        bpy.context.scene.collection.children.link(coll)
        
    # Helper to add object to collection
    def link_obj(obj):
        for c in list(obj.users_collection):
            if c != coll:
                c.objects.unlink(obj)
        if obj.name not in coll.objects:
            coll.objects.link(obj)

    # Official Wilfrid Laurier Golden Hawks Colors: Deep Purple (#4B2882) and Hawk Gold (#FDB813)
    hawk_purple = (0.294, 0.157, 0.510, 1.0)
    hawk_gold   = (0.992, 0.722, 0.075, 1.0)
    white_trim  = (0.95, 0.95, 0.95, 1.0)
    colors = [hawk_purple, hawk_gold, hawk_purple]
    stripe_colors = [hawk_gold, hawk_purple, hawk_gold]
    
    for i in range(3):
        h_name = f"Helmet_{i+1}"
        if not bpy.data.objects.get(h_name):
            # Create root empty controller
            empty = bpy.data.objects.new(h_name, None)
            empty.empty_display_type = 'ARROWS'
            empty.empty_display_size = 0.6
            empty.location = ((i - 1) * slot_spacing, 0.0, 0.0)
            coll.objects.link(empty)
            
            # Create Realistic Laurier Football Helmet Shell
            bpy.ops.mesh.primitive_uv_sphere_add(radius=0.75, location=(0, 0, 0.75))
            dome = bpy.context.active_object
            dome.name = f"Laurier_HelmetShell_{i+1}"
            dome.scale = (0.92, 1.05, 0.98)
            dome.parent = empty
            link_obj(dome)
            
            # Helmet Dome Material
            mat_helmet = bpy.data.materials.new(name=f"Mat_Laurier_Helmet_{i+1}")
            bsdf = mat_helmet.node_tree.nodes.get("Principled BSDF")
            if bsdf:
                bsdf.inputs['Base Color'].default_value = colors[i]
                bsdf.inputs['Roughness'].default_value = 0.25 # Glossy helmet finish
            dome.data.materials.append(mat_helmet)
            
            # Facemask Cage (Cylinder arch)
            bpy.ops.mesh.primitive_cylinder_add(
                radius=0.55, 
                depth=0.25, 
                location=(0, -0.35, 0.52), 
                rotation=(math.radians(90.0), 0, 0)
            )
            facemask = bpy.context.active_object
            facemask.name = f"Facemask_{i+1}"
            facemask.parent = empty
            link_obj(facemask)
            
            # Facemask Material (Hawk Gold or White)
            mat_mask = bpy.data.materials.new(name=f"Mat_Facemask_{i+1}")
            bsdf_m = mat_mask.node_tree.nodes.get("Principled BSDF")
            if bsdf_m:
                bsdf_m.inputs['Base Color'].default_value = stripe_colors[i]
                bsdf_m.inputs['Metallic'].default_value = 0.6
                bsdf_m.inputs['Roughness'].default_value = 0.3
            facemask.data.materials.append(mat_mask)

    # Create Official Football / Target
    if not bpy.data.objects.get("Football_CTRL"):
        fb_empty = bpy.data.objects.new("Football_CTRL", None)
        fb_empty.empty_display_type = 'SPHERE'
        fb_empty.empty_display_size = 0.4
        coll.objects.link(fb_empty)
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.35, location=(0, 0, 0.35))
        fb_mesh = bpy.context.active_object
        fb_mesh.name = "Laurier_Football_Mesh"
        fb_mesh.scale = (1.35, 0.75, 0.75)  # Authentic pigskin ratio
        fb_mesh.parent = fb_empty
        link_obj(fb_mesh)
        
        mat = bpy.data.materials.new(name="Mat_Laurier_Football")
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        if bsdf:
            bsdf.inputs['Base Color'].default_value = (0.28, 0.12, 0.04, 1.0) # Wilson leather brown
            bsdf.inputs['Roughness'].default_value = 0.65
        fb_mesh.data.materials.append(mat)

    # Ensure Camera
    if not scene.camera:
        cam_data = bpy.data.cameras.new("Shuffle_Camera")
        cam_obj = bpy.data.objects.new("Shuffle_Camera", cam_data)
        cam_obj.location = (0.0, -8.0, 4.0)
        cam_obj.rotation_euler = (math.radians(65.0), 0.0, 0.0)
        coll.objects.link(cam_obj)
        scene.camera = cam_obj


def get_shuffle_objects(props):
    """
    Resolves the 3 shuffling objects (over items) and the hidden prize object (under item).
    Prioritizes user-selected scene objects, then falls back to standard named objects.
    """
    objects = []
    # Helmet 1
    h1 = props.custom_helmet_1 or bpy.data.objects.get("Helmet_1") or bpy.data.objects.get("Empty_1")
    # Helmet 2
    h2 = props.custom_helmet_2 or bpy.data.objects.get("Helmet_2") or bpy.data.objects.get("Empty_2")
    # Helmet 3
    h3 = props.custom_helmet_3 or bpy.data.objects.get("Helmet_3") or bpy.data.objects.get("Empty_3")
    objects = [h1, h2, h3]
    
    # Prize / Football object
    prize = props.custom_football or bpy.data.objects.get("Football_CTRL") or bpy.data.objects.get("Football")
    
    return objects, prize


def bake_shuffle_to_scene(props):
    """Bakes collision-free keyframes into the scene."""
    scene = bpy.context.scene
    scene.render.fps = props.fps
    
    # Check if we have objects or need to spawn stand-ins
    objects, fb_ctrl = get_shuffle_objects(props)
    if not any(objects):
        setup_demo_scene_if_needed(props.slot_spacing)
        objects, fb_ctrl = get_shuffle_objects(props)
        
    valid_objects = [obj for obj in objects if obj is not None]
    if len(valid_objects) < 2:
        raise ValueError("Please select or name at least 2 objects (Helmet 1, 2, 3) to shuffle!")
    
    plan = ShufflePlan(
        num_items=3,
        slot_spacing=props.slot_spacing,
        y_depth_base=props.y_depth,
        bounce_height=props.bounce_height,
        fps=props.fps
    )
    
    target_idx = props.reveal_target - 1 if not props.randomize_target else None
    plan.generate_routine(
        num_swaps=props.num_swaps,
        swap_duration_frames=props.swap_duration,
        pause_frames=props.pause_frames,
        target_item=target_idx,
        style=props.movement_style
    )
    
    # Clear existing animation data on target objects
    for obj in valid_objects + ([fb_ctrl] if fb_ctrl else []):
        if obj and obj.animation_data:
            obj.animation_data_clear()

    # 1. Animate Helmets / Upper Items
    for frame in range(1, plan.total_frames + 1):
        evals = plan.evaluate_at_frame(frame)
        for item_id, obj in enumerate(objects):
            if not obj:
                continue
            pos, rot = evals[item_id]
            obj.location = pos.as_tuple()
            obj.rotation_euler = rot.as_tuple()
            obj.keyframe_insert(data_path="location", frame=frame)
            obj.keyframe_insert(data_path="rotation_euler", frame=frame)

    # 2. Animate Football / Prize following the winner helmet
    winning_item_id = plan.reveal_item_id
    if fb_ctrl:
        for frame in range(1, plan.total_frames + 1):
            evals = plan.evaluate_at_frame(frame)
            winner_pos, _ = evals[winning_item_id]
            fb_ctrl.location = (winner_pos.x, winner_pos.y, 0.0)
            fb_ctrl.keyframe_insert(data_path="location", frame=frame)

    # 3. Animate Reveal (Lifting helmet & tilt)
    reveal_start = plan.total_frames - 35
    reveal_end = plan.total_frames
    winner_obj = objects[winning_item_id]
    
    if winner_obj:
        evals_reveal = plan.evaluate_at_frame(reveal_start)
        base_pos, _ = evals_reveal[winning_item_id]
        for frame in range(reveal_start, reveal_end + 1):
            t = (frame - reveal_start) / max(1, (reveal_end - reveal_start))
            ease_lift = ease_smoothstep(t)
            
            lift_z = base_pos.z + props.reveal_height * ease_lift
            tilt_x = math.radians(props.reveal_tilt) * ease_lift
            
            winner_obj.location = (base_pos.x, base_pos.y, lift_z)
            winner_obj.rotation_euler = (tilt_x, 0.0, 0.0)
            winner_obj.keyframe_insert(data_path="location", frame=frame)
            winner_obj.keyframe_insert(data_path="rotation_euler", frame=frame)

    scene.frame_start = 1
    scene.frame_end = plan.total_frames
    scene.frame_set(1)
    return winning_item_id + 1, plan.total_frames


# ============================================================================
# BLENDER UI PROPERTIES, OPERATOR & PANEL
# ============================================================================

class WolfpackShuffleProperties(bpy.types.PropertyGroup):
    # Direct Custom Object Linking (Pick ANY object in scene)
    custom_helmet_1: bpy.props.PointerProperty(
        name="Helmet 1 (Left)",
        type=bpy.types.Object,
        description="Select any custom model or empty for Slot 1"
    )
    custom_helmet_2: bpy.props.PointerProperty(
        name="Helmet 2 (Center)",
        type=bpy.types.Object,
        description="Select any custom model or empty for Slot 2"
    )
    custom_helmet_3: bpy.props.PointerProperty(
        name="Helmet 3 (Right)",
        type=bpy.types.Object,
        description="Select any custom model or empty for Slot 3"
    )
    custom_football: bpy.props.PointerProperty(
        name="Hidden Prize (Under)",
        type=bpy.types.Object,
        description="Select any custom football, coin, or prize object hidden underneath"
    )

    num_swaps: bpy.props.IntProperty(
        name="Number of Swaps",
        description="Total shuffle operations",
        default=9,
        min=3,
        max=30
    )
    swap_duration: bpy.props.IntProperty(
        name="Swap Frames",
        description="Duration of each swap move in frames",
        default=22,
        min=10,
        max=60
    )
    pause_frames: bpy.props.IntProperty(
        name="Pause Frames",
        description="Short pause between moves for readability",
        default=4,
        min=0,
        max=20
    )
    fps: bpy.props.IntProperty(
        name="FPS",
        description="Render framerate",
        default=30,
        min=24,
        max=60
    )
    slot_spacing: bpy.props.FloatProperty(
        name="Slot Spacing",
        description="Distance between adjacent helmet slots (X-axis)",
        default=2.4,
        min=1.0,
        max=6.0,
        step=10
    )
    y_depth: bpy.props.FloatProperty(
        name="Passing Depth (Y)",
        description="Orbital clearance depth to strictly avoid collisions",
        default=1.35,
        min=0.8,
        max=4.0,
        step=5
    )
    bounce_height: bpy.props.FloatProperty(
        name="Vertical Bounce",
        description="Subtle Z-axis lift while sliding",
        default=0.25,
        min=0.0,
        max=1.5,
        step=5
    )
    reveal_height: bpy.props.FloatProperty(
        name="Reveal Lift",
        description="Height the winning helmet rises to reveal the football",
        default=1.8,
        min=0.5,
        max=5.0,
        step=10
    )
    reveal_tilt: bpy.props.FloatProperty(
        name="Reveal Tilt (deg)",
        description="Tilt angle of winning helmet during reveal",
        default=25.0,
        min=0.0,
        max=60.0
    )
    randomize_target: bpy.props.BoolProperty(
        name="Randomize Target",
        description="Automatically pick random winning helmet",
        default=True
    )
    reveal_target: bpy.props.IntProperty(
        name="Target Helmet",
        description="Which helmet hides football (1, 2, or 3)",
        default=2,
        min=1,
        max=3
    )
    movement_style: bpy.props.EnumProperty(
        name="Movement Style",
        description="Easing and motion waveform",
        items=[
            ('SMOOTH', "Smooth Broadcast", "Polished cubic ease for crisp broadcast view"),
            ('WHIP', "Stadium Whip", "Fast mid-pass snap for difficult tracking"),
            ('BOUNCY', "Arcade Bounce", "High vertical arc sinusoidal wave"),
        ],
        default='SMOOTH'
    )
    min_safe_distance: bpy.props.FloatProperty(
        name="Min Safe Distance",
        description="Collision threshold for safety check",
        default=1.1,
        min=0.5,
        max=3.0
    )


class WOLFPACK_OT_generate_shuffle(bpy.types.Operator):
    """Generate collision-free helmet shuffle animation"""
    bl_idname = "wolfpack.generate_shuffle"
    bl_label = "Generate Wolfpack Shuffle"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.wolfpack_shuffle
        try:
            winner, frames = bake_shuffle_to_scene(props)
            self.report({'INFO'}, f"Wolfpack Shuffle Generated! Ball under Helmet {winner} ({frames} frames)")
            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, f"Generation failed: {str(e)}")
            return {'CANCELLED'}


class WOLFPACK_OT_setup_demo(bpy.types.Operator):
    """Spawn 3 demo helmets, football, and camera"""
    bl_idname = "wolfpack.setup_demo"
    bl_label = "Setup Stand-in Helmets & Ball"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.wolfpack_shuffle
        setup_demo_scene_if_needed(props.slot_spacing)
        # Link to properties
        props.custom_helmet_1 = bpy.data.objects.get("Helmet_1")
        props.custom_helmet_2 = bpy.data.objects.get("Helmet_2")
        props.custom_helmet_3 = bpy.data.objects.get("Helmet_3")
        props.custom_football = bpy.data.objects.get("Football_CTRL")
        self.report({'INFO'}, "Stand-in scene created and linked successfully.")
        return {'FINISHED'}


class WOLFPACK_OT_link_selected(bpy.types.Operator):
    """Link currently selected 3 objects as Helmets 1, 2, 3 ordered from left to right"""
    bl_idname = "wolfpack.link_selected"
    bl_label = "Auto-Link Selected (Left to Right)"
    bl_description = "Select your 3 models and click this to automatically assign them by their X position"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.wolfpack_shuffle
        selected = list(context.selected_objects)
        if len(selected) < 3:
            self.report({'WARNING'}, "Please select at least 3 objects in the 3D viewport!")
            return {'CANCELLED'}
            
        # Sort left to right by X coordinate
        sorted_objs = sorted(selected[:3], key=lambda obj: obj.location.x)
        props.custom_helmet_1 = sorted_objs[0]
        props.custom_helmet_2 = sorted_objs[1]
        props.custom_helmet_3 = sorted_objs[2]
        
        self.report({'INFO'}, f"Linked: 1={sorted_objs[0].name}, 2={sorted_objs[1].name}, 3={sorted_objs[2].name}")
        return {'FINISHED'}


class WOLFPACK_OT_import_model(bpy.types.Operator):
    """Import a custom 3D model file (.obj, .fbx, .glb, .gltf)"""
    bl_idname = "wolfpack.import_model"
    bl_label = "Import 3D Model File"
    bl_description = "Open file dialog to import an OBJ, FBX, or GLTF model"
    
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    filter_glob: bpy.props.StringProperty(
        default="*.obj;*.fbx;*.gltf;*.glb",
        options={'HIDDEN'}
    )

    def execute(self, context):
        fp = self.filepath.lower()
        if fp.endswith(".obj"):
            if hasattr(bpy.ops.wm, "obj_import"):
                bpy.ops.wm.obj_import(filepath=self.filepath)
            else:
                bpy.ops.import_scene.obj(filepath=self.filepath)
        elif fp.endswith(".fbx"):
            bpy.ops.import_scene.fbx(filepath=self.filepath)
        elif fp.endswith(".glb") or fp.endswith(".gltf"):
            bpy.ops.import_scene.gltf(filepath=self.filepath)
        else:
            self.report({'ERROR'}, "Unsupported file format. Please use .obj, .fbx, or .gltf/.glb")
            return {'CANCELLED'}
            
        self.report({'INFO'}, f"Imported model: {bpy.context.active_object.name if bpy.context.active_object else 'Model'}")
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


class WOLFPACK_PT_sidebar_panel(bpy.types.Panel):
    """UI Panel in 3D Viewport Sidebar"""
    bl_label = "Wolfpack Glory Shuffle"
    bl_idname = "WOLFPACK_PT_sidebar_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Wolfpack Shuffle'

    def draw(self, context):
        layout = self.layout
        props = context.scene.wolfpack_shuffle

        # Custom Model Selection Box
        box = layout.box()
        box.label(text="Assign Your 3D Models", icon='OBJECT_DATA')
        box.prop(props, "custom_helmet_1", text="Shuffler 1 (Left)")
        box.prop(props, "custom_helmet_2", text="Shuffler 2 (Center)")
        box.prop(props, "custom_helmet_3", text="Shuffler 3 (Right)")
        box.prop(props, "custom_football", text="Hidden Prize (Under)")
        
        row = box.row(align=True)
        row.operator("wolfpack.link_selected", text="Auto-Assign 3 Selected", icon='RESTRICT_SELECT_OFF')
        row.operator("wolfpack.import_model", text="Import Model File", icon='IMPORT')

        box_demo = layout.box()
        box_demo.label(text="Or Use Quick Stand-ins", icon='DUPLICATE')
        box_demo.operator("wolfpack.setup_demo", text="Spawn Stand-in Models", icon='SCENE_DATA')

        box_time = layout.box()
        box_time.label(text="Shuffle Timing", icon='TIME')
        box_time.prop(props, "num_swaps")
        box_time.prop(props, "swap_duration")
        box_time.prop(props, "pause_frames")
        box_time.prop(props, "fps")

        box_phys = layout.box()
        box_phys.label(text="Collision & Spacing Mechanics", icon='PHYSICS')
        box_phys.prop(props, "slot_spacing")
        box_phys.prop(props, "y_depth")
        box_phys.prop(props, "bounce_height")
        box_phys.prop(props, "movement_style")

        box_rev = layout.box()
        box_rev.label(text="Reveal Settings", icon='HIDE_OFF')
        box_rev.prop(props, "randomize_target")
        if not props.randomize_target:
            box_rev.prop(props, "reveal_target")
        box_rev.prop(props, "reveal_height")
        box_rev.prop(props, "reveal_tilt")

        layout.separator()
        btn = layout.operator("wolfpack.generate_shuffle", text="Generate Animation", icon='PLAY')


classes = (
    WolfpackShuffleProperties,
    WOLFPACK_OT_generate_shuffle,
    WOLFPACK_OT_setup_demo,
    WOLFPACK_OT_link_selected,
    WOLFPACK_OT_import_model,
    WOLFPACK_PT_sidebar_panel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.wolfpack_shuffle = bpy.props.PointerProperty(type=WolfpackShuffleProperties)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.wolfpack_shuffle

# Standalone execution support: when run directly in Blender's Scripting Editor
if __name__ == "__main__":
    try:
        unregister()
    except Exception:
        pass
    register()
    print("[Wolfpack Glory] Plugin loaded and registered in View3D Sidebar > 'Wolfpack Shuffle'!")
