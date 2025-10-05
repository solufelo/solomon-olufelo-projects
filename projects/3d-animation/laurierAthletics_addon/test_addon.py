"""
Test Script for Laurier Football Shell Game Addon
=================================================

This script validates the addon installation and tests core functionality.
Run this in Blender's scripting workspace to verify everything is working.

Usage:
1. Open Blender Scripting workspace
2. Load this test script
3. Run the script (Alt+P)
4. Check console output for results

Author: Solomon Olufelo
Created: 2024
"""

import bpy
import sys
import traceback

def test_addon_registration():
    """Test if the addon is properly registered."""
    print("🧪 Testing addon registration...")
    
    try:
        # Check if addon is enabled
        addon_name = "Laurier Football Shell Game"
        addon_module = "laurier_football_shell_game"
        
        if addon_module in bpy.context.preferences.addons:
            print("✅ Addon is registered and enabled")
            return True
        else:
            print("❌ Addon is not registered or enabled")
            return False
    except Exception as e:
        print(f"❌ Error checking addon registration: {e}")
        return False

def test_operator_exists():
    """Test if the main operator exists."""
    print("🧪 Testing operator existence...")
    
    try:
        operator_id = "laurier.create_shell_game"
        if hasattr(bpy.ops, 'laurier'):
            if hasattr(bpy.ops.laurier, 'create_shell_game'):
                print("✅ Main operator exists")
                return True
        print("❌ Main operator not found")
        return False
    except Exception as e:
        print(f"❌ Error checking operator: {e}")
        return False

def test_property_group():
    """Test if property group is accessible."""
    print("🧪 Testing property group...")
    
    try:
        scene = bpy.context.scene
        if hasattr(scene, 'laurier_shell_game'):
            props = scene.laurier_shell_game
            # Test accessing some properties
            duration = props.duration_sec
            fps = props.fps
            print("✅ Property group accessible")
            return True
        else:
            print("❌ Property group not found in scene")
            return False
    except Exception as e:
        print(f"❌ Error checking property group: {e}")
        return False

def test_ui_panel():
    """Test if UI panel can be found."""
    print("🧪 Testing UI panel...")
    
    try:
        # Check if panel class exists
        panel_classes = [cls for cls in bpy.types.Panel.__subclasses__() 
                        if 'laurier' in cls.bl_idname.lower()]
        
        if panel_classes:
            print("✅ UI panel classes found")
            return True
        else:
            print("❌ UI panel classes not found")
            return False
    except Exception as e:
        print(f"❌ Error checking UI panel: {e}")
        return False

def create_test_scene():
    """Create a minimal test scene with required objects."""
    print("🧪 Creating test scene...")
    
    try:
        # Clear existing mesh objects
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False, confirm=False)
        
        # Create required empty objects
        empties = []
        for i in range(1, 4):
            bpy.ops.object.empty_add(type='PLAIN_AXES', location=(i-2, 0, 0))
            empty = bpy.context.active_object
            empty.name = f"Empty_{i}"
            empties.append(empty)
        
        # Create football control empty
        bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
        football_ctrl = bpy.context.active_object
        football_ctrl.name = "Football_CTRL"
        
        # Create simple helmet objects (cubes for testing)
        helmets = []
        for i, empty in enumerate(empties):
            bpy.ops.mesh.primitive_cube_add(size=1, location=empty.location)
            helmet = bpy.context.active_object
            helmet.name = f"Helmet_{i+1}"
            helmet.scale = (1.2, 0.8, 0.6)  # Make it helmet-like
            helmets.append(helmet)
        
        # Create football object
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.3, location=football_ctrl.location)
        football = bpy.context.active_object
        football.name = "Football"
        
        # Set up parenting relationships
        for i, (helmet, empty) in enumerate(zip(helmets, empties)):
            helmet.parent = empty
            helmet.parent_type = 'OBJECT'
        
        football.parent = football_ctrl
        football.parent_type = 'OBJECT'
        
        print("✅ Test scene created successfully")
        print(f"   Created {len(empties)} helmet empties")
        print(f"   Created {len(helmets)} helmet objects")
        print(f"   Created football and control empty")
        print(f"   Set up parenting relationships")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating test scene: {e}")
        traceback.print_exc()
        return False

def test_animation_creation():
    """Test creating a short animation."""
    print("🧪 Testing animation creation...")
    
    try:
        # Get scene properties
        scene = bpy.context.scene
        if not hasattr(scene, 'laurier_shell_game'):
            print("❌ Property group not available")
            return False
        
        props = scene.laurier_shell_game
        
        # Set up for quick test
        props.duration_sec = 2.0  # Short test
        props.fps = 12  # Low FPS for speed
        props.preset = 'QUICK_SNAPPY'
        
        # Try to run the operator
        result = bpy.ops.laurier.create_shell_game()
        
        if 'FINISHED' in result:
            print("✅ Animation creation successful")
            return True
        else:
            print(f"❌ Animation creation failed: {result}")
            return False
            
    except Exception as e:
        print(f"❌ Error during animation creation: {e}")
        traceback.print_exc()
        return False

def test_presets():
    """Test preset configurations."""
    print("🧪 Testing preset configurations...")
    
    try:
        scene = bpy.context.scene
        props = scene.laurier_shell_game
        
        presets = ['QUICK_SNAPPY', 'DRAMATIC_SLOW', 'SOCIAL_MEDIA', 
                  'BROADCAST_QUALITY', 'MINIMAL_CLEAN', 'HIGH_ENERGY']
        
        for preset in presets:
            props.preset = preset
            # Just test that preset can be set (actual application happens in operator)
            if props.preset == preset:
                print(f"✅ Preset '{preset}' can be set")
            else:
                print(f"❌ Preset '{preset}' failed to set")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing presets: {e}")
        return False

def run_all_tests():
    """Run all tests and provide summary."""
    print("🏈 Laurier Football Shell Game Addon - Test Suite")
    print("=" * 60)
    
    tests = [
        ("Addon Registration", test_addon_registration),
        ("Operator Existence", test_operator_exists),
        ("Property Group", test_property_group),
        ("UI Panel", test_ui_panel),
        ("Test Scene Creation", create_test_scene),
        ("Preset Configurations", test_presets),
        ("Animation Creation", test_animation_creation),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}")
        print("-" * 40)
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Test crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Addon is working correctly.")
        print("\nNext steps:")
        print("1. Open 3D Viewport sidebar (press N)")
        print("2. Look for 'Laurier Football' tab")
        print("3. Start creating animations!")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
        print("\nTroubleshooting:")
        print("1. Ensure addon is properly installed and enabled")
        print("2. Check Blender version (4.5+ required)")
        print("3. Restart Blender and try again")
        print("4. Check console for detailed error messages")

def main():
    """Main test function."""
    try:
        run_all_tests()
    except Exception as e:
        print(f"❌ Test suite crashed: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()
