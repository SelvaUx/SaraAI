#pragma once

#include <string>
#include <vector>
#include <memory>
#include <functional>

namespace SaraAI {
namespace Speech {

/**
 * Speech recognition result structure
 */
struct SpeechResult {
    std::string text;           // Recognized text
    float confidence;           // Confidence score (0.0 - 1.0)
    bool is_final;             // Whether this is a final result or partial
    double timestamp;          // Timestamp when speech was detected
    
    SpeechResult() : confidence(0.0f), is_final(false), timestamp(0.0) {}
    SpeechResult(const std::string& txt, float conf, bool final = true) 
        : text(txt), confidence(conf), is_final(final), timestamp(0.0) {}
};

/**
 * Audio configuration
 */
struct AudioConfig {
    int sample_rate = 16000;    // Sample rate in Hz
    int channels = 1;           // Number of channels (mono/stereo)
    int bits_per_sample = 16;   // Bits per sample
    size_t buffer_size = 4096;  // Buffer size in samples
    
    AudioConfig() = default;
    AudioConfig(int rate, int ch, int bits) 
        : sample_rate(rate), channels(ch), bits_per_sample(bits) {}
};

/**
 * Speech recognition configuration
 */
struct SpeechConfig {
    std::string model_path;         // Path to the model file
    std::string language = "en";    // Language code
    float min_confidence = 0.5f;    // Minimum confidence threshold
    bool enable_partial_results = true;  // Enable partial results
    int max_silence_ms = 2000;      // Max silence before ending recognition
    
    SpeechConfig() = default;
    SpeechConfig(const std::string& model, const std::string& lang = "en") 
        : model_path(model), language(lang) {}
};

/**
 * Callback function type for speech results
 */
using SpeechCallback = std::function<void(const SpeechResult&)>;

/**
 * Abstract base class for speech-to-text engines
 */
class STTEngine {
public:
    virtual ~STTEngine() = default;
    
    /**
     * Initialize the speech recognition engine
     * @param config Speech configuration
     * @param audio_config Audio configuration
     * @return true if initialization successful
     */
    virtual bool initialize(const SpeechConfig& config, const AudioConfig& audio_config) = 0;
    
    /**
     * Start continuous speech recognition
     * @param callback Function to call when speech is recognized
     * @return true if started successfully
     */
    virtual bool start_recognition(SpeechCallback callback) = 0;
    
    /**
     * Stop speech recognition
     */
    virtual void stop_recognition() = 0;
    
    /**
     * Process audio data directly
     * @param audio_data Raw audio data
     * @param length Length of audio data in bytes
     * @return Speech result (may be partial)
     */
    virtual SpeechResult process_audio(const uint8_t* audio_data, size_t length) = 0;
    
    /**
     * Check if the engine is currently recognizing
     * @return true if actively recognizing
     */
    virtual bool is_recognizing() const = 0;
    
    /**
     * Get the name of the engine
     * @return Engine name
     */
    virtual std::string get_engine_name() const = 0;
    
    /**
     * Get supported languages
     * @return Vector of language codes
     */
    virtual std::vector<std::string> get_supported_languages() const = 0;
};

/**
 * Factory function to create STT engines
 */
enum class STTEngineType {
    WHISPER_CPP,
    VOSK,
    DUMMY  // For testing
};

/**
 * Create a speech recognition engine
 * @param type Type of engine to create
 * @return Unique pointer to the engine, or nullptr if creation failed
 */
std::unique_ptr<STTEngine> create_stt_engine(STTEngineType type);

/**
 * Get available engine types
 * @return Vector of available engine types
 */
std::vector<STTEngineType> get_available_engines();

/**
 * Convert engine type to string
 * @param type Engine type
 * @return String representation
 */
std::string engine_type_to_string(STTEngineType type);

} // namespace Speech
} // namespace SaraAI