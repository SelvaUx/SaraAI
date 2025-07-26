import pyautogui
import time
import os

def open_application(app_name: str) -> None:
    """Search and open applications using Windows Search."""
    pyautogui.hotkey('win')  # Press the Windows key
    time.sleep(1)  # Wait for the Start Menu to open
    
    # Type the app name (e.g., 'notepad', 'cmd', etc.)
    pyautogui.write(app_name)
    time.sleep(1)  # Wait for search results to show up
    
    # Press Enter to open the first application in the search results
    pyautogui.press('enter')
    print(f"Opening {app_name} via Windows search.")

def screenshot() -> None:
    """Takes a screenshot and saves it."""
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\screenshot.png")
    img.save(img_path)
    print(f"Screenshot saved as {img_path}.")
