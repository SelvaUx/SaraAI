import pyautogui
import os
import time

def open_application(app_name: str) -> None:
    """Search and open applications using Windows Search by typing one letter at a time."""
    pyautogui.hotkey('win')  # Press the Windows key to open the Start Menu
    time.sleep(1)  # Wait for the Start Menu to open
    
    # Type the application name letter by letter
    for letter in app_name:
        pyautogui.write(letter)
        time.sleep(0.1)  # Simulate typing with a slight delay between each letter
    
    time.sleep(2)  # Wait for search results to show up
    
    # Press Enter to open the first application in the search results
    pyautogui.press('enter')
    print(f"Opening {app_name} via Windows search.")

def screenshot() -> None:
    """Takes a screenshot and saves it."""
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\screenshot.png")
    img.save(img_path)
    print(f"Screenshot saved as {img_path}.")
