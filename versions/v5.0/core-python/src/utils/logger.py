"""
SaraAI Logging Configuration
Structured logging setup with rich formatting
"""

import logging
import sys
from pathlib import Path
from typing import Optional
import structlog
from rich.console import Console
from rich.logging import RichHandler


def setup_logging(level: str = "INFO", log_file: Optional[Path] = None) -> structlog.BoundLogger:
    """
    Setup structured logging with rich formatting
    
    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR)
        log_file: Optional file path for logging
    
    Returns:
        Configured logger instance
    """
    
    # Configure standard library logging
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(message)s",
        datefmt="[%X]",
        handlers=[
            RichHandler(
                console=Console(stderr=True),
                show_time=True,
                show_path=True,
                rich_tracebacks=True,
                tracebacks_show_locals=True
            )
        ]
    )
    
    # Add file handler if specified
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(getattr(logging, level.upper()))
        file_handler.setFormatter(
            logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
        )
        logging.getLogger().addHandler(file_handler)
    
    # Configure structlog
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.add_logger_name,
            structlog.processors.TimeStamper(fmt="ISO"),
            structlog.dev.ConsoleRenderer(colors=True)
        ],
        wrapper_class=structlog.make_filtering_bound_logger(
            getattr(logging, level.upper())
        ),
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )
    
    # Return the logger
    logger = structlog.get_logger("saraai")
    return logger


def get_logger(name: str) -> structlog.BoundLogger:
    """Get a logger instance for a specific module"""
    return structlog.get_logger(name)


# Custom log formatters for different contexts
class ModuleLogFormatter:
    """Custom formatter for module-specific logging"""
    
    def __init__(self, module_name: str):
        self.module_name = module_name
    
    def format_message(self, level: str, message: str, **kwargs) -> str:
        """Format a log message with module context"""
        prefix_map = {
            "speech": "🎙️",
            "tts": "🔊", 
            "system": "⚙️",
            "knowledge": "📚",
            "dashboard": "🌐",
            "orchestrator": "🧠",
            "ai_brain": "🤖"
        }
        
        prefix = prefix_map.get(self.module_name, "📋")
        formatted = f"{prefix} [{self.module_name.upper()}] {message}"
        
        if kwargs:
            context_parts = [f"{k}={v}" for k, v in kwargs.items()]
            formatted += f" | {' '.join(context_parts)}"
        
        return formatted


# Helper functions for common logging patterns
def log_module_start(logger: structlog.BoundLogger, module_name: str):
    """Log module startup"""
    logger.info(f"🚀 Starting {module_name} module...")


def log_module_ready(logger: structlog.BoundLogger, module_name: str):
    """Log module ready state"""
    logger.info(f"✅ {module_name} module is ready")


def log_module_error(logger: structlog.BoundLogger, module_name: str, error: Exception):
    """Log module error"""
    logger.error(f"❌ {module_name} module error: {error}", exc_info=True)


def log_module_stop(logger: structlog.BoundLogger, module_name: str):
    """Log module shutdown"""
    logger.info(f"🛑 Stopping {module_name} module...")


def log_api_request(logger: structlog.BoundLogger, method: str, endpoint: str, status: int):
    """Log API request"""
    status_emoji = "✅" if 200 <= status < 300 else "⚠️" if 300 <= status < 400 else "❌"
    logger.info(f"{status_emoji} {method} {endpoint} -> {status}")


def log_voice_command(logger: structlog.BoundLogger, command: str, confidence: float):
    """Log voice command recognition"""
    confidence_emoji = "🎯" if confidence > 0.8 else "🔍" if confidence > 0.6 else "❓"
    logger.info(f"{confidence_emoji} Voice: '{command}' (confidence: {confidence:.2f})")


def log_system_action(logger: structlog.BoundLogger, action: str, result: str):
    """Log system action execution"""
    logger.info(f"⚙️ System: {action} -> {result}")


def log_knowledge_query(logger: structlog.BoundLogger, query: str, results_count: int):
    """Log knowledge base query"""
    logger.info(f"📚 Knowledge: '{query}' -> {results_count} results")


# Performance logging helpers
class PerformanceTimer:
    """Context manager for timing operations"""
    
    def __init__(self, logger: structlog.BoundLogger, operation: str):
        self.logger = logger
        self.operation = operation
        self.start_time = None
    
    def __enter__(self):
        import time
        self.start_time = time.time()
        self.logger.debug(f"⏱️ Starting {self.operation}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        duration = time.time() - self.start_time
        
        if exc_type:
            self.logger.error(f"❌ {self.operation} failed after {duration:.2f}s")
        else:
            emoji = "⚡" if duration < 1.0 else "🐌" if duration > 10.0 else "⏱️"
            self.logger.info(f"{emoji} {self.operation} completed in {duration:.2f}s")


# Error tracking
class ErrorTracker:
    """Track and log recurring errors"""
    
    def __init__(self, logger: structlog.BoundLogger):
        self.logger = logger
        self.error_counts = {}
    
    def log_error(self, error_key: str, error: Exception, max_count: int = 5):
        """Log an error with frequency tracking"""
        self.error_counts[error_key] = self.error_counts.get(error_key, 0) + 1
        count = self.error_counts[error_key]
        
        if count <= max_count:
            self.logger.error(
                f"❌ Error ({count}x): {error}",
                error_key=error_key,
                count=count,
                exc_info=True
            )
        elif count == max_count + 1:
            self.logger.error(
                f"🔇 Suppressing further '{error_key}' errors (occurred {count}x)",
                error_key=error_key
            )
    
    def reset_error_count(self, error_key: str):
        """Reset the error count for a specific key"""
        if error_key in self.error_counts:
            del self.error_counts[error_key]
    
    def get_error_summary(self) -> dict:
        """Get summary of all tracked errors"""
        return dict(self.error_counts)