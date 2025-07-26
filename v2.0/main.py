from application_handler import open_application, screenshot
from tts import speak
from utils import time as get_time, date as get_date, search_wikipedia, joke
from browser_handler import handle_browser_commands
from music_player import play_music
from voice_input import listen_for_command

import time

def handle_command(command: str) -> None:
    """Handles user commands and calls appropriate functions."""

    if "search" in command:
        speak(f"Searching for {command.replace('search', '').strip()} in Google.")
        handle_browser_commands(command)

    elif "open" in command:
        speak(f"Opening {command.replace('open', '').strip()} using Windows search.")
        handle_browser_commands(command)

    elif "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        result = search_wikipedia(query)
        speak(f"Here's what I found on Wikipedia: {result}")

    elif "screenshot" in command:
        screenshot()
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

    elif "play music" in command:
        play_music()
        speak("Playing music from your Music folder.")

    else:
        speak("Sorry, I didn't understand that command.")

def main():
    print("Welcome to Sara AI! Say 'Hey Sara' to begin.")
    speak("Welcome to Sara AI. Say 'Hey Sara' to begin.")

    while True:
        command = listen_for_command()
        if command:
            handle_command(command)

if __name__ == "__main__":
    main()
