#!/usr/bin/env python3
"""
Sara AI Music Controller
Handles music playback, media controls, and audio management
"""

import os
import time
import logging
import random
import subprocess
import pyautogui
from typing import List, Optional, Dict
import glob
from pathlib import Path

# Try importing pygame for audio playback
try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False
    print("⚠️ Pygame not available, using system media controls")

# Try importing playsound as fallback
try:
    from playsound import playsound
    PLAYSOUND_AVAILABLE = True
except ImportError:
    PLAYSOUND_AVAILABLE = False

class MusicController:
    def __init__(self):
        """Initialize music controller"""
        self.logger = logging.getLogger('MusicController')
        
        # Music settings
        self.current_song = None
        self.is_playing = False
        self.is_paused = False
        self.current_playlist = []
        self.current_index = 0
        self.volume = 0.7
        
        # Music directories
        self.music_directories = self.get_default_music_dirs()
        self.supported_formats = ['.mp3', '.wav', '.m4a', '.aac', '.flac', '.ogg']
        
        # Initialize pygame if available
        if PYGAME_AVAILABLE:
            try:
                pygame.mixer.init()
                self.logger.info("Pygame mixer initialized")
            except Exception as e:
                self.logger.warning(f"Pygame mixer init failed: {e}")
                
        print("🎵 Music Controller initialized")
        
    def get_default_music_dirs(self) -> List[str]:
        """Get default music directories"""
        music_dirs = []
        
        # Windows default music folders
        user_music = os.path.expanduser("~/Music")
        if os.path.exists(user_music):
            music_dirs.append(user_music)
            
        # Check for common music folders
        common_dirs = [
            os.path.expanduser("~/Documents/My Music"),
            os.path.expanduser("~/Downloads"),
            "C:/Users/Public/Music",
            "./music",  # Local music folder
        ]
        
        for dir_path in common_dirs:
            if os.path.exists(dir_path):
                music_dirs.append(dir_path)
                
        return music_dirs
        
    def scan_music_files(self, directory: str = None) -> List[str]:
        """Scan for music files in specified directory"""
        music_files = []
        
        if directory:
            scan_dirs = [directory]
        else:
            scan_dirs = self.music_directories
            
        for music_dir in scan_dirs:
            if not os.path.exists(music_dir):
                continue
                
            self.logger.info(f"Scanning music directory: {music_dir}")
            
            for format_ext in self.supported_formats:
                pattern = os.path.join(music_dir, f"**/*{format_ext}")
                files = glob.glob(pattern, recursive=True)
                music_files.extend(files)
                
        self.logger.info(f"Found {len(music_files)} music files")
        return music_files
        
    def create_playlist(self, directory: str = None) -> bool:
        """Create playlist from music files"""
        try:
            music_files = self.scan_music_files(directory)
            
            if not music_files:
                self.logger.warning("No music files found")
                return False
                
            self.current_playlist = music_files
            self.current_index = 0
            
            self.logger.info(f"Playlist created with {len(music_files)} songs")
            return True
            
        except Exception as e:
            self.logger.error(f"Error creating playlist: {e}")
            return False
            
    def play_music(self, file_path: str = None) -> bool:
        """Play music file or from playlist"""
        try:
            if file_path:
                # Play specific file
                self.current_song = file_path
            else:
                # Play from playlist
                if not self.current_playlist:
                    if not self.create_playlist():
                        return self.open_music_player()
                        
                if self.current_playlist:
                    self.current_song = self.current_playlist[self.current_index]
                else:
                    return self.open_music_player()
                    
            return self._play_file(self.current_song)
            
        except Exception as e:
            self.logger.error(f"Error playing music: {e}")
            return self.open_music_player()
            
    def _play_file(self, file_path: str) -> bool:
        """Internal method to play a specific file"""
        try:
            if not os.path.exists(file_path):
                self.logger.error(f"Music file not found: {file_path}")
                return False
                
            self.logger.info(f"Playing: {os.path.basename(file_path)}")
            
            if PYGAME_AVAILABLE:
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.set_volume(self.volume)
                pygame.mixer.music.play()
                self.is_playing = True
                self.is_paused = False
                return True
                
            elif PLAYSOUND_AVAILABLE:
                # Use playsound in background thread
                import threading
                thread = threading.Thread(target=playsound, args=(file_path,))
                thread.daemon = True
                thread.start()
                self.is_playing = True
                return True
                
            else:
                # Fallback to system default player
                os.startfile(file_path)
                self.is_playing = True
                return True
                
        except Exception as e:
            self.logger.error(f"Error playing file {file_path}: {e}")
            return False
            
    def pause_music(self) -> bool:
        """Pause current music"""
        try:
            if PYGAME_AVAILABLE and pygame.mixer.get_init():
                if self.is_playing and not self.is_paused:
                    pygame.mixer.music.pause()
                    self.is_paused = True
                    self.logger.info("Music paused")
                    return True
                else:
                    return self.system_media_control("pause")
            else:
                return self.system_media_control("pause")
                
        except Exception as e:
            self.logger.error(f"Error pausing music: {e}")
            return False
            
    def resume_music(self) -> bool:
        """Resume paused music"""
        try:
            if PYGAME_AVAILABLE and pygame.mixer.get_init():
                if self.is_paused:
                    pygame.mixer.music.unpause()
                    self.is_paused = False
                    self.logger.info("Music resumed")
                    return True
                else:
                    return self.system_media_control("play")
            else:
                return self.system_media_control("play")
                
        except Exception as e:
            self.logger.error(f"Error resuming music: {e}")
            return False
            
    def stop_music(self) -> bool:
        """Stop current music"""
        try:
            if PYGAME_AVAILABLE and pygame.mixer.get_init():
                pygame.mixer.music.stop()
                self.is_playing = False
                self.is_paused = False
                self.logger.info("Music stopped")
                return True
            else:
                return self.system_media_control("stop")
                
        except Exception as e:
            self.logger.error(f"Error stopping music: {e}")
            return False
            
    def next_song(self) -> bool:
        """Play next song in playlist"""
        try:
            if not self.current_playlist:
                return self.system_media_control("next")
                
            if self.current_index < len(self.current_playlist) - 1:
                self.current_index += 1
            else:
                self.current_index = 0  # Loop to beginning
                
            next_file = self.current_playlist[self.current_index]
            self.logger.info(f"Next song: {os.path.basename(next_file)}")
            
            return self.play_music(next_file)
            
        except Exception as e:
            self.logger.error(f"Error playing next song: {e}")
            return False
            
    def previous_song(self) -> bool:
        """Play previous song in playlist"""
        try:
            if not self.current_playlist:
                return self.system_media_control("previous")
                
            if self.current_index > 0:
                self.current_index -= 1
            else:
                self.current_index = len(self.current_playlist) - 1  # Loop to end
                
            prev_file = self.current_playlist[self.current_index]
            self.logger.info(f"Previous song: {os.path.basename(prev_file)}")
            
            return self.play_music(prev_file)
            
        except Exception as e:
            self.logger.error(f"Error playing previous song: {e}")
            return False
            
    def shuffle_playlist(self) -> bool:
        """Shuffle current playlist"""
        try:
            if self.current_playlist:
                random.shuffle(self.current_playlist)
                self.current_index = 0
                self.logger.info("Playlist shuffled")
                return True
            return False
            
        except Exception as e:
            self.logger.error(f"Error shuffling playlist: {e}")
            return False
            
    def set_volume(self, volume: float) -> bool:
        """Set music volume (0.0 to 1.0)"""
        try:
            volume = max(0.0, min(1.0, volume))  # Clamp between 0 and 1
            self.volume = volume
            
            if PYGAME_AVAILABLE and pygame.mixer.get_init():
                pygame.mixer.music.set_volume(volume)
                self.logger.info(f"Volume set to {int(volume * 100)}%")
                return True
            else:
                # Use system volume control as fallback
                return self.adjust_system_volume(int(volume * 100))
                
        except Exception as e:
            self.logger.error(f"Error setting volume: {e}")
            return False
            
    def adjust_system_volume(self, target_volume: int) -> bool:
        """Adjust system volume to target percentage"""
        try:
            # PowerShell script to set volume
            ps_script = f"""
            Add-Type -TypeDefinition @'
            using System.Runtime.InteropServices;
            [Guid("5CDF2C82-841E-4546-9722-0CF74078229A"), InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
            interface IAudioEndpointVolume {{
                int SetMasterVolumeLevelScalar(float fLevel, System.Guid pguidEventContext);
            }}
            [Guid("D666063F-1587-4E43-81F1-B948E807363F"), InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
            interface IMMDevice {{
                int Activate(ref System.Guid id, uint dwClsCtx, System.IntPtr pActivationParams, [MarshalAs(UnmanagedType.IUnknown)] out object ppInterface);
            }}
            [ComImport, Guid("A95664D2-9614-4F35-A746-DE8DB63617E6"), InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
            interface IMMDeviceEnumerator {{
                int GetDefaultAudioEndpoint(int dataFlow, int role, out IMMDevice ppEndpoint);
            }}
            [ComImport, Guid("BCDE0395-E52F-467C-8E3D-C4579291692E")]
            class MMDeviceEnumerator {{}}
            public class AudioEndpointVolume {{
                IAudioEndpointVolume _AudioEndpointVolume;
                public AudioEndpointVolume() {{
                    IMMDeviceEnumerator deviceEnumerator = (IMMDeviceEnumerator)(new MMDeviceEnumerator());
                    IMMDevice speakers;
                    deviceEnumerator.GetDefaultAudioEndpoint(0, 0, out speakers);
                    System.Guid IID_IAudioEndpointVolume = typeof(IAudioEndpointVolume).GUID;
                    object o;
                    speakers.Activate(ref IID_IAudioEndpointVolume, 0, System.IntPtr.Zero, out o);
                    _AudioEndpointVolume = (IAudioEndpointVolume)o;
                }}
                public void SetVolume(float level) {{
                    _AudioEndpointVolume.SetMasterVolumeLevelScalar(level, System.Guid.Empty);
                }}
            }}
'@
            $volume = New-Object AudioEndpointVolume
            $volume.SetVolume({target_volume / 100.0})
            """
            
            result = subprocess.run(['powershell', '-Command', ps_script],
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                self.logger.info(f"System volume set to {target_volume}%")
                return True
            else:
                return False
                
        except Exception as e:
            self.logger.error(f"Error adjusting system volume: {e}")
            return False
            
    def system_media_control(self, action: str) -> bool:
        """Use system media keys for control"""
        try:
            action = action.lower()
            
            if action == "play":
                pyautogui.press('playpause')
            elif action == "pause":
                pyautogui.press('playpause')
            elif action == "stop":
                pyautogui.press('stop')
            elif action == "next":
                pyautogui.press('nexttrack')
            elif action == "previous":
                pyautogui.press('prevtrack')
            else:
                return False
                
            self.logger.info(f"Media control: {action}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error with media control {action}: {e}")
            return False
            
    def open_music_player(self, player: str = None) -> bool:
        """Open default or specified music player"""
        try:
            if not player:
                # Try common music players
                players = [
                    "spotify", "groove music", "windows media player",
                    "vlc", "foobar2000", "winamp", "musicbee"
                ]
                
                for player_name in players:
                    if self._open_app(player_name):
                        return True
                        
                # Fallback to default media player
                return self._open_app("groove music")
            else:
                return self._open_app(player)
                
        except Exception as e:
            self.logger.error(f"Error opening music player: {e}")
            return False
            
    def _open_app(self, app_name: str) -> bool:
        """Helper method to open an application"""
        try:
            self.logger.info(f"Opening {app_name}")
            
            # Press Windows key
            pyautogui.press('win')
            time.sleep(1)
            
            # Type app name
            pyautogui.type(app_name)
            time.sleep(1.5)
            
            # Press Enter
            pyautogui.press('enter')
            time.sleep(2)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error opening {app_name}: {e}")
            return False
            
    def get_current_song_info(self) -> Dict:
        """Get information about currently playing song"""
        try:
            if self.current_song:
                file_path = Path(self.current_song)
                return {
                    'filename': file_path.name,
                    'path': str(file_path),
                    'directory': str(file_path.parent),
                    'extension': file_path.suffix,
                    'is_playing': self.is_playing,
                    'is_paused': self.is_paused,
                    'playlist_position': f"{self.current_index + 1}/{len(self.current_playlist)}" if self.current_playlist else "N/A"
                }
            else:
                return {'status': 'No song currently loaded'}
                
        except Exception as e:
            self.logger.error(f"Error getting song info: {e}")
            return {'error': str(e)}
            
    def create_music_folder(self) -> bool:
        """Create local music folder if it doesn't exist"""
        try:
            music_folder = "./music"
            if not os.path.exists(music_folder):
                os.makedirs(music_folder)
                self.logger.info(f"Created music folder: {music_folder}")
                
                # Add to music directories
                if music_folder not in self.music_directories:
                    self.music_directories.append(music_folder)
                    
                return True
            return True
            
        except Exception as e:
            self.logger.error(f"Error creating music folder: {e}")
            return False

def main():
    """Test music controller"""
    controller = MusicController()
    
    # Test music folder creation
    print("Creating music folder...")
    controller.create_music_folder()
    
    # Test playlist creation
    print("Scanning for music files...")
    if controller.create_playlist():
        print(f"Found {len(controller.current_playlist)} music files")
        
        # Test playback if files found
        if controller.current_playlist:
            print("Testing music playback...")
            controller.play_music()
            time.sleep(3)
            
            print("Testing pause...")
            controller.pause_music()
            time.sleep(2)
            
            print("Testing resume...")
            controller.resume_music()
            time.sleep(2)
            
            print("Testing stop...")
            controller.stop_music()
    else:
        print("No music files found, testing media player opening...")
        controller.open_music_player()
        
    # Test system media controls
    print("Testing system media controls...")
    controller.system_media_control("play")

if __name__ == "__main__":
    main()
