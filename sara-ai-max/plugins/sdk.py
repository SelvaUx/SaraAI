"""
Plugin SDK - Software Development Kit for creating Sara AI Max plugins.

This module provides the base classes and utilities for plugin development.
"""

import logging
from abc import ABC, abstractmethod
from typing import Dict, Any
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class PluginMetadata(BaseModel):
    """Metadata for a plugin."""
    name: str
    version: str
    author: str
    description: str
    requires: list = []


class PluginSDK:
    """SDK utilities for plugin developers."""
    
    @staticmethod
    def log(message: str):
        """
        Log a message from the plugin.
        
        Args:
            message: Log message
        """
        logger.info(f"[Plugin] {message}")
    
    @staticmethod
    def error(message: str):
        """
        Log an error from the plugin.
        
        Args:
            message: Error message
        """
        logger.error(f"[Plugin] {message}")
    
    @staticmethod
    def get_config(key: str, default: Any = None) -> Any:
        """
        Get configuration value.
        
        Args:
            key: Configuration key
            default: Default value
            
        Returns:
            Configuration value
        """
        # In production, load from config file
        return default


class Plugin(ABC):
    """Base class for all Sara AI Max plugins."""
    
    def __init__(self):
        """Initialize plugin."""
        self.sdk = PluginSDK()
        self.metadata = self.get_metadata()
        self.sdk.log(f"Initialized: {self.metadata.name} v{self.metadata.version}")
    
    @abstractmethod
    def get_metadata(self) -> PluginMetadata:
        """
        Get plugin metadata.
        
        Returns:
            Plugin metadata
        """
        pass
    
    @abstractmethod
    def execute(self, **kwargs) -> Dict[str, Any]:
        """
        Execute the plugin.
        
        Args:
            **kwargs: Plugin parameters
            
        Returns:
            Execution result dictionary
        """
        pass
    
    def on_load(self):
        """Called when plugin is loaded."""
        pass
    
    def on_unload(self):
        """Called when plugin is unloaded."""
        pass


# Example plugin template
class ExamplePlugin(Plugin):
    """Example plugin demonstrating the SDK."""
    
    def get_metadata(self) -> PluginMetadata:
        """Get plugin metadata."""
        return PluginMetadata(
            name="Example Plugin",
            version="1.0.0",
            author="Sara AI Max",
            description="Example plugin showing SDK usage"
        )
    
    def execute(self, **kwargs) -> Dict[str, Any]:
        """Execute the plugin."""
        self.sdk.log("Example plugin executed")
        
        return {
            'success': True,
            'message': 'Example plugin executed successfully',
            'data': kwargs
        }
