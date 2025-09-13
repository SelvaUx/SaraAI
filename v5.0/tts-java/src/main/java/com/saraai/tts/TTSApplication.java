package com.saraai.tts;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * SaraAI Text-to-Speech Module
 * 
 * Main Spring Boot application for the TTS service.
 * Provides REST API endpoints for text-to-speech conversion.
 */
@SpringBootApplication
@ComponentScan(basePackages = "com.saraai.tts")
public class TTSApplication {

    private static final Logger logger = LoggerFactory.getLogger(TTSApplication.class);

    public static void main(String[] args) {
        System.out.println("🔊 Starting SaraAI Text-to-Speech Module");
        System.out.println("=========================================");
        
        // Print Java version and system info
        logger.info("Java Version: {}", System.getProperty("java.version"));
        logger.info("Operating System: {} {}", 
                   System.getProperty("os.name"), 
                   System.getProperty("os.version"));
        
        try {
            // Start the Spring Boot application
            SpringApplication app = new SpringApplication(TTSApplication.class);
            
            // Set default properties if not specified
            if (System.getProperty("server.port") == null) {
                System.setProperty("server.port", "8002");
            }
            
            app.run(args);
            
            logger.info("✅ TTS Application started successfully");
            
        } catch (Exception e) {
            logger.error("❌ Failed to start TTS Application: {}", e.getMessage(), e);
            System.exit(1);
        }
    }

    /**
     * Bean for TTS engine configuration
     */
    @Bean
    public TTSEngineConfig ttsEngineConfig() {
        TTSEngineConfig config = new TTSEngineConfig();
        
        // Set default configuration from environment variables or defaults
        config.setEngineType(getEnvOrDefault("TTS_ENGINE", "FREETTS"));
        config.setVoiceName(getEnvOrDefault("TTS_VOICE", "kevin16"));
        config.setSpeechRate(Float.parseFloat(getEnvOrDefault("TTS_SPEECH_RATE", "150.0")));
        config.setVolume(Float.parseFloat(getEnvOrDefault("TTS_VOLUME", "1.0")));
        
        logger.info("TTS Configuration:");
        logger.info("  Engine: {}", config.getEngineType());
        logger.info("  Voice: {}", config.getVoiceName());
        logger.info("  Speech Rate: {}", config.getSpeechRate());
        logger.info("  Volume: {}", config.getVolume());
        
        return config;
    }

    /**
     * Bean for the TTS service
     */
    @Bean
    public TTSService ttsService(TTSEngineConfig config) {
        return new TTSService(config);
    }

    /**
     * Utility method to get environment variable or default value
     */
    private static String getEnvOrDefault(String envVar, String defaultValue) {
        String value = System.getenv(envVar);
        return value != null ? value : defaultValue;
    }
}