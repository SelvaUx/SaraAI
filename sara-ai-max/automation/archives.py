"""
Archives - ZIP, 7Z, RAR file handling.

This module provides archive compression and extraction.
"""

import logging
from pathlib import Path
from typing import Optional, List
import zipfile
import shutil

logger = logging.getLogger(__name__)


def create_zip(
    files: List[str],
    output_path: str,
    compression_level: int = 9
) -> bool:
    """
    Create a ZIP archive.
    
    Args:
        files: List of file paths to include
        output_path: Output ZIP file path
        compression_level: Compression level (0-9)
        
    Returns:
        True if successful
    """
    try:
        with zipfile.ZipFile(
            output_path,
            'w',
            zipfile.ZIP_DEFLATED,
            compresslevel=compression_level
        ) as zipf:
            for file_path in files:
                path = Path(file_path)
                if path.exists():
                    zipf.write(file_path, path.name)
                    logger.info(f"Added to archive: {file_path}")
        
        logger.info(f"Created ZIP archive: {output_path}")
        return True
        
    except Exception as e:
        logger.error(f"Error creating ZIP: {e}")
        return False


def extract_zip(
    archive_path: str,
    destination: Optional[str] = None
) -> bool:
    """
    Extract a ZIP archive.
    
    Args:
        archive_path: Path to ZIP file
        destination: Optional extraction destination
        
    Returns:
        True if successful
    """
    try:
        if not destination:
            destination = str(Path(archive_path).parent / "extracted")
        
        with zipfile.ZipFile(archive_path, 'r') as zipf:
            zipf.extractall(destination)
        
        logger.info(f"Extracted ZIP to: {destination}")
        return True
        
    except Exception as e:
        logger.error(f"Error extracting ZIP: {e}")
        return False


def compress_folder(
    folder_path: str,
    output_path: Optional[str] = None
) -> bool:
    """
    Compress an entire folder to ZIP.
    
    Args:
        folder_path: Folder to compress
        output_path: Optional output path
        
    Returns:
        True if successful
    """
    try:
        folder = Path(folder_path)
        
        if not folder.exists() or not folder.is_dir():
            logger.error(f"Folder not found: {folder_path}")
            return False
        
        if not output_path:
            output_path = str(folder.parent / f"{folder.name}.zip")
        
        # Create archive
        shutil.make_archive(
            str(Path(output_path).with_suffix('')),
            'zip',
            folder_path
        )
        
        logger.info(f"Compressed folder to: {output_path}")
        return True
        
    except Exception as e:
        logger.error(f"Error compressing folder: {e}")
        return False


def list_archive_contents(archive_path: str) -> List[str]:
    """
    List contents of a ZIP archive.
    
    Args:
        archive_path: Path to ZIP file
        
    Returns:
        List of file names in archive
    """
    try:
        with zipfile.ZipFile(archive_path, 'r') as zipf:
            return zipf.namelist()
            
    except Exception as e:
        logger.error(f"Error listing archive: {e}")
        return []
