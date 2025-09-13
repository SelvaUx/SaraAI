"""
Speech-to-Text Client Module
Handles communication with the C++ speech recognition module
"""

import asyncio
import aiohttp
import logging
import time
from typing import Optional, Callable, Dict, Any
from enum import Enum

from config.settings import Settings


class ListeningMode(Enum):
    """Different listening modes for the speech client"""
    INACTIVE = "inactive"
    WAKE_WORD = "wake_word"
    COMMAND = "command"


class SpeechToTextClient:
    """Client for communicating with the C++ speech recognition module"""
    
    def __init__(self, settings: Settings):
        self.settings = settings
        self.logger = logging.getLogger(__name__)
        self.base_url = f"http://{settings.speech_config.host}:{settings.speech_config.port}"
        self.session: Optional[aiohttp.ClientSession] = None
        self.listening_mode = ListeningMode.INACTIVE
        self.is_listening = False
        
        # Callbacks
        self.wake_word_callback: Optional[Callable] = None
        self.command_callback: Optional[Callable] = None
        
    async def start(self):
        """Initialize the speech client"""
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.settings.speech_config.timeout)
        )
        self.logger.info(f"Speech client initialized - {self.base_url}")
        
        # Test connection
        try:
            await self.health_check()
            self.logger.info("✅ Speech module is responsive")
        except Exception as e:
            self.logger.warning(f"⚠️ Speech module health check failed: {e}")
    
    async def shutdown(self):
        """Clean up the speech client"""
        if self.session:
            await self.session.close()
        self.logger.info("Speech client shut down")
    
    async def health_check(self) -> bool:
        """Check if the speech module is healthy"""
        try:
            if not self.session:
                return False
                
            async with self.session.get(f"{self.base_url}/health") as response:
                return response.status == 200
        except Exception as e:
            self.logger.debug(f"Health check failed: {e}")
            return False
    
    def set_wake_word_callback(self, callback: Callable[[str, float], None]):
        """Set callback for wake word detection"""
        self.wake_word_callback = callback
    
    def set_command_callback(self, callback: Callable[[str, float], None]):
        """Set callback for command recognition"""
        self.command_callback = callback
    
    async def start_wake_word_listening(self):
        """Start listening for wake words"""
        if not await self.health_check():
            self.logger.error("Cannot start wake word listening - speech module not available")
            return False
        
        self.listening_mode = ListeningMode.WAKE_WORD
        self.is_listening = True
        
        # Start continuous listening task
        asyncio.create_task(self._continuous_listening_loop())
        
        self.logger.info("🎙️ Started wake word listening mode")
        return True
    
    async def start_command_listening(self, timeout: float = 5.0) -> Optional[str]:
        """
        Start listening for a command after wake word detection
        
        Args:
            timeout: Maximum time to wait for command
            
        Returns:
            Recognized command text or None if timeout/error
        """
        if not await self.health_check():
            self.logger.error("Cannot start command listening - speech module not available")
            return None
        
        self.listening_mode = ListeningMode.COMMAND
        self.logger.info("🎧 Listening for command...")
        
        try:
            # Send command listening request
            command_data = {
                "mode": "command",
                "timeout": timeout,
                "sensitivity": "high"
            }
            
            async with self.session.post(
                f"{self.base_url}/api/recognize", 
                json=command_data
            ) as response:
                
                if response.status == 200:
                    result = await response.json()
                    text = result.get("text", "")
                    confidence = result.get("confidence", 0.0)
                    
                    if text and confidence > self.settings.confidence_threshold:
                        self.logger.info(f"📝 Command recognized: '{text}' (confidence: {confidence:.2f})")
                        
                        # Trigger callback if set
                        if self.command_callback:
                            await self._async_callback(self.command_callback, text, confidence)
                        
                        return text
                    else:
                        self.logger.info("No clear command recognized")
                        return None
                else:
                    self.logger.error(f"Command recognition failed: {response.status}")
                    return None
                    
        except asyncio.TimeoutError:
            self.logger.info("Command listening timeout")
            return None
        except Exception as e:
            self.logger.error(f"Command listening error: {e}")
            return None
        finally:
            # Return to wake word listening mode
            self.listening_mode = ListeningMode.WAKE_WORD
    
    async def _continuous_listening_loop(self):
        """Continuous listening loop for wake words"""
        while self.is_listening and self.listening_mode == ListeningMode.WAKE_WORD:
            try:
                # Poll for wake word detection
                await self._check_for_wake_word()
                
                # Short delay to prevent overwhelming the speech module
                await asyncio.sleep(0.1)
                
            except Exception as e:
                self.logger.error(f"Error in continuous listening: {e}")
                await asyncio.sleep(1.0)  # Longer delay on error
    
    async def _check_for_wake_word(self):
        """Check for wake word in audio stream"""
        try:
            wake_word_data = {
                "mode": "wake_word",
                "sensitivity": self.settings.wake_word_sensitivity,
                "wake_words": self.settings.wake_words
            }
            
            async with self.session.post(
                f"{self.base_url}/api/recognize",
                json=wake_word_data
            ) as response:
                
                if response.status == 200:
                    result = await response.json()
                    text = result.get("text", "")
                    confidence = result.get("confidence", 0.0)
                    
                    if text and confidence > self.settings.wake_word_sensitivity:
                        self.logger.debug(f"Audio detected: '{text}' (confidence: {confidence:.2f})")
                        
                        # Check if it contains a wake word
                        text_lower = text.lower()
                        for wake_word in self.settings.wake_words:
                            if wake_word.lower() in text_lower:
                                self.logger.info(f"✨ Wake word detected: '{wake_word}'")
                                
                                # Trigger callback if set
                                if self.wake_word_callback:
                                    await self._async_callback(self.wake_word_callback, wake_word, confidence)
                                
                                return
                                
        except Exception as e:
            # Don't log every error in continuous loop
            if "timeout" not in str(e).lower():
                self.logger.debug(f"Wake word check error: {e}")
    
    async def stop_listening(self):
        """Stop all listening modes"""
        self.is_listening = False
        self.listening_mode = ListeningMode.INACTIVE
        self.logger.info("Stopped speech listening")
    
    async def listen_for_speech(self, timeout: float = 30.0) -> Optional[str]:
        """
        Generic method to listen for any speech (for backward compatibility)
        
        Args:
            timeout: Maximum time to wait
            
        Returns:
            Recognized text or None
        """
        try:
            speech_data = {
                "mode": "general",
                "timeout": timeout
            }
            
            async with self.session.post(
                f"{self.base_url}/api/recognize",
                json=speech_data
            ) as response:
                
                if response.status == 200:
                    result = await response.json()
                    return result.get("text")
                    
        except Exception as e:
            self.logger.error(f"Speech recognition error: {e}")
            
        return None
    
    async def _async_callback(self, callback: Callable, text: str, confidence: float):
        """Handle async callback execution"""
        try:
            if asyncio.iscoroutinefunction(callback):
                await callback(text, confidence)
            else:
                callback(text, confidence)
        except Exception as e:
            self.logger.error(f"Callback execution error: {e}")
    
    def get_status(self) -> Dict[str, Any]:
        """Get current speech client status"""
        return {
            "listening": self.is_listening,
            "mode": self.listening_mode.value,
            "base_url": self.base_url,
            "session_active": self.session is not None
        }