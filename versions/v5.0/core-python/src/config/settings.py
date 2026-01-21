"""
SaraAI Configuration Settings
Centralized configuration management
"""

from dataclasses import dataclass, field
from typing import Dict, Any, Optional
from pathlib import Path
import os
import yaml
from dotenv import load_dotenv


@dataclass
class ModuleConfig:
    """Configuration for individual modules"""
    enabled: bool = True
    host: str = "localhost"
    port: int = 8000
    timeout: float = 30.0
    retry_attempts: int = 3
    config: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Settings:
    """Main configuration for SaraAI"""
    
    # Core settings
    app_name: str = "SaraAI 5.0"
    version: str = "5.0.0"
    debug: bool = False
    log_level: str = "INFO"
    
    # API settings
    api_host: str = "localhost"
    api_port: int = 8000
    
    # Dashboard settings
    dashboard_host: str = "localhost"
    dashboard_port: int = 3000
    
    # Module configurations
    speech_config: ModuleConfig = field(default_factory=lambda: ModuleConfig(port=8001))
    tts_config: ModuleConfig = field(default_factory=lambda: ModuleConfig(port=8002))
    system_config: ModuleConfig = field(default_factory=lambda: ModuleConfig(port=8003))
    knowledge_config: ModuleConfig = field(default_factory=lambda: ModuleConfig(port=8004))
    
    # AI settings
    wake_words: list = field(default_factory=lambda: ["sara", "hey sara", "computer", "assistant"])
    response_timeout: float = 5.0
    confidence_threshold: float = 0.7
    
    # Wake word detection settings
    wake_word_enabled: bool = True
    wake_word_sensitivity: float = 0.6
    audio_threshold: float = 0.01
    listening_timeout: float = 30.0  # seconds of silence before stopping listening
    wake_word_timeout: float = 3.0   # seconds to wait for command after wake word
    
    # Database settings
    database_url: str = "sqlite:///saraai.db"
    
    # File paths
    config_dir: Path = field(default_factory=lambda: Path.cwd() / "config")
    data_dir: Path = field(default_factory=lambda: Path.cwd() / "data")
    logs_dir: Path = field(default_factory=lambda: Path.cwd() / "logs")
    
    def __post_init__(self):
        """Ensure directories exist"""
        for directory in [self.config_dir, self.data_dir, self.logs_dir]:
            directory.mkdir(parents=True, exist_ok=True)


def load_settings(config_file: Optional[Path] = None) -> Settings:
    """Load settings from environment, config file, and defaults"""
    
    # Load environment variables
    load_dotenv()
    
    # Start with default settings
    settings = Settings()
    
    # Override with config file if provided
    if config_file and config_file.exists():
        try:
            with open(config_file, 'r') as f:
                config_data = yaml.safe_load(f)
                _update_settings_from_dict(settings, config_data)
        except Exception as e:
            print(f"Warning: Could not load config file {config_file}: {e}")
    
    # Override with environment variables
    _update_settings_from_env(settings)
    
    return settings


def _update_settings_from_dict(settings: Settings, config_dict: Dict[str, Any]):
    """Update settings from a dictionary"""
    for key, value in config_dict.items():
        if hasattr(settings, key):
            current_value = getattr(settings, key)
            
            # Handle nested ModuleConfig objects
            if isinstance(current_value, ModuleConfig) and isinstance(value, dict):
                for module_key, module_value in value.items():
                    if hasattr(current_value, module_key):
                        setattr(current_value, module_key, module_value)
            else:
                setattr(settings, key, value)


def _update_settings_from_env(settings: Settings):
    """Update settings from environment variables"""
    env_mappings = {
        "SARAAI_DEBUG": ("debug", lambda x: x.lower() == "true"),
        "SARAAI_LOG_LEVEL": ("log_level", str),
        "SARAAI_API_HOST": ("api_host", str),
        "SARAAI_API_PORT": ("api_port", int),
        "SARAAI_DASHBOARD_HOST": ("dashboard_host", str),
        "SARAAI_DASHBOARD_PORT": ("dashboard_port", int),
        "SARAAI_DATABASE_URL": ("database_url", str),
        
        # Module-specific environment variables
        "SARAAI_SPEECH_HOST": ("speech_config.host", str),
        "SARAAI_SPEECH_PORT": ("speech_config.port", int),
        "SARAAI_TTS_HOST": ("tts_config.host", str),
        "SARAAI_TTS_PORT": ("tts_config.port", int),
        "SARAAI_SYSTEM_HOST": ("system_config.host", str),
        "SARAAI_SYSTEM_PORT": ("system_config.port", int),
        "SARAAI_KNOWLEDGE_HOST": ("knowledge_config.host", str),
        "SARAAI_KNOWLEDGE_PORT": ("knowledge_config.port", int),
        
        # Wake word settings
        "SARAAI_WAKE_WORD_ENABLED": ("wake_word_enabled", lambda x: x.lower() == "true"),
        "SARAAI_WAKE_WORD_SENSITIVITY": ("wake_word_sensitivity", float),
        "SARAAI_AUDIO_THRESHOLD": ("audio_threshold", float),
    }
    
    for env_var, (attr_path, converter) in env_mappings.items():
        env_value = os.getenv(env_var)
        if env_value is not None:
            try:
                converted_value = converter(env_value)
                _set_nested_attr(settings, attr_path, converted_value)
            except (ValueError, TypeError) as e:
                print(f"Warning: Invalid value for {env_var}: {e}")


def _set_nested_attr(obj: Any, attr_path: str, value: Any):
    """Set a nested attribute using dot notation"""
    attrs = attr_path.split('.')
    current = obj
    
    # Navigate to the parent object
    for attr in attrs[:-1]:
        current = getattr(current, attr)
    
    # Set the final attribute
    setattr(current, attrs[-1], value)


def save_settings(settings: Settings, config_file: Path):
    """Save settings to a YAML config file"""
    config_dict = {
        "debug": settings.debug,
        "log_level": settings.log_level,
        "api_host": settings.api_host,
        "api_port": settings.api_port,
        "dashboard_host": settings.dashboard_host,
        "dashboard_port": settings.dashboard_port,
        "database_url": settings.database_url,
        
        "speech_config": {
            "enabled": settings.speech_config.enabled,
            "host": settings.speech_config.host,
            "port": settings.speech_config.port,
            "timeout": settings.speech_config.timeout,
        },
        
        "tts_config": {
            "enabled": settings.tts_config.enabled,
            "host": settings.tts_config.host,
            "port": settings.tts_config.port,
            "timeout": settings.tts_config.timeout,
        },
        
        "system_config": {
            "enabled": settings.system_config.enabled,
            "host": settings.system_config.host,
            "port": settings.system_config.port,
            "timeout": settings.system_config.timeout,
        },
        
        "knowledge_config": {
            "enabled": settings.knowledge_config.enabled,
            "host": settings.knowledge_config.host,
            "port": settings.knowledge_config.port,
            "timeout": settings.knowledge_config.timeout,
        },
        
        "wake_words": settings.wake_words,
        "response_timeout": settings.response_timeout,
        "confidence_threshold": settings.confidence_threshold,
    }
    
    try:
        config_file.parent.mkdir(parents=True, exist_ok=True)
        with open(config_file, 'w') as f:
            yaml.safe_dump(config_dict, f, default_flow_style=False, indent=2)
    except Exception as e:
        print(f"Error saving config file: {e}")
        raise