#include <iostream>
#include <memory>
#include <string>
#include <csignal>
#include <thread>
#include <chrono>

#include "speech_server.h"
#include "stt_interface.h"

using namespace SaraAI::Speech;

// Global server instance for signal handling
std::unique_ptr<SpeechServer> g_server;

void signal_handler(int signal) {
    std::cout << "\nReceived signal " << signal << ". Shutting down gracefully...\n";
    if (g_server) {
        g_server->stop();
    }
}

void print_usage(const char* program_name) {
    std::cout << "Usage: " << program_name << " [options]\n"
              << "Options:\n"
              << "  --port <port>       Port to listen on (default: 8001)\n"
              << "  --host <host>       Host to bind to (default: localhost)\n"
              << "  --engine <engine>   STT engine to use (whisper/vosk/dummy)\n"
              << "  --model <path>      Path to model file\n"
              << "  --language <lang>   Language code (default: en)\n"
              << "  --help              Show this help message\n";
}

int main(int argc, char* argv[]) {
    std::cout << "🎙️ SaraAI Speech Recognition Module v1.0\n";
    std::cout << "==========================================\n\n";
    
    // Default configuration
    std::string host = "localhost";
    int port = 8001;
    STTEngineType engine_type = STTEngineType::DUMMY;
    std::string model_path;
    std::string language = "en";
    
    // Parse command line arguments
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        
        if (arg == "--help") {
            print_usage(argv[0]);
            return 0;
        }
        else if (arg == "--port" && i + 1 < argc) {
            port = std::stoi(argv[++i]);
        }
        else if (arg == "--host" && i + 1 < argc) {
            host = argv[++i];
        }
        else if (arg == "--engine" && i + 1 < argc) {
            std::string engine = argv[++i];
            if (engine == "whisper") {
                engine_type = STTEngineType::WHISPER_CPP;
            } else if (engine == "vosk") {
                engine_type = STTEngineType::VOSK;
            } else if (engine == "dummy") {
                engine_type = STTEngineType::DUMMY;
            } else {
                std::cerr << "Unknown engine type: " << engine << std::endl;
                return 1;
            }
        }
        else if (arg == "--model" && i + 1 < argc) {
            model_path = argv[++i];
        }
        else if (arg == "--language" && i + 1 < argc) {
            language = argv[++i];
        }
        else {
            std::cerr << "Unknown argument: " << arg << std::endl;
            print_usage(argv[0]);
            return 1;
        }
    }
    
    // Show configuration
    std::cout << "Configuration:\n";
    std::cout << "  Host: " << host << "\n";
    std::cout << "  Port: " << port << "\n";
    std::cout << "  Engine: " << engine_type_to_string(engine_type) << "\n";
    std::cout << "  Language: " << language << "\n";
    if (!model_path.empty()) {
        std::cout << "  Model: " << model_path << "\n";
    }
    std::cout << "\n";
    
    try {
        // Create STT engine
        auto stt_engine = create_stt_engine(engine_type);
        if (!stt_engine) {
            std::cerr << "❌ Failed to create STT engine: " << engine_type_to_string(engine_type) << std::endl;
            return 1;
        }
        
        // Configure the engine
        SpeechConfig speech_config;
        speech_config.model_path = model_path;
        speech_config.language = language;
        speech_config.min_confidence = 0.5f;
        
        AudioConfig audio_config;
        audio_config.sample_rate = 16000;
        audio_config.channels = 1;
        audio_config.bits_per_sample = 16;
        
        if (!stt_engine->initialize(speech_config, audio_config)) {
            std::cerr << "❌ Failed to initialize STT engine" << std::endl;
            return 1;
        }
        
        std::cout << "✅ STT engine initialized successfully\n";
        
        // Create and configure the speech server
        g_server = std::make_unique<SpeechServer>(std::move(stt_engine));
        
        // Setup signal handlers
        std::signal(SIGINT, signal_handler);
        std::signal(SIGTERM, signal_handler);
        
        // Start the server
        std::cout << "🚀 Starting speech recognition server...\n";
        if (!g_server->start(host, port)) {
            std::cerr << "❌ Failed to start server on " << host << ":" << port << std::endl;
            return 1;
        }
        
        std::cout << "✨ Speech recognition server is running!\n";
        std::cout << "   API endpoint: http://" << host << ":" << port << "\n";
        std::cout << "   Health check: http://" << host << ":" << port << "/health\n";
        std::cout << "   Speech recognition: POST http://" << host << ":" << port << "/recognize\n\n";
        std::cout << "Press Ctrl+C to stop the server.\n\n";
        
        // Keep the server running
        g_server->wait_for_shutdown();
        
        std::cout << "🛑 Server stopped.\n";
        
    } catch (const std::exception& e) {
        std::cerr << "❌ Exception: " << e.what() << std::endl;
        return 1;
    } catch (...) {
        std::cerr << "❌ Unknown exception occurred" << std::endl;
        return 1;
    }
    
    std::cout << "👋 Goodbye!\n";
    return 0;
}