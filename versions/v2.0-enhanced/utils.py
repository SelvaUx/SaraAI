import wikipedia
import datetime
import pyjokes
import os
import subprocess
import pyautogui

# ------------------ Wiki ------------------
def search_wikipedia(query: str) -> str:
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.exceptions.DisambiguationError:
        return "Multiple results found. Please be more specific."
    except Exception as e:
        return f"I couldn't find anything: {e}"

# ------------------ Time / Date ------------------
def get_time() -> str:
    now = datetime.datetime.now().strftime("%I:%M %p")
    return f"The current time is {now}"

def get_date() -> str:
    now = datetime.datetime.now()
    return f"Today is {now:%d %B %Y}"

# ------------------ Joke ------------------
def joke() -> str:
    return pyjokes.get_joke()

# ------------------ Brightness (Windows) ------------------
def change_brightness(level: str):
    try:
        level = int(level)
        level = max(0, min(100, level))
        cmd = f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{level})"
        subprocess.run(["powershell", "-Command", cmd], check=True)
    except Exception:
        pass  # fallback on laptops with missing WMI

# ------------------ File / Folder helpers ------------------
def create_folder(name: str):
    path = os.path.join(os.path.expanduser("~\\Desktop"), name)
    os.makedirs(path, exist_ok=True)
    pyautogui.alert(f"Folder '{name}' created on Desktop.")

def create_file(name: str):
    path = os.path.join(os.path.expanduser("~\\Desktop"), name)
    open(path, "w").close()
    pyautogui.alert(f"File '{name}' created on Desktop.")