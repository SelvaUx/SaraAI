#!/usr/bin/env python3
"""
Sara AI Uninstall Manager
Handles application uninstallation via Control Panel automation and registry
"""

import os
import time
import logging
import subprocess
import pyautogui
import winreg
from typing import List, Dict, Optional

class UninstallManager:
    def __init__(self):
        """Initialize uninstall manager"""
        self.logger = logging.getLogger('UninstallManager')
        
        # Application mappings for common software
        self.app_mappings = self.load_app_mappings()
        
        # Automation settings
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 1.0
        
        print("🗑️ Uninstall Manager initialized")
        
    def load_app_mappings(self) -> Dict:
        """Load common application name mappings for uninstallation"""
        return {
            # Browsers
            "chrome": "Google Chrome",
            "google chrome": "Google Chrome",
            "firefox": "Mozilla Firefox", 
            "mozilla firefox": "Mozilla Firefox",
            "edge": "Microsoft Edge",
            "internet explorer": "Internet Explorer",
            
            # Media Players
            "vlc": "VLC media player",
            "spotify": "Spotify",
            "itunes": "iTunes",
            "windows media player": "Windows Media Player",
            
            # Office Applications
            "office": "Microsoft Office",
            "word": "Microsoft Office Word",
            "excel": "Microsoft Office Excel", 
            "powerpoint": "Microsoft Office PowerPoint",
            "outlook": "Microsoft Office Outlook",
            
            # Development Tools
            "visual studio code": "Microsoft Visual Studio Code",
            "vs code": "Microsoft Visual Studio Code",
            "visual studio": "Microsoft Visual Studio",
            "notepad++": "Notepad++",
            "git": "Git",
            "python": "Python",
            "node": "Node.js",
            "nodejs": "Node.js",
            
            # Communication
            "discord": "Discord",
            "skype": "Skype",
            "teams": "Microsoft Teams",
            "zoom": "Zoom",
            
            # Gaming
            "steam": "Steam",
            "epic games": "Epic Games Launcher",
            "origin": "Origin",
            "uplay": "Uplay",
            
            # Utilities
            "7zip": "7-Zip",
            "winrar": "WinRAR",
            "ccleaner": "CCleaner",
            "malwarebytes": "Malwarebytes",
            
            # Adobe Products
            "photoshop": "Adobe Photoshop",
            "acrobat": "Adobe Acrobat",
            "reader": "Adobe Acrobat Reader",
            
            # Antivirus
            "avast": "Avast",
            "avg": "AVG",
            "norton": "Norton",
            "mcafee": "McAfee"
        }
        
    def get_installed_programs(self) -> List[Dict]:
        """Get list of installed programs from registry"""
        programs = []
        
        try:
            # Check both 32-bit and 64-bit registry locations
            registry_paths = [
                (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
                (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"),
                (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
            ]
            
            for hkey, path in registry_paths:
                try:
                    registry_key = winreg.OpenKey(hkey, path)
                    
                    for i in range(winreg.QueryInfoKey(registry_key)[0]):
                        try:
                            subkey_name = winreg.EnumKey(registry_key, i)
                            subkey = winreg.OpenKey(registry_key, subkey_name)
                            
                            try:
                                name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                
                                # Get additional info if available
                                try:
                                    version = winreg.QueryValueEx(subkey, "DisplayVersion")[0]
                                except FileNotFoundError:
                                    version = "Unknown"
                                    
                                try:
                                    publisher = winreg.QueryValueEx(subkey, "Publisher")[0]
                                except FileNotFoundError:
                                    publisher = "Unknown"
                                    
                                try:
                                    uninstall_string = winreg.QueryValueEx(subkey, "UninstallString")[0]
                                except FileNotFoundError:
                                    uninstall_string = ""
                                
                                programs.append({
                                    'name': name,
                                    'version': version,
                                    'publisher': publisher,
                                    'uninstall_string': uninstall_string,
                                    'registry_key': subkey_name
                                })
                                
                            except FileNotFoundError:
                                continue
                                
                            winreg.CloseKey(subkey)
                            
                        except Exception:
                            continue
                            
                    winreg.CloseKey(registry_key)
                    
                except Exception as e:
                    self.logger.warning(f"Could not access registry path {path}: {e}")
                    continue
                    
        except Exception as e:
            self.logger.error(f"Error getting installed programs: {e}")
            
        self.logger.info(f"Found {len(programs)} installed programs")
        return programs
        
    def find_program(self, program_name: str) -> Optional[Dict]:
        """Find a program in the installed programs list"""
        try:
            # Normalize program name
            program_name = program_name.lower().strip()
            
            # Check for mapped names
            mapped_name = self.app_mappings.get(program_name, program_name)
            
            # Get installed programs
            programs = self.get_installed_programs()
            
            # Search for exact match first
            for program in programs:
                if program['name'].lower() == mapped_name.lower():
                    return program
                    
            # Search for partial match
            for program in programs:
                if mapped_name.lower() in program['name'].lower():
                    return program
                    
            # Search for original name if mapping didn't work
            if mapped_name != program_name:
                for program in programs:
                    if program_name in program['name'].lower():
                        return program
                        
            return None
            
        except Exception as e:
            self.logger.error(f"Error finding program {program_name}: {e}")
            return None
            
    def uninstall_application(self, app_name: str) -> bool:
        """Uninstall application via Control Panel automation"""
        try:
            self.logger.info(f"Attempting to uninstall: {app_name}")
            
            # Find the program
            program = self.find_program(app_name)
            
            if not program:
                self.logger.warning(f"Program not found: {app_name}")
                return self.uninstall_via_control_panel(app_name)
                
            # Try uninstall via registry uninstall string first
            if program['uninstall_string']:
                self.logger.info(f"Using uninstall string: {program['uninstall_string']}")
                return self.uninstall_via_registry(program)
            else:
                # Fallback to Control Panel method
                return self.uninstall_via_control_panel(program['name'])
                
        except Exception as e:
            self.logger.error(f"Error uninstalling {app_name}: {e}")
            return False
            
    def uninstall_via_registry(self, program: Dict) -> bool:
        """Uninstall program using its registry uninstall string"""
        try:
            uninstall_string = program['uninstall_string']
            
            # Clean up the uninstall string
            if uninstall_string.startswith('"') and uninstall_string.endswith('"'):
                uninstall_string = uninstall_string[1:-1]
                
            self.logger.info(f"Executing uninstall command: {uninstall_string}")
            
            # Execute the uninstall command
            result = subprocess.run(uninstall_string, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                self.logger.info(f"Successfully uninstalled {program['name']}")
                return True
            else:
                self.logger.warning(f"Uninstall command returned code {result.returncode}")
                return self.uninstall_via_control_panel(program['name'])
                
        except Exception as e:
            self.logger.error(f"Error in registry uninstall: {e}")
            return self.uninstall_via_control_panel(program['name'])
            
    def uninstall_via_control_panel(self, app_name: str) -> bool:
        """Uninstall application via Control Panel automation"""
        try:
            self.logger.info(f"Opening Control Panel for {app_name}")
            
            # Open Control Panel Programs and Features
            if not self.open_programs_and_features():
                return False
                
            time.sleep(3)  # Wait for Control Panel to load
            
            # Search for the application
            if not self.search_in_programs_list(app_name):
                self.logger.warning(f"Could not find {app_name} in programs list")
                return False
                
            # Attempt to uninstall
            return self.perform_uninstall_action()
            
        except Exception as e:
            self.logger.error(f"Error in Control Panel uninstall: {e}")
            return False
            
    def open_programs_and_features(self) -> bool:
        """Open Windows Programs and Features"""
        try:
            # Method 1: Use Run dialog
            pyautogui.hotkey('win', 'r')
            time.sleep(1)
            
            pyautogui.type('appwiz.cpl')
            time.sleep(0.5)
            
            pyautogui.press('enter')
            time.sleep(3)
            
            self.logger.info("Opened Programs and Features")
            return True
            
        except Exception as e:
            self.logger.error(f"Error opening Programs and Features: {e}")
            
            # Method 2: Try via Settings
            try:
                pyautogui.hotkey('win', 'i')  # Open Settings
                time.sleep(2)
                
                pyautogui.type('apps')
                time.sleep(1)
                
                pyautogui.press('enter')
                time.sleep(2)
                
                return True
                
            except Exception as e2:
                self.logger.error(f"Error opening via Settings: {e2}")
                return False
                
    def search_in_programs_list(self, app_name: str) -> bool:
        """Search for application in programs list"""
        try:
            # Try to find search box and search
            pyautogui.hotkey('ctrl', 'f')  # Try to open search
            time.sleep(1)
            
            # Check for mapped name
            search_name = self.app_mappings.get(app_name.lower(), app_name)
            
            pyautogui.type(search_name)
            time.sleep(2)
            
            # Press Tab to navigate to results
            pyautogui.press('tab')
            time.sleep(1)
            
            # Press Enter to select first result
            pyautogui.press('enter')
            time.sleep(1)
            
            self.logger.info(f"Searched for {search_name} in programs list")
            return True
            
        except Exception as e:
            self.logger.error(f"Error searching in programs list: {e}")
            
            # Fallback: try to scroll and find manually
            try:
                # Press first letter of app name to jump to that section
                if app_name:
                    pyautogui.press(app_name[0].lower())
                    time.sleep(1)
                    
                return True
                
            except Exception as e2:
                self.logger.error(f"Error in fallback search: {e2}")
                return False
                
    def perform_uninstall_action(self) -> bool:
        """Perform the actual uninstall action"""
        try:
            # Right-click to open context menu
            pyautogui.rightClick()
            time.sleep(1)
            
            # Look for uninstall option
            # Try pressing 'U' for uninstall
            pyautogui.press('u')
            time.sleep(1)
            
            # Confirm uninstall if prompted
            # Look for common confirmation buttons
            try:
                # Try to find and click "Yes" or "Uninstall" button
                pyautogui.press('enter')  # Default action
                time.sleep(2)
                
                # If there's another confirmation
                pyautogui.press('y')  # For "Yes"
                time.sleep(1)
                
            except Exception:
                pass
                
            self.logger.info("Uninstall action initiated")
            return True
            
        except Exception as e:
            self.logger.error(f"Error performing uninstall action: {e}")
            return False
            
    def uninstall_via_winget(self, app_name: str) -> bool:
        """Try to uninstall using Windows Package Manager (winget)"""
        try:
            self.logger.info(f"Trying winget uninstall for {app_name}")
            
            # Search for the package first
            search_result = subprocess.run(
                ['winget', 'search', app_name],
                capture_output=True,
                text=True
            )
            
            if search_result.returncode != 0:
                self.logger.warning("Winget not available or search failed")
                return False
                
            # Try to uninstall
            uninstall_result = subprocess.run(
                ['winget', 'uninstall', app_name, '--accept-source-agreements'],
                capture_output=True,
                text=True
            )
            
            if uninstall_result.returncode == 0:
                self.logger.info(f"Successfully uninstalled {app_name} via winget")
                return True
            else:
                self.logger.warning(f"Winget uninstall failed: {uninstall_result.stderr}")
                return False
                
        except FileNotFoundError:
            self.logger.warning("Winget not found on system")
            return False
        except Exception as e:
            self.logger.error(f"Error with winget uninstall: {e}")
            return False
            
    def list_uninstallable_programs(self, filter_term: str = None) -> List[Dict]:
        """List programs that can be uninstalled"""
        try:
            programs = self.get_installed_programs()
            
            if filter_term:
                filter_term = filter_term.lower()
                filtered_programs = [
                    p for p in programs 
                    if filter_term in p['name'].lower() or 
                       filter_term in p['publisher'].lower()
                ]
                return filtered_programs
            else:
                return programs
                
        except Exception as e:
            self.logger.error(f"Error listing programs: {e}")
            return []
            
    def get_program_info(self, app_name: str) -> Optional[Dict]:
        """Get detailed information about an installed program"""
        try:
            program = self.find_program(app_name)
            
            if program:
                # Add additional information
                program['can_uninstall'] = bool(program['uninstall_string'])
                program['uninstall_method'] = 'registry' if program['uninstall_string'] else 'control_panel'
                
                return program
            else:
                return None
                
        except Exception as e:
            self.logger.error(f"Error getting program info: {e}")
            return None
            
    def bulk_uninstall(self, app_names: List[str]) -> Dict[str, bool]:
        """Uninstall multiple applications"""
        results = {}
        
        for app_name in app_names:
            try:
                self.logger.info(f"Bulk uninstalling: {app_name}")
                results[app_name] = self.uninstall_application(app_name)
                
                # Wait between uninstalls
                time.sleep(5)
                
            except Exception as e:
                self.logger.error(f"Error in bulk uninstall for {app_name}: {e}")
                results[app_name] = False
                
        return results
        
    def suggest_cleanup(self) -> List[str]:
        """Suggest programs that might be good candidates for removal"""
        try:
            programs = self.get_installed_programs()
            suggestions = []
            
            # Look for common bloatware patterns
            bloatware_patterns = [
                'mcafee', 'norton trial', 'trial', 'toolbar', 'coupon',
                'shopping', 'games', 'weather', 'news', 'updater'
            ]
            
            for program in programs:
                program_name_lower = program['name'].lower()
                
                for pattern in bloatware_patterns:
                    if pattern in program_name_lower:
                        suggestions.append(program['name'])
                        break
                        
            return suggestions[:10]  # Return top 10 suggestions
            
        except Exception as e:
            self.logger.error(f"Error generating cleanup suggestions: {e}")
            return []

def main():
    """Test uninstall manager"""
    manager = UninstallManager()
    
    # Test getting installed programs
    print("Getting installed programs...")
    programs = manager.get_installed_programs()
    print(f"Found {len(programs)} installed programs")
    
    # Show first 5 programs
    for i, program in enumerate(programs[:5]):
        print(f"{i+1}. {program['name']} ({program['version']}) by {program['publisher']}")
    
    # Test search
    print("\nTesting program search...")
    test_app = "notepad"
    program = manager.find_program(test_app)
    if program:
        print(f"Found: {program['name']}")
    else:
        print(f"Program '{test_app}' not found")
    
    # Test cleanup suggestions
    print("\nCleanup suggestions:")
    suggestions = manager.suggest_cleanup()
    for suggestion in suggestions:
        print(f"- {suggestion}")

if __name__ == "__main__":
    main()
