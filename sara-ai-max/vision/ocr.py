"""
OCR Engine - Optical Character Recognition for reading screen text.

This module provides OCR capabilities using Tesseract and easyocr.
"""

import logging
from typing import Optional, List, Tuple
from pathlib import Path

logger = logging.getLogger(__name__)


class OCREngine:
    """Optical Character Recognition engine."""
    
    def __init__(self, engine: str = "tesseract"):
        """
        Initialize OCR engine.
        
        Args:
            engine: OCR engine to use (tesseract or easyocr)
        """
        self.engine_type = engine
        self.tesseract_available = False
        self.easyocr_available = False
        
        # Try to import OCR libraries
        try:
            import pytesseract
            self.tesseract_available = True
            logger.info("Tesseract OCR available")
        except ImportError:
            logger.warning("Tesseract not available. Install with: pip install pytesseract")
        
        try:
            import easyocr
            self.easyocr_available = True
            logger.info("EasyOCR available")
        except ImportError:
            logger.warning("EasyOCR not available. Install with: pip install easyocr")
    
    def read_image(self, image_path: str) -> str:
        """
        Extract text from an image file.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Extracted text
        """
        try:
            if self.engine_type == "tesseract" and self.tesseract_available:
                return self._tesseract_read(image_path)
            elif self.engine_type == "easyocr" and self.easyocr_available:
                return self._easyocr_read(image_path)
            else:
                logger.error(f"OCR engine {self.engine_type} not available")
                return ""
        except Exception as e:
            logger.error(f"Error reading image: {e}")
            return ""
    
    def read_screen_region(
        self,
        x: int,
        y: int,
        width: int,
        height: int
    ) -> str:
        """
        Read text from a specific screen region.
        
        Args:
            x: X coordinate
            y: Y coordinate
            width: Region width
            height: Region height
            
        Returns:
            Extracted text
        """
        try:
            # Capture screen region first
            from PIL import ImageGrab
            
            bbox = (x, y, x + width, y + height)
            screenshot = ImageGrab.grab(bbox)
            
            # Save temporarily
            temp_path = "temp_ocr.png"
            screenshot.save(temp_path)
            
            # Read with OCR
            text = self.read_image(temp_path)
            
            # Clean up
            Path(temp_path).unlink(missing_ok=True)
            
            return text
            
        except Exception as e:
            logger.error(f"Error reading screen region: {e}")
            return ""
    
    def find_text_on_screen(self, search_text: str) -> Optional[Tuple[int, int]]:
        """
        Find specific text on screen and return its location.
        
        Args:
            search_text: Text to find
            
        Returns:
            (x, y) coordinates or None
        """
        try:
            from PIL import ImageGrab
            
            # Capture full screen
            screenshot = ImageGrab.grab()
            temp_path = "temp_screen.png"
            screenshot.save(temp_path)
            
            # Read all text with locations
            # This requires more advanced OCR with bounding boxes
            logger.warning("Text location finding requires advanced OCR setup")
            
            Path(temp_path).unlink(missing_ok=True)
            return None
            
        except Exception as e:
            logger.error(f"Error finding text: {e}")
            return None
    
    def _tesseract_read(self, image_path: str) -> str:
        """Read image using Tesseract."""
        try:
            import pytesseract
            from PIL import Image
            
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)
            logger.info(f"Tesseract extracted {len(text)} characters")
            return text.strip()
            
        except Exception as e:
            logger.error(f"Tesseract error: {e}")
            return ""
    
    def _easyocr_read(self, image_path: str) -> str:
        """Read image using EasyOCR."""
        try:
            import easyocr
            
            reader = easyocr.Reader(['en'])
            result = reader.readtext(image_path)
            
            # Combine all detected text
            text = ' '.join([detection[1] for detection in result])
            logger.info(f"EasyOCR extracted {len(text)} characters")
            return text.strip()
            
        except Exception as e:
            logger.error(f"EasyOCR error: {e}")
            return ""
