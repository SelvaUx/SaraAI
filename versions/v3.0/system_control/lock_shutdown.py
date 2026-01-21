#!/usr/bin/env python3
"""
Sara AI System Controller
Handles system operations like shutdown, lock, volume control, and screenshots
"""

import os
import time
import logging
import subprocess
import pyautogui
from datetime import datetime
from typing import Optional

class SystemController:
    def __init__(self):
        """Initialize system controller"""
        self.logger = logging.getLogger('SystemController')
        
        # Screenshot directory
        self.screenshot_dir = "screenshots"
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)
            
        print("⚙️ System Controller initialized")
        
    def shutdown(self, delay: int = 10) -> bool:
        """Shutdown the system with optional delay"""
        try:
            self.logger.info(f"Shutting down system in {delay} seconds")
            
            # Use Windows shutdown command
            cmd = f"shutdown /s /t {delay}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                self.logger.info("Shutdown command executed successfully")
                return True
            else:
                self.logger.error(f"Shutdown failed: {result.stderr}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error shutting down: {e}")
            return False
            
    def restart(self, delay: int = 10) -> bool:
        """Restart the system with optional delay"""
        try:
            self.logger.info(f"Restarting system in {delay} seconds")
            
            # Use Windows restart command
            cmd = f"shutdown /r /t {delay}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                self.logger.info("Restart command executed successfully")
                return True
            else:
                self.logger.error(f"Restart failed: {result.stderr}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error restarting: {e}")
            return False
            
    def cancel_shutdown(self) -> bool:
        """Cancel pending shutdown or restart"""
        try:
            self.logger.info("Cancelling shutdown/restart")
            
            cmd = "shutdown /a"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                self.logger.info("Shutdown/restart cancelled successfully")
                return True
            else:
                self.logger.warning("No shutdown to cancel or cancellation failed")
                return False
                
        except Exception as e:
            self.logger.error(f"Error cancelling shutdown: {e}")
            return False
            
    def lock_screen(self) -> bool:
        """Lock the screen"""
        try:
            self.logger.info("Locking screen")
            
            # Use Windows + L to lock screen
            pyautogui.hotkey('win', 'l')
            time.sleep(1)
            
            self.logger.info("Screen locked successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Error locking screen: {e}")
            return False
            
    def sleep_system(self) -> bool:
        """Put system to sleep"""
        try:
            self.logger.info("Putting system to sleep")
            
            # Use rundll32 to sleep
            cmd = "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
            result = subprocess.run(cmd, shell=True)
            
            self.logger.info("System sleep initiated")
            return True
            
        except Exception as e:
            self.logger.error(f"Error putting system to sleep: {e}")
            return False
            
    def hibernate_system(self) -> bool:
        """Hibernate the system"""
        try:
            self.logger.info("Hibernating system")
            
            cmd = "shutdown /h"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                self.logger.info("Hibernate command executed successfully")
                return True
            else:
                self.logger.error(f"Hibernate failed: {result.stderr}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error hibernating: {e}")
            return False
            
    def adjust_volume(self, action: str, amount: int = 10) -> bool:
        """Adjust system volume"""
        try:
            action = action.lower()
            self.logger.info(f"Adjusting volume: {action}")
            
            if action in ['up', 'increase', 'raise']:
                # Volume up
                for _ in range(amount // 2):  # Each press is about 2%
                    pyautogui.press('volumeup')
                    time.sleep(0.1)
                    
            elif action in ['down', 'decrease', 'lower']:
                # Volume down
                for _ in range(amount // 2):
                    pyautogui.press('volumedown')
                    time.sleep(0.1)
                    
            elif action in ['mute', 'silence']:
                # Mute/unmute
                pyautogui.press('volumemute')
                
            else:
                self.logger.warning(f"Unknown volume action: {action}")
                return False
                
            self.logger.info(f"Volume {action} completed")
            return True
            
        except Exception as e:
            self.logger.error(f"Error adjusting volume: {e}")
            return False
            
    def set_volume_powershell(self, level: int) -> bool:
        """Set volume to specific level using PowerShell"""
        try:
            if not 0 <= level <= 100:
                self.logger.error("Volume level must be between 0 and 100")
                return False
                
            self.logger.info(f"Setting volume to {level}%")
            
            # PowerShell script to set volume
            ps_script = f"""
            Add-Type -TypeDefinition @'
            using System.Runtime.InteropServices;
            [Guid("5CDF2C82-841E-4546-9722-0CF74078229A"), InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
            interface IAudioEndpointVolume {{
                int RegisterControlChangeNotify(IntPtr pNotify);
                int UnregisterControlChangeNotify(IntPtr pNotify);
                int GetChannelCount(out int pnChannelCount);
                int SetMasterVolumeLevel(float fLevelDB, Guid pguidEventContext);
                int SetMasterVolumeLevelScalar(float fLevel, Guid pguidEventContext);
                int GetMasterVolumeLevel(out float pfLevelDB);
                int GetMasterVolumeLevelScalar(out float pfLevel);
                int SetChannelVolumeLevel(uint nChannel, float fLevelDB, Guid pguidEventContext);
                int SetChannelVolumeLevelScalar(uint nChannel, float fLevel, Guid pguidEventContext);
                int GetChannelVolumeLevel(uint nChannel, out float pfLevelDB);
                int GetChannelVolumeLevelScalar(uint nChannel, out float pfLevel);
                int SetMute([MarshalAs(UnmanagedType.Bool)] bool bMute, Guid pguidEventContext);
                int GetMute(out bool pbMute);
                int GetVolumeStepInfo(out uint pnStep, out uint pnStepCount);
                int VolumeStepUp(Guid pguidEventContext);
                int VolumeStepDown(Guid pguidEventContext);
                int QueryHardwareSupport(out uint pdwHardwareSupportMask);
                int GetVolumeRange(out float pflVolumeMindB, out float pflVolumeMaxdB, out float pflVolumeIncrementdB);
            }}
            [Guid("D666063F-1587-4E43-81F1-B948E807363F"), InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
            interface IMMDevice {{
                int Activate(ref Guid id, uint dwClsCtx, IntPtr pActivationParams, [MarshalAs(UnmanagedType.IUnknown)] out object ppInterface);
            }}
            [ComImport, Guid("A95664D2-9614-4F35-A746-DE8DB63617E6"), InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
            interface IMMDeviceEnumerator {{
                int EnumAudioEndpoints(int dataFlow, int dwStateMask, out IntPtr ppDevices);
                int GetDefaultAudioEndpoint(int dataFlow, int role, out IMMDevice ppEndpoint);
            }}
            [ComImport, Guid("BCDE0395-E52F-467C-8E3D-C4579291692E")]
            class MMDeviceEnumerator {{
            }}
            public class AudioEndpointVolume {{
                IAudioEndpointVolume _AudioEndpointVolume;
                public AudioEndpointVolume() {{
                    IMMDeviceEnumerator deviceEnumerator = (IMMDeviceEnumerator)(new MMDeviceEnumerator());
                    IMMDevice speakers;
                    deviceEnumerator.GetDefaultAudioEndpoint(0, 0, out speakers);
                    Guid IID_IAudioEndpointVolume = typeof(IAudioEndpointVolume).GUID;
                    object o;
                    speakers.Activate(ref IID_IAudioEndpointVolume, 0, IntPtr.Zero, out o);
                    _AudioEndpointVolume = (IAudioEndpointVolume)o;
                }}
                public float MasterVolumeLevel {{
                    get {{
                        float level;
                        _AudioEndpointVolume.GetMasterVolumeLevelScalar(out level);
                        return level;
                    }}
                    set {{
                        _AudioEndpointVolume.SetMasterVolumeLevelScalar(value, Guid.Empty);
                    }}
                }}
            }}
'@
            $volume = New-Object AudioEndpointVolume
            $volume.MasterVolumeLevel = {level / 100.0}
            """
            
            result = subprocess.run(['powershell', '-Command', ps_script], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                self.logger.info(f"Volume set to {level}% successfully")
                return True
            else:
                self.logger.error(f"Failed to set volume: {result.stderr}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error setting volume: {e}")
            return False
            
    def take_screenshot(self, filename: str = None) -> Optional[str]:
        """Take a screenshot and save it"""
        try:
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"screenshot_{timestamp}.png"
                
            filepath = os.path.join(self.screenshot_dir, filename)
            
            self.logger.info(f"Taking screenshot: {filepath}")
            
            # Take screenshot
            screenshot = pyautogui.screenshot()
            screenshot.save(filepath)
            
            self.logger.info(f"Screenshot saved: {filepath}")
            return filepath
            
        except Exception as e:
            self.logger.error(f"Error taking screenshot: {e}")
            return None
            
    def get_battery_status(self) -> dict:
        """Get battery status information"""
        try:
            # PowerShell command to get battery info
            ps_script = """
            Get-WmiObject -Class Win32_Battery | Select-Object EstimatedChargeRemaining, BatteryStatus | ConvertTo-Json
            """
            
            result = subprocess.run(['powershell', '-Command', ps_script], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0 and result.stdout.strip():
                import json
                battery_info = json.loads(result.stdout)
                
                if isinstance(battery_info, list):
                    battery_info = battery_info[0] if battery_info else {}
                    
                return {
                    'charge_remaining': battery_info.get('EstimatedChargeRemaining', 'Unknown'),
                    'status': battery_info.get('BatteryStatus', 'Unknown')
                }
            else:
                return {'charge_remaining': 'No battery', 'status': 'No battery'}
                
        except Exception as e:
            self.logger.error(f"Error getting battery status: {e}")
            return {'charge_remaining': 'Error', 'status': 'Error'}
            
    def open_task_manager(self) -> bool:
        """Open Task Manager"""
        try:
            pyautogui.hotkey('ctrl', 'shift', 'esc')
            time.sleep(2)
            self.logger.info("Task Manager opened")
            return True
            
        except Exception as e:
            self.logger.error(f"Error opening Task Manager: {e}")
            return False
            
    def empty_recycle_bin(self) -> bool:
        """Empty the Recycle Bin"""
        try:
            self.logger.info("Emptying Recycle Bin")
            
            # PowerShell command to empty recycle bin
            ps_script = """
            Clear-RecycleBin -Force -ErrorAction SilentlyContinue
            """
            
            result = subprocess.run(['powershell', '-Command', ps_script], 
                                  capture_output=True, text=True)
            
            self.logger.info("Recycle Bin emptied")
            return True
            
        except Exception as e:
            self.logger.error(f"Error emptying Recycle Bin: {e}")
            return False
            
    def get_system_info(self) -> dict:
        """Get basic system information"""
        try:
            # Get system info using PowerShell
            ps_script = """
            $os = Get-WmiObject -Class Win32_OperatingSystem
            $cs = Get-WmiObject -Class Win32_ComputerSystem
            @{
                'OS' = $os.Caption
                'Version' = $os.Version
                'Architecture' = $os.OSArchitecture
                'TotalMemory' = [math]::Round($cs.TotalPhysicalMemory / 1GB, 2)
                'ComputerName' = $cs.Name
                'Manufacturer' = $cs.Manufacturer
                'Model' = $cs.Model
            } | ConvertTo-Json
            """
            
            result = subprocess.run(['powershell', '-Command', ps_script], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                import json
                return json.loads(result.stdout)
            else:
                return {}
                
        except Exception as e:
            self.logger.error(f"Error getting system info: {e}")
            return {}

def main():
    """Test system controller"""
    controller = SystemController()
    
    # Test screenshot
    print("Taking screenshot...")
    screenshot_path = controller.take_screenshot()
    if screenshot_path:
        print(f"Screenshot saved: {screenshot_path}")
    
    # Test volume control
    print("Testing volume control...")
    controller.adjust_volume("up", 5)
    time.sleep(1)
    controller.adjust_volume("down", 5)
    
    # Test system info
    print("Getting system info...")
    info = controller.get_system_info()
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
