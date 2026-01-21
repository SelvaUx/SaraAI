package com.saraai.tts;

import javax.speech.Central;
import javax.speech.synthesis.Synthesizer;
import javax.speech.synthesis.SynthesizerModeDesc;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class TTSService {

    private static final Logger logger = LoggerFactory.getLogger(TTSService.class);
    private final TTSEngineConfig config;
    private Synthesizer synthesizer;

    public TTSService(TTSEngineConfig config) {
        this.config = config;
        initialize();
    }

    private void initialize() {
        try {
            logger.info("Initializing TTS engine with type: {}", config.getEngineType());
            
            // Set up the synthesizer
            System.setProperty("freetts.voices", "com.sun.speech.freetts.en.us.cmu_us_kal.KevinVoiceDirectory");
            Central.registerEngineCentral("com.sun.speech.freetts.jsapi.FreeTTSEngineCentral");
            synthesizer = Central.createSynthesizer(new SynthesizerModeDesc(java.util.Locale.US));

            if (synthesizer == null) {
                logger.error("Cannot create a synthesizer. Please check your configuration.");
                System.exit(1);
            }

            synthesizer.allocate();
            synthesizer.resume();

            // Set voice properties from config
            // Note: Voice selection would be more complex in a real application
            
            logger.info("TTS engine initialized successfully.");
            
        } catch (Exception e) {
            logger.error("Failed to initialize TTS engine: {}", e.getMessage(), e);
        }
    }

    public void speak(String text) {
        if (synthesizer == null) {
            logger.error("TTS synthesizer is not initialized. Cannot speak.");
            return;
        }
        
        try {
            logger.info("Speaking: '{}'", text);
            synthesizer.speakPlainText(text, null);
            synthesizer.waitEngineState(Synthesizer.QUEUE_EMPTY);
        } catch (Exception e) {
            logger.error("Error during speech synthesis: {}", e.getMessage(), e);
        }
    }
}
