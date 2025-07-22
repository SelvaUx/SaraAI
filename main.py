from application_handler import open_application, screenshot
from tts import speak
from utils import time as get_time, date as get_date, search_wikipedia, joke
from browser_handler import handle_browser_commands
import time

def handle_command(command: str) -> None:
    """Handles user commands and calls appropriate functions."""
    
    if "search" in command:
        # Pass the search query to handle_browser_commands
        speak(f"Searching for {command.replace('search', '').strip()} in Google.")
        handle_browser_commands(command)
    
    elif "open" in command:
        # Pass the open application command to handle_browser_commands (open app via Windows search)
        speak(f"Opening {command.replace('open', '').strip()} using Windows search.")
        handle_browser_commands(command)
    
    elif "wikipedia" in command:
        # Extract the query and perform a Wikipedia search
        query = command.replace("wikipedia", "").strip()  # Extract the search term
        result = search_wikipedia(query)
        speak(f"Here's what I found on Wikipedia: {result}")
    
    elif "screenshot" in command:
        screenshot()  # Capture and save a screenshot
        speak("Screenshot taken and saved in your Pictures folder.")
    
    elif "time" in command:
        result = get_time()
        speak(result)
    
    elif "date" in command:
        result = get_date()
        speak(result)
    
    elif "joke" in command:
        joke_text = joke()
        speak(joke_text)
    
    else:
        speak("Sorry, I didn't understand that command.")

def main():
    print("Welcome to Sara AI! How can I assist you today?")
    
    # Speak the welcome message with a more professional tone
    speak("Welcome to Sara AI! How can I assist you today?")
    
    while True:
        query = input("Enter command: ").lower()
        handle_command(query)

if __name__ == "__main__":
    main()
