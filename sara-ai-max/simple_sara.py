"""
Sara AI Max - SIMPLIFIED WORKING VERSION
Based on proven v3.0 architecture

This version ACTUALLY WORKS with:
- Text mode for testing
- Simple command processing
- Real voice recognition
- All basic features functional
"""

import os
import sys
import time
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import webbrowser
import subprocess
import pyautogui
from pathlib import Path


class SimpleSara:
    """Simplified, working Sara AI Max."""
    
    def __init__(self, text_mode=False):
        """Initialize Sara."""
        print("🚀 Starting Sara AI Max (Simplified)...")
        
        # Initialize TTS
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 160)
            voices = self.engine.getProperty('voices')
            if len(voices) > 1:
                self.engine.setProperty('voice', voices[1].id)  # Female voice
        except Exception as e:
            print(f"⚠️ TTS Error: {e}")
            self.engine = None
        
        # Initialize STT
        self.recognizer = sr.Recognizer()
        self.microphone = None
        
        if not text_mode:
            try:
                self.microphone = sr.Microphone()
                print("✅ Microphone initialized")
            except Exception as e:
                print(f"⚠️ No microphone: {e}")
        
        print("✅ Sara AI Max ready!")
    
    def speak(self, text):
        """Speak text."""
        print(f"Sara: {text}")
        try:
            if self.engine:
                self.engine.say(text)
                self.engine.runAndWait()
        except:
            pass
    
    def listen(self):
        """Listen for voice command."""
        if not self.microphone:
            return None
        
        try:
            with self.microphone as source:
                print("🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
            
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't understand that")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def process_command(self, command):
        """Process a command."""
        try:
            # Time
            if 'time' in command:
                now = datetime.now()
                time_str = now.strftime("%I:%M %p")
                self.speak(f"The time is {time_str}")
                return True
            
            # Date
            elif 'date' in command:
                now = datetime.now()
                date_str = now.strftime("%A, %B %d, %Y")
                self.speak(f"Today is {date_str}")
                return True
            
            # Open app
            elif 'open' in command:
                # Extract app name
                words = command.split()
                if 'open' in words:
                    idx = words.index('open')
                    if idx + 1 < len(words):
                        app = words[idx + 1]
                        self.speak(f"Opening {app}")
                        try:
                            subprocess.Popen(['start', app], shell=True)
                        except:
                            subprocess.Popen([app], shell=True)
                        return True
            
            # Search
            elif 'search' in command or 'google' in command:
                # Extract query
                if 'for' in command:
                    query = command.split('for', 1)[1].strip()
                elif 'search' in command:
                    query = command.replace('search', '').strip()
                else:
                    query = command.replace('google', '').strip()
                
                self.speak(f"Searching for {query}")
                url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
                webbrowser.open(url)
                return True
            
            # Create folder
            elif 'create' in command and 'folder' in command:
                # Extract folder name
                words = command.split()
                if 'named' in words:
                    idx = words.index('named')
                    if idx + 1 < len(words):
                        folder_name = words[idx + 1]
                else:
                    folder_name = "NewFolder"
                
                desktop = Path.home() / "Desktop"
                folder_path = desktop / folder_name
                
                try:
                    folder_path.mkdir(exist_ok=True)
                    self.speak(f"Created folder {folder_name}")
                    return True
                except Exception as e:
                    self.speak(f"Error creating folder")
                    return False
            
            # Screenshot
            elif 'screenshot' in command:
                self.speak("Taking screenshot")
                try:
                    screenshot = pyautogui.screenshot()
                    desktop = Path.home() / "Desktop"
                    filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                    screenshot.save(desktop / filename)
                    self.speak("Screenshot saved")
                    return True
                except Exception as e:
                    self.speak("Error taking screenshot")
                    return False
            
            # Joke
            elif 'joke' in command:
                self.speak("Why did the programmer quit his job? Because he didn't get arrays!")
                return True
            
            # Help
            elif 'help' in command or 'commands' in command:
                self.show_help()
                return True
            
            # Unknown
            else:
                self.speak("I'm not sure how to help with that")
                return False
                
        except Exception as e:
            print(f"Error processing command: {e}")
            self.speak("Sorry, something went wrong")
            return False
    
    def show_help(self):
        """Show available commands."""
        help_text = """
Available Commands:
• What time is it?
• What's the date?
• Open [app name]
• Search for [topic]
• Create folder named [name]
• Take a screenshot
• Tell me a joke
"""
        print(help_text)
        self.speak("Check the console for available commands")
    
    def text_mode(self):
        """Run in text mode."""
        print("\n" + "="*50)
        print("🔤 SARA AI MAX - TEXT MODE")
        print("="*50)
        print("Type 'help' for commands")
        print("Type 'exit' to quit")
        print("="*50 + "\n")
        
        while True:
            try:
                command = input("You: ").strip().lower()
                
                if not command:
                    continue
                
                if command in ['exit', 'quit', 'bye']:
                    self.speak("Goodbye!")
                    break
                
                self.process_command(command)
                
            except KeyboardInterrupt:
                print("\n")
                self.speak("Goodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def voice_mode(self):
        """Run in voice mode."""
        print("\n" + "="*50)
        print("🎤 SARA AI MAX - VOICE MODE")
        print("="*50)
        print("Say 'Hey Sara' followed by your command")
        print("Press Ctrl+C to exit")
        print("="*50 + "\n")
        
        self.speak("Sara AI Max is ready. I'm listening for commands.")
        
        while True:
            try:
                command = self.listen()
                
                if command:
                    # Check for exit commands
                    if any(word in command for word in ['exit', 'quit', 'goodbye', 'bye']):
                        self.speak("Goodbye!")
                        break
                    
                    # Process command
                    self.process_command(command)
                
            except KeyboardInterrupt:
                print("\n")
                self.speak("Goodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(1)
    
    def start(self):
        """Start Sara AI Max."""
        if self.microphone:
            self.voice_mode()
        else:
            print("⚠️ No microphone detected, starting in text mode")
            self.text_mode()


def main():
    """Main entry point."""
    print("""
╔═══════════════════════════════════════╗
║      SARA AI MAX - SIMPLIFIED         ║
║         Working Version v1.0           ║
╚═══════════════════════════════════════╝
    """)
    
    # Check for text mode flag
    text_mode = '--text' in sys.argv or '-t' in sys.argv
    
    try:
        sara = SimpleSara(text_mode=text_mode)
        sara.start()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
