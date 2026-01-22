"""
System Control - System information, volume, brightness, power management.

This module provides cross-platform system control functions.
"""

import logging
import platform
import subprocess
import webbrowser
from datetime import datetime
from typing import Optional
import psutil

logger = logging.getLogger(__name__)


def get_system_info(info_type: str = 'system') -> str:
    """
    Get system information.
    
    Args:
        info_type: Type of information (time, date, system)
        
    Returns:
        Information as a string
    """
    try:
        if info_type == 'time':
            now = datetime.now()
            return f"The current time is {now.strftime('%I:%M %p')}"
        
        elif info_type == 'date':
            now = datetime.now()
            return f"Today is {now.strftime('%A, %B %d, %Y')}"
        
        elif info_type == 'system':
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            return (
                f"CPU usage: {cpu_percent}%, "
                f"Memory usage: {memory.percent}%, "
                f"Disk usage: {disk.percent}%"
            )
        
        else:
            return "Unknown information type"
            
    except Exception as e:
        logger.error(f"Error getting system info: {e}")
        return "Sorry, I couldn't get that information"


def control_volume(action: str) -> bool:
    """
    Control system volume.
    
    Args:
        action: increase, decrease, or mute
        
    Returns:
        True if successful, False otherwise
    """
    try:
        logger.info(f"Volume control: {action}")
        
        # Platform-specific volume control
        if platform.system() == 'Windows':
            if action == 'increase':
                subprocess.run(['nircmd.exe', 'changesysvolume', '2000'], check=False)
            elif action == 'decrease':
                subprocess.run(['nircmd.exe', 'changesysvolume', '-2000'], check=False)
            elif action == 'mute':
                subprocess.run(['nircmd.exe', 'mutesysvolume', '1'], check=False)
            elif action == 'unmute':
                subprocess.run(['nircmd.exe', 'mutesysvolume', '0'], check=False)
            return True
        else:
            logger.warning("Volume control not implemented for this platform")
            return False
            
    except Exception as e:
        logger.error(f"Error controlling volume: {e}")
        return False


def control_brightness(action: str) -> bool:
    """
    Control screen brightness.
    
    Args:
        action: increase or decrease
        
    Returns:
        True if successful, False otherwise
    """
    try:
        logger.info(f"Brightness control: {action}")
        
        # Brightness control is platform-specific and complex
        # For MVP, we'll log the action
        logger.warning("Brightness control not yet fully implemented")
        return False
        
    except Exception as e:
        logger.error(f"Error controlling brightness: {e}")
        return False


def web_search(query: str) -> bool:
    """
    Open a web search in the default browser.
    
    Args:
        query: Search query
        
    Returns:
        True if successful, False otherwise
    """
    try:
        logger.info(f"Web search: {query}")
        
        # Open Google search
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(search_url)
        return True
        
    except Exception as e:
        logger.error(f"Error performing web search: {e}")
        return False


def shutdown():
    """Shutdown the computer."""
    try:
        logger.info("Shutting down system")
        
        if platform.system() == 'Windows':
            subprocess.run(['shutdown', '/s', '/t', '5'], check=False)
        else:
            subprocess.run(['shutdown', '-h', 'now'], check=False)
            
    except Exception as e:
        logger.error(f"Error shutting down: {e}")


def restart():
    """Restart the computer."""
    try:
        logger.info("Restarting system")
        
        if platform.system() == 'Windows':
            subprocess.run(['shutdown', '/r', '/t', '5'], check=False)
        else:
            subprocess.run(['shutdown', '-r', 'now'], check=False)
            
    except Exception as e:
        logger.error(f"Error restarting: {e}")


def lock_screen():
    """Lock the screen."""
    try:
        logger.info("Locking screen")
        
        if platform.system() == 'Windows':
            subprocess.run(['rundll32.exe', 'user32.dll,LockWorkStation'], check=False)
        elif platform.system() == 'Darwin':  # macOS
            subprocess.run(['/System/Library/CoreServices/Menu Extras/User.menu/Contents/Resources/CGSession', '-suspend'], check=False)
        else:  # Linux
            subprocess.run(['xdg-screensaver', 'lock'], check=False)
            
    except Exception as e:
        logger.error(f"Error locking screen: {e}")
