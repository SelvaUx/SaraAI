"""
Base Skill - Base class for all Sara AI Max skills.

Skills are modular, reusable task executors.
"""

import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class SkillMetadata(BaseModel):
    """Metadata about a skill."""
    name: str
    description: str
    version: str = "1.0.0"
    author: str = "Sara AI Max"
    requires_internet: bool = False
    requires_permissions: list = []


class SkillResult(BaseModel):
    """Result from skill execution."""
    success: bool
    message: Optional[str] = None
    data: Dict[str, Any] = {}
    error: Optional[str] = None


class BaseSkill(ABC):
    """Base class for all skills."""
    
    def __init__(self):
        """Initialize skill."""
        self.metadata = self.get_metadata()
        logger.info(f"Initialized skill: {self.metadata.name}")
    
    @abstractmethod
    def get_metadata(self) -> SkillMetadata:
        """
        Get skill metadata.
        
        Returns:
            Skill metadata
        """
        pass
    
    @abstractmethod
    async def execute(self, **kwargs) -> SkillResult:
        """
        Execute the skill.
        
        Args:
            **kwargs: Skill parameters
            
        Returns:
            Skill execution result
        """
        pass
    
    @abstractmethod
    def validate_params(self, **kwargs) -> bool:
        """
        Validate skill parameters.
        
        Args:
            **kwargs: Parameters to validate
            
        Returns:
            True if valid
        """
        pass
    
    def __str__(self) -> str:
        """String representation."""
        return f"{self.metadata.name} v{self.metadata.version}"
