"""
Text-to-Speech Client Module
Handles communication with the Java TTS module
"""

import aiohttp
import logging
from typing import Optional, Dict, Any

from config.settings import Settings


class TextToSpeechClient:
    """Client for communicating with the Java TTS module"""
    
    def __init__(self, settings: Settings):
        self.settings = settings
        self.logger = logging.getLogger(__name__)
        self.base_url = f"http://{settings.tts_config.host}:{settings.tts_config.port}"
        self.session: Optional[aiohttp.ClientSession] = None
        
    async def start(self):
        """Initialize the TTS client"""
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.settings.tts_config.timeout)
        )
        self.logger.info(f"TTS client initialized - {self.base_url}")
        
        try:
            await self.health_check()
            self.logger.info("✅ TTS module is responsive")
        except Exception as e:
            self.logger.warning(f"⚠️ TTS module health check failed: {e}")
    
    async def shutdown(self):
        """Clean up the TTS client"""
        if self.session:
            await self.session.close()
        self.logger.info("TTS client shut down")
    
    async def health_check(self) -> bool:
        """Check if the TTS module is healthy"""
        try:
            if not self.session:
                return False
                
            async with self.session.get(f"{self.base_url}/health") as response:
                return response.status == 200
        except Exception as e:
            self.logger.debug(f"TTS health check failed: {e}")
            return False
    
    async def synthesize_speech(self, text: str, voice: str = "default") -> bool:
        """
        Synthesize and play speech
        
        Args:
            text: Text to convert to speech
            voice: Voice to use for synthesis
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if not self.session:
                return False
            
            tts_data = {
                "text": text,
                "voice": voice,
                "format": "wav"
            }
            
            async with self.session.post(
                f"{self.base_url}/api/synthesize",
                json=tts_data
            ) as response:
                
                if response.status == 200:
                    self.logger.info(f"🔊 Speech synthesized: '{text[:50]}...'")
                    return True
                else:
                    self.logger.error(f"TTS synthesis failed: {response.status}")
                    return False
                    
        except Exception as e:
            self.logger.error(f"TTS synthesis error: {e}")
            return False
    
    async def get_voices(self) -> list:
        """Get available voices"""
        try:
            if not self.session:
                return []
            
            async with self.session.get(f"{self.base_url}/api/voices") as response:
                if response.status == 200:
                    result = await response.json()
                    return result.get("voices", [])
                    
        except Exception as e:
            self.logger.error(f"Error getting voices: {e}")
            
        return []