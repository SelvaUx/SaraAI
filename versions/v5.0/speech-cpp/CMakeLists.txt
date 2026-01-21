cmake_minimum_required(VERSION 3.16)
project(SaraAI_Speech VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find packages
find_package(PkgConfig REQUIRED)

# Options for different speech recognition backends
option(USE_WHISPER_CPP "Use Whisper.cpp for speech recognition" ON)
option(USE_VOSK "Use Vosk for speech recognition" OFF)

# Include directories
include_directories(include)

# Source files
set(SOURCES
    src/speech_server.cpp
    src/audio_capture.cpp
    src/speech_processor.cpp
    src/main.cpp
)

# Headers
set(HEADERS
    include/speech_server.h
    include/audio_capture.h
    include/speech_processor.h
    include/stt_interface.h
)

# Create executable
add_executable(saraai_speech ${SOURCES})

# Platform-specific settings
if(WIN32)
    # Windows-specific settings
    target_compile_definitions(saraai_speech PRIVATE WIN32_LEAN_AND_MEAN)
    
    # Link Windows audio libraries
    target_link_libraries(saraai_speech 
        winmm
        ws2_32
        wsock32
    )
elseif(UNIX)
    # Linux-specific settings
    find_package(PkgConfig REQUIRED)
    
    # Find ALSA for audio
    pkg_check_modules(ALSA REQUIRED alsa)
    target_link_libraries(saraai_speech ${ALSA_LIBRARIES})
    target_include_directories(saraai_speech PRIVATE ${ALSA_INCLUDE_DIRS})
    
    # Find pthread
    find_package(Threads REQUIRED)
    target_link_libraries(saraai_speech Threads::Threads)
endif()

# HTTP server library (simple built-in server)
set(HTTP_SOURCES
    src/http_server.cpp
)
target_sources(saraai_speech PRIVATE ${HTTP_SOURCES})

# Conditional compilation for speech engines
if(USE_WHISPER_CPP)
    target_compile_definitions(saraai_speech PRIVATE USE_WHISPER_CPP)
    
    # TODO: Add Whisper.cpp as submodule or find_package
    # For now, we'll create placeholder implementation
    target_sources(saraai_speech PRIVATE src/whisper_backend.cpp)
endif()

if(USE_VOSK)
    target_compile_definitions(saraai_speech PRIVATE USE_VOSK)
    
    # TODO: Find Vosk library
    # For now, we'll create placeholder implementation  
    target_sources(saraai_speech PRIVATE src/vosk_backend.cpp)
endif()

# Compiler flags
if(MSVC)
    target_compile_options(saraai_speech PRIVATE /W4)
else()
    target_compile_options(saraai_speech PRIVATE -Wall -Wextra -Wpedantic)
endif()

# Build type specific flags
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    target_compile_definitions(saraai_speech PRIVATE DEBUG)
else()
    target_compile_definitions(saraai_speech PRIVATE NDEBUG)
endif()

# Installation
install(TARGETS saraai_speech 
    RUNTIME DESTINATION bin
)

# Copy configuration files
install(FILES config/speech_config.json
    DESTINATION config
    OPTIONAL
)

# Print build information
message(STATUS "SaraAI Speech Module Configuration:")
message(STATUS "  Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS "  C++ standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "  Use Whisper.cpp: ${USE_WHISPER_CPP}")
message(STATUS "  Use Vosk: ${USE_VOSK}")
message(STATUS "  Install prefix: ${CMAKE_INSTALL_PREFIX}")