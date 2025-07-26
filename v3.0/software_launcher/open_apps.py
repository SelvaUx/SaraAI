#!/usr/bin/env python3
"""
Sara AI Software Launcher
Opens applications and software via Windows search automation
"""

import os
import time
import logging
import pyautogui
import subprocess
from typing import Dict, List, Optional

class AppLauncher:
    def __init__(self):
        """Initialize application launcher"""
        self.logger = logging.getLogger('AppLauncher')
        
        # Common application mappings
        self.app_mappings = self.load_app_mappings()
        
        # Automation settings
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5
        
        print("🚀 App Launcher initialized")
        
    def load_app_mappings(self) -> Dict:
        """Load common application name mappings"""
        return {
            # Browsers
            "browser": "chrome",
            "chrome": "chrome",
            "firefox": "firefox",
            "edge": "microsoft edge",
            "internet explorer": "iexplore",
            
            # Text Editors
            "notepad": "notepad",
            "text editor": "notepad",
            "editor": "notepad",
            "vs code": "visual studio code",
            "vscode": "visual studio code",
            "visual studio": "visual studio",
            "atom": "atom",
            "sublime": "sublime text",
            
            # Media Players
            "media player": "windows media player",
            "vlc": "vlc",
            "music": "groove music",
            "music player": "groove music",
            "spotify": "spotify",
            "youtube music": "youtube music",
            
            # Office Applications
            "word": "microsoft word",
            "excel": "microsoft excel",
            "powerpoint": "microsoft powerpoint",
            "outlook": "microsoft outlook",
            "office": "microsoft office",
            
            # System Tools
            "calculator": "calculator",
            "calc": "calculator",
            "paint": "paint",
            "terminal": "windows terminal",
            "cmd": "command prompt",
            "powershell": "powershell",
            "task manager": "task manager",
            "control panel": "control panel",
            "settings": "settings",
            
            # File Management
            "file explorer": "file explorer",
            "explorer": "file explorer",
            "files": "file explorer",
            
            # Communication
            "teams": "microsoft teams",
            "skype": "skype",
            "discord": "discord",
            "zoom": "zoom",
            
            # Development Tools
            "git": "git bash",
            "github": "github desktop",
            "docker": "docker desktop",
            "postman": "postman",
            
            # Graphics
            "photoshop": "adobe photoshop",
            "illustrator": "adobe illustrator",
            "gimp": "gimp",
            
            # Games
            "steam": "steam",
            "epic games": "epic games launcher",
            "xbox": "xbox"
        }
        
    def open_application(self, app_name: str) -> bool:
        """Open application via Windows search"""
        try:
            # Normalize app name
            app_name = app_name.lower().strip()
            
            # Check for mapped applications
            search_term = self.app_mappings.get(app_name, app_name)
            
            self.logger.info(f"Opening application: {search_term}")
            
            # Press Windows key to open search
            pyautogui.press('win')
            time.sleep(1)
            
            # Type application name
            pyautogui.type(search_term)
            time.sleep(1.5)  # Wait for search results
            
            # Press Enter to open the first result
            pyautogui.press('enter')
            time.sleep(2)  # Wait for application to start
            
            self.logger.info(f"Application opened: {search_term}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error opening application: {e}")
            return False
            
    def open_multiple_apps(self, app_list: List[str]) -> bool:
        """Open multiple applications"""
        try:
            success_count = 0
            
            for app in app_list:
                if self.open_application(app):
                    success_count += 1
                    time.sleep(2)  # Delay between app launches
                    
            self.logger.info(f"Opened {success_count}/{len(app_list)} applications")
            return success_count == len(app_list)
            
        except Exception as e:
            self.logger.error(f"Error opening multiple applications: {e}")
            return False
            
    def close_application(self, app_name: str = None) -> bool:
        """Close current or specified application"""
        try:
            if app_name:
                # Find and close specific application
                self.logger.info(f"Closing application: {app_name}")
                # This would require more complex window management
                # For now, just close the active window
                
            # Close active window with Alt+F4
            pyautogui.hotkey('alt', 'f4')
            time.sleep(1)
            
            self.logger.info("Application closed")
            return True
            
        except Exception as e:
            self.logger.error(f"Error closing application: {e}")
            return False
            
    def switch_to_application(self, app_name: str) -> bool:
        """Switch to running application using Alt+Tab"""
        try:
            self.logger.info(f"Switching to: {app_name}")
            
            # Use Alt+Tab to switch applications
            pyautogui.hotkey('alt', 'tab')
            time.sleep(0.5)
            
            # Could implement more sophisticated window detection here
            # For now, just cycling through with Alt+Tab
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error switching to application: {e}")
            return False
            
    def minimize_all_windows(self) -> bool:
        """Minimize all windows (Windows + D)"""
        try:
            pyautogui.hotkey('win', 'd')
            self.logger.info("All windows minimized")
            return True
            
        except Exception as e:
            self.logger.error(f"Error minimizing windows: {e}")
            return False
            
    def show_desktop(self) -> bool:
        """Show desktop"""
        return self.minimize_all_windows()
        
    def open_start_menu(self) -> bool:
        """Open Windows Start Menu"""
        try:
            pyautogui.press('win')
            time.sleep(1)
            self.logger.info("Start menu opened")
            return True
            
        except Exception as e:
            self.logger.error(f"Error opening start menu: {e}")
            return False
            
    def open_run_dialog(self) -> bool:
        """Open Windows Run dialog"""
        try:
            pyautogui.hotkey('win', 'r')
            time.sleep(1)
            self.logger.info("Run dialog opened")
            return True
            
        except Exception as e:
            self.logger.error(f"Error opening run dialog: {e}")
            return False
            
    def run_command(self, command: str) -> bool:
        """Run command via Run dialog"""
        try:
            # Open Run dialog
            if not self.open_run_dialog():
                return False
                
            # Type command
            pyautogui.type(command)
            time.sleep(0.5)
            
            # Press Enter
            pyautogui.press('enter')
            time.sleep(1)
            
            self.logger.info(f"Command executed: {command}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error running command: {e}")
            return False
            
    def open_microsoft_store(self, search_term: str = None) -> bool:
        """Open Microsoft Store and optionally search"""
        try:
            self.logger.info("Opening Microsoft Store")
            
            if not self.open_application("microsoft store"):
                return False
                
            if search_term:
                time.sleep(3)  # Wait for store to load
                
                # Click search or use Ctrl+F
                pyautogui.hotkey('ctrl', 'f')
                time.sleep(1)
                
                # Type search term
                pyautogui.type(search_term)
                time.sleep(0.5)
                
                # Press Enter
                pyautogui.press('enter')
                
                self.logger.info(f"Searched in Microsoft Store: {search_term}")
                
            return True
            
        except Exception as e:
            self.logger.error(f"Error opening Microsoft Store: {e}")
            return False
            
    def get_running_applications(self) -> List[str]:
        """Get list of running applications (basic implementation)"""
        try:
            # Use tasklist command to get running processes
            result = subprocess.run(['tasklist'], capture_output=True, text=True)
            
            if result.returncode == 0:
                # Parse the output to extract application names
                lines = result.stdout.split('\n')
                apps = []
                
                for line in lines[3:]:  # Skip header lines
                    if line.strip():
                        parts = line.split()
                        if parts:
                            app_name = parts[0]
                            if not app_name.endswith('.exe'):
                                app_name += '.exe'
                            apps.append(app_name)
                            
                return apps[:20]  # Return first 20 for brevity
            else:
                return []
                
        except Exception as e:
            self.logger.error(f"Error getting running applications: {e}")
            return []
            
    def kill_application(self, app_name: str) -> bool:
        """Kill application by name"""
        try:
            self.logger.info(f"Killing application: {app_name}")
            
            # Add .exe if not present
            if not app_name.endswith('.exe'):
                app_name += '.exe'
                
            # Use taskkill command
            result = subprocess.run(['taskkill', '/f', '/im', app_name], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                self.logger.info(f"Application killed successfully: {app_name}")
                return True
            else:
                self.logger.warning(f"Could not kill application: {app_name}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error killing application: {e}")
            return False
            
    def open_system_settings(self, setting_category: str = None) -> bool:
        """Open Windows Settings"""
        try:
            if not self.open_application("settings"):
                return False
                
            if setting_category:
                time.sleep(2)  # Wait for settings to load
                
                # Search for specific setting
                pyautogui.type(setting_category)
                time.sleep(1)
                pyautogui.press('enter')
                
                self.logger.info(f"Opened settings: {setting_category}")
                
            return True
            
        except Exception as e:
            self.logger.error(f"Error opening system settings: {e}")
            return False

def main():
    """Test app launcher"""
    launcher = AppLauncher()
    
    # Test opening applications
    print("Testing app launching...")
    
    test_apps = ["notepad", "calculator", "paint"]
    
    for app in test_apps:
        print(f"Opening {app}...")
        launcher.open_application(app)
        time.sleep(3)
        
        print(f"Closing {app}...")
        launcher.close_application()
        time.sleep(2)

if __name__ == "__main__":
    main()
