"""
Natural Language Understanding - Intent parsing and entity extraction.

This module parses user commands into structured intents.
"""

import logging
import re
from enum import Enum
from typing import Dict, List, Any, Optional
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class IntentType(str, Enum):
    """Types of intents Sara can understand."""
    
    # System control
    SYSTEM_INFO = "system_info"
    VOLUME_CONTROL = "volume_control"
    BRIGHTNESS_CONTROL = "brightness_control"
    SHUTDOWN = "shutdown"
    RESTART = "restart"
    LOCK = "lock"
    
    # Application control
    OPEN_APP = "open_app"
    CLOSE_APP = "close_app"
    SWITCH_APP = "switch_app"
    
    # File operations
    CREATE_FILE = "create_file"
    DELETE_FILE = "delete_file"
    CREATE_FOLDER = "create_folder"
    DELETE_FOLDER = "delete_folder"
    SEARCH_FILE = "search_file"
    OPEN_FILE = "open_file"
    
    # Utilities
    TIME = "time"
    DATE = "date"
    WEATHER = "weather"
    JOKE = "joke"
    SEARCH_WEB = "search_web"
    
    # Unknown
    UNKNOWN = "unknown"


class Intent(BaseModel):
    """Structured representation of user intent."""
    
    intent_type: IntentType
    entities: Dict[str, Any] = {}
    confidence: float = 1.0
    raw_text: str


class NLUEngine:
    """Natural Language Understanding engine."""
    
    def __init__(self):
        """Initialize NLU engine with intent patterns."""
        self.patterns = self._build_patterns()
        logger.info("NLU engine initialized")
    
    def _build_patterns(self) -> Dict[IntentType, List[str]]:
        """Build regex patterns for intent matching."""
        return {
            # System control
            IntentType.TIME: [
                r"what.*time",
                r"tell.*time",
                r"current time",
            ],
            IntentType.DATE: [
                r"what.*date",
                r"today.*date",
                r"current date",
            ],
            IntentType.VOLUME_CONTROL: [
                r"(increase|decrease|set|adjust).*(volume|sound)",
                r"volume (up|down)",
                r"(mute|unmute)",
            ],
            IntentType.BRIGHTNESS_CONTROL: [
                r"(increase|decrease|set).*(brightness|screen)",
                r"brightness (up|down)",
            ],
            IntentType.SHUTDOWN: [
                r"shut.*down",
                r"power.*off",
                r"turn.*off.*computer",
            ],
            IntentType.RESTART: [
                r"restart",
                r"reboot",
            ],
            IntentType.LOCK: [
                r"lock.*screen",
                r"lock.*computer",
            ],
            IntentType.SYSTEM_INFO: [
                r"system.*info",
                r"cpu.*usage",
                r"memory.*usage",
                r"disk.*space",
            ],
            
            # Application control
            IntentType.OPEN_APP: [
                r"open ([a-zA-Z0-9 ]+)",
                r"launch ([a-zA-Z0-9 ]+)",
                r"start ([a-zA-Z0-9 ]+)",
            ],
            IntentType.CLOSE_APP: [
                r"close ([a-zA-Z0-9 ]+)",
                r"quit ([a-zA-Z0-9 ]+)",
                r"exit ([a-zA-Z0-9 ]+)",
            ],
            
            # File operations
            IntentType.CREATE_FOLDER: [
                r"create (a |)folder.*named ([a-zA-Z0-9 ]+)",
                r"make (a |)folder.*named ([a-zA-Z0-9 ]+)",
                r"new folder ([a-zA-Z0-9 ]+)",
            ],
            IntentType.DELETE_FOLDER: [
                r"delete.*folder ([a-zA-Z0-9 ]+)",
                r"remove.*folder ([a-zA-Z0-9 ]+)",
            ],
            IntentType.CREATE_FILE: [
                r"create (a |)file.*named ([a-zA-Z0-9. ]+)",
                r"new file ([a-zA-Z0-9. ]+)",
            ],
            IntentType.SEARCH_FILE: [
                r"find.*file ([a-zA-Z0-9. ]+)",
                r"search.*for ([a-zA-Z0-9. ]+)",
                r"locate ([a-zA-Z0-9. ]+)",
            ],
            
            # Utilities
            IntentType.SEARCH_WEB: [
                r"search.*for (.+)",
                r"google (.+)",
                r"look.*up (.+)",
            ],
            IntentType.JOKE: [
                r"tell.*joke",
                r"make.*laugh",
                r"something funny",
            ],
            IntentType.WEATHER: [
                r"what.*weather",
                r"weather.*in (.+)",
                r"temperature",
            ],
        }
    
    def parse(self, text: str) -> Intent:
        """
        Parse user command text into a structured Intent.
        
        Args:
            text: User command text
            
        Returns:
            Parsed Intent object
        """
        text_lower = text.lower().strip()
        logger.info(f"Parsing: {text_lower}")
        
        # Try to match against patterns
        for intent_type, patterns in self.patterns.items():
            for pattern in patterns:
                match = re.search(pattern, text_lower)
                if match:
                    # Extract entities from groups
                    entities = {}
                    if match.groups():
                        if intent_type in [IntentType.OPEN_APP, IntentType.CLOSE_APP]:
                            entities['app_name'] = match.group(1).strip()
                        elif intent_type == IntentType.CREATE_FOLDER:
                            entities['folder_name'] = match.groups()[-1].strip()
                        elif intent_type == IntentType.CREATE_FILE:
                            entities['file_name'] = match.groups()[-1].strip()
                        elif intent_type == IntentType.SEARCH_WEB:
                            entities['query'] = match.group(1).strip()
                        elif intent_type == IntentType.SEARCH_FILE:
                            entities['file_name'] = match.group(1).strip()
                        elif intent_type == IntentType.WEATHER:
                            if match.groups():
                                entities['location'] = match.group(1).strip()
                        
                        # Volume and brightness
                        if intent_type == IntentType.VOLUME_CONTROL:
                            if 'up' in text_lower or 'increase' in text_lower:
                                entities['action'] = 'increase'
                            elif 'down' in text_lower or 'decrease' in text_lower:
                                entities['action'] = 'decrease'
                            elif 'mute' in text_lower:
                                entities['action'] = 'mute'
                            elif 'unmute' in text_lower:
                                entities['action'] = 'unmute'
                        
                        if intent_type == IntentType.BRIGHTNESS_CONTROL:
                            if 'up' in text_lower or 'increase' in text_lower:
                                entities['action'] = 'increase'
                            elif 'down' in text_lower or 'decrease' in text_lower:
                                entities['action'] = 'decrease'
                    
                    return Intent(
                        intent_type=intent_type,
                        entities=entities,
                        confidence=0.9,
                        raw_text=text
                    )
        
        # No pattern matched
        logger.warning(f"Could not parse intent from: {text}")
        return Intent(
            intent_type=IntentType.UNKNOWN,
            entities={},
            confidence=0.0,
            raw_text=text
        )
