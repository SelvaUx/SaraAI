"""
Wake Word Detection Module
Handles continuous listening and wake word recognition
"""

import asyncio
import logging
import time
from typing import List, Optional, Callable
import re
from dataclasses import dataclass

from config.settings import Settings


@dataclass
class WakeWordEvent:
    """Event triggered when a wake word is detected"""
    wake_word: str
    confidence: float
    timestamp: float
    audio_data: Optional[bytes] = None


class WakeWordDetector:
    """
    Wake word detector that continuously monitors audio input
    for predefined wake words using simple text matching
    """
    
    def __init__(self, settings: Settings):
        self.settings = settings
        self.logger = logging.getLogger(__name__)
        self.is_listening = False
        self.is_active = False
        self.wake_word_callback: Optional[Callable] = None
        
        # Normalize wake words for better matching
        self.wake_words = [word.lower().strip() for word in settings.wake_words]
        self.logger.info(f"Initialized with wake words: {self.wake_words}")
    
    def set_wake_word_callback(self, callback: Callable[[WakeWordEvent], None]):
        """Set callback function to be called when wake word is detected"""
        self.wake_word_callback = callback
    
    def start_listening(self):
        """Start continuous listening for wake words"""
        if not self.settings.wake_word_enabled:
            self.logger.info("Wake word detection is disabled")
            return
            
        self.is_listening = True
        self.is_active = True
        self.logger.info("🎙️ Wake word detection started - listening for: " + ", ".join(self.wake_words))
    
    def stop_listening(self):
        """Stop listening for wake words"""
        self.is_listening = False
        self.is_active = False
        self.logger.info("Wake word detection stopped")
    
    async def process_audio_text(self, text: str) -> Optional[WakeWordEvent]:
        """
        Process transcribed text to detect wake words
        
        Args:
            text: Transcribed audio text
            
        Returns:
            WakeWordEvent if wake word detected, None otherwise
        """
        if not self.is_listening or not text:
            return None
        
        text_lower = text.lower().strip()
        self.logger.debug(f"Processing audio text: '{text_lower}'")
        
        # Check for wake words
        for wake_word in self.wake_words:
            if self._matches_wake_word(text_lower, wake_word):
                confidence = self._calculate_confidence(text_lower, wake_word)
                
                if confidence >= self.settings.wake_word_sensitivity:
                    self.logger.info(f"✨ Wake word detected: '{wake_word}' (confidence: {confidence:.2f})")
                    
                    event = WakeWordEvent(
                        wake_word=wake_word,
                        confidence=confidence,
                        timestamp=time.time()
                    )
                    
                    # Trigger callback if set
                    if self.wake_word_callback:
                        try:
                            await self._async_callback(event)
                        except Exception as e:
                            self.logger.error(f"Error in wake word callback: {e}")
                    
                    return event
        
        return None
    
    def _matches_wake_word(self, text: str, wake_word: str) -> bool:
        """Check if text contains the wake word"""
        # Exact match
        if wake_word in text:
            return True
        
        # Word boundary match (more strict)
        pattern = r'\b' + re.escape(wake_word) + r'\b'
        if re.search(pattern, text):
            return True
        
        # Fuzzy match for slight variations
        words = text.split()
        wake_words = wake_word.split()
        
        if len(wake_words) == 1:
            # Single word wake word
            for word in words:
                if self._fuzzy_match(word, wake_word):
                    return True
        else:
            # Multi-word wake word
            for i in range(len(words) - len(wake_words) + 1):
                segment = ' '.join(words[i:i + len(wake_words)])
                if self._fuzzy_match(segment, wake_word):
                    return True
        
        return False
    
    def _fuzzy_match(self, text1: str, text2: str, threshold: float = 0.8) -> bool:
        """Simple fuzzy matching based on character similarity"""
        if not text1 or not text2:
            return False
        
        # Simple Levenshtein-like approach
        text1, text2 = text1.lower(), text2.lower()
        
        if len(text1) == 0:
            return len(text2) == 0
        if len(text2) == 0:
            return False
        
        # Calculate similarity ratio
        max_len = max(len(text1), len(text2))
        common_chars = sum(1 for c1, c2 in zip(text1, text2) if c1 == c2)
        similarity = common_chars / max_len
        
        return similarity >= threshold
    
    def _calculate_confidence(self, text: str, wake_word: str) -> float:
        """Calculate confidence score for wake word detection"""
        # Base confidence
        confidence = 0.5
        
        # Exact match gets high confidence
        if wake_word == text.strip():
            confidence = 1.0
        elif wake_word in text:
            # Partial match
            confidence = 0.8
        else:
            # Fuzzy match
            confidence = 0.6
        
        # Adjust based on text length (shorter is better for wake words)
        text_words = len(text.split())
        wake_word_words = len(wake_word.split())
        
        if text_words == wake_word_words:
            confidence += 0.1
        elif text_words < wake_word_words + 3:  # Allow some extra words
            confidence += 0.05
        else:
            confidence -= 0.1  # Penalize very long phrases
        
        return min(1.0, max(0.0, confidence))
    
    async def _async_callback(self, event: WakeWordEvent):
        """Handle async callback execution"""
        if asyncio.iscoroutinefunction(self.wake_word_callback):
            await self.wake_word_callback(event)
        else:
            self.wake_word_callback(event)
    
    def get_status(self) -> dict:
        """Get current detector status"""
        return {
            "listening": self.is_listening,
            "active": self.is_active,
            "wake_words": self.wake_words,
            "sensitivity": self.settings.wake_word_sensitivity,
            "enabled": self.settings.wake_word_enabled
        }