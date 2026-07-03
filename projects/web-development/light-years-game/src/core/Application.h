#pragma once

#include <SFML/Graphics.hpp>

namespace ly
{
    // Owns the window and runs the game loop.
    // Phase 1: fixed-timestep loop + render clear.
    // Phase 2 will grow: World ownership, actor ticking.
    class Application
    {
    public:
        Application(unsigned int windowWidth, unsigned int windowHeight,
                    const std::string& title);

        // Runs until the window closes. Fixed-timestep update, render as fast as allowed.
        void Run();

    private:
        void TickInternal(float deltaTime);
        void RenderInternal();

        sf::RenderWindow mWindow;
        float mTargetFrameRate;
        sf::Clock mTickClock;
    };
}
