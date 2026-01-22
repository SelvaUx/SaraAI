"""
Voice Engine - Wake word detection, speech-to-text, and text-to-speech.

This module handles all voice I/O for Sara AI Max.
"""

import asyncio
import logging
from typing import Optional
import pyttsx3

logger = logging.getLogger(__name__)


class VoiceEngine:
    """Handles wake word detection, STT, and TTS."""
    
    def __init__(self):
        """Initialize voice engine."""
        # Initialize TTS engine
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 160)  # Speed
        self.tts_engine.setProperty('volume', 1.0)  # Volume
        
        # Try to set a better voice if available
        voices = self.tts_engine.getProperty('voices')
        if len(voices) > 1:
            self.tts_engine.setProperty('voice', voices[1].id)  # Female voice
        
        self.listening = False
        
        logger.info("Voice engine initialized")
    
    async def listen_for_wake_word(self, timeout: int = 10) -> bool:
        """
        Listen for the wake word "Hey Sara" or "Sara".
        
        Args:
            timeout: Maximum seconds to listen
            
        Returns:
            True if wake word detected, False otherwise
        """
        try:
            # For MVP, we'll use a simple approach
            # In production, use Porcupine or similar for wake word detection
            import speech_recognition as sr
            
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                # Adjust for ambient noise
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                try:
                    # Listen with timeout
                    audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=3)
                    
                    # Recognize using Google Speech Recognition
                    text = recognizer.recognize_google(audio).lower()
                    logger.info(f"Heard: {text}")
                    
                    # Check for wake words
                    if 'hey sara' in text or 'sara' in text or 'hey sarah' in text:
                        return True
                        
                except sr.WaitTimeoutError:
                    pass  # Timeout, continue listening
                except sr.UnknownValueError:
                    pass  # Could not understand audio
                except Exception as e:
                    logger.error(f"Error in wake word detection: {e}")
                    
        except Exception as e:
            logger.error(f"Voice engine error: {e}")
        
        return False
    
    async def listen_for_command(self, timeout: int = 10) -> Optional[str]:
        """
        Listen for a voice command.
        
        Args:
            timeout: Maximum seconds to listen
            
        Returns:
            Recognized command text or None
        """
        try:
            import speech_recognition as sr
            
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                logger.info("Listening for command...")
                
                # Adjust for ambient noise
                recognizer.adjust_for_ambient_noise(source, duration=0.3)
                
                try:
                    # Listen for command
                    audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=10)
                    
                    # Recognize speech
                    text = recognizer.recognize_google(audio)
                    logger.info(f"Command recognized: {text}")
                    return text
                    
                except sr.WaitTimeoutError:
                    logger.warning("Timeout waiting for command")
                    return None
                except sr.UnknownValueError:
                    logger.warning("Could not understand audio")
                    self.speak("Sorry, I didn't understand that.")
                    return None
                    
        except Exception as e:
            logger.error(f"Error listening for command: {e}")
            return None
    
    def speak(self, text: str):
        """
        Speak the given text using TTS.
        
        Args:
            text: Text to speak
        """
        try:
            logger.info(f"Speaking: {text}")
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            logger.error(f"TTS error: {e}")
    
    def cleanup(self):
        """Clean up resources."""
        try:
            self.tts_engine.stop()
        except:
            pass
