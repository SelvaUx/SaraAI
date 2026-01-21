#!/usr/bin/env python3
"""
Sara AI - Your Personal Offline JARVIS in Python
Main Engine - FIXED VERSION with better error handling
"""

import os
import sys
import time
import threading
import logging
from datetime import datetime

# Import configuration for performance optimization
try:
    from config import (
        VOICE_SETTINGS, AI_SETTINGS, SYSTEM_SETTINGS, FEATURES,
        STARTUP_SETTINGS, MEMORY_SETTINGS, DYNAMIC_SETTINGS
    )
except ImportError:
    # Fallback settings if config.py is not available
    VOICE_SETTINGS = {'wake_word_timeout': 0.5, 'command_timeout': 5}
    AI_SETTINGS = {'use_rule_based_only': True, 'use_local_ai': False}
    SYSTEM_SETTINGS = {'automation_delay': 0.3, 'fast_mode': True}
    FEATURES = {'voice_commands': True, 'app_launcher': True, 'system_control': True,
               'browser_control': True, 'code_writer': True, 'music_control': True,
               'file_manager': True, 'uninstall_manager': False}
    STARTUP_SETTINGS = {'lazy_load_modules': True, 'quick_start_mode': True}
    MEMORY_SETTINGS = {'max_history_items': 50}
    DYNAMIC_SETTINGS = {'max_worker_threads': 2}

# Import core modules immediately
try:
    from voice_engine import VoiceEngine
    from ai_engine import AIEngine
    CORE_MODULES_AVAILABLE = True
except ImportError as e:
    print(f"❌ Core modules not available: {e}")
    CORE_MODULES_AVAILABLE = False

# Lazy load optional modules based on configuration
BrowserController = None
CodeWriter = None
MusicController = None
FileManager = None
UninstallManager = None

try:
    if FEATURES.get('browser_control', True):
        from browser_control.browser import BrowserController
except ImportError:
    print("⚠️ Browser control not available")

try:
    if FEATURES.get('code_writer', True):
        from code_writer.write_code import CodeWriter
except ImportError:
    print("⚠️ Code writer not available")

try:
    if FEATURES.get('music_control', True):
        from music_control.music import MusicController
except ImportError:
    print("⚠️ Music control not available")

try:
    from software_launcher.open_apps import AppLauncher
    from system_control.lock_shutdown import SystemController
except ImportError as e:
    print(f"❌ Essential modules not available: {e}")
    sys.exit(1)

try:
    if FEATURES.get('file_manager', True):
        from system_control.file_manager import FileManager
except ImportError:
    print("⚠️ File manager not available")

try:
    if FEATURES.get('uninstall_manager', False):
        from system_control.uninstall import UninstallManager
except ImportError:
    print("⚠️ Uninstall manager not available")

class SaraAI:
    def __init__(self, text_mode=False):
        """Initialize Sara AI with all required modules"""
        print("🚀 Initializing Sara AI (Performance Mode)...")
        
        if not CORE_MODULES_AVAILABLE:
            print("❌ Core modules not available, cannot start")
            sys.exit(1)
        
        # Setup logging (minimal for performance)
        self.setup_logging()
        
        # Initialize core engines with performance settings
        print("  📡 Loading voice engine...")
        try:
            self.voice_engine = VoiceEngine(skip_microphone=text_mode)
        except Exception as e:
            print(f"❌ Voice engine failed: {e}")
            self.voice_engine = None
        
        print("  🧠 Loading AI engine...")
        try:
            self.ai_engine = AIEngine()
        except Exception as e:
            print(f"❌ AI engine failed: {e}")
            sys.exit(1)
        
        # Initialize controllers conditionally for better performance
        print("  🚀 Loading controllers...")
        
        # Always load essential controllers
        try:
            self.app_launcher = AppLauncher()
            self.system_controller = SystemController()
        except Exception as e:
            print(f"❌ Essential controllers failed: {e}")
            sys.exit(1)
        
        # Load optional controllers based on configuration
        self.browser_controller = None
        self.code_writer = None
        self.music_controller = None
        self.file_manager = None
        self.uninstall_manager = None
        
        try:
            if BrowserController and FEATURES.get('browser_control', True):
                self.browser_controller = BrowserController()
        except Exception as e:
            print(f"⚠️ Browser controller failed: {e}")
            
        try:
            if CodeWriter and FEATURES.get('code_writer', True):
                self.code_writer = CodeWriter()
        except Exception as e:
            print(f"⚠️ Code writer failed: {e}")
            
        try:
            if MusicController and FEATURES.get('music_control', True):
                self.music_controller = MusicController()
        except Exception as e:
            print(f"⚠️ Music controller failed: {e}")
            
        try:
            if FileManager and FEATURES.get('file_manager', True):
                self.file_manager = FileManager()
        except Exception as e:
            print(f"⚠️ File manager failed: {e}")
            
        try:
            if UninstallManager and FEATURES.get('uninstall_manager', False):
                self.uninstall_manager = UninstallManager()
        except Exception as e:
            print(f"⚠️ Uninstall manager failed: {e}")
        
        # State variables
        self.is_active = False
        self.listening = False
        self.command_count = 0
        self.last_cleanup = time.time()
        
        print("✅ Sara AI initialized successfully!")
        
    def speak(self, text: str):
        """Speak with fallback to text output"""
        try:
            if self.voice_engine:
                self.voice_engine.speak(text)
            else:
                print(f"Sara: {text}")
        except Exception as e:
            self.logger.debug(f"TTS failed: {e}")
            print(f"Sara: {text}")
        
    def setup_logging(self):
        """Setup logging configuration"""
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f'{log_dir}/sara_ai.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger('SaraAI')
        
    def wake_word_listener(self):
        """Listen for wake word in separate thread"""
        if not self.voice_engine or not self.voice_engine.microphone:
            print("⚠️ No microphone available for wake word detection")
            return
            
        while True:
            try:
                if self.voice_engine.detect_wake_word():
                    self.logger.info("Wake word detected!")
                    self.speak("Yes, I'm listening.")
                    self.process_voice_command()
                time.sleep(0.1)
            except KeyboardInterrupt:
                break
            except Exception as e:
                self.logger.error(f"Error in wake word listener: {e}")
                time.sleep(1)  # Wait before retrying
            
    def process_voice_command(self):
        """Process voice command after wake word detection"""
        try:
            # Get voice input
            if not self.voice_engine:
                return
                
            command = self.voice_engine.listen_for_command()
            if not command:
                self.speak("I didn't catch that. Could you repeat?")
                return
                
            self.logger.info(f"Command received: {command}")
            
            # Process command through AI engine
            intent, entities = self.ai_engine.understand_command(command)
            
            # Execute appropriate action
            self.execute_command(intent, entities, command)
            
        except Exception as e:
            self.logger.error(f"Error processing command: {e}")
            self.speak("Sorry, I encountered an error processing your command.")
            
    def execute_command(self, intent, entities, original_command):
        """Execute the appropriate command based on intent"""
        try:
            if intent == "browser_search":
                if self.browser_controller:
                    query = entities.get('query', original_command)
                    self.browser_controller.search_and_open(query)
                    self.speak(f"Searching for {query}")
                else:
                    self.speak("Browser control is not available")
                
            elif intent == "open_app":
                app_name = entities.get('app_name', original_command)
                self.app_launcher.open_application(app_name)
                self.speak(f"Opening {app_name}")
                
            elif intent == "write_code":
                if self.code_writer:
                    code_type = entities.get('code_type', 'html')
                    self.code_writer.create_code_template(code_type)
                    self.speak(f"Creating {code_type} code template")
                else:
                    self.speak("Code writer is not available")
                
            elif intent == "play_music":
                if self.music_controller:
                    self.music_controller.play_music()
                    self.speak("Playing music")
                else:
                    self.speak("Music control is not available")
                
            elif intent == "pause_music":
                if self.music_controller:
                    self.music_controller.pause_music()
                    self.speak("Music paused")
                else:
                    self.speak("Music control is not available")
                
            elif intent == "system_shutdown":
                self.speak("Shutting down the system")
                self.system_controller.shutdown()
                
            elif intent == "system_lock":
                self.speak("Locking the system")
                self.system_controller.lock_screen()
                
            elif intent == "create_file":
                if self.file_manager:
                    filename = entities.get('filename', 'new_file.txt')
                    self.file_manager.create_file(filename)
                    self.speak(f"Created file {filename}")
                else:
                    self.speak("File manager is not available")
                
            elif intent == "create_folder":
                if self.file_manager:
                    foldername = entities.get('foldername', 'new_folder')
                    self.file_manager.create_folder(foldername)
                    self.speak(f"Created folder {foldername}")
                else:
                    self.speak("File manager is not available")
                
            elif intent == "uninstall_app":
                if self.uninstall_manager:
                    app_name = entities.get('app_name', original_command)
                    self.uninstall_manager.uninstall_application(app_name)
                    self.speak(f"Uninstalling {app_name}")
                else:
                    self.speak("Uninstall manager is not available")
                
            elif intent == "take_screenshot":
                self.system_controller.take_screenshot()
                self.speak("Screenshot taken")
                
            elif intent == "volume_control":
                action = entities.get('action', 'up')
                self.system_controller.adjust_volume(action)
                self.speak(f"Volume {action}")
                
            elif intent == "general_chat":
                response = self.ai_engine.generate_response(original_command)
                self.speak(response)
                
            else:
                self.speak("I'm not sure how to help with that yet.")
                
        except Exception as e:
            self.logger.error(f"Error executing command: {e}")
            self.speak("Sorry, I couldn't complete that task.")
            
    def text_mode(self):
        """Text-based testing mode"""
        print("\n🔤 Sara AI Text Mode")
        print("💡 Type commands or 'help' for assistance")
        print("💡 Type 'exit' to quit")
        print("-" * 50)
        
        while True:
            try:
                command = input("\nSara> ").strip()
                
                if not command:
                    continue
                    
                if command.lower() in ['exit', 'quit', 'goodbye']:
                    self.speak("Goodbye!")
                    break
                    
                elif command.lower() in ['help', 'commands']:
                    self.show_help()
                    continue
                    
                # Process command through AI engine
                intent, entities = self.ai_engine.understand_command(command)
                print(f"Debug: Intent={intent}, Entities={entities}")
                
                # Execute command
                self.execute_command(intent, entities, command)
                
            except KeyboardInterrupt:
                print("\n👋 Sara AI shutting down...")
                self.speak("Goodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
                
    def show_help(self):
        """Show available commands"""
        help_text = """
🎯 Available Commands:
• "search for [topic]" - Web search
• "open [app]" - Launch applications  
• "write [language] code" - Generate code
• "take a screenshot" - Capture screen
• "volume up/down" - Control volume
• "what time is it?" - Get current time
• "hello" - General conversation
        """
        print(help_text)
            
    def start(self):
        """Start Sara AI system"""
        # Check if microphone is available
        if not self.voice_engine or not self.voice_engine.microphone:
            print("⚠️ Microphone not available, starting in text mode...")
            self.text_mode()
            return
            
        print("🎤 Sara AI is now active! Say 'Hey Sara' to wake me up.")
        print("💡 Tip: Press Ctrl+C to exit")
        
        try:
            self.speak("Sara AI is now active. Say Hey Sara to wake me up.")
        except Exception as e:
            print(f"⚠️ TTS Error: {e}")
        
        # Start wake word listener in separate thread
        wake_thread = threading.Thread(target=self.wake_word_listener)
        wake_thread.daemon = True
        wake_thread.start()
        
        # Keep main thread alive
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n👋 Sara AI shutting down...")
            self.speak("Goodbye!")
            sys.exit(0)

def main():
    """Main entry point"""
    try:
        # Check for text mode argument
        if len(sys.argv) > 1 and sys.argv[1].lower() in ['--text', '-t', 'text']:
            print("🔤 Starting Sara AI in text mode...")
            sara = SaraAI(text_mode=True)
            sara.text_mode()
        else:
            sara = SaraAI()
            sara.start()
    except Exception as e:
        print(f"❌ Error starting Sara AI: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()