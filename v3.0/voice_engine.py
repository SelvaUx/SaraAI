#!/usr/bin/env python3
"""
Sara AI Voice Engine
Handles wake word detection, speech-to-text, and text-to-speech functionality
"""

import os
import sys
import time
import threading
import queue
import json
import speech_recognition as sr
import pyttsx3
import logging
from typing import Optional

# Try importing pyaudio for advanced audio features
try:
    import pyaudio
    import wave
    PYAUDIO_AVAILABLE = True
except ImportError:
    PYAUDIO_AVAILABLE = False
    print("⚠️ PyAudio not available, using basic audio features")

# Try importing vosk for offline STT
try:
    import vosk
    VOSK_AVAILABLE = True
except ImportError:
    VOSK_AVAILABLE = False
    print("⚠️ Vosk not available, using online STT as fallback")

class VoiceEngine:
    def __init__(self, skip_microphone=False):
        """Initialize voice engine with STT and TTS"""
        self.logger = logging.getLogger('VoiceEngine')
        self.skip_microphone = skip_microphone
        
        # Initialize TTS engine with error handling
        try:
            self.tts_engine = pyttsx3.init()
            self.setup_tts()
        except Exception as e:
            self.logger.error(f"TTS initialization failed: {e}")
            self.tts_engine = None
            print("⚠️ Text-to-speech not available")
        
        # Initialize STT components with error handling
        if not self.skip_microphone:
            try:
                self.recognizer = sr.Recognizer()
                self.microphone = sr.Microphone()
            except Exception as e:
                self.logger.error(f"Microphone initialization failed: {e}")
                self.recognizer = None
                self.microphone = None
                print("⚠️ Microphone not available")
        else:
            self.recognizer = None
            self.microphone = None
            print("🔇 Microphone initialization skipped")
        
        # Wake word settings
        self.wake_words = ["hey sara", "sara", "hey sarah", "sarah"]
        self.is_listening_for_wake_word = False
        
        # Setup offline STT if available
        self.setup_offline_stt()
        
        # Audio settings - with timeout protection
        if not self.skip_microphone:
            try:
                self.setup_audio_calibration()
            except Exception as e:
                self.logger.error(f"Audio calibration failed: {e}")
                print("⚠️ Audio calibration failed, using defaults")
        
        print("🎤 Voice Engine initialized")
        
    def setup_tts(self):
        """Setup text-to-speech engine"""
        try:
            # Get available voices
            voices = self.tts_engine.getProperty('voices')
            
            # Try to set a female voice (for Sara)
            for voice in voices:
                if 'female' in voice.name.lower() or 'sara' in voice.name.lower():
                    self.tts_engine.setProperty('voice', voice.id)
                    break
            
            # Set speech rate and volume
            self.tts_engine.setProperty('rate', 180)  # Words per minute
            self.tts_engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)
            
            self.logger.info("TTS engine configured successfully")
            
        except Exception as e:
            self.logger.error(f"Error setting up TTS: {e}")
            
    def setup_offline_stt(self):
        """Setup offline speech-to-text with Vosk"""
        self.vosk_model = None
        self.vosk_rec = None
        
        if VOSK_AVAILABLE:
            try:
                # Check for Vosk model
                model_path = "models/vosk-model-en-us-0.22"
                if os.path.exists(model_path):
                    self.vosk_model = vosk.Model(model_path)
                    self.vosk_rec = vosk.KaldiRecognizer(self.vosk_model, 16000)
                    print("✅ Offline STT (Vosk) initialized")
                else:
                    print("⚠️ Vosk model not found, using online STT")
                    
            except Exception as e:
                self.logger.error(f"Error setting up Vosk: {e}")
                
    def setup_audio_calibration(self):
        """Calibrate microphone for ambient noise"""
        if not self.microphone or not self.recognizer:
            print("⚠️ Microphone not available, skipping calibration")
            return
            
        try:
            print("🎧 Calibrating microphone for ambient noise...")
            
            # Use threading with timeout to prevent hanging
            import threading
            import signal
            
            def calibrate():
                with self.microphone as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            # Create and start calibration thread
            calibration_thread = threading.Thread(target=calibrate)
            calibration_thread.daemon = True
            calibration_thread.start()
            
            # Wait for calibration with timeout
            calibration_thread.join(timeout=3.0)
            
            if calibration_thread.is_alive():
                print("⚠️ Microphone calibration timed out, using defaults")
                if self.recognizer:
                    self.recognizer.energy_threshold = 300
                    self.recognizer.dynamic_energy_threshold = True
            else:
                print("✅ Microphone calibrated")
            
        except Exception as e:
            self.logger.error(f"Error calibrating microphone: {e}")
            # Set default values if calibration fails
            if self.recognizer:
                self.recognizer.energy_threshold = 300
                self.recognizer.dynamic_energy_threshold = True
            print("⚠️ Using default microphone settings")
            
    def speak(self, text: str):
        """Convert text to speech"""
        try:
            if self.tts_engine:
                self.logger.info(f"Speaking: {text}")
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()
            else:
                print(f"Sara: {text}")  # Fallback to text output
            
        except Exception as e:
            self.logger.error(f"Error in TTS: {e}")
            print(f"Sara: {text}")  # Fallback to text output
            
    def listen_for_audio(self, timeout: int = 5) -> Optional[str]:
        """Listen for audio input and return transcript"""
        if not self.microphone or not self.recognizer:
            self.logger.warning("Microphone not available")
            return None
            
        try:
            with self.microphone as source:
                self.logger.info("Listening for audio...")
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=10)
                
            # Try offline STT first
            if self.vosk_rec:
                return self.transcribe_with_vosk(audio)
            else:
                return self.transcribe_with_google(audio)
                
        except sr.WaitTimeoutError:
            self.logger.debug("Listening timeout")
            return None
        except Exception as e:
            self.logger.error(f"Error listening for audio: {e}")
            return None
            
    def transcribe_with_vosk(self, audio) -> Optional[str]:
        """Transcribe audio using Vosk (offline)"""
        try:
            # Convert audio to wav format for Vosk
            wav_data = audio.get_wav_data()
            
            # Process with Vosk
            if self.vosk_rec.AcceptWaveform(wav_data):
                result = json.loads(self.vosk_rec.Result())
                return result.get('text', '').strip()
            else:
                result = json.loads(self.vosk_rec.PartialResult())
                return result.get('partial', '').strip()
                
        except Exception as e:
            self.logger.error(f"Error with Vosk transcription: {e}")
            return self.transcribe_with_google(audio)  # Fallback
            
    def transcribe_with_google(self, audio) -> Optional[str]:
        """Transcribe audio using Google STT (online fallback)"""
        try:
            text = self.recognizer.recognize_google(audio).lower()
            self.logger.info(f"Transcribed: {text}")
            return text
            
        except sr.UnknownValueError:
            self.logger.warning("Could not understand audio")
            return None
        except sr.RequestError as e:
            self.logger.error(f"Google STT error: {e}")
            return None
            
    def detect_wake_word(self) -> bool:
        """Detect wake word in continuous listening mode"""
        try:
            # Quick listen for wake word with shorter timeout
            audio_text = self.listen_for_audio(timeout=0.5)
            
            if audio_text:
                for wake_word in self.wake_words:
                    if wake_word in audio_text.lower():
                        self.logger.info(f"Wake word detected: {wake_word}")
                        return True
                        
            return False
            
        except sr.WaitTimeoutError:
            # This is expected during continuous listening
            return False
        except Exception as e:
            self.logger.debug(f"Wake word detection error: {e}")
            return False
            
    def listen_for_command(self, timeout: int = 10) -> Optional[str]:
        """Listen for a command after wake word detection"""
        if not self.microphone or not self.recognizer:
            print("⚠️ Microphone not available for commands")
            return None
            
        try:
            print("🎤 Listening for command...")
            self.speak("How can I help you?")
            
            command = self.listen_for_audio(timeout=timeout)
            
            if command:
                self.logger.info(f"Command received: {command}")
                return command.strip()
            else:
                self.logger.warning("No command received")
                return None
                
        except Exception as e:
            self.logger.error(f"Error listening for command: {e}")
            return None
            
    def continuous_listening(self, callback_func):
        """Continuous listening mode for wake word detection"""
        self.is_listening_for_wake_word = True
        
        while self.is_listening_for_wake_word:
            try:
                if self.detect_wake_word():
                    callback_func()
                    
                time.sleep(0.1)  # Small delay to prevent excessive CPU usage
                
            except KeyboardInterrupt:
                self.is_listening_for_wake_word = False
                break
            except Exception as e:
                self.logger.error(f"Error in continuous listening: {e}")
                time.sleep(1)  # Wait before retrying
                
    def stop_listening(self):
        """Stop continuous listening"""
        self.is_listening_for_wake_word = False
        self.logger.info("Stopped listening for wake word")
        
    def test_voice_system(self):
        """Test both TTS and STT systems"""
        print("🧪 Testing Voice System...")
        
        # Test TTS
        self.speak("Voice system test initiated. Text to speech is working.")
        
        # Test STT
        print("Now testing speech recognition. Please say something...")
        result = self.listen_for_command(timeout=5)
        
        if result:
            self.speak(f"I heard you say: {result}")
            print("✅ Voice system test completed successfully")
        else:
            self.speak("I didn't hear anything clearly.")
            print("⚠️ Speech recognition test inconclusive")

def main():
    """Test the voice engine"""
    engine = VoiceEngine()
    engine.test_voice_system()

if __name__ == "__main__":
    main()
