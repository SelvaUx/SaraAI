
import os
import subprocess
import platform

def play_music() -> None:
    """Opens the default music player."""
    try:
        if platform.system() == "Windows":
            # Try to open default music folder and let Windows handle default player
            music_folder = os.path.join(os.path.expanduser("~"), "Music")
            if os.path.exists(music_folder) and os.listdir(music_folder):
                song_path = os.path.join(music_folder, os.listdir(music_folder)[0])
                os.startfile(song_path)
            else:
                print("No music files found in the Music folder or the folder does not exist.")
        else:
            print("Music player functionality is only implemented for Windows.")
    except Exception as e:
        print(f"Error playing music: {e}")
