#!/usr/bin/env python3
"""
Sara AI Configuration
Performance and feature settings
"""

# ========================================
# PERFORMANCE SETTINGS
# ========================================

# Voice Engine Performance
VOICE_SETTINGS = {
    'wake_word_timeout': 0.5,  # Reduced from 1.0 for faster response
    'command_timeout': 5,      # Reduced from 10
    'audio_chunk_size': 1024,  # Smaller chunks for faster processing
    'sample_rate': 16000,      # Standard rate for good quality/performance balance
    'pause_threshold': 0.8,    # Faster speech detection
    'energy_threshold': 300,   # Auto-adjust based on ambient noise
    'dynamic_energy_threshold': True
}

# AI Engine Performance  
AI_SETTINGS = {
    'use_local_ai': False,     # Disable by default for speed
    'use_rule_based_only': True,  # Much faster than AI models
    'response_cache': True,    # Cache common responses
    'max_cache_size': 100,     # Limit memory usage
    'ai_timeout': 2.0,         # Quick timeout for AI requests
    'fallback_to_rules': True  # Always fallback to rules if AI is slow
}

# System Performance
SYSTEM_SETTINGS = {
    'automation_delay': 0.3,   # Reduced from 0.5
    'fast_mode': True,         # Skip unnecessary delays
    'parallel_processing': True,  # Use threading where possible
    'minimize_logging': False,  # Set to True in production
    'cache_app_mappings': True,
    'preload_modules': True
}

# ========================================
# FEATURE TOGGLES (Disable unused features)
# ========================================

FEATURES = {
    # Core features (always enabled)
    'voice_commands': True,
    'app_launcher': True,
    'system_control': True,
    'browser_control': True,
    'code_writer': True,
    
    # Optional features (disable to improve performance)
    'music_control': True,     # Set to False if not using music
    'file_manager': True,      # Set to False if not using file ops
    'uninstall_manager': False, # Slow registry scanning - disable by default
    
    # Advanced features (disable for performance)
    'ai_chat': False,          # Disable AI chat for speed
    'offline_stt': False,      # Use online STT (faster startup)
    'computer_vision': False,  # Disable CV features
    'advanced_nlp': False      # Disable heavy NLP processing
}

# ========================================
# AUDIO SETTINGS
# ========================================

AUDIO_SETTINGS = {
    'use_pygame': True,        # Faster than alternatives
    'audio_buffer_size': 512,  # Smaller buffer for responsiveness
    'use_system_volume': True, # Faster than programmatic control
    'skip_audio_calibration': False,  # Keep for accuracy
    'audio_format': 'mp3',     # Compressed format for speed
    'max_audio_length': 300    # 5 minutes max to avoid memory issues
}

# ========================================
# STARTUP OPTIMIZATION
# ========================================

STARTUP_SETTINGS = {
    'skip_module_tests': True,     # Skip time-consuming tests
    'lazy_load_modules': True,     # Load modules only when needed
    'background_initialization': True,  # Initialize non-critical modules in background
    'quick_start_mode': True,      # Minimal initialization for fast startup
    'preload_common_apps': True,   # Cache common application paths
    'disable_update_checks': True  # Skip version/update checks at startup
}

# ========================================
# MEMORY OPTIMIZATION
# ========================================

MEMORY_SETTINGS = {
    'max_history_items': 50,       # Limit command history
    'clear_cache_interval': 300,   # Clear caches every 5 minutes
    'max_log_file_size': 10,       # 10MB max log file
    'garbage_collect_interval': 60, # Force garbage collection every minute
    'limit_concurrent_operations': 3  # Max 3 operations at once
}

# ========================================
# NETWORK SETTINGS
# ========================================

NETWORK_SETTINGS = {
    'connection_timeout': 2.0,     # Quick timeout for network requests
    'max_retries': 1,              # Limit retries
    'use_connection_pooling': True,
    'dns_cache_timeout': 300,      # 5 minute DNS cache
    'disable_ssl_verification': False  # Keep security
}

# ========================================
# DEVELOPMENT/DEBUG SETTINGS
# ========================================

DEBUG_SETTINGS = {
    'debug_mode': False,
    'verbose_logging': False,
    'profile_performance': False,
    'log_timing': False,
    'show_memory_usage': False
}

# ========================================
# PLATFORM-SPECIFIC OPTIMIZATIONS
# ========================================

import platform

PLATFORM_OPTIMIZATIONS = {
    'windows': {
        'use_win32_api': True,         # Use native Windows APIs
        'disable_transparency': True,   # Disable UI transparency
        'high_dpi_aware': True,        # Better performance on high DPI
        'process_priority': 'normal'    # Don't interfere with system
    }
}

# Apply platform-specific settings
CURRENT_PLATFORM = platform.system().lower()
if CURRENT_PLATFORM in PLATFORM_OPTIMIZATIONS:
    globals().update(PLATFORM_OPTIMIZATIONS[CURRENT_PLATFORM])

# ========================================
# DYNAMIC SETTINGS BASED ON SYSTEM
# ========================================

import psutil

def get_optimized_settings():
    """Get settings optimized for current system"""
    cpu_count = psutil.cpu_count()
    memory_gb = psutil.virtual_memory().total / (1024**3)
    
    settings = {}
    
    # Adjust based on CPU cores
    if cpu_count >= 8:
        settings['max_worker_threads'] = 4
        settings['parallel_processing'] = True
    elif cpu_count >= 4:
        settings['max_worker_threads'] = 2
        settings['parallel_processing'] = True
    else:
        settings['max_worker_threads'] = 1
        settings['parallel_processing'] = False
    
    # Adjust based on RAM
    if memory_gb >= 16:
        settings['cache_size'] = 200
        settings['preload_modules'] = True
    elif memory_gb >= 8:
        settings['cache_size'] = 100
        settings['preload_modules'] = True
    else:
        settings['cache_size'] = 50
        settings['preload_modules'] = False
        settings['minimize_memory_usage'] = True
    
    return settings

# Apply dynamic optimizations
DYNAMIC_SETTINGS = get_optimized_settings()

# ========================================
# PERFORMANCE MONITORING
# ========================================

MONITORING_SETTINGS = {
    'enable_performance_monitoring': False,  # Enable if you want to track performance
    'performance_log_interval': 30,          # Log performance every 30 seconds
    'memory_threshold_warning': 500,         # Warn if using >500MB
    'cpu_threshold_warning': 80              # Warn if using >80% CPU
}
