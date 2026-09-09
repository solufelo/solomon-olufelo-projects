"""
Laurier Athletics & Rockstar Games Spec - Comprehensive Addon Test Suite
========================================================================
Author: Solomon Olufelo (Tools & Pipeline Developer)
Version: 3.5.0 (AAA Studio Spec)

Usage:
  blender.exe -b --python test_addon.py
"""

import bpy
import sys
import os
import json
import time

def run_suite():
    print("=" * 70)
    print("  WOLFPACK GLORY v3.5.0 (ROCKSTAR GAMES SPEC) AUTOMATED TEST SUITE")
    print("=" * 70)

    # 1. Addon Registration Check
    print("[TEST 1] Addon Registration & Manifest Verification...")
    addon_name = "wolfpack_shuffle"
    if addon_name not in bpy.context.preferences.addons:
        try:
            bpy.ops.preferences.addon_enable(module=addon_name)
            print("  -> PASS: Addon registered and enabled from Blender preferences.")
        except Exception as e:
            print(f"  -> FAIL: Could not enable addon: {e}")
            return False
    else:
        print("  -> PASS: Addon is already active in preferences.")

    scene = bpy.context.scene
    props = getattr(scene, "wolfpack_shuffle", None)
    if not props:
        print("  -> FAIL: Scene.wolfpack_shuffle property group missing!")
        return False

    # 2. Verify Properties
    print("[TEST 2] Verifying Rockstar Studio Properties & UI Stages...")
    expected_props = [
        "last_bake_ms", "last_bake_keys", "last_bake_speed", "last_memory_mb",
        "show_motion_trajectories", "game_engine_target", "ui_tab",
        "bumper_layout_mode", "text_exit_style"
    ]
    for p in expected_props:
        assert hasattr(props, p), f"Missing property: {p}"
    print(f"  -> PASS: All {len(expected_props)} studio properties verified.")

    # 3. Setup Venue
    print("[TEST 3] Running wolfpack.setup_demo...")
    res_demo = bpy.ops.wolfpack.setup_demo()
    assert 'FINISHED' in res_demo, "setup_demo failed"
    print("  -> PASS: Venue scene spawned successfully.")

    # 4. Generate Shuffle with Telemetry Profiler
    print("[TEST 4] Running wolfpack.generate_shuffle with Real-Time Profiler...")
    props.num_swaps = 4
    props.prepend_entry_bumper = True
    props.bumper_lead_frames = 60
    props.show_motion_trajectories = True
    
    t0 = time.perf_counter()
    res_shuf = bpy.ops.wolfpack.generate_shuffle()
    assert 'FINISHED' in res_shuf, "generate_shuffle failed"
    
    print(f"  -> Telemetry Bake Duration: {props.last_bake_ms:.2f} ms")
    print(f"  -> Telemetry Keyframe Channels: {props.last_bake_keys} keys")
    print(f"  -> Telemetry Throughput: {props.last_bake_speed:.0f} keys/second")
    print(f"  -> Telemetry Memory Peak: +{props.last_memory_mb:.3f} MB")
    assert props.last_bake_ms > 0.0, "Telemetry execution time was 0"
    print("  -> PASS: Real-time telemetry profiling verified.")

    # 5. 3D Motion Trajectory Arcs
    print("[TEST 5] Verifying 3D Motion Trajectory Arcs in Viewport...")
    traj_obj = bpy.data.objects.get("Wolfpack_Motion_Trajectories")
    assert traj_obj is not None, "Missing Wolfpack_Motion_Trajectories object"
    assert len(traj_obj.data.splines) >= 3, f"Expected >= 3 splines, got {len(traj_obj.data.splines)}"
    assert len(traj_obj.data.materials) >= 3, f"Expected >= 3 materials, got {len(traj_obj.data.materials)}"
    print(f"  -> PASS: 3D Motion Arcs verified ({len(traj_obj.data.splines)} splines, {len(traj_obj.data.materials)} materials).")

    # 6. Game Engine Animation Track Exporter
    print("[TEST 6] Testing wolfpack.export_game_engine_anim...")
    res_anim = bpy.ops.wolfpack.export_game_engine_anim()
    assert 'FINISHED' in res_anim, "export_game_engine_anim failed"
    
    track_file = os.path.join(os.getcwd(), "wolfpack_anim_tracks.json")
    assert os.path.isfile(track_file), f"Track file not found: {track_file}"
    with open(track_file, "r", encoding="utf-8") as f:
        track_data = json.load(f)
    assert "actors" in track_data, "Missing actors"
    assert len(track_data["actors"]) >= 3, "Expected >= 3 actors"
    actor_one = list(track_data["actors"].values())[0]
    sample = actor_one["samples"][0]
    assert "quaternion_wxyz" in sample, "Missing quaternions"
    assert "velocity_vector" in sample, "Missing velocities"
    assert "position_game_engine" in sample, "Missing game engine Y-up"
    print(f"  -> PASS: AAA Game Engine Animation Track verified ({len(track_data['actors'])} actors, {track_data['metadata']['total_frames']} frames).")

    # 7. Telemetry Benchmark Export
    print("[TEST 7] Testing wolfpack.export_telemetry...")
    res_bench = bpy.ops.wolfpack.export_telemetry()
    assert 'FINISHED' in res_bench, "export_telemetry failed"
    bench_file = os.path.join(os.getcwd(), "wolfpack_telemetry_benchmark.json")
    assert os.path.isfile(bench_file), f"Benchmark file not found: {bench_file}"
    print("  -> PASS: Benchmark report verified.")

    # 8. Broadcast Cue Sheet Export
    print("[TEST 8] Testing wolfpack.export_cue_sheet...")
    res_cue = bpy.ops.wolfpack.export_cue_sheet()
    assert 'FINISHED' in res_cue, "export_cue_sheet failed"
    print("  -> PASS: SMPTE Cue Sheet export verified.")

    print("=" * 70)
    print("  ALL 8 TESTS PASSED (100% SUCCESS) - ROCKSTAR GAMES READY")
    print("=" * 70)
    return True

if __name__ == "__main__":
    if not run_suite():
        sys.exit(1)
