import pyautogui, os, time, subprocess, platform

def open_application(app_name: str) -> None:
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.write(app_name)
    time.sleep(1.5)
    pyautogui.press('enter')
    print(f"Opening {app_name}")

def screenshot():
    img = pyautogui.screenshot()
    path = os.path.expanduser("~\\Pictures\\screenshot.png")
    img.save(path)
    print("Screenshot saved.")

def shutdown():
    if platform.system() == "Windows":
        subprocess.run(["shutdown", "/s", "/t", "0"])

def restart():
    if platform.system() == "Windows":
        subprocess.run(["shutdown", "/r", "/t", "0"])

def lock():
    if platform.system() == "Windows":
        subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"])

def volume(action: str):
    """action: up / down / mute"""
    if action == "up":
        pyautogui.press("volumeup")
    elif action == "down":
        pyautogui.press("volumedown")
    elif action == "mute":
        pyautogui.press("volumemute")