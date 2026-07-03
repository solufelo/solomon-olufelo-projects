cmake_minimum_required(VERSION 3.21)

project(LightYears
    VERSION 0.1.0
    DESCRIPTION "Space shooter built with SFML"
    LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Dependencies via vcpkg manifest (vcpkg.json)
find_package(SFML COMPONENTS Graphics Window System CONFIG REQUIRED)

add_executable(LightYears
    src/main.cpp
    src/core/Application.cpp
)

target_include_directories(LightYears PRIVATE src)

target_link_libraries(LightYears PRIVATE
    SFML::Graphics
    SFML::Window
    SFML::System
)

if(MSVC)
    target_compile_options(LightYears PRIVATE /W4)
else()
    target_compile_options(LightYears PRIVATE -Wall -Wextra)
endif()

# Copy assets next to the binary (folder exists from day one, fills up later)
add_custom_command(TARGET LightYears POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_directory_if_different
        ${CMAKE_SOURCE_DIR}/assets $<TARGET_FILE_DIR:LightYears>/assets
)
