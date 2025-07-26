#!/usr/bin/env python3
"""
Sara AI - Fast Startup Mode
Minimal features for maximum performance
"""

import time
import logging
import urllib.parse
import os
from datetime import datetime

# Minimal imports for fast startup
import speech_recognition as sr
import pyttsx3
import pyautogui
import psutil

print("🚀 Sara AI Fast Mode - Starting...")

class FastSaraAI:
    def __init__(self):
        """Fast initialization with minimal features"""
        print("  ⚡ Initializing core systems...")
        
        # Setup logging
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(os.path.join(log_dir, 'sara_fast.log')),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger('FastSara')
        
        # Voice system (essential)
        print("  🎤 Voice system...")
        self.setup_voice()
        
        # Basic automation
        print("  🖱️ Automation system...")
        self.setup_automation()
        
        # State
        self.is_listening = False
        
        print("✅ Fast Sara AI ready!")
        
    def setup_voice(self):
        """Setup minimal voice system"""
        try:
            # Text-to-speech
            self.tts = pyttsx3.init()
            self.tts.setProperty('rate', 200)  # Faster speech
            self.tts.setProperty('volume', 0.9)
            
            # Get available voices and set a good one
            voices = self.tts.getProperty('voices')
            if voices:
                # Try to set a female voice if available
                for voice in voices:
                    if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
                        self.tts.setProperty('voice', voice.id)
                        break
            
            # Speech recognition
            self.recognizer = sr.Recognizer()
            self.recognizer.energy_threshold = 300
            self.recognizer.dynamic_energy_threshold = True
            self.recognizer.pause_threshold = 0.8
            
            # Initialize microphone
            self.microphone = sr.Microphone()
            
            # Quick calibration
            print("  🎧 Calibrating microphone...")
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
            self.logger.info("Voice system initialized successfully")
                
        except Exception as e:
            error_msg = f"Voice setup error: {e}"
            print(f"⚠️ {error_msg}")
            self.logger.error(error_msg)
            
    def setup_automation(self):
        """Setup minimal automation"""
        try:
            pyautogui.FAILSAFE = True
            pyautogui.PAUSE = 0.2  # Fast automation
            
        except Exception as e:
            print(f"⚠️ Automation setup error: {e}")
            
    def speak(self, text):
        """Quick text-to-speech"""
        try:
            self.tts.say(text)
            self.tts.runAndWait()
        except Exception:
            print(f"Sara: {text}")  # Fallback to text
            
    def listen(self):
        """Quick voice recognition"""
        try:
            with self.microphone as source:
                audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=5)
            return self.recognizer.recognize_google(audio).lower()
        except Exception:
            return None
            
    def detect_wake_word(self):
        """Simple wake word detection"""
        try:
            audio = self.listen()
            if audio and ('sara' in audio or 'hey sara' in audio):
                return True
        except Exception:
            pass
        return False
        
    def execute_command(self, command):
        """Execute basic commands quickly"""
        command = command.lower()
        
        # App launching (fast)
        if 'open' in command:
            apps = {
                'notepad': 'notepad',
                'calculator': 'calc',
                'paint': 'mspaint',
                'chrome': 'chrome',
                'firefox': 'firefox',
                'file explorer': 'explorer',
                'task manager': 'taskmgr'
            }
            
            for app_name, app_cmd in apps.items():
                if app_name in command:
                    try:
                        pyautogui.press('win')
                        time.sleep(0.5)
                        pyautogui.type(app_cmd)
                        time.sleep(0.5)
                        pyautogui.press('enter')
                        self.speak(f"Opening {app_name}")
                        return
                    except Exception:
                        pass
                        
        # System commands (fast)
        elif 'screenshot' in command or 'capture screen' in command or 'take screenshot' in command:
            try:
                # Create screenshots directory if it doesn't exist
                screenshots_dir = "screenshots"
                if not os.path.exists(screenshots_dir):
                    os.makedirs(screenshots_dir)
                
                # Take screenshot
                screenshot = pyautogui.screenshot()
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = os.path.join(screenshots_dir, f"screenshot_{timestamp}.png")
                screenshot.save(filename)
                
                self.speak(f"Screenshot saved as {filename}")
                print(f"📸 Screenshot saved: {filename}")
                return
            except Exception as e:
                self.speak("Failed to take screenshot")
                print(f"❌ Screenshot error: {e}")
                return
                
        elif 'lock' in command:
            try:
                pyautogui.hotkey('win', 'l')
                self.speak("Screen locked")
                return
            except Exception:
                pass
                
        elif 'volume up' in command:
            try:
                for _ in range(3):
                    pyautogui.press('volumeup')
                self.speak("Volume up")
                return
            except Exception:
                pass
                
        elif 'volume down' in command:
            try:
                for _ in range(3):
                    pyautogui.press('volumedown')
                self.speak("Volume down")
                return
            except Exception:
                pass
                
        # Web search (fast)
        elif 'search' in command:
            try:
                # Extract search query
                query = command.replace('search for', '').replace('search', '').strip()
                if query:
                    pyautogui.press('win')
                    time.sleep(0.5)
                    pyautogui.type('chrome')
                    time.sleep(0.5)
                    pyautogui.press('enter')
                    time.sleep(2)
                    pyautogui.hotkey('ctrl', 'l')
                    time.sleep(0.5)
                    pyautogui.type(f"https://www.google.com/search?q={urllib.parse.quote_plus(query)}")
                    pyautogui.press('enter')
                    self.speak(f"Searching for {query}")
                    return
            except Exception:
                pass
                
        # Time and date
        elif 'time' in command:
            current_time = time.strftime("%I:%M %p")
            self.speak(f"The time is {current_time}")
            return
            
        elif 'date' in command:
            current_date = time.strftime("%A, %B %d, %Y")
            self.speak(f"Today is {current_date}")
            return
            
        # Screenshot with region (advanced)
        elif 'screenshot region' in command or 'capture region' in command:
            try:
                self.speak("Click and drag to select the region to capture")
                time.sleep(2)
                
                # Get region from user (simplified - full screen for now)
                screenshots_dir = "screenshots"
                if not os.path.exists(screenshots_dir):
                    os.makedirs(screenshots_dir)
                
                screenshot = pyautogui.screenshot()
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = os.path.join(screenshots_dir, f"region_screenshot_{timestamp}.png")
                screenshot.save(filename)
                
                self.speak("Region screenshot saved")
                print(f"📸 Region screenshot saved: {filename}")
                return
            except Exception as e:
                self.speak("Failed to take region screenshot")
                print(f"❌ Region screenshot error: {e}")
                return
                
        # System information
        elif 'system info' in command or 'system information' in command:
            try:
                # Get basic system info
                cpu_percent = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()
                disk = psutil.disk_usage('/')
                
                info = f"CPU usage: {cpu_percent}%. Memory usage: {memory.percent}%. Disk usage: {disk.percent}%"
                self.speak(info)
                print(f"💻 System Info: {info}")
                return
            except Exception as e:
                self.speak("Failed to get system information")
                print(f"❌ System info error: {e}")
                return
                
        # Help command
        elif 'help' in command or 'what can you do' in command or 'commands' in command:
            help_text = """I can help you with:
            - Take screenshots: 'take screenshot' or 'capture screen'
            - Open applications: 'open calculator', 'open notepad', 'open chrome'
            - System controls: 'lock screen', 'volume up', 'volume down'
            - Web search: 'search for python tutorials'
            - Time and date: 'what time is it', 'what's the date'
            - System info: 'system information'
            - Exit: 'goodbye' or 'exit'
            """
            self.speak("Here are some things I can do for you")
            print("📋 Available Commands:")
            print(help_text)
            return
            
        # Exit command
        elif 'exit' in command or 'quit' in command or 'goodbye' in command or 'stop' in command:
            self.speak("Goodbye! Sara AI is shutting down.")
            print("👋 Sara AI shutting down...")
            return "exit"
        
        # Default response
        self.speak("I didn't understand that command. Say 'help' to see available commands.")
        
    def run(self):
        """Main loop"""
        print("🎤 Fast Sara AI active! Say 'Hey Sara' to activate.")
        self.speak("Fast Sara AI is ready")
        
        while True:
            try:
                if self.detect_wake_word():
                    self.speak("Yes?")
                    command = self.listen()
                    
                    if command:
                        print(f"🎤 Command: {command}")
                        result = self.execute_command(command)
                        if result == "exit":
                            break
                    else:
                        self.speak("I didn't hear anything")
                        
                time.sleep(0.1)  # Small delay
                
            except KeyboardInterrupt:
                self.speak("Goodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(1)

def main():
    """Fast startup"""
    try:
        sara = FastSaraAI()
        sara.run()
    except Exception as e:
        print(f"❌ Fast Sara AI error: {e}")
        
if __name__ == "__main__":
    main()
