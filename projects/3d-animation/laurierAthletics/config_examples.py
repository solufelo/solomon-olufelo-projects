"""
Configuration Examples for Laurier Shell Game Animation
======================================================

This file contains different configuration presets for various animation styles.
Copy the desired CONFIG dictionary into the main script to use different effects.

Author: Solomon Olufelo
Created: 2024
"""

# ============================================================================
# PRESET CONFIGURATIONS
# ============================================================================

# Quick and Snappy (5 seconds, fast shuffle)
QUICK_SNAPPY = {
    "duration_sec": 5.0,
    "fps": 24,
    "shuffle_speed": 3.0,
    "shuffle_cycles": 3,
    "shuffle_amplitude": 1.5,
    "vertical_bounce": 0.2,
    "spacing_buffer": 1.2,
    "reveal_target": 2,
    "reveal_duration": 1.0,
    "reveal_height": 0.8,
    "camera_sway": True,
    "sway_amount": 0.05,
    "ease_out": True,
    "ease_duration": 0.8,
    "randomize_target": True,
    "add_dust_effects": False,
}

# Dramatic and Slow (12 seconds, cinematic feel)
DRAMATIC_SLOW = {
    "duration_sec": 12.0,
    "fps": 24,
    "shuffle_speed": 1.2,
    "shuffle_cycles": 6,
    "shuffle_amplitude": 3.0,
    "vertical_bounce": 0.5,
    "spacing_buffer": 2.0,
    "reveal_target": 1,
    "reveal_duration": 2.5,
    "reveal_height": 1.5,
    "camera_sway": True,
    "sway_amount": 0.15,
    "ease_out": True,
    "ease_duration": 2.0,
    "randomize_target": False,
    "add_dust_effects": False,
}

# Social Media Style (3 seconds, energetic)
SOCIAL_MEDIA = {
    "duration_sec": 3.0,
    "fps": 30,
    "shuffle_speed": 4.0,
    "shuffle_cycles": 2,
    "shuffle_amplitude": 1.0,
    "vertical_bounce": 0.4,
    "spacing_buffer": 1.0,
    "reveal_target": 3,
    "reveal_duration": 0.8,
    "reveal_height": 1.2,
    "camera_sway": True,
    "sway_amount": 0.2,
    "ease_out": False,
    "ease_duration": 0.5,
    "randomize_target": True,
    "add_dust_effects": False,
}

# Broadcast Quality (8 seconds, professional)
BROADCAST_QUALITY = {
    "duration_sec": 8.0,
    "fps": 24,
    "shuffle_speed": 2.0,
    "shuffle_cycles": 4,
    "shuffle_amplitude": 2.0,
    "vertical_bounce": 0.3,
    "spacing_buffer": 1.5,
    "reveal_target": 2,
    "reveal_duration": 1.5,
    "reveal_height": 1.0,
    "camera_sway": True,
    "sway_amount": 0.1,
    "ease_out": True,
    "ease_duration": 1.0,
    "randomize_target": True,
    "add_dust_effects": False,
}

# Minimal and Clean (6 seconds, subtle)
MINIMAL_CLEAN = {
    "duration_sec": 6.0,
    "fps": 24,
    "shuffle_speed": 1.5,
    "shuffle_cycles": 3,
    "shuffle_amplitude": 1.2,
    "vertical_bounce": 0.1,
    "spacing_buffer": 1.8,
    "reveal_target": 1,
    "reveal_duration": 1.2,
    "reveal_height": 0.6,
    "camera_sway": False,
    "sway_amount": 0.0,
    "ease_out": True,
    "ease_duration": 1.5,
    "randomize_target": False,
    "add_dust_effects": False,
}

# High Energy (4 seconds, fast and bouncy)
HIGH_ENERGY = {
    "duration_sec": 4.0,
    "fps": 30,
    "shuffle_speed": 3.5,
    "shuffle_cycles": 3,
    "shuffle_amplitude": 1.8,
    "vertical_bounce": 0.6,
    "spacing_buffer": 1.3,
    "reveal_target": 3,
    "reveal_duration": 1.0,
    "reveal_height": 1.4,
    "camera_sway": True,
    "sway_amount": 0.25,
    "ease_out": False,
    "ease_duration": 0.5,
    "randomize_target": True,
    "add_dust_effects": False,
}

# ============================================================================
# CUSTOMIZATION TEMPLATES
# ============================================================================

# Template for creating your own configuration
CUSTOM_TEMPLATE = {
    # Animation timing
    "duration_sec": 8.0,           # Total animation duration
    "fps": 24,                     # Frames per second (24 for film, 30 for video)
    "shuffle_speed": 2.0,          # Speed of shuffle movements (1.0-5.0)
    "shuffle_cycles": 4,           # Number of shuffle cycles (2-8)
    
    # Movement parameters
    "shuffle_amplitude": 2.0,      # Horizontal movement range (0.5-4.0)
    "vertical_bounce": 0.3,        # Vertical bounce height (0.0-1.0)
    "spacing_buffer": 1.5,         # Minimum distance between helmets (1.0-3.0)
    
    # Reveal settings
    "reveal_target": 2,            # Which helmet (1, 2, or 3) hides football
    "reveal_duration": 1.5,        # Reveal animation duration (0.5-3.0)
    "reveal_height": 1.0,          # How high helmet lifts (0.5-2.0)
    
    # Camera and effects
    "camera_sway": True,           # Add camera movement (True/False)
    "sway_amount": 0.1,            # Camera sway intensity (0.0-0.3)
    "ease_out": True,              # Slow down before reveal (True/False)
    "ease_duration": 1.0,          # Ease-out duration (0.5-2.0)
    
    # Randomization
    "randomize_target": True,      # Random football location (True/False)
    "add_dust_effects": False,     # Particle effects (True/False, v2 feature)
}

# ============================================================================
# PARAMETER GUIDES
# ============================================================================

PARAMETER_GUIDES = {
    "duration_sec": {
        "description": "Total animation duration in seconds",
        "recommended_range": "3.0 - 15.0",
        "notes": "Shorter for social media, longer for broadcast"
    },
    "fps": {
        "description": "Frames per second for animation",
        "recommended_values": "24 (film), 30 (video), 60 (smooth)",
        "notes": "Higher FPS = smoother but larger files"
    },
    "shuffle_speed": {
        "description": "Speed of helmet shuffle movements",
        "recommended_range": "1.0 - 5.0",
        "notes": "Higher = faster shuffle, lower = more dramatic"
    },
    "shuffle_amplitude": {
        "description": "How far helmets move horizontally",
        "recommended_range": "0.5 - 4.0",
        "notes": "Larger = more dramatic movement, smaller = subtle"
    },
    "vertical_bounce": {
        "description": "Height of vertical bounce effect",
        "recommended_range": "0.0 - 1.0",
        "notes": "0.0 = no bounce, 1.0 = very bouncy"
    },
    "spacing_buffer": {
        "description": "Minimum distance between helmets",
        "recommended_range": "1.0 - 3.0",
        "notes": "Larger = more space, smaller = closer together"
    },
    "camera_sway": {
        "description": "Add subtle camera movement",
        "recommended_values": "True for dynamic feel, False for static",
        "notes": "Adds cinematic quality"
    },
    "sway_amount": {
        "description": "Intensity of camera sway",
        "recommended_range": "0.0 - 0.3",
        "notes": "0.0 = no sway, 0.3 = very noticeable"
    }
}

# ============================================================================
# USAGE INSTRUCTIONS
# ============================================================================

"""
HOW TO USE THESE CONFIGURATIONS:

1. Choose a preset that matches your needs:
   - QUICK_SNAPPY: For fast-paced content
   - DRAMATIC_SLOW: For cinematic promos
   - SOCIAL_MEDIA: For Instagram/TikTok
   - BROADCAST_QUALITY: For TV/web
   - MINIMAL_CLEAN: For subtle effects
   - HIGH_ENERGY: For exciting content

2. Copy the configuration into laurier_shell_game.py:
   - Replace the CONFIG dictionary at the top of the main script
   - Or modify the existing CONFIG with values from your chosen preset

3. Example usage:
   ```python
   # In laurier_shell_game.py, replace CONFIG with:
   CONFIG = QUICK_SNAPPY  # or any other preset
   ```

4. Customize further:
   - Use CUSTOM_TEMPLATE as a starting point
   - Refer to PARAMETER_GUIDES for detailed explanations
   - Test different values to find your perfect animation

5. Pro tips:
   - Start with a preset and make small adjustments
   - Test with shorter durations first (duration_sec: 3.0)
   - Use randomize_target: True for variety
   - Enable camera_sway for more dynamic shots
"""
