"""
Plugin Manager - Load, validate, and manage plugins.

This module handles plugin lifecycle and sandboxing.
"""

import logging
import importlib.util
from pathlib import Path
from typing import Dict, List, Optional
from .sdk import Plugin, PluginMetadata

logger = logging.getLogger(__name__)


class PluginManager:
    """Manage plugins for Sara AI Max."""
    
    def __init__(self, plugin_dir: str = "plugins/installed"):
        """
        Initialize plugin manager.
        
        Args:
            plugin_dir: Directory containing plugin files
        """
        self.plugin_dir = Path(plugin_dir)
        self.plugin_dir.mkdir(parents=True, exist_ok=True)
        
        self.loaded_plugins: Dict[str, Plugin] = {}
        
        logger.info(f"Plugin manager initialized: {self.plugin_dir}")
    
    def discover_plugins(self) -> List[str]:
        """
        Discover available plugins.
        
        Returns:
            List of plugin names
        """
        plugins = []
        
        for plugin_file in self.plugin_dir.glob("*.py"):
            if plugin_file.stem != "__init__":
                plugins.append(plugin_file.stem)
        
        logger.info(f"Discovered {len(plugins)} plugins")
        return plugins
    
    def load_plugin(self, plugin_name: str) -> bool:
        """
        Load a plugin by name.
        
        Args:
            plugin_name: Name of the plugin to load
            
        Returns:
            True if loaded successfully
        """
        try:
            plugin_path = self.plugin_dir / f"{plugin_name}.py"
            
            if not plugin_path.exists():
                logger.error(f"Plugin not found: {plugin_name}")
                return False
            
            # Load module
            spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
            if not spec or not spec.loader:
                logger.error(f"Could not load plugin: {plugin_name}")
                return False
            
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Find Plugin class
            plugin_class = None
            for item in dir(module):
                obj = getattr(module, item)
                if isinstance(obj, type) and issubclass(obj, Plugin) and obj != Plugin:
                    plugin_class = obj
                    break
            
            if not plugin_class:
                logger.error(f"No Plugin class found in: {plugin_name}")
                return False
            
            # Instantiate plugin
            plugin = plugin_class()
            
            # Validate plugin
            if not self.validate_plugin(plugin):
                logger.error(f"Plugin validation failed: {plugin_name}")
                return False
            
            # Store plugin
            self.loaded_plugins[plugin_name] = plugin
            logger.info(f"Loaded plugin: {plugin_name}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error loading plugin {plugin_name}: {e}")
            return False
    
    def unload_plugin(self, plugin_name: str) -> bool:
        """
        Unload a plugin.
        
        Args:
            plugin_name: Name of plugin to unload
            
        Returns:
            True if unloaded successfully
        """
        if plugin_name in self.loaded_plugins:
            del self.loaded_plugins[plugin_name]
            logger.info(f"Unloaded plugin: {plugin_name}")
            return True
        return False
    
    def validate_plugin(self, plugin: Plugin) -> bool:
        """
        Validate a plugin.
        
        Args:
            plugin: Plugin to validate
            
        Returns:
            True if valid
        """
        try:
            # Check metadata
            metadata = plugin.get_metadata()
            if not metadata.name or not metadata.version:
                return False
            
            # Check required methods
            if not hasattr(plugin, 'execute'):
                return False
            
            return True
            
        except Exception as e:
            logger.error(f"Plugin validation error: {e}")
            return False
    
    def execute_plugin(self, plugin_name: str, **kwargs) -> Optional[dict]:
        """
        Execute a loaded plugin.
        
        Args:
            plugin_name: Name of plugin to execute
            **kwargs: Plugin parameters
            
        Returns:
            Plugin result or None
        """
        if plugin_name not in self.loaded_plugins:
            logger.error(f"Plugin not loaded: {plugin_name}")
            return None
        
        try:
            plugin = self.loaded_plugins[plugin_name]
            result = plugin.execute(**kwargs)
            return result
            
        except Exception as e:
            logger.error(f"Error executing plugin {plugin_name}: {e}")
            return None
    
    def list_loaded_plugins(self) -> List[str]:
        """
        Get list of loaded plugins.
        
        Returns:
            List of plugin names
        """
        return list(self.loaded_plugins.keys())
