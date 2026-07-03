# Light Years — C++ to WebAssembly Game Engine (Work in Progress) 🚀

A C++ 2D space shooter and custom game engine designed to compile directly to **WebAssembly (WASM)** via **Emscripten** for instant browser-playable deployment.

> [!NOTE]
> **Project Status:** This repository is the **current active focus of development**. The primary goal is compiling the native fixed-timestep game loop into a true desktop executable (`.exe`) and deploying the compiled Emscripten WebAssembly web build. Once these milestones are complete, active development will shift to the **Creative Engine** operating system.

Currently completed features:
- **Custom Fixed-Timestep Loop:** Decouples execution physics simulation from rendering frame rate, ensuring deterministic actor ticks on all monitors (60Hz to 380Hz).
- **Desktop Window Context:** Native window initialization and clear/draw loop.
- **CMake Build System:** Configured for automated compiler preset builds.

---

## 🎯 Architecture & Target Features (Roadmap)

*   **Custom Fixed-Timestep Loop (Completed):** Decouples execution physics simulation from rendering frame rate, ensuring deterministic actor ticks on all monitors (60Hz to 380Hz).
*   **WebAssembly Compile Target (Planned):** Toolchain integration using `emscripten` to target HTML5 Canvas.
*   **Asset Management Pool (Planned):** Cached asset loader to manage texture loading, sound effects, and fonts cleanly, avoiding redundant memory overhead.
*   **Entity / Actor System (Planned):** Low-level object-oriented hierarchy for rendering transforms and coordinate ticking.
*   **Object Pooling (Planned):** Prevents heap allocation overhead during high-frequency projectile/particle spawns.

---

## 🛠️ Build Prerequisites

### Native Desktop Build
*   **Compiler:** Visual Studio 2022 Build Tools (with C++ workload) or GCC/Clang on Unix.
*   **Build Tool:** CMake 3.21+
*   **Package Manager:** vcpkg (`VCPKG_ROOT` environment variable configured)

```bash
# Setup build preset and compile
cmake --preset default
cmake --build --preset default

# Run the executable
.\build\Debug\LightYears.exe
```

### WebAssembly (Emscripten) Build
*   **SDK:** Emscripten SDK (`emsdk` initialized in environment)

```bash
# Compile via emscripten presets
emcmake cmake -B build-wasm -DPLATFORM=WASM
cmake --build build-wasm
```

---

## 📁 Repository Structure

```
light-years-game/
├── engine/              # Core engine: tick loops, entity containers, pools, timers
├── game/                # Game logic: player ships, enemy waves, projectile models
├── platform/
│   ├── desktop/         # Native Raylib graphics context & window initialization
│   └── wasm/            # Emscripten HTML shell, preloaded assets, canvas mapping
├── assets/              # Fonts, audio files, textures
└── CMakeLists.txt       # Build compilation directives
```

---

## 🏁 Migration Roadmap

- [x] **Phase 1:** SFML Native Desktop Scaffold, Fixed Game Loop, CMake CI (Done - archived as reference).
- [ ] **Phase 2:** Port core Window & Tick loops to Raylib desktop context.
- [ ] **Phase 3:** Port Actor, World, and Asset Pool architecture.
- [ ] **Phase 4:** Player input, projectile firing, and high-frequency Object Pooling.
- [ ] **Phase 5:** Integrate Emscripten SDK compiler bindings (`emcc` / `emcmake`).
- [ ] **Phase 6:** Build WASM shell + asset preloading pipeline, compile native `.exe` build, and deploy live web demo.
- [ ] **Phase 7:** Polish mechanics, finalize documentation, and transition development focus to the **Creative Engine** SaaS platform.

---

## ⚠️ Learn-First Discipline
This engine is built step-by-step following the **Learn-First** coding protocol. Every function, coordinate transformation, and memory allocator is hand-written, explained closed-book, and audited to guarantee full technical ownership. No template-dumping or unverified code blocks.
