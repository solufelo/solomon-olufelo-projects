#include "core/Application.h"

namespace ly
{
    Application::Application(unsigned int windowWidth, unsigned int windowHeight,
                             const std::string& title)
        : mWindow{ sf::VideoMode({windowWidth, windowHeight}), title },
          mTargetFrameRate{ 60.f },
          mTickClock{}
    {
    }

    void Application::Run()
    {
        mTickClock.restart();
        float accumulatedTime = 0.f;
        const float targetDeltaTime = 1.f / mTargetFrameRate;

        while (mWindow.isOpen())
        {
            while (const std::optional event = mWindow.pollEvent())
            {
                if (event->is<sf::Event::Closed>())
                {
                    mWindow.close();
                }
            }

            accumulatedTime += mTickClock.restart().asSeconds();
            while (accumulatedTime > targetDeltaTime)
            {
                accumulatedTime -= targetDeltaTime;
                TickInternal(targetDeltaTime);
            }
            RenderInternal();
        }
    }

    void Application::TickInternal(float deltaTime)
    {
        // Phase 2: world->Tick(deltaTime)
        (void)deltaTime;
    }

    void Application::RenderInternal()
    {
        mWindow.clear(sf::Color{ 10, 10, 26 }); // deep space, not pure black
        // Phase 2: world->Render(mWindow)
        mWindow.display();
    }
}
