bl_info = {
    "name": "Wolfpack Glory Helmet Shuffle",
    "author": "Solomon Olufelo / Wolfpack Glory",
    "version": (3, 1, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Wolfpack Shuffle",
    "description": "Modular broadcast motion graphics suite for stadium videoboards (5-beat cognitive pacing, Home Show entry bumper, After Effects cue sheets, 3 outcome variants, Field Goal suite, cinematic sky & compositor lens rig)",
    "category": "Animation",
}

import bpy
import os
import math
import random
import json
import csv
from typing import List, Tuple, Dict, Optional

# Global cache of last generated shuffle plan (for cue sheet export & After Effects bridge)
_LAST_SHUFFLE_PLAN: Optional['ShufflePlan'] = None

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
    def __init__(self, move_type: str, slots: List[int], start_frame: int, end_frame: int, y_depth: float, bounce_height: float, style: str = 'SMOOTH', bank_angle: float = 14.0):
        self.move_type = move_type      # 'PAIR_SWAP' or 'CAROUSEL'
        self.slots = slots              # Slot indices participating
        self.start_frame = start_frame
        self.end_frame = end_frame
        self.y_depth = y_depth
        self.bounce_height = bounce_height
        self.style = style
        self.bank_angle = bank_angle


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
        fps: int = 30,
        bank_angle: float = 14.0
    ):
        self.num_items = num_items
        self.slot_spacing = slot_spacing
        self.y_depth_base = y_depth_base
        self.bounce_height = bounce_height
        self.fps = fps
        self.bank_angle = bank_angle
        
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
        desired_outcome_slot: Optional[int] = None,
        style: str = 'SMOOTH',
        start_frame: int = 30,
        suspense_duration: int = 30
    ):
        self.moves.clear()
        self.slot_occupant = list(range(self.num_items))
        self.item_slot = list(range(self.num_items))
        
        if target_item is not None and 0 <= target_item < self.num_items:
            self.ball_holder_item_id = target_item
        else:
            self.ball_holder_item_id = random.randint(0, self.num_items - 1)
        
        current_frame = start_frame
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
                style=style,
                bank_angle=self.bank_angle
            )
            self.moves.append(move)
            current_frame = move.end_frame + pause_frames
            
            occ1, occ2 = self.slot_occupant[s1], self.slot_occupant[s2]
            self.slot_occupant[s1], self.slot_occupant[s2] = occ2, occ1
            self.item_slot[occ1] = s2
            self.item_slot[occ2] = s1
        
        # Enforce deterministic outcome variant (Variant A: Slot 1 / Left, Variant B: Slot 2 / Center, Variant C: Slot 3 / Right)
        if desired_outcome_slot is not None and 0 <= desired_outcome_slot < self.num_items:
            curr_slot = self.item_slot[self.ball_holder_item_id]
            if curr_slot != desired_outcome_slot:
                s1, s2 = curr_slot, desired_outcome_slot
                dist_factor = abs(s1 - s2)
                y_depth = self.y_depth_base * (1.0 + (dist_factor - 1) * 0.35)
                move = MoveStep(
                    move_type='PAIR_SWAP',
                    slots=[s1, s2],
                    start_frame=current_frame,
                    end_frame=current_frame + swap_duration_frames,
                    y_depth=y_depth,
                    bounce_height=self.bounce_height,
                    style=style,
                    bank_angle=self.bank_angle
                )
                self.moves.append(move)
                current_frame = move.end_frame + pause_frames
                
                occ1, occ2 = self.slot_occupant[s1], self.slot_occupant[s2]
                self.slot_occupant[s1], self.slot_occupant[s2] = occ2, occ1
                self.item_slot[occ1] = s2
                self.item_slot[occ2] = s1
        
        self.reveal_item_id = self.ball_holder_item_id
        self.shuffle_end_frame = current_frame - pause_frames
        self.total_frames = current_frame + suspense_duration + 50  # Suspense beat + reveal lift & tilt buffer

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
        
        # Orbit paths with guaranteed passing depth and centripetal banking around motion vector
        bank_rad = math.radians(current_move.bank_angle)
        pos_it1 = Vector3(
            x=x_mid - sign * x_radius * math.cos(theta),
            y=+current_move.y_depth * math.sin(theta),
            z=p1.z + vertical_offset
        )
        bank_it1 = -bank_rad * math.sin(theta) * sign
        
        pos_it2 = Vector3(
            x=x_mid + sign * x_radius * math.cos(theta),
            y=-current_move.y_depth * math.sin(theta),
            z=p2.z + vertical_offset
        )
        bank_it2 = +bank_rad * math.sin(theta) * sign
        
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

def setup_demo_scene_if_needed(slot_spacing: float = 2.4, venue_preset: str = 'FOOTBALL_TURF'):
    """
    Creates standard Empty controllers, stand-in helmets, ball/prize, and venue environment
    supporting Football Turf, Basketball Hardwood, and Clean Studio presets.
    """
    scene = bpy.context.scene
    required_empties = ["Helmet_1", "Helmet_2", "Helmet_3", "Football_CTRL"]
    existing = [name for name in required_empties if bpy.data.objects.get(name)]
    
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
            bsdf = mat_helmet.node_tree.nodes.get("Principled BSDF") if mat_helmet.node_tree else None
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
            bsdf_m = mat_mask.node_tree.nodes.get("Principled BSDF") if mat_mask.node_tree else None
            if bsdf_m:
                bsdf_m.inputs['Base Color'].default_value = stripe_colors[i]
                bsdf_m.inputs['Metallic'].default_value = 0.6
                bsdf_m.inputs['Roughness'].default_value = 0.3
            facemask.data.materials.append(mat_mask)

    # Create Ball / Prize Target Object
    if not bpy.data.objects.get("Football_CTRL"):
        fb_empty = bpy.data.objects.new("Football_CTRL", None)
        fb_empty.empty_display_type = 'SPHERE'
        fb_empty.empty_display_size = 0.35
        coll.objects.link(fb_empty)
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.28, location=(0, 0, 0.22))
        fb_mesh = bpy.context.active_object
        fb_mesh.name = "Laurier_Football_Mesh"
        fb_mesh.parent = fb_empty
        link_obj(fb_mesh)
        
        if venue_preset == 'BASKETBALL_COURT':
            fb_mesh.scale = (1.0, 1.0, 1.0)
            mat_ball = bpy.data.materials.new(name="Mat_Laurier_Basketball")
            bsdf_b = mat_ball.node_tree.nodes.get("Principled BSDF") if mat_ball.node_tree else None
            if bsdf_b:
                bsdf_b.inputs['Base Color'].default_value = (0.85, 0.32, 0.05, 1.0) # Spalding orange
                bsdf_b.inputs['Roughness'].default_value = 0.45
            fb_mesh.data.materials.append(mat_ball)
        else:
            fb_mesh.scale = (1.25, 0.72, 0.72)  # Authentic pigskin ratio
            mat_ball = bpy.data.materials.new(name="Mat_Laurier_Football")
            bsdf_b = mat_ball.node_tree.nodes.get("Principled BSDF") if mat_ball.node_tree else None
            if bsdf_b:
                bsdf_b.inputs['Base Color'].default_value = (0.28, 0.12, 0.04, 1.0) # Wilson leather brown
                bsdf_b.inputs['Roughness'].default_value = 0.65
            fb_mesh.data.materials.append(mat_ball)

    # Ensure Broadcast Camera & Optics
    cam_obj = bpy.data.objects.get("Shuffle_Camera")
    if not cam_obj:
        cam_data = bpy.data.cameras.new("Shuffle_Camera")
        cam_obj = bpy.data.objects.new("Shuffle_Camera", cam_data)
        cam_obj.location = (0.0, -8.0, 4.0)
        cam_obj.rotation_euler = (math.radians(65.0), 0.0, 0.0)
        cam_data.lens = 50.0
        coll.objects.link(cam_obj)
        
    scene.camera = cam_obj
    if cam_obj.data:
        cam_obj.data.dof.use_dof = True
        cam_obj.data.dof.focus_object = bpy.data.objects.get("Helmet_2")
        cam_obj.data.dof.aperture_fstop = 2.8

    # Multi-Venue Ground Stage
    stage_obj = bpy.data.objects.get("Stadium_Turf_Pitch")
    if not stage_obj:
        bpy.ops.mesh.primitive_plane_add(size=24.0, location=(0.0, 0.0, -0.01))
        stage_obj = bpy.context.active_object
        stage_obj.name = "Stadium_Turf_Pitch"
        link_obj(stage_obj)
        
        mat_stage = bpy.data.materials.new(name=f"Mat_Venue_{venue_preset}")
        bsdf_s = mat_stage.node_tree.nodes.get("Principled BSDF") if mat_stage.node_tree else None
        if bsdf_s:
            if venue_preset == 'BASKETBALL_COURT':
                bsdf_s.inputs['Base Color'].default_value = (0.48, 0.28, 0.12, 1.0) # Golden maple court
                bsdf_s.inputs['Roughness'].default_value = 0.12 # High gloss arena varnish
                bsdf_s.inputs['Metallic'].default_value = 0.0
                if 'Specular IOR Level' in bsdf_s.inputs:
                    bsdf_s.inputs['Specular IOR Level'].default_value = 0.85
            elif venue_preset == 'CLEAN_STUDIO':
                bsdf_s.inputs['Base Color'].default_value = (0.02, 0.02, 0.03, 1.0) # Carbon slate cyc
                bsdf_s.inputs['Roughness'].default_value = 0.25
                bsdf_s.inputs['Metallic'].default_value = 0.2
            else:
                bsdf_s.inputs['Base Color'].default_value = (0.04, 0.18, 0.06, 1.0) # Knight-Newbrough Field turf
                bsdf_s.inputs['Roughness'].default_value = 0.45
                if 'Specular IOR Level' in bsdf_s.inputs:
                    bsdf_s.inputs['Specular IOR Level'].default_value = 0.35
        stage_obj.data.materials.append(mat_stage)

    # 4-Point Stadium Floodlight Rig
    light_rig = [
        ("Floodlight_Key_L", (-5.5, -4.5, 6.0), (1.0, 0.95, 0.85, 1.0), 1200.0),
        ("Floodlight_Key_R", (5.5, -4.5, 6.0), (1.0, 0.95, 0.85, 1.0), 1200.0),
        ("Floodlight_Rim_Back", (0.0, 5.0, 4.5), (0.45, 0.15, 0.95, 1.0), 800.0), # Laurier Purple Rim
        ("Floodlight_Fill_Front", (0.0, -6.5, 3.5), (0.99, 0.72, 0.10, 1.0), 450.0), # Laurier Gold Fill
    ]
    for l_name, l_pos, l_color, l_power in light_rig:
        if not bpy.data.objects.get(l_name):
            l_data = bpy.data.lights.new(name=l_name, type='SPOT')
            l_data.energy = l_power
            l_data.color = l_color[:3]
            l_data.spot_size = math.radians(65.0)
            l_data.spot_blend = 0.35
            
            l_obj = bpy.data.objects.new(name=l_name, object_data=l_data)
            l_obj.location = l_pos
            # Angle light toward center
            dx, dy, dz = -l_pos[0], -l_pos[1], -l_pos[2]
            dist = math.sqrt(dx*dx + dy*dy + dz*dz)
            rot_y = math.atan2(dx, dz)
            rot_x = -math.asin(dy / dist) if dist > 0 else 0
            l_obj.rotation_euler = (rot_x, rot_y, 0.0)
            
            coll.objects.link(l_obj)


def setup_goalposts(coll = None) -> List[bpy.types.Object]:
    """
    Spawns authentic collegiate optic yellow 3D upright goalposts in the background:
    - Gooseneck support post at (0, 12.0, 1.6)
    - Crossbar of width 5.64m (18.5ft) at height 3.05m (10ft)
    - Vertical uprights rising 9.14m (30ft) at X = +/- 2.82m
    - Laurier purple wind streamers fluttering at upright tips
    """
    if coll is None:
        coll = bpy.data.collections.get("Wolfpack_Shuffle") or bpy.context.scene.collection
        
    created_objs = []
    
    # 1. Goalpost Golden Yellow Material
    mat_goal = bpy.data.materials.get("Mat_Goalpost_Optic_Yellow")
    if not mat_goal:
        mat_goal = bpy.data.materials.new(name="Mat_Goalpost_Optic_Yellow")
        bsdf = mat_goal.node_tree.nodes.get("Principled BSDF") if mat_goal.node_tree else None
        if bsdf:
            bsdf.inputs['Base Color'].default_value = (1.0, 0.85, 0.02, 1.0) # Stadium Optic Yellow
            bsdf.inputs['Metallic'].default_value = 0.35
            bsdf.inputs['Roughness'].default_value = 0.18
            if 'Specular IOR Level' in bsdf.inputs:
                bsdf.inputs['Specular IOR Level'].default_value = 0.75
                
    # Streamer Material
    mat_streamer = bpy.data.materials.get("Mat_Goalpost_Streamer")
    if not mat_streamer:
        mat_streamer = bpy.data.materials.new(name="Mat_Goalpost_Streamer")
        bsdf_st = mat_streamer.node_tree.nodes.get("Principled BSDF") if mat_streamer.node_tree else None
        if bsdf_st:
            bsdf_st.inputs['Base Color'].default_value = (0.35, 0.05, 0.65, 1.0) # Laurier Purple Ribbon
            bsdf_st.inputs['Roughness'].default_value = 0.6
            
    # Remove existing goalposts if present
    gp_names = [
        "Goalpost_Base", "Goalpost_Crossbar", "Goalpost_Upright_L", "Goalpost_Upright_R",
        "Goalpost_Streamer_L", "Goalpost_Streamer_R"
    ]
    for n in gp_names:
        old = bpy.data.objects.get(n)
        if old:
            bpy.data.objects.remove(old, do_unlink=True)
            
    # Base curved/angled gooseneck post
    bpy.ops.mesh.primitive_cylinder_add(radius=0.10, depth=3.2, location=(0, 12.0, 1.6))
    base_post = bpy.context.active_object
    base_post.name = "Goalpost_Base"
    base_post.data.materials.append(mat_goal)
    created_objs.append(base_post)
    
    # Horizontal Crossbar
    bpy.ops.mesh.primitive_cylinder_add(
        radius=0.065, 
        depth=5.64, 
        location=(0, 11.5, 3.05), 
        rotation=(0, math.radians(90.0), 0)
    )
    crossbar = bpy.context.active_object
    crossbar.name = "Goalpost_Crossbar"
    crossbar.data.materials.append(mat_goal)
    crossbar.parent = base_post
    created_objs.append(crossbar)
    
    # Left Upright
    bpy.ops.mesh.primitive_cylinder_add(radius=0.055, depth=9.14, location=(-2.82, 11.5, 7.62))
    up_l = bpy.context.active_object
    up_l.name = "Goalpost_Upright_L"
    up_l.data.materials.append(mat_goal)
    up_l.parent = crossbar
    created_objs.append(up_l)
    
    # Right Upright
    bpy.ops.mesh.primitive_cylinder_add(radius=0.055, depth=9.14, location=(2.82, 11.5, 7.62))
    up_r = bpy.context.active_object
    up_r.name = "Goalpost_Upright_R"
    up_r.data.materials.append(mat_goal)
    up_r.parent = crossbar
    created_objs.append(up_r)
    
    # Wind Streamers (fluttering ribbons at upright tips)
    for s_name, parent_up, x_pos in [("Goalpost_Streamer_L", up_l, -2.82), ("Goalpost_Streamer_R", up_r, 2.82)]:
        bpy.ops.mesh.primitive_plane_add(size=0.65, location=(x_pos, 11.52, 12.3))
        streamer = bpy.context.active_object
        streamer.name = s_name
        streamer.scale = (0.15, 1.0, 1.2)
        streamer.rotation_euler = (0, math.radians(15.0), math.radians(20.0))
        streamer.data.materials.append(mat_streamer)
        streamer.parent = parent_up
        created_objs.append(streamer)
        
    return created_objs


def setup_cinematic_atmosphere(coll = None):
    """
    Builds a high-concept cinematic environment and optical compositing pipeline:
    1. Atmospheric Sky Dome with layered storm clouds and sunset amber sunburst.
    2. High-angle rim/kicker backlights to pop the 3D helmets off the clouds.
    3. Procedural yardlines on Knight-Newbrough Field turf.
    4. Modern Blender 5.2.1 LTS Compositor Node Graph (Fog Glow bloom, anamorphic lens dispersion).
    """
    scene = bpy.context.scene
    if coll is None:
        coll = bpy.data.collections.get("Wolfpack_Shuffle") or scene.collection
        
    # 1. Procedural Sky Dome
    sky_obj = bpy.data.objects.get("Sky_Dome_Atmosphere")
    if not sky_obj:
        bpy.ops.mesh.primitive_uv_sphere_add(radius=45.0, location=(0, 0, 0))
        sky_obj = bpy.context.active_object
        sky_obj.name = "Sky_Dome_Atmosphere"
        if sky_obj.name not in coll.objects:
            coll.objects.link(sky_obj)
        
    # Invert face normals so inside is visible to camera
    sky_obj.scale = (-1.0, 1.0, 1.0)
        
    mat_sky = bpy.data.materials.get("Mat_Atmosphere_Sky")
    if not mat_sky:
        mat_sky = bpy.data.materials.new(name="Mat_Atmosphere_Sky")
        nodes = mat_sky.node_tree.nodes
        links = mat_sky.node_tree.links
        nodes.clear()
        
        out = nodes.new('ShaderNodeOutputMaterial')
        emit = nodes.new('ShaderNodeEmission')
        ramp = nodes.new('ShaderNodeValToRGB')
        tex_noise = nodes.new('ShaderNodeTexNoise')
        tex_coord = nodes.new('ShaderNodeTexCoord')
        mapping = nodes.new('ShaderNodeMapping')
        
        ramp.color_ramp.elements[0].position = 0.25
        ramp.color_ramp.elements[0].color = (0.06, 0.01, 0.12, 1.0) # Deep Purple Horizon
        ramp.color_ramp.elements[1].position = 0.65
        ramp.color_ramp.elements[1].color = (0.95, 0.55, 0.10, 1.0) # Golden Sunburst Cloud Edge
        el_top = ramp.color_ramp.elements.new(0.90)
        el_top.color = (0.08, 0.04, 0.18, 1.0) # Night Sky
        
        tex_noise.inputs['Scale'].default_value = 2.8
        tex_noise.inputs['Detail'].default_value = 4.5
        tex_noise.inputs['Roughness'].default_value = 0.65
        
        links.new(tex_coord.outputs['Generated'], mapping.inputs['Vector'])
        links.new(mapping.outputs['Vector'], tex_noise.inputs['Vector'])
        links.new(tex_noise.outputs['Fac'], ramp.inputs['Fac'])
        links.new(ramp.outputs['Color'], emit.inputs['Color'])
        emit.inputs['Strength'].default_value = 1.2
        links.new(emit.outputs['Emission'], out.inputs['Surface'])
        
    if mat_sky.name not in sky_obj.data.materials:
        sky_obj.data.materials.append(mat_sky)
        
    # 2. Dramatic Rim Kickers (Backlights behind helmets)
    rim_lights = [
        ("Atmosphere_Rim_L", (-6.0, 7.5, 5.0), (1.0, 0.85, 0.4, 1.0), 2200.0), # Amber Sun Flare
        ("Atmosphere_Rim_R", (6.0, 7.5, 5.0), (0.55, 0.15, 0.95, 1.0), 2200.0), # Deep Purple Rim
    ]
    for r_name, r_pos, r_color, r_energy in rim_lights:
        l_obj = bpy.data.objects.get(r_name)
        if not l_obj:
            l_data = bpy.data.lights.new(name=r_name, type='SPOT')
            l_data.energy = r_energy
            l_data.color = r_color[:3]
            l_data.spot_size = math.radians(60.0)
            l_data.spot_blend = 0.45
            l_obj = bpy.data.objects.new(name=r_name, object_data=l_data)
            l_obj.location = r_pos
            l_obj.rotation_euler = (math.radians(45.0), 0.0, math.radians(180.0))
            coll.objects.link(l_obj)
            
    # 3. Ground Stage Yardlines
    stage_obj = bpy.data.objects.get("Stadium_Turf_Pitch")
    if stage_obj:
        mat_turf = bpy.data.materials.get("Mat_Venue_FOOTBALL_TURF")
        if not mat_turf:
            mat_turf = bpy.data.materials.new(name="Mat_Venue_FOOTBALL_TURF")
        if mat_turf.node_tree:
            nodes = mat_turf.node_tree.nodes
            links = mat_turf.node_tree.links
            nodes.clear()
            
            out_s = nodes.new('ShaderNodeOutputMaterial')
            bsdf_s = nodes.new('ShaderNodeBsdfPrincipled')
            tc = nodes.new('ShaderNodeTexCoord')
            sep = nodes.new('ShaderNodeSeparateXYZ')
            m_scale = nodes.new('ShaderNodeMath')
            m_fract = nodes.new('ShaderNodeMath')
            r_lines = nodes.new('ShaderNodeValToRGB')
            mix_c = nodes.new('ShaderNodeMix')
            
            m_scale.operation = 'MULTIPLY'
            m_scale.inputs[1].default_value = 0.35
            m_fract.operation = 'FRACT'
            
            r_lines.color_ramp.elements[0].position = 0.92
            r_lines.color_ramp.elements[0].color = (0.0, 0.0, 0.0, 1.0)
            r_lines.color_ramp.elements[1].position = 0.96
            r_lines.color_ramp.elements[1].color = (1.0, 1.0, 1.0, 1.0)
            
            mix_c.data_type = 'RGBA'
            mix_c.inputs[6].default_value = (0.035, 0.165, 0.055, 1.0) # Knight-Newbrough Turf
            mix_c.inputs[7].default_value = (0.92, 0.92, 0.90, 1.0) # Chalk line
            
            links.new(tc.outputs['Generated'], sep.inputs['Vector'])
            links.new(sep.outputs['Y'], m_scale.inputs[0])
            links.new(m_scale.outputs['Value'], m_fract.inputs[0])
            links.new(m_fract.outputs['Value'], r_lines.inputs['Fac'])
            links.new(r_lines.outputs['Color'], mix_c.inputs['Factor'])
            links.new(mix_c.outputs[2], bsdf_s.inputs['Base Color'])
            bsdf_s.inputs['Roughness'].default_value = 0.42
            links.new(bsdf_s.outputs['BSDF'], out_s.inputs['Surface'])
            
    # 4. Modern Blender 5.2.1 LTS Compositor Graph
    try:
        tree = bpy.data.node_groups.get("Laurier_Cinematic_Compositor")
        if not tree:
            tree = bpy.data.node_groups.new(name="Laurier_Cinematic_Compositor", type='CompositorNodeTree')
        scene.compositing_node_group = tree
        tree.nodes.clear()
        
        if not tree.interface.items_tree:
            tree.interface.new_socket(name='Image', in_out='OUTPUT', socket_type='NodeSocketColor')
            
        rl = tree.nodes.new('CompositorNodeRLayers')
        rl.location = (-400, 0)
        
        glare = tree.nodes.new('CompositorNodeGlare')
        glare.location = (-150, 0)
        if 'Threshold' in glare.inputs:
            glare.inputs['Threshold'].default_value = 0.68
        if 'Size' in glare.inputs:
            glare.inputs['Size'].default_value = 7
            
        lens = tree.nodes.new('CompositorNodeLensdist')
        lens.location = (100, 0)
        if 'Distortion' in lens.inputs:
            lens.inputs['Distortion'].default_value = 0.012
        if 'Dispersion' in lens.inputs:
            lens.inputs['Dispersion'].default_value = 0.006
            
        out_c = tree.nodes.new('NodeGroupOutput')
        out_c.location = (350, 0)
        
        tree.links.new(rl.outputs['Image'], glare.inputs['Image'])
        tree.links.new(glare.outputs['Image'], lens.inputs['Image'])
        tree.links.new(lens.outputs['Image'], out_c.inputs['Image'])
    except Exception as e:
        print("[Wolfpack Glory] Compositor setup note:", e)


# ============================================================================
# LAURIER BRAND ASSETS: TYPOGRAPHY & LED CONTRAST MATERIALS
# ============================================================================

def load_laurier_font(font_type: str = 'RADWAVE') -> Optional[bpy.types.VectorFont]:
    """
    Loads Hailey's specified typography for Laurier Athletics:
    - RADWAVE: Display / Hype headers & explosive stingers ("Radwave Demo 400.otf")
    - AGENCYFB: Condensed sports broadcast font for downs/numerals ("AGENCYB.TTF", "agencyfb_bold.ttf")
    """
    if font_type == 'DEFAULT':
        return None
        
    font_file_map = {
        'RADWAVE': ['Radwave Demo 400.otf', 'RadwaveFont-Demo.otf', 'radwave_demo_400.otf'],
        'AGENCYFB': ['AGENCYB.TTF', 'agencyfb_bold.ttf', 'Agency FB Black Wide.ttf', 'AGENCYR.TTF']
    }
    
    # Check already loaded fonts in Blender
    for font_obj in bpy.data.fonts:
        name_lower = font_obj.name.lower()
        if font_type == 'RADWAVE' and 'radwave' in name_lower:
            return font_obj
        elif font_type == 'AGENCYFB' and 'agency' in name_lower:
            return font_obj
            
    search_paths = [
        "C:/Windows/Fonts",
        "C:/Windows/Fonts/",
        os.path.expandvars("%WINDIR%/Fonts"),
    ]
    
    candidates = font_file_map.get(font_type, [])
    for folder in search_paths:
        for fname in candidates:
            fp = os.path.join(folder, fname)
            if os.path.exists(fp):
                try:
                    loaded = bpy.data.fonts.load(fp)
                    return loaded
                except Exception:
                    continue
    return None


def get_laurier_materials() -> Tuple[bpy.types.Material, bpy.types.Material]:
    """
    Creates or retrieves high-contrast stadium LED shaders:
    - Mat_Laurier_Gold_Core: Metallic Golden Hawks gold face (#FDB913) with gentle emission for diode clarity
    - Mat_Laurier_Purple_Bevel: Laurier darkness deep purple outline/bevel (#20003B) - zero white border glare
    """
    # 1. Gold Core Face
    mat_gold = bpy.data.materials.get("Mat_Laurier_Gold_Core")
    if not mat_gold:
        mat_gold = bpy.data.materials.new(name="Mat_Laurier_Gold_Core")
        bsdf = mat_gold.node_tree.nodes.get("Principled BSDF") if mat_gold.node_tree else None
        if bsdf:
            bsdf.inputs['Base Color'].default_value = (0.992, 0.725, 0.075, 1.0) # #FDB913
            bsdf.inputs['Metallic'].default_value = 0.88
            bsdf.inputs['Roughness'].default_value = 0.18
            if 'Emission Color' in bsdf.inputs:
                bsdf.inputs['Emission Color'].default_value = (0.992, 0.725, 0.075, 1.0)
                bsdf.inputs['Emission Strength'].default_value = 0.22
            elif 'Emission' in bsdf.inputs:
                bsdf.inputs['Emission'].default_value = (0.992, 0.725, 0.075, 1.0)

    # 2. Deep Purple Bevel / Stroke
    mat_purple = bpy.data.materials.get("Mat_Laurier_Purple_Bevel")
    if not mat_purple:
        mat_purple = bpy.data.materials.new(name="Mat_Laurier_Purple_Bevel")
        bsdf = mat_purple.node_tree.nodes.get("Principled BSDF") if mat_purple.node_tree else None
        if bsdf:
            bsdf.inputs['Base Color'].default_value = (0.125, 0.0, 0.231, 1.0) # #20003B Deep Purple
            bsdf.inputs['Roughness'].default_value = 0.35
            bsdf.inputs['Metallic'].default_value = 0.4
            if 'Specular IOR Level' in bsdf.inputs:
                bsdf.inputs['Specular IOR Level'].default_value = 0.5
            
    return mat_gold, mat_purple


def cleanup_conflicting_text_graphics(current_mode='SHUFFLE'):
    """
    Prevents different graphic modes (Bumper vs Shuffle vs Stinger) from overlapping,
    ghosting, or sitting in front of the camera simultaneously.
    """
    to_remove = []
    for obj in bpy.data.objects:
        if current_mode == 'SHUFFLE':
            if obj.name.startswith("Wolfpack_Bumper_") or obj.name.startswith("Stinger_"):
                to_remove.append(obj)
        elif current_mode == 'BUMPER':
            if obj.name.startswith("Wolfpack_Banner_") or obj.name.startswith("Wolfpack_Slot_Badge_") or obj.name.startswith("Stinger_"):
                to_remove.append(obj)
        elif current_mode == 'STINGER':
            if obj.name.startswith("Wolfpack_Banner_") or obj.name.startswith("Wolfpack_Slot_Badge_") or obj.name.startswith("Wolfpack_Bumper_"):
                to_remove.append(obj)
                
    for obj in to_remove:
        try:
            bpy.data.objects.remove(obj, do_unlink=True)
        except Exception:
            pass


def setup_phase_text_banner(coll, name, text, font_type='RADWAVE', z_offset=0.0):
    """
    Creates a stylized 3D stadium text banner with dual-layer collegiate lockup:
    - Front face: Laurier Gold Core
    - Backing bevel: Laurier Deep Purple Stroke (offset cleanly to prevent z-fighting)
    - Applied typography: Hailey's Radwave / Agency FB
    - Elevated Z-height (1.35m) so it floats in the upper-third stadium sky
      and never blocks the helmets when zooming in!
    """
    mat_gold, mat_purple = get_laurier_materials()
    vfont = load_laurier_font(font_type)
    
    txt_obj = bpy.data.objects.get(name)
    stroke_obj = bpy.data.objects.get(f"{name}_Stroke")
    
    target_loc = (0.0, -3.2, 1.35 + z_offset)
    target_rot = (math.radians(65.0), 0.0, 0.0)
    
    if not txt_obj:
        txt_data = bpy.data.curves.new(type='FONT', name=f"{name}_Data")
        txt_obj = bpy.data.objects.new(name, txt_data)
        txt_data.body = text
        if vfont:
            txt_data.font = vfont
        txt_data.align_x = 'CENTER'
        txt_data.align_y = 'CENTER'
        txt_data.size = 0.58
        txt_data.extrude = 0.045
        txt_data.bevel_depth = 0.008
        txt_data.bevel_resolution = 4
        
        txt_obj.location = target_loc
        txt_obj.rotation_euler = target_rot
        coll.objects.link(txt_obj)
        txt_obj.data.materials.append(mat_gold)
        
        # Backing Purple Bevel Stroke
        stroke_data = bpy.data.curves.new(type='FONT', name=f"{name}_Stroke_Data")
        stroke_obj = bpy.data.objects.new(f"{name}_Stroke", stroke_data)
        stroke_data.body = text
        if vfont:
            stroke_data.font = vfont
        stroke_data.align_x = 'CENTER'
        stroke_data.align_y = 'CENTER'
        stroke_data.size = 0.58
        stroke_data.extrude = 0.040
        stroke_data.bevel_depth = 0.024
        stroke_data.bevel_resolution = 4
        
        stroke_obj.parent = txt_obj
        # Offset cleanly Y=+0.022 behind gold face to strictly prevent z-fighting
        stroke_obj.location = (0.0, 0.022, -0.002)
        coll.objects.link(stroke_obj)
        stroke_obj.data.materials.append(mat_purple)
    else:
        txt_obj.location = target_loc
        txt_obj.rotation_euler = target_rot
        txt_obj.data.body = text
        if vfont:
            txt_obj.data.font = vfont
        txt_obj.data.size = 0.58
        txt_obj.data.extrude = 0.045
        txt_obj.data.bevel_depth = 0.008
        txt_obj.data.bevel_resolution = 4
        
        if not stroke_obj:
            stroke_data = bpy.data.curves.new(type='FONT', name=f"{name}_Stroke_Data")
            stroke_obj = bpy.data.objects.new(f"{name}_Stroke", stroke_data)
            stroke_data.body = text
            if vfont:
                stroke_data.font = vfont
            stroke_data.align_x = 'CENTER'
            stroke_data.align_y = 'CENTER'
            stroke_data.size = 0.58
            stroke_data.extrude = 0.040
            stroke_data.bevel_depth = 0.024
            stroke_data.bevel_resolution = 4
            stroke_obj.parent = txt_obj
            stroke_obj.location = (0.0, 0.022, -0.002)
            coll.objects.link(stroke_obj)
            stroke_obj.data.materials.append(mat_purple)
        else:
            stroke_obj.location = (0.0, 0.022, -0.002)
            stroke_obj.data.body = text
            if vfont:
                stroke_obj.data.font = vfont
            stroke_obj.data.size = 0.58
            stroke_obj.data.extrude = 0.040
            stroke_obj.data.bevel_depth = 0.024
            stroke_obj.data.bevel_resolution = 4
                
    return txt_obj
                
# ============================================================================
# BROADCAST COMPOSITING & SOUND DESIGN CUE SHEET EXPORTER
# ============================================================================

def frame_to_timecode_str(frame: int, fps: int = 30) -> str:
    """Calculates SMPTE timecode string HH:MM:SS:FF."""
    total_sec = frame / fps
    hh = int(total_sec // 3600)
    mm = int((total_sec % 3600) // 60)
    ss = int(total_sec % 60)
    ff = int(frame % fps)
    return f"{hh:02d}:{mm:02d}:{ss:02d}:{ff:02d}"


def export_broadcast_cue_sheet(plan, props, winning_item_id: int, total_frames: int, filepath_base: Optional[str] = None) -> Tuple[str, str]:
    """
    Exports a timestamped broadcast cue sheet (.json and .csv)
    recording every swap, pause, and reveal timecode for sound designers and After Effects artists.
    """
    if not filepath_base:
        if bpy.data.filepath:
            folder = os.path.dirname(bpy.data.filepath)
            filepath_base = os.path.join(folder, "wolfpack_shuffle_cues")
        else:
            folder = r"C:\Users\Administrator\.gemini\antigravity\scratch\wolfpack_shuffle"
            os.makedirs(folder, exist_ok=True)
            filepath_base = os.path.join(folder, "wolfpack_shuffle_cues")
            
    fps = props.fps
    winning_slot_idx = plan.item_slot[winning_item_id]
    winning_slot_label = f"Slot {winning_slot_idx + 1}"
    
    intro_offset = props.intro_lift_duration if props.show_intro_reveal else 20
    suspense_start = plan.shuffle_end_frame
    reveal_question_frame = suspense_start + 12
    reveal_lift_start = plan.total_frames - 35
    
    cues = [
        {
            "frame": 1,
            "timecode": frame_to_timecode_str(1, fps),
            "event": "SCENE_START_ENTRY_HOOK",
            "description": "Camera dollys in, 3 helmets resting in initial slots",
            "recommended_sfx": "crowd_murmur_ambient"
        },
    ]
    
    if props.show_intro_reveal:
        f_lift = max(2, int(intro_offset * 0.25))
        cues.append({
            "frame": f_lift,
            "timecode": frame_to_timecode_str(f_lift, fps),
            "event": "PRIZE_SHOWCASE_LIFT",
            "description": f"Winning helmet lifts displaying prize underneath at slot {winning_item_id + 1}",
            "recommended_sfx": "bell_ding_high_ping"
        })
        cues.append({
            "frame": intro_offset,
            "timecode": frame_to_timecode_str(intro_offset, fps),
            "event": "PRIZE_LOCK_IMPACT",
            "description": "Helmet drops firmly back over ball; text clears out for clean tracking",
            "recommended_sfx": "thud_heavy_impact"
        })
        
    cues.append({
        "frame": intro_offset + 10,
        "timecode": frame_to_timecode_str(intro_offset + 10, fps),
        "event": "CLEAN_SWAP_FRENZY_START",
        "description": "Active orbital shuffle begins; screen is 100% clean of text for visual tracking",
        "recommended_sfx": "crowd_cheer_fast_swish"
    })
    
    for i, m in enumerate(plan.moves):
        s1, s2 = m.slots
        cues.append({
            "frame": m.start_frame,
            "timecode": frame_to_timecode_str(m.start_frame, fps),
            "event": f"SWAP_{i + 1}_PASS",
            "description": f"Orbital swap between Slot {s1 + 1} and Slot {s2 + 1} (depth Y={m.y_depth:.2f}m, bank {m.bank_angle:.1f}deg)",
            "recommended_sfx": "air_whoosh_quick"
        })
        
    cues.append({
        "frame": suspense_start,
        "timecode": frame_to_timecode_str(suspense_start, fps),
        "event": "SUSPENSE_STANDSTILL_FREEZE",
        "description": "All helmets come to an abrupt standstill in final resting slots",
        "recommended_sfx": "dramatic_stop_reverb"
    })
    
    cues.append({
        "frame": reveal_question_frame,
        "timecode": frame_to_timecode_str(reveal_question_frame, fps),
        "event": "CALL_TO_ACTION_WHERE_IS_IT",
        "description": "WHERE IS IT? banner pops in with interactive [1], [2], [3] slot badges",
        "recommended_sfx": "tension_heartbeat_countdown"
    })
    
    cues.append({
        "frame": reveal_lift_start,
        "timecode": frame_to_timecode_str(reveal_lift_start, fps),
        "event": f"REVEAL_WINNER_{winning_slot_label.upper().replace(' ', '_')}",
        "description": f"Winning helmet lifts at {winning_slot_label} to unveil the prize; winner banner pops",
        "recommended_sfx": "celebratory_stadium_horn_pyro"
    })
    
    cues.append({
        "frame": total_frames,
        "timecode": frame_to_timecode_str(total_frames, fps),
        "event": "SCENE_END",
        "description": "End of animation playback",
        "recommended_sfx": "crowd_roar_fade"
    })
    
    # Write JSON
    json_path = filepath_base + ".json"
    data = {
        "suite": "Wolfpack Glory Helmet Shuffle v3.0",
        "author": "Solomon Olufelo / Wilfrid Laurier Athletics",
        "client": "Wilfrid Laurier Golden Hawks",
        "fps": fps,
        "total_frames": total_frames,
        "duration_seconds": round(total_frames / fps, 2),
        "outcome_variant": props.target_outcome,
        "winning_slot": winning_slot_label,
        "winning_item_id": winning_item_id + 1,
        "venue_preset": getattr(props, "venue_preset", "FOOTBALL_TURF"),
        "cues": cues
    }
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        
    # Write CSV
    csv_path = filepath_base + ".csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Frame", "Timecode", "Event", "SFX_Recommendation", "Description"])
        for c in cues:
            writer.writerow([c["frame"], c["timecode"], c["event"], c["recommended_sfx"], c["description"]])
            
    return json_path, csv_path


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
    
    # Ensure no lingering bumper or stinger text blocks view
    cleanup_conflicting_text_graphics('SHUFFLE')
    
    # Check if we have objects or need to spawn stand-ins
    objects, fb_ctrl = get_shuffle_objects(props)
    if not any(objects):
        setup_demo_scene_if_needed(props.slot_spacing, getattr(props, "venue_preset", "FOOTBALL_TURF"))
        objects, fb_ctrl = get_shuffle_objects(props)
        
    valid_objects = [obj for obj in objects if obj is not None]
    if len(valid_objects) < 2:
        raise ValueError("Please select or name at least 2 objects (Helmet 1, 2, 3) to shuffle!")
    
    plan = ShufflePlan(
        num_items=3,
        slot_spacing=props.slot_spacing,
        y_depth_base=props.y_depth,
        bounce_height=props.bounce_height,
        fps=props.fps,
        bank_angle=props.bank_angle
    )
    
    # Storyboard Intro: if enabled, reserve frames at beginning for showing where ball is hidden
    intro_offset = props.intro_lift_duration if props.show_intro_reveal else 20
    
    desired_slot = None
    if props.target_outcome == 'SLOT_1':
        desired_slot = 0
    elif props.target_outcome == 'SLOT_2':
        desired_slot = 1
    elif props.target_outcome == 'SLOT_3':
        desired_slot = 2

    target_idx = props.reveal_target - 1 if not props.randomize_target else None
    plan.generate_routine(
        num_swaps=props.num_swaps,
        swap_duration_frames=props.swap_duration,
        pause_frames=props.pause_frames,
        target_item=target_idx,
        desired_outcome_slot=desired_slot,
        style=props.movement_style,
        start_frame=intro_offset + 10,
        suspense_duration=props.suspense_duration
    )
    
    # Clear existing animation data on target objects
    for obj in valid_objects + ([fb_ctrl] if fb_ctrl else []):
        if obj and obj.animation_data:
            obj.animation_data_clear()

    winning_item_id = plan.reveal_item_id
    winner_obj = objects[winning_item_id]

    # 1. Animate Helmets / Upper Items across the shuffle routine
    for frame in range(intro_offset + 1, plan.total_frames + 1):
        evals = plan.evaluate_at_frame(frame)
        for item_id, obj in enumerate(objects):
            if not obj:
                continue
            pos, rot = evals[item_id]
            obj.location = pos.as_tuple()
            obj.rotation_euler = rot.as_tuple()
            obj.keyframe_insert(data_path="location", frame=frame)
            obj.keyframe_insert(data_path="rotation_euler", frame=frame)

    # 2. Animate Storyboard Intro Phase (Showcasing where the ball is hidden FIRST)
    if props.show_intro_reveal and winner_obj:
        init_evals = plan.evaluate_at_frame(intro_offset + 1)
        for item_id, obj in enumerate(objects):
            if not obj:
                continue
            base_p, _ = init_evals[item_id]
            if item_id == winning_item_id:
                # Frame 1 to 10: rest
                # Frame 10 to intro_offset - 10: lifted up displaying football
                # Frame intro_offset - 10 to intro_offset: drops back down over ball
                lift_h = props.reveal_height * 0.95
                tilt_rad = math.radians(props.reveal_tilt * 0.8)
                
                # Frame 1: on ground
                obj.location = base_p.as_tuple()
                obj.rotation_euler = (0.0, 0.0, 0.0)
                obj.keyframe_insert(data_path="location", frame=1)
                obj.keyframe_insert(data_path="rotation_euler", frame=1)
                
                # Frame 12: lifted
                f_lift = max(2, int(intro_offset * 0.25))
                obj.location = (base_p.x, base_p.y, base_p.z + lift_h)
                obj.rotation_euler = (tilt_rad, 0.0, 0.0)
                obj.keyframe_insert(data_path="location", frame=f_lift)
                obj.keyframe_insert(data_path="rotation_euler", frame=f_lift)
                
                # Frame hold:
                f_hold = int(intro_offset * 0.70)
                obj.location = (base_p.x, base_p.y, base_p.z + lift_h)
                obj.rotation_euler = (tilt_rad, 0.0, 0.0)
                obj.keyframe_insert(data_path="location", frame=f_hold)
                obj.keyframe_insert(data_path="rotation_euler", frame=f_hold)
                
                # Frame drop down:
                obj.location = base_p.as_tuple()
                obj.rotation_euler = (0.0, 0.0, 0.0)
                obj.keyframe_insert(data_path="location", frame=intro_offset)
                obj.keyframe_insert(data_path="rotation_euler", frame=intro_offset)
            else:
                # Other helmets stay resting on ground
                obj.location = base_p.as_tuple()
                obj.rotation_euler = (0.0, 0.0, 0.0)
                obj.keyframe_insert(data_path="location", frame=1)
                obj.keyframe_insert(data_path="rotation_euler", frame=1)
                obj.keyframe_insert(data_path="location", frame=intro_offset)
                obj.keyframe_insert(data_path="rotation_euler", frame=intro_offset)
    elif not props.show_intro_reveal:
        # Pre-roll rest keyframes
        init_evals = plan.evaluate_at_frame(intro_offset + 1)
        for item_id, obj in enumerate(objects):
            if obj:
                base_p, _ = init_evals[item_id]
                obj.location = base_p.as_tuple()
                obj.rotation_euler = (0.0, 0.0, 0.0)
                obj.keyframe_insert(data_path="location", frame=1)
                obj.keyframe_insert(data_path="rotation_euler", frame=1)

    # 3. Animate Football / Prize following the winner helmet
    if fb_ctrl:
        for frame in range(1, plan.total_frames + 1):
            evals = plan.evaluate_at_frame(frame)
            winner_pos, _ = evals[winning_item_id]
            fb_ctrl.location = (winner_pos.x, winner_pos.y, props.prize_z_offset)
            fb_ctrl.keyframe_insert(data_path="location", frame=frame)

    # 4. Animate Suspense Pause & Final Reveal (Lifting winning helmet & tilt)
    # Storyboard structure:
    #   Shuffle ends at: plan.shuffle_end_frame
    #   Suspense pause:  plan.shuffle_end_frame -> plan.shuffle_end_frame + props.suspense_duration
    #   Reveal banner:   pops in at plan.shuffle_end_frame + 12 (Asking "WHERE IS IT?")
    #   Helmet reveal:   begins lifting at plan.total_frames - 35
    suspense_start = plan.shuffle_end_frame
    reveal_question_frame = suspense_start + 12
    reveal_lift_start = plan.total_frames - 35
    reveal_lift_end = plan.total_frames
    
    if winner_obj:
        evals_reveal = plan.evaluate_at_frame(reveal_lift_start)
        base_pos, _ = evals_reveal[winning_item_id]
        
        # Ensure helmet stays grounded during suspense pause
        winner_obj.location = base_pos.as_tuple()
        winner_obj.rotation_euler = (0.0, 0.0, 0.0)
        winner_obj.keyframe_insert(data_path="location", frame=suspense_start)
        winner_obj.keyframe_insert(data_path="rotation_euler", frame=suspense_start)
        winner_obj.keyframe_insert(data_path="location", frame=reveal_lift_start)
        winner_obj.keyframe_insert(data_path="rotation_euler", frame=reveal_lift_start)
        
        # Dramatic smooth lift + forward tilt to unveil football
        for frame in range(reveal_lift_start, reveal_lift_end + 1):
            t = (frame - reveal_lift_start) / max(1, (reveal_lift_end - reveal_lift_start))
            ease_lift = ease_smoothstep(t)
            
            lift_z = base_pos.z + props.reveal_height * ease_lift
            tilt_x = math.radians(props.reveal_tilt) * ease_lift
            
            winner_obj.location = (base_pos.x, base_pos.y, lift_z)
            winner_obj.rotation_euler = (tilt_x, 0.0, 0.0)
            winner_obj.keyframe_insert(data_path="location", frame=frame)
            winner_obj.keyframe_insert(data_path="rotation_euler", frame=frame)

    # 5. Animated 3D Jumbotron Storyboard Text Banners (5-Beat Cognitive Hierarchy)
    if props.create_text_banner:
        coll = bpy.data.collections.get("Wolfpack_Shuffle") or bpy.context.scene.collection
        winning_slot_idx = plan.item_slot[winning_item_id]
        winning_slot_number = winning_slot_idx + 1
        
        banner_intro = setup_phase_text_banner(coll, "Wolfpack_Banner_Intro", props.banner_intro_text, font_type=props.banner_font)
        banner_rev = setup_phase_text_banner(coll, "Wolfpack_Banner_Reveal", props.banner_reveal_text, font_type=props.banner_font)
        banner_win = setup_phase_text_banner(coll, "Wolfpack_Banner_Winner", f"SLOT {winning_slot_number} WINS!", font_type=props.banner_font)
        
        # --- BEAT 2: INTRO BANNER ("WATCH CLOSELY!") ---
        # Starts at scale 0 on frame 1, drops in with kinetic overshoot at frame 8,
        # holds, then wipes out smoothly before the swapping frenzy begins!
        if banner_intro.animation_data:
            banner_intro.animation_data_clear()
            
        intro_end = max(12, intro_offset - 4)
        
        # Frame 1: Hidden in upper sky
        banner_intro.scale = (0.0, 0.0, 0.0)
        banner_intro.location = (0.0, -2.6, 2.2)
        banner_intro.rotation_euler = (math.radians(45.0), math.radians(-10.0), math.radians(20.0))
        banner_intro.keyframe_insert(data_path="scale", frame=1)
        banner_intro.keyframe_insert(data_path="location", frame=1)
        banner_intro.keyframe_insert(data_path="rotation_euler", frame=1)
        
        # Frame 8: Kinetic Drop Slam Overshoot (1.20x)
        banner_intro.scale = (1.20, 1.20, 1.20)
        banner_intro.location = (0.0, -3.2, 1.35)
        banner_intro.rotation_euler = (math.radians(68.0), math.radians(2.0), math.radians(-2.0))
        banner_intro.keyframe_insert(data_path="scale", frame=8)
        banner_intro.keyframe_insert(data_path="location", frame=8)
        banner_intro.keyframe_insert(data_path="rotation_euler", frame=8)
        
        # Frame 14: Settle to rest
        banner_intro.scale = (1.0, 1.0, 1.0)
        banner_intro.location = (0.0, -3.2, 1.35)
        banner_intro.rotation_euler = (math.radians(65.0), 0.0, 0.0)
        banner_intro.keyframe_insert(data_path="scale", frame=14)
        banner_intro.keyframe_insert(data_path="location", frame=14)
        banner_intro.keyframe_insert(data_path="rotation_euler", frame=14)
        
        # Hold
        if intro_end > 18:
            banner_intro.scale = (1.02, 1.02, 1.02)
            banner_intro.location = (0.0, -3.2, 1.38)
            banner_intro.keyframe_insert(data_path="scale", frame=intro_end - 4)
            banner_intro.keyframe_insert(data_path="location", frame=intro_end - 4)
            
        # Frame intro_end: High-speed snap wipe exit
        banner_intro.scale = (0.0, 0.0, 0.0)
        banner_intro.location = (6.0, -3.2, 1.6)
        banner_intro.rotation_euler = (math.radians(65.0), 0.0, math.radians(-30.0))
        banner_intro.keyframe_insert(data_path="scale", frame=intro_end)
        banner_intro.keyframe_insert(data_path="location", frame=intro_end)
        banner_intro.keyframe_insert(data_path="rotation_euler", frame=intro_end)
        banner_intro.scale = (0.0, 0.0, 0.0)
        banner_intro.keyframe_insert(data_path="scale", frame=plan.total_frames)

        # --- BEAT 4: SUSPENSE BANNER ("WHERE IS IT?") ---
        # Stays hidden through swapping frenzy. Slams in dynamically during suspense freeze!
        if banner_rev.animation_data:
            banner_rev.animation_data_clear()
            
        rev_start = reveal_question_frame
        rev_end = max(rev_start + 15, reveal_lift_start - 2)
        
        # Hidden from 1 through rev_start - 6
        banner_rev.scale = (0.0, 0.0, 0.0)
        banner_rev.location = (0.0, -2.6, 2.2)
        banner_rev.rotation_euler = (math.radians(45.0), 0.0, math.radians(15.0))
        banner_rev.keyframe_insert(data_path="scale", frame=1)
        banner_rev.keyframe_insert(data_path="location", frame=1)
        banner_rev.keyframe_insert(data_path="rotation_euler", frame=1)
        banner_rev.keyframe_insert(data_path="scale", frame=max(1, rev_start - 6))
        banner_rev.keyframe_insert(data_path="location", frame=max(1, rev_start - 6))
        banner_rev.keyframe_insert(data_path="rotation_euler", frame=max(1, rev_start - 6))
        
        # Frame rev_start: The Question Slam (1.25x Overshoot)
        banner_rev.scale = (1.25, 1.25, 1.25)
        banner_rev.location = (0.0, -3.2, 1.35)
        banner_rev.rotation_euler = (math.radians(68.0), math.radians(1.0), math.radians(-1.0))
        banner_rev.keyframe_insert(data_path="scale", frame=rev_start)
        banner_rev.keyframe_insert(data_path="location", frame=rev_start)
        banner_rev.keyframe_insert(data_path="rotation_euler", frame=rev_start)
        
        # Frame rev_start + 6: Settle
        banner_rev.scale = (1.0, 1.0, 1.0)
        banner_rev.location = (0.0, -3.2, 1.35)
        banner_rev.rotation_euler = (math.radians(65.0), 0.0, 0.0)
        banner_rev.keyframe_insert(data_path="scale", frame=rev_start + 6)
        banner_rev.keyframe_insert(data_path="location", frame=rev_start + 6)
        banner_rev.keyframe_insert(data_path="rotation_euler", frame=rev_start + 6)
        
        # Hold
        banner_rev.scale = (1.03, 1.03, 1.03)
        banner_rev.location = (0.0, -3.2, 1.38)
        banner_rev.keyframe_insert(data_path="scale", frame=rev_end - 4)
        banner_rev.keyframe_insert(data_path="location", frame=rev_end - 4)
        
        # Wipe exit to make way for winner
        banner_rev.scale = (0.0, 0.0, 0.0)
        banner_rev.location = (-6.0, -3.2, 1.6)
        banner_rev.rotation_euler = (math.radians(65.0), 0.0, math.radians(30.0))
        banner_rev.keyframe_insert(data_path="scale", frame=rev_end)
        banner_rev.keyframe_insert(data_path="location", frame=rev_end)
        banner_rev.keyframe_insert(data_path="rotation_euler", frame=rev_end)
        banner_rev.scale = (0.0, 0.0, 0.0)
        banner_rev.keyframe_insert(data_path="scale", frame=plan.total_frames)

        # --- BEAT 5: WINNER REVEAL BANNER ("SLOT [X] WINS!") ---
        if banner_win.animation_data:
            banner_win.animation_data_clear()
            
        win_start = reveal_lift_start
        
        # Hidden from 1 to win_start - 4
        banner_win.scale = (0.0, 0.0, 0.0)
        banner_win.location = (0.0, -2.6, 2.3)
        banner_win.rotation_euler = (math.radians(50.0), math.radians(-10.0), math.radians(20.0))
        banner_win.keyframe_insert(data_path="scale", frame=1)
        banner_win.keyframe_insert(data_path="location", frame=1)
        banner_win.keyframe_insert(data_path="rotation_euler", frame=1)
        banner_win.keyframe_insert(data_path="scale", frame=max(1, win_start - 4))
        banner_win.keyframe_insert(data_path="location", frame=max(1, win_start - 4))
        banner_win.keyframe_insert(data_path="rotation_euler", frame=max(1, win_start - 4))
        
        # Massive gold boom slam impact (1.28x Overshoot)
        banner_win.scale = (1.28, 1.28, 1.28)
        banner_win.location = (0.0, -3.2, 1.35)
        banner_win.rotation_euler = (math.radians(68.0), 0.0, 0.0)
        banner_win.keyframe_insert(data_path="scale", frame=win_start + 7)
        banner_win.keyframe_insert(data_path="location", frame=win_start + 7)
        banner_win.keyframe_insert(data_path="rotation_euler", frame=win_start + 7)
        
        # Settle
        banner_win.scale = (1.0, 1.0, 1.0)
        banner_win.location = (0.0, -3.2, 1.35)
        banner_win.rotation_euler = (math.radians(65.0), 0.0, 0.0)
        banner_win.keyframe_insert(data_path="scale", frame=win_start + 13)
        banner_win.keyframe_insert(data_path="location", frame=win_start + 13)
        banner_win.keyframe_insert(data_path="rotation_euler", frame=win_start + 13)
        
        # Hold to end with slow heroic drift
        banner_win.scale = (1.05, 1.05, 1.05)
        banner_win.location = (0.0, -3.2, 1.40)
        banner_win.keyframe_insert(data_path="scale", frame=plan.total_frames)
        banner_win.keyframe_insert(data_path="location", frame=plan.total_frames)
        
        # Shuffle Banner (if enabled)
        if not props.clean_screen_during_shuffle:
            banner_shuf = setup_phase_text_banner(coll, "Wolfpack_Banner_Shuffle", props.banner_shuffle_text, font_type=props.banner_font)
            if banner_shuf.animation_data:
                banner_shuf.animation_data_clear()
            banner_shuf.scale = (0.0, 0.0, 0.0)
            banner_shuf.keyframe_insert(data_path="scale", frame=1)
            banner_shuf.keyframe_insert(data_path="scale", frame=intro_offset + 4)
            banner_shuf.scale = (1.0, 1.0, 1.0)
            banner_shuf.keyframe_insert(data_path="scale", frame=intro_offset + 8)
            banner_shuf.keyframe_insert(data_path="scale", frame=suspense_start)
            banner_shuf.scale = (0.0, 0.0, 0.0)
            banner_shuf.keyframe_insert(data_path="scale", frame=suspense_start + 4)
            banner_shuf.keyframe_insert(data_path="scale", frame=plan.total_frames)
        else:
            b_shuf_old = bpy.data.objects.get("Wolfpack_Banner_Shuffle")
            if b_shuf_old:
                bpy.data.objects.remove(b_shuf_old, do_unlink=True)
    else:
        for b_name in ["Wolfpack_Banner_Intro", "Wolfpack_Banner_Reveal", "Wolfpack_Banner_Winner", "Wolfpack_Banner_Shuffle"]:
            b_old = bpy.data.objects.get(b_name)
            if b_old:
                bpy.data.objects.remove(b_old, do_unlink=True)

    # 6. Interactive Slot HUD Badges ([ 1 ], [ 2 ], [ 3 ]) — Staggered Domino Wave
    if props.show_slot_hud_numbers:
        coll = bpy.data.collections.get("Wolfpack_Shuffle") or bpy.context.scene.collection
        vfont_agency = load_laurier_font('AGENCYFB')
        mat_gold, mat_purple = get_laurier_materials()
        winning_slot_idx = plan.item_slot[winning_item_id]
        rev_start = reveal_question_frame
        
        for s_idx in range(3):
            badge_name = f"Wolfpack_Slot_Badge_{s_idx + 1}"
            center = plan.get_slot_center(s_idx)
            target_badge_loc = (center.x, -1.2, 0.95)
            
            b_obj = bpy.data.objects.get(badge_name)
            if not b_obj:
                b_data = bpy.data.curves.new(type='FONT', name=f"{badge_name}_Data")
                b_obj = bpy.data.objects.new(badge_name, b_data)
                b_data.body = f"[ {s_idx + 1} ]"
                if vfont_agency:
                    b_data.font = vfont_agency
                b_data.align_x = 'CENTER'
                b_data.align_y = 'CENTER'
                b_data.size = 0.45
                b_data.extrude = 0.035
                b_data.bevel_depth = 0.008
                b_data.bevel_resolution = 4
                coll.objects.link(b_obj)
                b_obj.data.materials.append(mat_gold)
            else:
                b_obj.data.body = f"[ {s_idx + 1} ]"
                if vfont_agency:
                    b_obj.data.font = vfont_agency
                b_obj.data.size = 0.45
                b_obj.data.extrude = 0.035
                b_obj.data.bevel_depth = 0.008
                b_obj.data.bevel_resolution = 4
                
            b_obj.location = target_badge_loc
            b_obj.rotation_euler = (math.radians(65.0), 0.0, 0.0)
            if b_obj.animation_data:
                b_obj.animation_data_clear()
                
            # Staggered Domino Wave: Badge 1 at rev_start+5, Badge 2 at rev_start+10, Badge 3 at rev_start+15
            badge_stagger = s_idx * 5
            b_pop_start = rev_start + 5 + badge_stagger
            
            # Hidden until its individual stagger time
            b_obj.scale = (0.0, 0.0, 0.0)
            b_obj.location = (target_badge_loc[0], target_badge_loc[1], 0.50)
            b_obj.keyframe_insert(data_path="scale", frame=1)
            b_obj.keyframe_insert(data_path="location", frame=1)
            b_obj.keyframe_insert(data_path="scale", frame=max(1, b_pop_start - 2))
            b_obj.keyframe_insert(data_path="location", frame=max(1, b_pop_start - 2))
            
            # Snappy bounce overshoot
            b_obj.scale = (1.25, 1.25, 1.25)
            b_obj.location = (target_badge_loc[0], target_badge_loc[1], 1.02)
            b_obj.keyframe_insert(data_path="scale", frame=b_pop_start + 3)
            b_obj.keyframe_insert(data_path="location", frame=b_pop_start + 3)
            
            # Settle to rest
            b_obj.scale = (1.0, 1.0, 1.0)
            b_obj.location = target_badge_loc
            b_obj.keyframe_insert(data_path="scale", frame=b_pop_start + 6)
            b_obj.keyframe_insert(data_path="location", frame=b_pop_start + 6)
            b_obj.keyframe_insert(data_path="scale", frame=reveal_lift_start - 2)
            b_obj.keyframe_insert(data_path="location", frame=reveal_lift_start - 2)
            
            if s_idx == winning_slot_idx:
                # Winner badge pulses up to 1.45x and hovers
                b_obj.scale = (1.45, 1.45, 1.45)
                b_obj.location = (target_badge_loc[0], target_badge_loc[1], 1.08)
                b_obj.keyframe_insert(data_path="scale", frame=reveal_lift_start + 6)
                b_obj.keyframe_insert(data_path="location", frame=reveal_lift_start + 6)
                b_obj.keyframe_insert(data_path="scale", frame=plan.total_frames)
                b_obj.keyframe_insert(data_path="location", frame=plan.total_frames)
            else:
                # Losing badges pop out smoothly
                b_obj.scale = (0.0, 0.0, 0.0)
                b_obj.location = (target_badge_loc[0], target_badge_loc[1], 0.50)
                b_obj.keyframe_insert(data_path="scale", frame=reveal_lift_start + 3)
                b_obj.keyframe_insert(data_path="location", frame=reveal_lift_start + 3)
                b_obj.keyframe_insert(data_path="scale", frame=plan.total_frames)
                b_obj.keyframe_insert(data_path="location", frame=plan.total_frames)
    else:
        for s_idx in range(3):
            badge_old = bpy.data.objects.get(f"Wolfpack_Slot_Badge_{s_idx + 1}")
            if badge_old:
                bpy.data.objects.remove(badge_old, do_unlink=True)

    # 7. Automated Broadcast Cue Sheet Exporter (.json and .csv for After Effects)
    global _LAST_SHUFFLE_PLAN
    _LAST_SHUFFLE_PLAN = plan
    try:
        export_broadcast_cue_sheet(plan, props, winning_item_id, plan.total_frames)
    except Exception as e:
        print("[Wolfpack Glory] Cue sheet auto-export note:", e)

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
        default=0.15,
        min=0.0,
        max=1.5,
        step=5
    )
    bank_angle: bpy.props.FloatProperty(
        name="Centripetal Bank Angle",
        description="Dynamic tilt along movement vector during high-speed sweeps",
        default=12.0,
        min=0.0,
        max=45.0,
        step=1
    )
    prize_z_offset: bpy.props.FloatProperty(
        name="Prize Z Offset",
        description="Vertical height offset for the hidden football/prize to ensure it stays completely inside helmet during moves",
        default=0.0,
        min=-0.5,
        max=0.5,
        step=1
    )
    suspense_duration: bpy.props.IntProperty(
        name="Suspense Pause (Frames)",
        description="Dramatic pause between final shuffle swap and 'WHERE IS IT?' reveal banner",
        default=36,
        min=10,
        max=150,
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
    # Storyboard & Broadcast Presentation Options
    show_intro_reveal: bpy.props.BoolProperty(
        name="Intro Storyboard Phase",
        description="Lift helmet at start to showcase where the prize is hidden before shuffling begins",
        default=True
    )
    intro_lift_duration: bpy.props.IntProperty(
        name="Intro Duration (Frames)",
        description="Frames spent showcasing the prize before the shuffle starts",
        default=45,
        min=20,
        max=120
    )
    create_text_banner: bpy.props.BoolProperty(
        name="3D Jumbotron Text Banner",
        description="Adds an animated 3D stadium text sign (e.g. 'KEEP YOUR EYES ON THE BALL!' -> 'SHUFFLING...' -> 'WHERE IS IT?')",
        default=True
    )
    banner_intro_text: bpy.props.StringProperty(
        name="Intro Text",
        default="WATCH CLOSELY!"
    )
    banner_shuffle_text: bpy.props.StringProperty(
        name="Shuffle Text",
        default="KEEP YOUR EYES ON THE BALL!"
    )
    banner_reveal_text: bpy.props.StringProperty(
        name="Reveal Text",
        default="WHERE IS IT?"
    )

    min_safe_distance: bpy.props.FloatProperty(
        name="Min Safe Distance",
        description="Collision threshold for safety check",
        default=1.1,
        min=0.5,
        max=3.0
    )
    
    # Cognitive Visual Pacing & HUD Badges
    clean_screen_during_shuffle: bpy.props.BoolProperty(
        name="Clean Screen (Swapping Phase)",
        description="Hide all 3D banners during active shuffle so audience focus is 100% on tracking helmets without cognitive text interference",
        default=True
    )
    show_slot_hud_numbers: bpy.props.BoolProperty(
        name="Slot HUD Badges ([ 1 ] [ 2 ] [ 3 ])",
        description="Display interactive slot number badges during suspense pause so stadium crowd and host can call out picks",
        default=True
    )
    venue_preset: bpy.props.EnumProperty(
        name="Venue Staging",
        description="Procedural venue environment and lighting setup",
        items=[
            ('FOOTBALL_TURF', "University Stadium (Football Turf)", "Golden Hawks green turf with gridiron yardlines and stadium spot keylights"),
            ('BASKETBALL_COURT', "Athletic Complex (Hardwood Court)", "Polished golden maple basketball court with key and 3-point lines"),
            ('CLEAN_STUDIO', "Clean Broadcast Studio (Dark Cyc)", "Dark carbon cyc infinity floor with contrast rim lighting for commercial reels"),
        ],
        default='FOOTBALL_TURF'
    )
    
    # "Home Show" Entry Screen Bumper Properties
    entry_title: bpy.props.StringProperty(
        name="Entry Title",
        description="Headline for Home Show entry bumper",
        default="GOLDEN HAWKS SHUFFLE"
    )
    entry_subtitle: bpy.props.StringProperty(
        name="Entry Subtitle",
        description="Subtitle for Home Show entry bumper",
        default="THE ULTIMATE HELMET CHALLENGE"
    )
    entry_sponsor: bpy.props.StringProperty(
        name="Entry Sponsor Tag",
        description="Sponsor or presenter tag line",
        default="PRESENTED BY WILFRID LAURIER ATHLETICS"
    )
    entry_duration: bpy.props.IntProperty(
        name="Entry Bumper Duration (Frames)",
        description="Duration of the Home Show entry bumper in frames",
        default=60,
        min=30,
        max=180
    )

    # Game-Day 3 Deterministic Outcome Variants
    target_outcome: bpy.props.EnumProperty(
        name="Game-Day Outcome Variant",
        description="Select outcome variation for game-day rotation (prevents fans seeing repetitive winners)",
        items=[
            ('RANDOM', "Random Outcome (Surprise)", "Ball lands under naturally winning helmet"),
            ('SLOT_1', "Variant A: Left Helmet Wins (Slot 1)", "Guarantees the ball finishes under Slot 1 (Left)"),
            ('SLOT_2', "Variant B: Center Helmet Wins (Slot 2)", "Guarantees the ball finishes under Slot 2 (Center)"),
            ('SLOT_3', "Variant C: Right Helmet Wins (Slot 3)", "Guarantees the ball finishes under Slot 3 (Right)"),
        ],
        default='RANDOM'
    )
    
    # Laurier Athletics Brand Typography (Hailey's Directives)
    banner_font: bpy.props.EnumProperty(
        name="Brand Typography Font",
        description="Select typography for 3D stadium graphics (Hailey's Brand Guidelines: Radwave & Agency FB)",
        items=[
            ('RADWAVE', "Radwave Display (Headline / Hype)", "High-impact athletic display typeface"),
            ('AGENCYFB', "Agency FB Bold (Broadcast / Downs)", "Crisp condensed collegiate broadcast typography"),
            ('DEFAULT', "Blender Standard (Bfont)", "Default vector font"),
        ],
        default='RADWAVE'
    )
    
    # Modular In-Game Videoboard Stingers & Bumpers
    stinger_type: bpy.props.EnumProperty(
        name="Stinger Cue",
        description="Select modular in-game broadcast bumper to generate",
        items=[
            ('TOUCHDOWN', "Touchdown Bumper (Radwave)", "Explosive golden scoring stinger with deep purple bevel"),
            ('FIELD_GOAL_GOOD', "Field Goal: IT'S GOOD! (Radwave)", "Explosive scoring celebration stinger with golden flash"),
            ('FIELD_GOAL_ATTEMPT', "Field Goal: 45 Yds Attempt (Agency FB)", "High-stakes collegiate kick attempt countdown"),
            ('FIELD_GOAL_BLOCKED', "Field Goal: BLOCKED! (Radwave)", "Defensive stop & turnover alert"),
            ('INTERCEPTION', "Interception Alert (Radwave)", "High-tension defensive turnover alert bumper"),
            ('1ST_DOWN', "1st Down Marker (Agency FB)", "Chain mover collegiate down graphic"),
            ('2ND_DOWN', "2nd Down Marker (Agency FB)", "Mid-down offensive marker"),
            ('3RD_DOWN_SHORT', "3rd & Short (Agency FB)", "High-stakes short yardage tension cue"),
            ('3RD_DOWN_LONG', "3rd & Long (Agency FB)", "Crowd noise / defense stand-up rally cue"),
        ],
        default='TOUCHDOWN'
    )


class WOLFPACK_OT_setup_atmosphere(bpy.types.Operator):
    """Build procedural atmospheric sky dome, storm clouds, backlights, and modern Blender 5.2 compositor lens graph"""
    bl_idname = "wolfpack.setup_atmosphere"
    bl_label = "Build Cinematic Sky, Clouds & Lens Rig"
    bl_description = "Creates dramatic twilight sky dome, clouds, rim lights, and sets up real-time compositor bloom & anamorphic dispersion"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        setup_cinematic_atmosphere()
        self.report({'INFO'}, "Cinematic atmosphere, clouds & compositor lens rig configured!")
        return {'FINISHED'}


class WOLFPACK_OT_setup_goalposts(bpy.types.Operator):
    """Spawn 3D collegiate upright goalposts with golden yellow coating and wind streamers"""
    bl_idname = "wolfpack.setup_goalposts"
    bl_label = "Spawn 3D Uprights & Goalposts"
    bl_description = "Creates authentic NCAA/U SPORTS collegiate goalposts in the background"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        setup_goalposts()
        self.report({'INFO'}, "Collegiate 3D goalposts spawned in scene!")
        return {'FINISHED'}


class WOLFPACK_OT_generate_stinger(bpy.types.Operator):
    """Generate modular 3D in-game videoboard stinger with Hailey's typography (Radwave / Agency FB) and LED anti-glare shaders"""
    bl_idname = "wolfpack.generate_stinger"
    bl_label = "Generate 3D Stinger"
    bl_description = "Generates an animated ESPN-style 3D stinger for the selected game-day event"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.wolfpack_shuffle
        st_type = props.stinger_type
        
        # Clean conflicting text from other modes (Bumper/Shuffle)
        cleanup_conflicting_text_graphics('STINGER')
        
        # If Field Goal stinger, ensure 3D goalposts are spawned
        if st_type.startswith('FIELD_GOAL') and not bpy.data.objects.get("Goalpost_Base"):
            setup_goalposts()
            
        # Typography pairing rule from Hailey:
        # Radwave for explosive hype events (Touchdown, Interception, It's Good!)
        # Agency FB for collegiate broadcast yardage, downs, and stats
        if st_type in ('TOUCHDOWN', 'INTERCEPTION', 'FIELD_GOAL_GOOD', 'FIELD_GOAL_BLOCKED'):
            f_choice = 'RADWAVE'
        else:
            f_choice = 'AGENCYFB'
            
        stinger_data = {
            'TOUCHDOWN': ("TOUCHDOWN", "GOLDEN HAWKS SCORE", 65),
            'FIELD_GOAL_GOOD': ("IT'S GOOD!", "3 POINTS // GOLDEN HAWKS", 65),
            'FIELD_GOAL_ATTEMPT': ("FIELD GOAL", "45 YARDS // 4TH DOWN", 55),
            'FIELD_GOAL_BLOCKED': ("BLOCKED!", "TURNOVER ON DOWNS // DEFENSE", 60),
            'INTERCEPTION': ("INTERCEPTION", "TURNOVER! DEFENSE BALL", 60),
            '1ST_DOWN': ("1ST DOWN", "MOVE THE CHAINS", 55),
            '2ND_DOWN': ("2ND DOWN", "GOLDEN HAWKS OFFENSE", 50),
            '3RD_DOWN_SHORT': ("3RD & SHORT", "GET ON YOUR FEET!", 55),
            '3RD_DOWN_LONG': ("3RD & LONG", "DEFENSE // STAND UP!", 60),
        }
        
        headline, subtitle, total_frames = stinger_data.get(st_type, ("GOLDEN HAWKS", "WILFRID LAURIER", 60))
        
        coll_name = "Wolfpack_Stingers"
        coll = bpy.data.collections.get(coll_name)
        if not coll:
            coll = bpy.data.collections.new(coll_name)
            bpy.context.scene.collection.children.link(coll)
            
        mat_gold, mat_purple = get_laurier_materials()
        vfont_head = load_laurier_font(f_choice)
        vfont_sub = load_laurier_font('AGENCYFB')
        
        base_name = f"Stinger_{st_type}"
        old_obj = bpy.data.objects.get(base_name)
        if old_obj:
            bpy.data.objects.remove(old_obj, do_unlink=True)
        old_stroke = bpy.data.objects.get(f"{base_name}_Stroke")
        if old_stroke:
            bpy.data.objects.remove(old_stroke, do_unlink=True)
        old_sub = bpy.data.objects.get(f"{base_name}_Sub")
        if old_sub:
            bpy.data.objects.remove(old_sub, do_unlink=True)
            
        # 1. Headline 3D Curve (Front Gold Face)
        txt_d = bpy.data.curves.new(type='FONT', name=f"{base_name}_Text")
        txt_d.body = headline
        if vfont_head:
            txt_d.font = vfont_head
        txt_d.align_x = 'CENTER'
        txt_d.align_y = 'CENTER'
        txt_d.size = 0.95
        txt_d.extrude = 0.065
        txt_d.bevel_depth = 0.008
        txt_d.bevel_resolution = 4
        
        # Elevated Z height (1.35m) so it majestically floats above helmets and never clips into turf
        obj_head = bpy.data.objects.new(base_name, txt_d)
        obj_head.location = (0.0, -3.2, 1.35)
        obj_head.rotation_euler = (math.radians(65.0), 0.0, 0.0)
        coll.objects.link(obj_head)
        obj_head.data.materials.append(mat_gold)
        
        # Headline Backing Stroke (Deep Purple Bevel - No White Border Glare, zero z-fighting)
        stroke_d = bpy.data.curves.new(type='FONT', name=f"{base_name}_Stroke")
        stroke_d.body = headline
        if vfont_head:
            stroke_d.font = vfont_head
        stroke_d.align_x = 'CENTER'
        stroke_d.align_y = 'CENTER'
        stroke_d.size = 0.95
        stroke_d.extrude = 0.050
        stroke_d.bevel_depth = 0.026
        stroke_d.bevel_resolution = 4
        
        # Pushed cleanly behind gold face (Y=+0.022) to strictly eliminate z-fighting / polygon flicker
        obj_stroke = bpy.data.objects.new(f"{base_name}_Stroke", stroke_d)
        obj_stroke.parent = obj_head
        obj_stroke.location = (0.0, 0.022, -0.002)
        coll.objects.link(obj_stroke)
        obj_stroke.data.materials.append(mat_purple)
        
        # 2. Subtitle 3D Curve (Agency FB)
        sub_d = bpy.data.curves.new(type='FONT', name=f"{base_name}_SubText")
        sub_d.body = subtitle
        if vfont_sub:
            sub_d.font = vfont_sub
        sub_d.align_x = 'CENTER'
        sub_d.align_y = 'CENTER'
        sub_d.size = 0.38
        sub_d.extrude = 0.035
        sub_d.bevel_depth = 0.005
        sub_d.bevel_resolution = 3
        
        obj_sub = bpy.data.objects.new(f"{base_name}_Sub", sub_d)
        obj_sub.parent = obj_head
        obj_sub.location = (0.0, -0.008, -0.62)
        coll.objects.link(obj_sub)
        obj_sub.data.materials.append(mat_gold)
        
        # Keyframe Animation (Kinetic 3D Spin, BOOM Impact Slam, Settle, Drift & Sweep Exit)
        if obj_head.animation_data:
            obj_head.animation_data_clear()
        if obj_sub.animation_data:
            obj_sub.animation_data_clear()
            
        # --- HEADLINE: SPIN & BOOM ENTRANCE ---
        # Frame 1: Dynamic 3D angled spin in air
        obj_head.scale = (0.0, 0.0, 0.0)
        obj_head.location = (0.0, -2.6, 2.3)
        obj_head.rotation_euler = (math.radians(45.0), math.radians(-15.0), math.radians(28.0))
        obj_head.keyframe_insert(data_path="scale", frame=1)
        obj_head.keyframe_insert(data_path="location", frame=1)
        obj_head.keyframe_insert(data_path="rotation_euler", frame=1)
        
        # Frame 10: THE BOOM SLAM (Kinetic 1.25x Overshoot)
        obj_head.scale = (1.25, 1.25, 1.25)
        obj_head.location = (0.0, -3.2, 1.35)
        obj_head.rotation_euler = (math.radians(68.0), math.radians(2.0), math.radians(-2.0))
        obj_head.keyframe_insert(data_path="scale", frame=10)
        obj_head.keyframe_insert(data_path="location", frame=10)
        obj_head.keyframe_insert(data_path="rotation_euler", frame=10)
        
        # Frame 16: Rest Settle
        obj_head.scale = (1.0, 1.0, 1.0)
        obj_head.location = (0.0, -3.2, 1.35)
        obj_head.rotation_euler = (math.radians(65.0), 0.0, 0.0)
        obj_head.keyframe_insert(data_path="scale", frame=16)
        obj_head.keyframe_insert(data_path="location", frame=16)
        obj_head.keyframe_insert(data_path="rotation_euler", frame=16)
        
        # Frame (total_frames - 10): Heroic floating drift hold
        obj_head.scale = (1.06, 1.06, 1.06)
        obj_head.location = (0.0, -3.2, 1.42)
        obj_head.rotation_euler = (math.radians(65.0), 0.0, 0.0)
        obj_head.keyframe_insert(data_path="scale", frame=total_frames - 10)
        obj_head.keyframe_insert(data_path="location", frame=total_frames - 10)
        obj_head.keyframe_insert(data_path="rotation_euler", frame=total_frames - 10)
        
        # Frame total_frames: High-speed snap sweep exit
        obj_head.scale = (0.0, 0.0, 0.0)
        obj_head.location = (7.5, -3.2, 1.8)
        obj_head.rotation_euler = (math.radians(65.0), 0.0, math.radians(-35.0))
        obj_head.keyframe_insert(data_path="scale", frame=total_frames)
        obj_head.keyframe_insert(data_path="location", frame=total_frames)
        obj_head.keyframe_insert(data_path="rotation_euler", frame=total_frames)
        
        # --- SUBTITLE: STAGGERED SECONDARY WHIP ---
        # Frame 1 to 7: Hidden
        obj_sub.scale = (0.0, 0.0, 0.0)
        obj_sub.location = (0.0, -0.008, -0.90)
        obj_sub.keyframe_insert(data_path="scale", frame=1)
        obj_sub.keyframe_insert(data_path="location", frame=1)
        obj_sub.keyframe_insert(data_path="scale", frame=7)
        obj_sub.keyframe_insert(data_path="location", frame=7)
        
        # Frame 13: Subtitle whips in from bottom with overshoot
        obj_sub.scale = (1.18, 1.18, 1.18)
        obj_sub.location = (0.0, -0.008, -0.58)
        obj_sub.keyframe_insert(data_path="scale", frame=13)
        obj_sub.keyframe_insert(data_path="location", frame=13)
        
        # Frame 18: Settle
        obj_sub.scale = (1.0, 1.0, 1.0)
        obj_sub.location = (0.0, -0.008, -0.62)
        obj_sub.keyframe_insert(data_path="scale", frame=18)
        obj_sub.keyframe_insert(data_path="location", frame=18)
        
        # Frame (total_frames - 10): Hold
        obj_sub.scale = (1.0, 1.0, 1.0)
        obj_sub.location = (0.0, -0.008, -0.62)
        obj_sub.keyframe_insert(data_path="scale", frame=total_frames - 10)
        obj_sub.keyframe_insert(data_path="location", frame=total_frames - 10)
        
        # Frame total_frames: Exit
        obj_sub.scale = (0.0, 0.0, 0.0)
        obj_sub.keyframe_insert(data_path="scale", frame=total_frames)

        # --- CAMERA IMPACT MICRO-SHAKE (BOOM PUNCH) ---
        cam_obj = bpy.data.objects.get("Shuffle_Camera")
        if cam_obj:
            if cam_obj.animation_data:
                cam_obj.animation_data_clear()
            base_cam_loc = (0.0, -8.0, 4.0)
            cam_obj.location = base_cam_loc
            cam_obj.keyframe_insert(data_path="location", frame=1)
            cam_obj.keyframe_insert(data_path="location", frame=9)
            
            # Frame 10: Bass punch kickback
            cam_obj.location = (0.0, -8.18, 4.06)
            cam_obj.keyframe_insert(data_path="location", frame=10)
            
            # Frame 14: Settle back to base position
            cam_obj.location = base_cam_loc
            cam_obj.keyframe_insert(data_path="location", frame=14)
            cam_obj.keyframe_insert(data_path="location", frame=total_frames)

        context.scene.frame_start = 1
        context.scene.frame_end = total_frames
        context.scene.frame_set(1)
        
        self.report({'INFO'}, f"Generated {headline} stinger ({total_frames} frames) with {f_choice} spin-boom animation!")
        return {'FINISHED'}


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
        setup_demo_scene_if_needed(props.slot_spacing, props.venue_preset)
        # Link to properties
        props.custom_helmet_1 = bpy.data.objects.get("Helmet_1")
        props.custom_helmet_2 = bpy.data.objects.get("Helmet_2")
        props.custom_helmet_3 = bpy.data.objects.get("Helmet_3")
        props.custom_football = bpy.data.objects.get("Football_CTRL")
        self.report({'INFO'}, f"Stand-in scene created for venue '{props.venue_preset}' and linked successfully.")
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


class WOLFPACK_OT_generate_entry_bumper(bpy.types.Operator):
    """Generate standalone/integrated 'Home Show' 3D Entry Screen Bumper with Radwave & Agency FB typography"""
    bl_idname = "wolfpack.generate_entry_bumper"
    bl_label = "Generate Home Show Entry Bumper"
    bl_description = "Creates an ESPN/Fox Sports style 3D intro bumper screen for the Golden Hawks Shuffle"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.wolfpack_shuffle
        coll = bpy.data.collections.get("Wolfpack_Shuffle") or context.scene.collection
        mat_gold, mat_purple = get_laurier_materials()
        vfont_radwave = load_laurier_font('RADWAVE')
        vfont_agency = load_laurier_font('AGENCYFB')
        
        # Clean conflicting text from other modes (Shuffle/Stinger)
        cleanup_conflicting_text_graphics('BUMPER')
        
        # Clean previous bumper elements
        for name in ["Wolfpack_Bumper_Title", "Wolfpack_Bumper_Sub", "Wolfpack_Bumper_Sponsor"]:
            old = bpy.data.objects.get(name)
            if old:
                bpy.data.objects.remove(old, do_unlink=True)
                
        # 1. Main Title: Radwave Display (Dual-layer Gold + Deep Purple Stroke)
        t_data = bpy.data.curves.new(type='FONT', name="Wolfpack_Bumper_Title_Data")
        t_data.body = props.entry_title
        if vfont_radwave:
            t_data.font = vfont_radwave
        t_data.align_x = 'CENTER'
        t_data.align_y = 'CENTER'
        t_data.size = 0.85
        t_data.extrude = 0.065
        t_data.bevel_depth = 0.008
        t_data.bevel_resolution = 4
        
        # Elevated Z height (1.35m) so it majestically floats above helmets and never clips into turf
        obj_title = bpy.data.objects.new("Wolfpack_Bumper_Title", t_data)
        obj_title.location = (0.0, -3.2, 1.35)
        obj_title.rotation_euler = (math.radians(65.0), 0.0, 0.0)
        coll.objects.link(obj_title)
        obj_title.data.materials.append(mat_gold)
        
        # Backing stroke (anti-glare deep purple bevel - offset cleanly to prevent z-fighting)
        s_data = bpy.data.curves.new(type='FONT', name="Wolfpack_Bumper_Title_Stroke_Data")
        s_data.body = props.entry_title
        if vfont_radwave:
            s_data.font = vfont_radwave
        s_data.align_x = 'CENTER'
        s_data.align_y = 'CENTER'
        s_data.size = 0.85
        s_data.extrude = 0.050
        s_data.bevel_depth = 0.026
        s_data.bevel_resolution = 4
        
        obj_stroke = bpy.data.objects.new("Wolfpack_Bumper_Title_Stroke", s_data)
        obj_stroke.parent = obj_title
        obj_stroke.location = (0.0, 0.022, -0.002)
        coll.objects.link(obj_stroke)
        obj_stroke.data.materials.append(mat_purple)
        
        # 2. Subtitle: Agency FB Bold
        sub_data = bpy.data.curves.new(type='FONT', name="Wolfpack_Bumper_Sub_Data")
        sub_data.body = props.entry_subtitle
        if vfont_agency:
            sub_data.font = vfont_agency
        sub_data.align_x = 'CENTER'
        sub_data.align_y = 'CENTER'
        sub_data.size = 0.38
        sub_data.extrude = 0.035
        sub_data.bevel_depth = 0.005
        sub_data.bevel_resolution = 3
        
        obj_sub = bpy.data.objects.new("Wolfpack_Bumper_Sub", sub_data)
        obj_sub.parent = obj_title
        obj_sub.location = (0.0, -0.008, -0.58)
        coll.objects.link(obj_sub)
        obj_sub.data.materials.append(mat_gold)
        
        # 3. Sponsor Tag: Agency FB
        sp_data = bpy.data.curves.new(type='FONT', name="Wolfpack_Bumper_Sponsor_Data")
        sp_data.body = props.entry_sponsor
        if vfont_agency:
            sp_data.font = vfont_agency
        sp_data.align_x = 'CENTER'
        sp_data.align_y = 'CENTER'
        sp_data.size = 0.22
        sp_data.extrude = 0.022
        sp_data.bevel_depth = 0.004
        sp_data.bevel_resolution = 3
        
        obj_sponsor = bpy.data.objects.new("Wolfpack_Bumper_Sponsor", sp_data)
        obj_sponsor.parent = obj_title
        obj_sponsor.location = (0.0, -0.008, -0.98)
        coll.objects.link(obj_sponsor)
        obj_sponsor.data.materials.append(mat_purple)
        
        # Kinetic Staggered Spin & Boom Keyframing
        dur = props.entry_duration
        for anim_o in [obj_title, obj_sub, obj_sponsor]:
            if anim_o.animation_data:
                anim_o.animation_data_clear()
            
        # --- TITLE: 3D SPIN & BOOM SLAM ---
        # Frame 1: Angled spin in air
        obj_title.scale = (0.0, 0.0, 0.0)
        obj_title.location = (0.0, -2.6, 2.3)
        obj_title.rotation_euler = (math.radians(45.0), math.radians(-15.0), math.radians(28.0))
        obj_title.keyframe_insert(data_path="scale", frame=1)
        obj_title.keyframe_insert(data_path="location", frame=1)
        obj_title.keyframe_insert(data_path="rotation_euler", frame=1)
        
        # Frame 10: THE BOOM SLAM (Kinetic Overshoot)
        obj_title.scale = (1.25, 1.25, 1.25)
        obj_title.location = (0.0, -3.2, 1.35)
        obj_title.rotation_euler = (math.radians(68.0), math.radians(2.0), math.radians(-2.0))
        obj_title.keyframe_insert(data_path="scale", frame=10)
        obj_title.keyframe_insert(data_path="location", frame=10)
        obj_title.keyframe_insert(data_path="rotation_euler", frame=10)
        
        # Frame 16: Rest Settle
        obj_title.scale = (1.0, 1.0, 1.0)
        obj_title.location = (0.0, -3.2, 1.35)
        obj_title.rotation_euler = (math.radians(65.0), 0.0, 0.0)
        obj_title.keyframe_insert(data_path="scale", frame=16)
        obj_title.keyframe_insert(data_path="location", frame=16)
        obj_title.keyframe_insert(data_path="rotation_euler", frame=16)
        
        # Frame dur - 10: Heroic drift
        obj_title.scale = (1.06, 1.06, 1.06)
        obj_title.location = (0.0, -3.2, 1.42)
        obj_title.keyframe_insert(data_path="scale", frame=dur - 10)
        obj_title.keyframe_insert(data_path="location", frame=dur - 10)
        
        # Frame dur: High-speed snap sweep exit
        obj_title.scale = (0.0, 0.0, 0.0)
        obj_title.location = (7.5, -3.2, 1.8)
        obj_title.rotation_euler = (math.radians(65.0), 0.0, math.radians(-35.0))
        obj_title.keyframe_insert(data_path="scale", frame=dur)
        obj_title.keyframe_insert(data_path="location", frame=dur)
        obj_title.keyframe_insert(data_path="rotation_euler", frame=dur)
        
        # --- SUBTITLE: STAGGERED SECONDARY WHIP ---
        obj_sub.scale = (0.0, 0.0, 0.0)
        obj_sub.location = (0.0, -0.008, -0.85)
        obj_sub.keyframe_insert(data_path="scale", frame=1)
        obj_sub.keyframe_insert(data_path="location", frame=1)
        obj_sub.keyframe_insert(data_path="scale", frame=7)
        obj_sub.keyframe_insert(data_path="location", frame=7)
        
        obj_sub.scale = (1.18, 1.18, 1.18)
        obj_sub.location = (0.0, -0.008, -0.54)
        obj_sub.keyframe_insert(data_path="scale", frame=13)
        obj_sub.keyframe_insert(data_path="location", frame=13)
        
        obj_sub.scale = (1.0, 1.0, 1.0)
        obj_sub.location = (0.0, -0.008, -0.58)
        obj_sub.keyframe_insert(data_path="scale", frame=18)
        obj_sub.keyframe_insert(data_path="location", frame=18)
        obj_sub.keyframe_insert(data_path="scale", frame=dur - 10)
        obj_sub.keyframe_insert(data_path="location", frame=dur - 10)
        
        obj_sub.scale = (0.0, 0.0, 0.0)
        obj_sub.keyframe_insert(data_path="scale", frame=dur)
        
        # --- SPONSOR TAG: TERTIARY SNAP ---
        obj_sponsor.scale = (0.0, 0.0, 0.0)
        obj_sponsor.keyframe_insert(data_path="scale", frame=1)
        obj_sponsor.keyframe_insert(data_path="scale", frame=12)
        
        obj_sponsor.scale = (1.15, 1.15, 1.15)
        obj_sponsor.keyframe_insert(data_path="scale", frame=17)
        
        obj_sponsor.scale = (1.0, 1.0, 1.0)
        obj_sponsor.keyframe_insert(data_path="scale", frame=21)
        obj_sponsor.keyframe_insert(data_path="scale", frame=dur - 10)
        
        obj_sponsor.scale = (0.0, 0.0, 0.0)
        obj_sponsor.keyframe_insert(data_path="scale", frame=dur)

        # --- CAMERA IMPACT MICRO-SHAKE (BOOM PUNCH) ---
        cam_obj = bpy.data.objects.get("Shuffle_Camera")
        if cam_obj:
            if cam_obj.animation_data:
                cam_obj.animation_data_clear()
            base_cam_loc = (0.0, -8.0, 4.0)
            cam_obj.location = base_cam_loc
            cam_obj.keyframe_insert(data_path="location", frame=1)
            cam_obj.keyframe_insert(data_path="location", frame=9)
            
            # Frame 10: Bass punch kickback
            cam_obj.location = (0.0, -8.18, 4.06)
            cam_obj.keyframe_insert(data_path="location", frame=10)
            
            # Frame 14: Settle back to base position
            cam_obj.location = base_cam_loc
            cam_obj.keyframe_insert(data_path="location", frame=14)
            cam_obj.keyframe_insert(data_path="location", frame=dur)
        
        context.scene.frame_start = 1
        context.scene.frame_end = dur
        context.scene.frame_set(1)
        
        self.report({'INFO'}, f"Home Show Entry Bumper generated ({dur} frames)!")
        return {'FINISHED'}


class WOLFPACK_OT_export_cue_sheet(bpy.types.Operator):
    """Export After Effects & Sound Design Broadcast Cue Sheet (.json & .csv)"""
    bl_idname = "wolfpack.export_cue_sheet"
    bl_label = "Export AE Cue Sheet (.json & .csv)"
    bl_description = "Exports timestamped SMPTE cue sheet recording all swaps, pauses, and reveal timecodes for After Effects and sound design"
    bl_options = {'REGISTER'}

    def execute(self, context):
        global _LAST_SHUFFLE_PLAN
        scene = context.scene
        props = scene.wolfpack_shuffle
        plan = _LAST_SHUFFLE_PLAN
        winning_id = getattr(plan, "reveal_item_id", 0) if plan else 0
        total_f = getattr(plan, "total_frames", scene.frame_end) if plan else scene.frame_end
        
        if not plan:
            plan = ShufflePlan(
                num_items=3,
                slot_spacing=props.slot_spacing,
                fps=props.fps
            )
            desired_slot = None
            if props.target_outcome == 'SLOT_1':
                desired_slot = 0
            elif props.target_outcome == 'SLOT_2':
                desired_slot = 1
            elif props.target_outcome == 'SLOT_3':
                desired_slot = 2
            plan.generate_routine(
                num_swaps=props.num_swaps,
                swap_duration_frames=props.swap_duration,
                pause_frames=props.pause_frames,
                desired_outcome_slot=desired_slot,
                start_frame=props.intro_lift_duration + 10 if props.show_intro_reveal else 30,
                suspense_duration=props.suspense_duration
            )
            winning_id = plan.reveal_item_id
            total_f = plan.total_frames
            
        try:
            j_path, c_path = export_broadcast_cue_sheet(plan, props, winning_id, total_f)
            self.report({'INFO'}, f"Exported cue sheets: {os.path.basename(j_path)} and {os.path.basename(c_path)}")
            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, f"Cue sheet export failed: {str(e)}")
            return {'CANCELLED'}


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

        # 1. "Home Show" 3D Entry Screen Bumper
        box_bump = layout.box()
        box_bump.label(text="Home Show 3D Entry Bumper", icon='COMMUNITY')
        box_bump.prop(props, "entry_title", text="Title")
        box_bump.prop(props, "entry_subtitle", text="Subtitle")
        box_bump.prop(props, "entry_sponsor", text="Sponsor")
        box_bump.prop(props, "entry_duration", text="Duration")
        box_bump.operator("wolfpack.generate_entry_bumper", text="Generate 3D Entry Bumper", icon='PLAY')

        # 2. Game-Day 3 Deterministic Outcome Variants Box
        box_var = layout.box()
        box_var.label(text="Game-Day Outcome Variants (3 Variants)", icon='FORCE_DRAG')
        box_var.prop(props, "target_outcome", text="Outcome")

        # 3. Cognitive Visual Pacing & HUD Badges
        box_cog = layout.box()
        box_cog.label(text="Cognitive Pacing & Visual Bandwidth", icon='VIS_SEL_11')
        box_cog.prop(props, "clean_screen_during_shuffle", text="Clean Screen (Zero Text During Swaps)")
        box_cog.prop(props, "show_slot_hud_numbers", text="Slot HUD Badges [ 1 ] [ 2 ] [ 3 ]")

        # 4. Multi-Venue Staging Presets
        box_venue = layout.box()
        box_venue.label(text="Multi-Venue Staging", icon='SCENE_DATA')
        box_venue.prop(props, "venue_preset", text="Venue")
        box_venue.operator("wolfpack.setup_demo", text="Spawn / Update Venue Scene", icon='DUPLICATE')

        # 5. Cinematic Compositor & Atmospheric Set Design
        box_comp = layout.box()
        box_comp.label(text="Cinematic Atmosphere & Lens Rig", icon='IMAGE_BACKGROUND')
        box_comp.operator("wolfpack.setup_atmosphere", text="Build Atmospheric Sky & Compositor", icon='OUTLINER_OB_LIGHT')
        box_comp.operator("wolfpack.setup_goalposts", text="Spawn 3D Uprights & Goalposts", icon='SNAP_GRID')

        # 6. Laurier Brand Typography & LED Shaders Box (Hailey's Directives)
        box_font = layout.box()
        box_font.label(text="Laurier Brand Typography (Hailey's Spec)", icon='FONT_DATA')
        box_font.prop(props, "banner_font", text="Typography")
        col_f = box_font.column(align=True)
        col_f.label(text="• Radwave: Hype Headers & Stingers", icon='RIGHTARROW_THIN')
        col_f.label(text="• Agency FB: Downs, Yards & Stats", icon='RIGHTARROW_THIN')
        col_f.label(text="• Anti-Glare: Deep Purple (#20003B) & Gold (#FDB913)", icon='MATERIAL')

        # 7. Modular In-Game Videoboard Stingers & Bumpers Box
        box_st = layout.box()
        box_st.label(text="In-Game Modular Stingers", icon='DECORATE_ANIMATE')
        box_st.prop(props, "stinger_type", text="Stinger Event")
        box_st.operator("wolfpack.generate_stinger", text="Generate 3D Stinger", icon='PLAY')

        # 8. Custom Model Selection Box
        box = layout.box()
        box.label(text="Assign Your 3D Models", icon='OBJECT_DATA')
        box.prop(props, "custom_helmet_1", text="Shuffler 1 (Left)")
        box.prop(props, "custom_helmet_2", text="Shuffler 2 (Center)")
        box.prop(props, "custom_helmet_3", text="Shuffler 3 (Right)")
        box.prop(props, "custom_football", text="Hidden Prize (Under)")
        
        row = box.row(align=True)
        row.operator("wolfpack.link_selected", text="Auto-Assign 3 Selected", icon='RESTRICT_SELECT_OFF')
        row.operator("wolfpack.import_model", text="Import Model File", icon='IMPORT')

        # 9. Shuffle Timing & Collision Dynamics
        box_time = layout.box()
        box_time.label(text="Shuffle Timing & FPS", icon='TIME')
        box_time.prop(props, "num_swaps")
        box_time.prop(props, "swap_duration")
        box_time.prop(props, "pause_frames")
        box_time.prop(props, "fps")

        box_phys = layout.box()
        box_phys.label(text="Collision & Dynamics Mechanics", icon='PHYSICS')
        box_phys.prop(props, "slot_spacing")
        box_phys.prop(props, "y_depth")
        box_phys.prop(props, "bounce_height")
        box_phys.prop(props, "bank_angle")
        box_phys.prop(props, "movement_style")

        # 10. Reveal & Suspense Settings
        box_rev = layout.box()
        box_rev.label(text="Reveal & Suspense Settings", icon='HIDE_OFF')
        box_rev.prop(props, "randomize_target")
        if not props.randomize_target:
            box_rev.prop(props, "reveal_target")
        box_rev.prop(props, "suspense_duration")
        box_rev.prop(props, "reveal_height")
        box_rev.prop(props, "reveal_tilt")
        box_rev.prop(props, "prize_z_offset")

        # 11. Storyboard Presentation Box
        box_story = layout.box()
        box_story.label(text="Storyboard & Game Presentation", icon='SCENE')
        box_story.prop(props, "show_intro_reveal", text="Show Ball First (Intro Lift)")
        if props.show_intro_reveal:
            box_story.prop(props, "intro_lift_duration", text="Intro Lift Duration")
        box_story.prop(props, "create_text_banner", text="Generate 3D Stadium Banner")
        if props.create_text_banner:
            box_story.prop(props, "banner_intro_text", text="Intro Text")
            box_story.prop(props, "banner_shuffle_text", text="Shuffle Text")
            box_story.prop(props, "banner_reveal_text", text="Reveal Text")

        # 12. After Effects & Audio Cue Sheet Bridge
        box_cue = layout.box()
        box_cue.label(text="After Effects & Audio Cue Sheet", icon='OUTPUT')
        box_cue.operator("wolfpack.export_cue_sheet", text="Export AE Cue Sheet (.json & .csv)", icon='EXPORT')

        layout.separator()
        btn = layout.operator("wolfpack.generate_shuffle", text="Generate Wolfpack Shuffle Animation", icon='PLAY')


classes = (
    WolfpackShuffleProperties,
    WOLFPACK_OT_generate_shuffle,
    WOLFPACK_OT_setup_demo,
    WOLFPACK_OT_link_selected,
    WOLFPACK_OT_import_model,
    WOLFPACK_OT_setup_atmosphere,
    WOLFPACK_OT_setup_goalposts,
    WOLFPACK_OT_generate_stinger,
    WOLFPACK_OT_generate_entry_bumper,
    WOLFPACK_OT_export_cue_sheet,
    WOLFPACK_PT_sidebar_panel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.wolfpack_shuffle = bpy.props.PointerProperty(type=WolfpackShuffleProperties)

def unregister():
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except Exception:
            pass
    if hasattr(bpy.types.Scene, "wolfpack_shuffle"):
        try:
            del bpy.types.Scene.wolfpack_shuffle
        except Exception:
            pass

# Standalone execution support: when run directly in Blender's Scripting Editor
if __name__ == "__main__":
    try:
        unregister()
    except Exception:
        pass
    register()
    print("[Wolfpack Glory] Plugin loaded and registered in View3D Sidebar > 'Wolfpack Shuffle'!")
