"""
Context Manager - Session memory and conversation context.

This module maintains conversation history and context.
"""

import logging
from typing import List, Dict, Any, Optional
from datetime import datetime
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class ContextEntry(BaseModel):
    """A single context entry."""
    
    timestamp: str
    role: str  # 'user' or 'assistant'
    content: str
    metadata: Dict[str, Any] = {}


class ContextManager:
    """Manages conversation context and memory."""
    
    def __init__(self, max_history: int = 50):
        """
        Initialize context manager.
        
        Args:
            max_history: Maximum number of entries to keep in history
        """
        self.history: List[ContextEntry] = []
        self.max_history = max_history
        self.session_start = datetime.now()
        self.context_variables: Dict[str, Any] = {}
        
        logger.info("Context manager initialized")
    
    def add_user_message(self, message: str, metadata: Optional[Dict] = None):
        """
        Add a user message to context.
        
        Args:
            message: User's message
            metadata: Optional metadata about the message
        """
        entry = ContextEntry(
            timestamp=datetime.now().isoformat(),
            role='user',
            content=message,
            metadata=metadata or {}
        )
        
        self.history.append(entry)
        self._trim_history()
        logger.info(f"Added user message to context: {message[:50]}...")
    
    def add_assistant_message(self, message: str, metadata: Optional[Dict] = None):
        """
        Add an assistant message to context.
        
        Args:
            message: Assistant's message
            metadata: Optional metadata about the message
        """
        entry = ContextEntry(
            timestamp=datetime.now().isoformat(),
            role='assistant',
            content=message,
            metadata=metadata or {}
        )
        
        self.history.append(entry)
        self._trim_history()
        logger.info(f"Added assistant message to context: {message[:50]}...")
    
    def get_recent_context(self, count: int = 10) -> List[ContextEntry]:
        """
        Get recent context entries.
        
        Args:
            count: Number of recent entries to return
            
        Returns:
            List of recent context entries
        """
        return self.history[-count:]
    
    def set_variable(self, key: str, value: Any):
        """
        Set a context variable.
        
        Args:
            key: Variable key
            value: Variable value
        """
        self.context_variables[key] = value
        logger.info(f"Set context variable: {key}")
    
    def get_variable(self, key: str, default: Any = None) -> Any:
        """
        Get a context variable.
        
        Args:
            key: Variable key
            default: Default value if key not found
            
        Returns:
            Variable value or default
        """
        return self.context_variables.get(key, default)
    
    def clear_context(self):
        """Clear all context and start fresh."""
        self.history.clear()
        self.context_variables.clear()
        self.session_start = datetime.now()
        logger.info("Context cleared")
    
    def _trim_history(self):
        """Trim history to max_history length."""
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]
