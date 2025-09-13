"""
Basic AI Brain implementation
This will contain the core AI logic for processing commands
"""

from typing import Dict, Any
from dataclasses import dataclass
import logging
from config.settings import Settings


@dataclass
class AIResponse:
    """Response from the AI brain"""
    action: str
    module: str
    params: Dict[str, Any]
    confidence: float
    response_text: str


class AIBrain:
    """Basic AI brain for processing commands"""
    
    def __init__(self, settings: Settings):
        self.settings = settings
        self.logger = logging.getLogger(__name__)
    
    async def process_command(self, text: str) -> AIResponse:
        """Process a text command and return an AI response"""
        text_lower = text.lower().strip()
        self.logger.info(f"Processing command: '{text}'")
        
        # Time and date queries
        if any(word in text_lower for word in ["time", "clock", "what time"]):
            return AIResponse(
                action="get_time",
                module="system",
                params={},
                confidence=0.9,
                response_text="I'll get the current time for you."
            )
        
        elif any(word in text_lower for word in ["date", "today", "what day"]):
            return AIResponse(
                action="get_date",
                module="system",
                params={},
                confidence=0.9,
                response_text="Let me tell you today's date."
            )
        
        # Weather queries
        elif any(word in text_lower for word in ["weather", "temperature", "forecast"]):
            return AIResponse(
                action="get_weather", 
                module="knowledge",
                params={"location": "local"},
                confidence=0.8,
                response_text="Let me check the weather for you."
            )
        
        # Search queries
        elif any(word in text_lower for word in ["search", "find", "lookup", "tell me about"]):
            # Extract search query
            query = text
            for wake_word in ["search for", "find", "lookup", "tell me about"]:
                if wake_word in text_lower:
                    query = text_lower.replace(wake_word, "").strip()
                    break
            
            return AIResponse(
                action="search",
                module="knowledge", 
                params={"query": query},
                confidence=0.8,
                response_text=f"I'll search for information about {query}."
            )
        
        # System control commands
        elif any(word in text_lower for word in ["open", "launch", "start"]):
            # Extract application name
            app_name = "application"
            if "notepad" in text_lower:
                app_name = "notepad"
            elif "calculator" in text_lower:
                app_name = "calc"
            elif "browser" in text_lower or "chrome" in text_lower:
                app_name = "chrome"
            elif "explorer" in text_lower or "file manager" in text_lower:
                app_name = "explorer"
            
            return AIResponse(
                action="launch_app",
                module="system",
                params={"app": app_name},
                confidence=0.8,
                response_text=f"I'll open {app_name} for you."
            )
        
        # Volume control
        elif any(word in text_lower for word in ["volume up", "louder", "increase volume"]):
            return AIResponse(
                action="volume_up",
                module="system",
                params={"amount": 10},
                confidence=0.9,
                response_text="Increasing volume."
            )
        
        elif any(word in text_lower for word in ["volume down", "quieter", "decrease volume"]):
            return AIResponse(
                action="volume_down",
                module="system",
                params={"amount": 10},
                confidence=0.9,
                response_text="Decreasing volume."
            )
        
        elif any(word in text_lower for word in ["mute", "silence"]):
            return AIResponse(
                action="mute",
                module="system",
                params={},
                confidence=0.9,
                response_text="Muting audio."
            )
        
        # Greetings and conversation
        elif any(word in text_lower for word in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]):
            return AIResponse(
                action="greet",
                module="tts",
                params={"text": "Hello! I'm SaraAI. How can I help you today?"},
                confidence=0.9,
                response_text="Hello! I'm SaraAI. How can I help you today?"
            )
        
        elif any(word in text_lower for word in ["how are you", "how's it going"]):
            return AIResponse(
                action="status",
                module="tts",
                params={"text": "I'm doing well, thank you! All my systems are running smoothly."},
                confidence=0.8,
                response_text="I'm doing well, thank you! All my systems are running smoothly."
            )
        
        elif any(word in text_lower for word in ["thank you", "thanks"]):
            return AIResponse(
                action="acknowledge",
                module="tts",
                params={"text": "You're welcome! Is there anything else I can help you with?"},
                confidence=0.9,
                response_text="You're welcome! Is there anything else I can help you with?"
            )
        
        # Help and information
        elif any(word in text_lower for word in ["help", "what can you do", "commands"]):
            help_text = ("I can help you with many things! I can tell you the time and date, "
                        "search for information, control your system, adjust volume, open applications, "
                        "and have conversations. Just speak naturally and I'll do my best to help!")
            return AIResponse(
                action="help",
                module="tts",
                params={"text": help_text},
                confidence=0.9,
                response_text=help_text
            )
        
        # Shutdown commands
        elif any(word in text_lower for word in ["goodbye", "bye", "exit", "quit", "stop listening"]):
            return AIResponse(
                action="goodbye",
                module="tts",
                params={"text": "Goodbye! Have a great day!"},
                confidence=0.9,
                response_text="Goodbye! Have a great day!"
            )
        
        # Default response for unrecognized commands
        else:
            return AIResponse(
                action="unknown",
                module="tts",
                params={"text": "I'm not sure how to help with that. You can ask me about the time, weather, search for information, or say 'help' to learn more about what I can do."},
                confidence=0.5,
                response_text="I'm not sure how to help with that. Try asking for help to see what I can do."
            )
