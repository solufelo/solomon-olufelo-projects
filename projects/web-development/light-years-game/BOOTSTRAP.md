# Toolchain Bootstrap — COMPLETE (2026-06-11)

Installed on this machine. Keep for reference if you rebuild from scratch.

```powershell
# 1. Git
winget install --id Git.Git -e --accept-source-agreements --accept-package-agreements

# 2. CMake
winget install --id Kitware.CMake -e

# 3. Visual Studio 2022 Build Tools with C++ workload (the big one, ~7GB)
winget install --id Microsoft.VisualStudio.2022.BuildTools -e --override "--quiet --add Microsoft.VisualStudio.Workload.VCTools --includeRecommended"

# 4. vcpkg
git clone https://github.com/microsoft/vcpkg C:\Tools\vcpkg
C:\Tools\vcpkg\bootstrap-vcpkg.bat
setx VCPKG_ROOT C:\Tools\vcpkg

# 5. Wire this folder to the GitHub repo (history lives there)
cd C:\Users\Administrator\Projects\light-years-game
git init
git remote add origin https://github.com/solufelo/light-years-game.git
git fetch origin
git checkout -b main
# (resolve README conflict in favor of the new one, then first commit)

# 6. First build
cmake --preset default
cmake --build --preset default
.\build\Debug\LightYears.exe   # -> deep-space window, 60Hz fixed-timestep loop
```
