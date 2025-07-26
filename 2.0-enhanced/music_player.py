import os
import subprocess
import platform
import pyautogui
import time

def play_music() -> None:
    """Play the first audio file in the user’s Music folder."""
    try:
        if platform.system() != "Windows":
            print("Music player is Windows-only.")
            return

        music_dir = os.path.join(os.path.expanduser("~"), "Music")
        if not os.path.isdir(music_dir):
            print("Music folder not found.")
            return

        files = [f for f in os.listdir(music_dir)
                 if f.lower().endswith((".mp3", ".wav", ".flac", ".m4a"))]
        if not files:
            print("No audio files in Music folder.")
            return

        first_song = os.path.join(music_dir, files[0])
        os.startfile(first_song)
        print(f"Playing {files[0]}")
    except Exception as e:
        print(f"Error playing music: {e}")

def media_control(action: str) -> None:
    """Send media keys: play/pause, next, previous."""
    key_map = {
        "pause music": "playpause",
        "resume music": "playpause",
        "next track": "nexttrack",
        "previous track": "prevtrack"
    }
    key = key_map.get(action.lower())
    if key:
        pyautogui.press(key)
        print(f"Sent {key}")
    else:
        print("Unknown media command")