"""
UI Finder - Find UI elements using template matching and object detection.

This module provides visual UI element detection on screen.
"""

import logging
from typing import Optional, Tuple, List
import numpy as np

logger = logging.getLogger(__name__)


class UIFinder:
    """Find UI elements on screen using computer vision."""
    
    def __init__(self):
        """Initialize UI finder."""
        self.cv2_available = False
        
        try:
            import cv2
            self.cv2_available = True
            logger.info("OpenCV available for UI finding")
        except ImportError:
            logger.warning("OpenCV not available. Install with: pip install opencv-python")
    
    def find_template(
        self,
        template_path: str,
        threshold: float = 0.8
    ) -> Optional[Tuple[int, int]]:
        """
        Find a UI element by template matching.
        
        Args:
            template_path: Path to template image
            threshold: Match threshold (0-1)
            
        Returns:
            (x, y) coordinates of match or None
        """
        if not self.cv2_available:
            logger.error("OpenCV not available")
            return None
        
        try:
            import cv2
            from PIL import ImageGrab
            
            # Capture screen
            screenshot = ImageGrab.grab()
            screen_np = np.array(screenshot)
            screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
            
            # Load template
            template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
            
            # Perform template matching
            result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
            if max_val >= threshold:
                logger.info(f"Template found at {max_loc} with confidence {max_val}")
                return max_loc
            else:
                logger.info(f"Template not found (best match: {max_val})")
                return None
                
        except Exception as e:
            logger.error(f"Error finding template: {e}")
            return None
    
    def find_all_templates(
        self,
        template_path: str,
        threshold: float = 0.8
    ) -> List[Tuple[int, int]]:
        """
        Find all occurrences of a template on screen.
        
        Args:
            template_path: Path to template image
            threshold: Match threshold (0-1)
            
        Returns:
            List of (x, y) coordinates
        """
        if not self.cv2_available:
            logger.error("OpenCV not available")
            return []
        
        try:
            import cv2
            from PIL import ImageGrab
            
            # Capture screen
            screenshot = ImageGrab.grab()
            screen_np = np.array(screenshot)
            screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
            
            # Load template
            template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
            h, w = template.shape
            
            # Perform template matching
            result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
            
            # Find all matches above threshold
            locations = np.where(result >= threshold)
            matches = list(zip(*locations[::-1]))
            
            logger.info(f"Found {len(matches)} template matches")
            return matches
            
        except Exception as e:
            logger.error(f"Error finding templates: {e}")
            return []
    
    def find_color(
        self,
        color_rgb: Tuple[int, int, int],
        tolerance: int = 10
    ) -> List[Tuple[int, int]]:
        """
        Find pixels of a specific color on screen.
        
        Args:
            color_rgb: RGB color tuple
            tolerance: Color match tolerance
            
        Returns:
            List of (x, y) coordinates
        """
        if not self.cv2_available:
            logger.error("OpenCV not available")
            return []
        
        try:
            import cv2
            from PIL import ImageGrab
            
            # Capture screen
            screenshot = ImageGrab.grab()
            screen_np = np.array(screenshot)
            
            # Create color range
            lower = np.array([max(0, c - tolerance) for c in color_rgb])
            upper = np.array([min(255, c + tolerance) for c in color_rgb])
            
            # Find matching colors
            mask = cv2.inRange(screen_np, lower, upper)
            locations = np.where(mask > 0)
            matches = list(zip(*locations[::-1]))
            
            logger.info(f"Found {len(matches)} color matches")
            return matches[:100]  # Limit results
            
        except Exception as e:
            logger.error(f"Error finding color: {e}")
            return []
