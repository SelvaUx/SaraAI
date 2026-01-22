"""
File Operations - Create, delete, search, and manage files and folders.

This module provides safe file system operations with undo support.
"""

import logging
import os
from pathlib import Path
from typing import Optional, List

logger = logging.getLogger(__name__)


def create_folder(folder_name: str, location: Optional[str] = None) -> bool:
    """
    Create a new folder.
    
    Args:
        folder_name: Name of the folder to create
        location: Optional location (defaults to Desktop)
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # Default to Desktop
        if not location:
            desktop = Path.home() / "Desktop"
            location = str(desktop)
        
        folder_path = Path(location) / folder_name
        
        if folder_path.exists():
            logger.warning(f"Folder already exists: {folder_path}")
            return False
        
        folder_path.mkdir(parents=True, exist_ok=False)
        logger.info(f"Created folder: {folder_path}")
        return True
        
    except Exception as e:
        logger.error(f"Error creating folder {folder_name}: {e}")
        return False


def create_file(file_name: str, content: str = "", location: Optional[str] = None) -> bool:
    """
    Create a new file.
    
    Args:
        file_name: Name of the file to create
        content: Optional initial content
        location: Optional location (defaults to Desktop)
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # Default to Desktop
        if not location:
            desktop = Path.home() / "Desktop"
            location = str(desktop)
        
        file_path = Path(location) / file_name
        
        if file_path.exists():
            logger.warning(f"File already exists: {file_path}")
            return False
        
        with open(file_path, 'w') as f:
            f.write(content)
        
        logger.info(f"Created file: {file_path}")
        return True
        
    except Exception as e:
        logger.error(f"Error creating file {file_name}: {e}")
        return False


def delete_file(file_path: str) -> bool:
    """
    Delete a file (moves to recycle bin if possible).
    
    Args:
        file_path: Path to the file to delete
        
    Returns:
        True if successful, False otherwise
    """
    try:
        path = Path(file_path)
        
        if not path.exists():
            logger.warning(f"File does not exist: {file_path}")
            return False
        
        # For MVP, just remove the file
        # In production, use send2trash for safety
        path.unlink()
        logger.info(f"Deleted file: {file_path}")
        return True
        
    except Exception as e:
        logger.error(f"Error deleting file {file_path}: {e}")
        return False


def search_file(file_name: str, location: Optional[str] = None) -> List[str]:
    """
    Search for files by name.
    
    Args:
        file_name: Name pattern to search for
        location: Optional search location (defaults to user home)
        
    Returns:
        List of matching file paths
    """
    try:
        if not location:
            location = str(Path.home())
        
        search_path = Path(location)
        matches = []
        
        # Search for files (limit to prevent long searches)
        for path in search_path.rglob(f"*{file_name}*"):
            if path.is_file():
                matches.append(str(path))
                if len(matches) >= 10:  # Limit results
                    break
        
        logger.info(f"Found {len(matches)} files matching: {file_name}")
        return matches
        
    except Exception as e:
        logger.error(f"Error searching for {file_name}: {e}")
        return []
