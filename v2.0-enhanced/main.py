from application_handler import open_application, screenshot, shutdown, restart, lock, volume
from tts import speak
from utils import get_time, get_date, search_wikipedia, joke, change_brightness, create_folder, create_file
from browser_handler import handle_browser_commands, youtube_search
from music_player import play_music, media_control
from code_writer import write_code, create_project
from file_handler import list_files, delete_file, move_file
from task_manager import list_tasks, kill_task
from gesture_handler import start_gesture_listener   # experimental
from face_unlock import try_face_unlock              # experimental
from voice_input import listen_for_command, WAKE_WORD
import time

def handle_command(command: str) -> None:
    cmd = command.lower()

    # ---------- VOICE & AI ----------
    if "hello" in cmd or "hi sara" in cmd:
        speak("Hello! How can I help you?")
    elif "goodbye" in cmd:
        speak("Goodbye!")
        exit()

    # ---------- PC CONTROL ----------
    elif "open" in cmd:
        app_name = command.replace("open", "").strip()
        open_application(app_name)
    elif "shutdown" in cmd or "turn off" in cmd:
        speak("Shutting down now.")
        shutdown()
    elif "restart" in cmd or "reboot" in cmd:
        speak("Restarting now.")
        restart()
    elif "lock" in cmd:
        speak("Locking the PC.")
        lock()
    elif "volume up" in cmd:
        volume("up")
    elif "volume down" in cmd:
        volume("down")
    elif "mute" in cmd:
        volume("mute")

    # ---------- CODE WRITER ----------
    elif "create project" in cmd:
        name = cmd.replace("create project", "").strip()
        create_project(name)
    elif "write code" in cmd:
        snippet = cmd.replace("write code", "").strip()
        write_code(snippet)

    # ---------- BROWSER / WEB ----------
    elif "youtube" in cmd:
        query = cmd.replace("youtube", "").strip()
        youtube_search(query)
    elif any(k in cmd for k in ["search on", "open website"]):
        handle_browser_commands(command)

    # ---------- MEDIA ----------
    elif "play music" in cmd:
        play_music()
    elif cmd in {"pause music", "resume music", "next track", "previous track"}:
        media_control(cmd)

    # ---------- UTILITIES ----------
    elif "screenshot" in cmd:
        screenshot()
        speak("Screenshot saved.")
    elif "time" in cmd:
        speak(get_time())
    elif "date" in cmd:
        speak(get_date())
    elif "brightness" in cmd:
        val = cmd.replace("brightness", "").strip()
        change_brightness(val)
    elif "create folder" in cmd:
        name = cmd.replace("create folder", "").strip()
        create_folder(name)
    elif "create file" in cmd:
        name = cmd.replace("create file", "").strip()
        create_file(name)

    # ---------- FILE & TASK ----------
    elif "list files" in cmd:
        list_files()
    elif "delete file" in cmd:
        f = cmd.replace("delete file", "").strip()
        delete_file(f)
    elif "move file" in cmd:
        # expects "move file source to dest"
        parts = cmd.replace("move file", "").strip()
        src, dst = parts.split(" to ")
        move_file(src.strip(), dst.strip())
    elif "list tasks" in cmd:
        list_tasks()
    elif "kill task" in cmd:
        t = cmd.replace("kill task", "").strip()
        kill_task(t)

    # ---------- EXPERIMENTAL ----------
    elif "start gestures" in cmd:
        speak("Starting gesture listener.")
        start_gesture_listener()
    elif "face unlock" in cmd:
        speak("Looking for your face.")
        try_face_unlock()

    else:
        speak("Sorry, I didn't understand that.")

def main():
    speak("Welcome to Sara AI. Say 'Hey Sara' to begin.")
    while True:
        cmd = listen_for_command()
        if cmd:
            handle_command(cmd)

if __name__ == "__main__":
    main()
