"""
Screenshot Capture - Advanced screen capture capabilities.

This module provides comprehensive screenshot functionality.
"""

import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple

logger = logging.getLogger(__name__)


class ScreenshotCapture:
    """Advanced screenshot capture."""
    
    def __init__(self, default_save_dir: Optional[str] = None):
        """
        Initialize screenshot capture.
        
        Args:
            default_save_dir: Default directory for saving screenshots
        """
        if default_save_dir:
            self.save_dir = Path(default_save_dir)
        else:
            self.save_dir = Path.home() / "Pictures" / "Sara_Screenshots"
        
        # Create directory if it doesn't exist
        self.save_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Screenshot save directory: {self.save_dir}")
    
    def capture_full_screen(self, filename: Optional[str] = None) -> str:
        """
        Capture the full screen.
        
        Args:
            filename: Optional custom filename
            
        Returns:
            Path to saved screenshot
        """
        try:
            from PIL import ImageGrab
            
            screenshot = ImageGrab.grab()
            
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"screenshot_{timestamp}.png"
            
            filepath = self.save_dir / filename
            screenshot.save(filepath)
            
            logger.info(f"Screenshot saved: {filepath}")
            return str(filepath)
            
        except Exception as e:
            logger.error(f"Error capturing screenshot: {e}")
            return ""
    
    def capture_region(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        filename: Optional[str] = None
    ) -> str:
        """
        Capture a specific screen region.
        
        Args:
            x: X coordinate
            y: Y coordinate
            width: Region width
            height: Region height
            filename: Optional custom filename
            
        Returns:
            Path to saved screenshot
        """
        try:
            from PIL import ImageGrab
            
            bbox = (x, y, x + width, y + height)
            screenshot = ImageGrab.grab(bbox)
            
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"region_{timestamp}.png"
            
            filepath = self.save_dir / filename
            screenshot.save(filepath)
            
            logger.info(f"Region screenshot saved: {filepath}")
            return str(filepath)
            
        except Exception as e:
            logger.error(f"Error capturing region: {e}")
            return ""
    
    def capture_window(self, window_title: str, filename: Optional[str] = None) -> str:
        """
        Capture a specific window.
        
        Args:
            window_title: Title of the window to capture
            filename: Optional custom filename
            
        Returns:
            Path to saved screenshot
        """
        try:
            # Window-specific capture requires platform-specific code
            logger.warning("Window capture requires platform-specific implementation")
            return self.capture_full_screen(filename)
            
        except Exception as e:
            logger.error(f"Error capturing window: {e}")
            return ""
    
    def get_screen_size(self) -> Tuple[int, int]:
        """
        Get screen dimensions.
        
        Returns:
            (width, height) tuple
        """
        try:
            from PIL import ImageGrab
            
            screenshot = ImageGrab.grab()
            return screenshot.size
            
        except Exception as e:
            logger.error(f"Error getting screen size: {e}")
            return (0, 0)
