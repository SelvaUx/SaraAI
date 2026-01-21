import pyautogui
import time
import os
import sys

# Disable fail-safe (Move mouse to corner to abort) if needed, or keep True for safety
pyautogui.FAILSAFE = True

def open_application(app_name: str) -> None:
    """Search and open applications using Windows Search by typing one letter at a time."""
    print(f"Attempting to open: {app_name}")
    pyautogui.hotkey('win')  # Press the Windows key to open the Start Menu
    time.sleep(1)  # Wait for the Start Menu to open
    
    # Type the application name letter by letter
    for letter in app_name:
        pyautogui.write(letter)
        time.sleep(0.05)  # Simulate typing delay
    
    time.sleep(1)  # Wait for search results
    
    # Press Enter to open the first application
    pyautogui.press('enter')
    print(f"Opening {app_name} via Windows search.")

def screenshot() -> None:
    """Takes a screenshot and saves it."""
    # Ensure folder exists
    pictures_dir = os.path.expanduser("~\\Pictures")
    if not os.path.exists(pictures_dir):
        os.makedirs(pictures_dir)
        
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    img_path = os.path.join(pictures_dir, f"screenshot_{timestamp}.png")
    
    img = pyautogui.screenshot()
    img.save(img_path)
    print(f"Screenshot saved as {img_path}.")

def send_whatsapp_message(contact: str, message: str) -> None:
    """Sends a WhatsApp message using the desktop application."""
    print(f"Sending WhatsApp message to {contact}: {message}")
    
    # Open WhatsApp
    open_application("whatsapp")
    time.sleep(2) # Wait for WhatsApp to open/focus
    
    # Search for contact
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(0.5)
    
    # Clear any previous search
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    
    # Type contact name
    pyautogui.write(contact)
    time.sleep(2.0) # Wait for search results
    
    # Select first result
    # Press Down to ensure we select the contact from the list, not just stay in search
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1) # Wait for chat to load
    
    # Type message
    pyautogui.write(message)
    time.sleep(0.5)
    
    # Send
    pyautogui.press('enter')
    print("Message sent.")

if __name__ == "__main__":
    # Argument handling from Node.js
    # Usage: python automation.py [command] [args]
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "open" and len(sys.argv) > 2:
            app_name = " ".join(sys.argv[2:]) # Join remaining args as app name
            open_application(app_name)
            
        elif command == "screenshot":
            screenshot()
            
        elif command == "whatsapp" and len(sys.argv) > 3:
            # Expecting: python automation.py whatsapp "Contact Name" "Message"
            contact = sys.argv[2]
            message = " ".join(sys.argv[3:]) # Join remaining args as message just in case
            send_whatsapp_message(contact, message)
            
        else:
            print("Unknown command")