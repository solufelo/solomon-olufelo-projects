"""
Laurier Football Shell Game Addon
=================================

Blender addon for creating automated 3D shell game shuffle animations
for Laurier Football promotional content.

Author: Solomon Olufelo
Version: 1.0.0
Compatible: Blender 4.x
"""

import bpy
from . import laurier_shell_game

def register():
    """Register the addon."""
    laurier_shell_game.register_properties()
    bpy.utils.register_class(laurier_shell_game.LaurierShellGameOperator)
    bpy.utils.register_class(laurier_shell_game.LaurierShellGamePanel)

def unregister():
    """Unregister the addon."""
    bpy.utils.unregister_class(laurier_shell_game.LaurierShellGamePanel)
    bpy.utils.unregister_class(laurier_shell_game.LaurierShellGameOperator)
    laurier_shell_game.unregister_properties()

if __name__ == "__main__":
    register()
