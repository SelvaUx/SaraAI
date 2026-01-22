"""
Sara AI Max - Graphical User Interface

A modern GUI with both text and voice input modes.
"""

import asyncio
import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
from datetime import datetime
from typing import Optional

from sara_core.voice_engine import VoiceEngine
from sara_core.nlu import NLUEngine
from sara_core.planner import Planner
from sara_core.executor import Executor
from sara_core.security import SecurityManager
from sara_core.context import ContextManager


class SaraGUI:
    """Sara AI Max GUI Application."""
    
    def __init__(self):
        """Initialize GUI."""
        self.root = tk.Tk()
        self.root.title("Sara AI Max - Your Intelligent Desktop Assistant")
        self.root.geometry("900x700")
        self.root.configure(bg='#1e1e1e')
        
        # Initialize Sara components
        self.context = ContextManager()
        self.security = SecurityManager()
        self.voice = VoiceEngine()
        self.nlu = NLUEngine()
        self.planner = Planner(self.security)
        self.executor = Executor(self.security, self.context)
        
        # GUI state
        self.voice_mode = False
        self.is_listening = False
        
        # Create UI
        self.create_widgets()
        
        # Log startup
        self.append_message("system", "Sara AI Max initialized. Ready to assist!")
    
    def create_widgets(self):
        """Create GUI widgets."""
        # Title bar
        title_frame = tk.Frame(self.root, bg='#2d2d2d', height=60)
        title_frame.pack(fill=tk.X, padx=0, pady=0)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame,
            text="🤖 SARA AI MAX",
            font=('Arial', 20, 'bold'),
            bg='#2d2d2d',
            fg='#00ff88'
        )
        title_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        # Status indicator
        self.status_label = tk.Label(
            title_frame,
            text="● Ready",
            font=('Arial', 12),
            bg='#2d2d2d',
            fg='#00ff88'
        )
        self.status_label.pack(side=tk.RIGHT, padx=20, pady=10)
        
        # Main content area
        content_frame = tk.Frame(self.root, bg='#1e1e1e')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - Conversation
        left_panel = tk.Frame(content_frame, bg='#1e1e1e')
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # Conversation display
        conv_label = tk.Label(
            left_panel,
            text="Conversation",
            font=('Arial', 12, 'bold'),
            bg='#1e1e1e',
            fg='#ffffff'
        )
        conv_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.conversation_display = scrolledtext.ScrolledText(
            left_panel,
            wrap=tk.WORD,
            font=('Consolas', 10),
            bg='#2d2d2d',
            fg='#ffffff',
            insertbackground='#00ff88',
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.conversation_display.pack(fill=tk.BOTH, expand=True)
        self.conversation_display.config(state=tk.DISABLED)
        
        # Right panel - Controls
        right_panel = tk.Frame(content_frame, bg='#2d2d2d', width=300)
        right_panel.pack(side=tk.RIGHT, fill=tk.Y, padx=(5, 0))
        right_panel.pack_propagate(False)
        
        # Mode selector
        mode_frame = tk.Frame(right_panel, bg='#2d2d2d')
        mode_frame.pack(fill=tk.X, padx=15, pady=15)
        
        mode_label = tk.Label(
            mode_frame,
            text="Input Mode",
            font=('Arial', 11, 'bold'),
            bg='#2d2d2d',
            fg='#ffffff'
        )
        mode_label.pack(anchor=tk.W, pady=(0, 8))
        
        self.mode_var = tk.StringVar(value="text")
        
        text_radio = tk.Radiobutton(
            mode_frame,
            text="📝 Text Mode",
            variable=self.mode_var,
            value="text",
            font=('Arial', 10),
            bg='#2d2d2d',
            fg='#ffffff',
            selectcolor='#1e1e1e',
            activebackground='#2d2d2d',
            activeforeground='#00ff88',
            command=self.on_mode_change
        )
        text_radio.pack(anchor=tk.W, pady=2)
        
        voice_radio = tk.Radiobutton(
            mode_frame,
            text="🎤 Voice Mode",
            variable=self.mode_var,
            value="voice",
            font=('Arial', 10),
            bg='#2d2d2d',
            fg='#ffffff',
            selectcolor='#1e1e1e',
            activebackground='#2d2d2d',
            activeforeground='#00ff88',
            command=self.on_mode_change
        )
        voice_radio.pack(anchor=tk.W, pady=2)
        
        # Test commands
        test_frame = tk.Frame(right_panel, bg='#2d2d2d')
        test_frame.pack(fill=tk.X, padx=15, pady=15)
        
        test_label = tk.Label(
            test_frame,
            text="Quick Test Commands",
            font=('Arial', 11, 'bold'),
            bg='#2d2d2d',
            fg='#ffffff'
        )
        test_label.pack(anchor=tk.W, pady=(0, 8))
        
        test_commands = [
            ("⏰ What time is it?", "what time is it"),
            ("📅 What's the date?", "what's the date"),
            ("💻 System info", "system info"),
            ("🔍 Search Python", "search for Python tutorials"),
            ("📁 Create folder", "create folder named TestFolder"),
            ("😄 Tell a joke", "tell me a joke"),
        ]
        
        for label, command in test_commands:
            btn = tk.Button(
                test_frame,
                text=label,
                font=('Arial', 9),
                bg='#3d3d3d',
                fg='#ffffff',
                activebackground='#00ff88',
                activeforeground='#1e1e1e',
                relief=tk.FLAT,
                cursor='hand2',
                command=lambda cmd=command: self.send_test_command(cmd)
            )
            btn.pack(fill=tk.X, pady=3)
        
        # Input area
        input_frame = tk.Frame(self.root, bg='#2d2d2d', height=100)
        input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        input_frame.pack_propagate(False)
        
        # Text input
        self.text_input = tk.Entry(
            input_frame,
            font=('Arial', 11),
            bg='#3d3d3d',
            fg='#ffffff',
            insertbackground='#00ff88',
            relief=tk.FLAT
        )
        self.text_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 5), pady=10)
        self.text_input.bind('<Return>', lambda e: self.send_message())
        
        # Send button
        self.send_button = tk.Button(
            input_frame,
            text="Send ➤",
            font=('Arial', 11, 'bold'),
            bg='#00ff88',
            fg='#1e1e1e',
            activebackground='#00cc66',
            relief=tk.FLAT,
            cursor='hand2',
            command=self.send_message,
            width=10
        )
        self.send_button.pack(side=tk.RIGHT, padx=(5, 10), pady=10, ipady=8)
        
        # Voice button (initially hidden)
        self.voice_button = tk.Button(
            input_frame,
            text="🎤 Start Listening",
            font=('Arial', 11, 'bold'),
            bg='#ff5555',
            fg='#ffffff',
            activebackground='#ff3333',
            relief=tk.FLAT,
            cursor='hand2',
            command=self.toggle_voice_listening
        )
    
    def on_mode_change(self):
        """Handle mode change."""
        mode = self.mode_var.get()
        
        if mode == "text":
            self.voice_button.pack_forget()
            self.text_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 5), pady=10)
            self.send_button.pack(side=tk.RIGHT, padx=(5, 10), pady=10, ipady=8)
            self.voice_mode = False
        else:
            self.text_input.pack_forget()
            self.send_button.pack_forget()
            self.voice_button.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            self.voice_mode = True
    
    def toggle_voice_listening(self):
        """Toggle voice listening."""
        if not self.is_listening:
            self.is_listening = True
            self.voice_button.config(
                text="🛑 Stop Listening",
                bg='#00ff88',
                fg='#1e1e1e'
            )
            self.status_label.config(text="● Listening...", fg='#ff5555')
            threading.Thread(target=self.listen_voice, daemon=True).start()
        else:
            self.is_listening = False
            self.voice_button.config(
                text="🎤 Start Listening",
                bg='#ff5555',
                fg='#ffffff'
            )
            self.status_label.config(text="● Ready", fg='#00ff88')
    
    def listen_voice(self):
        """Listen for voice input."""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            while self.is_listening:
                # Listen for command
                command = loop.run_until_complete(
                    self.voice.listen_for_command(timeout=5)
                )
                
                if command and self.is_listening:
                    self.root.after(0, lambda: self.append_message("user", command))
                    self.root.after(0, lambda: self.process_command(command))
        except Exception as e:
            self.root.after(0, lambda: self.append_message("error", f"Voice error: {str(e)}"))
        finally:
            loop.close()
    
    def send_test_command(self, command: str):
        """Send a test command."""
        self.text_input.delete(0, tk.END)
        self.text_input.insert(0, command)
        self.send_message()
    
    def send_message(self):
        """Send text message."""
        message = self.text_input.get().strip()
        if not message:
            return
        
        self.text_input.delete(0, tk.END)
        self.append_message("user", message)
        self.process_command(message)
    
    def process_command(self, command: str):
        """Process a command."""
        self.status_label.config(text="● Processing...", fg='#ffaa00')
        
        def process():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            try:
                # Parse intent
                intent = self.nlu.parse(command)
                
                # Create plan
                plan = self.planner.create_plan(intent)
                
                # Execute
                result = loop.run_until_complete(self.executor.execute(plan))
                
                # Display result
                if result.success:
                    response = result.message or "Done!"
                    self.root.after(0, lambda: self.append_message("sara", response))
                    
                    # Speak if voice mode
                    if self.voice_mode:
                        self.voice.speak(response)
                else:
                    error = result.error or "Something went wrong"
                    self.root.after(0, lambda: self.append_message("error", error))
                
            except Exception as e:
                self.root.after(0, lambda: self.append_message("error", f"Error: {str(e)}"))
            finally:
                self.root.after(0, lambda: self.status_label.config(text="● Ready", fg='#00ff88'))
                loop.close()
        
        threading.Thread(target=process, daemon=True).start()
    
    def append_message(self, sender: str, message: str):
        """Append message to conversation."""
        self.conversation_display.config(state=tk.NORMAL)
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Color coding
        colors = {
            "user": "#00ccff",
            "sara": "#00ff88",
            "system": "#ffaa00",
            "error": "#ff5555"
        }
        
        prefixes = {
            "user": "You",
            "sara": "Sara",
            "system": "System",
            "error": "Error"
        }
        
        color = colors.get(sender, "#ffffff")
        prefix = prefixes.get(sender, "Unknown")
        
        # Insert timestamp
        self.conversation_display.insert(tk.END, f"[{timestamp}] ", "timestamp")
        self.conversation_display.tag_config("timestamp", foreground="#888888")
        
        # Insert sender
        self.conversation_display.insert(tk.END, f"{prefix}: ", sender)
        self.conversation_display.tag_config(sender, foreground=color, font=('Consolas', 10, 'bold'))
        
        # Insert message
        self.conversation_display.insert(tk.END, f"{message}\n")
        
        self.conversation_display.config(state=tk.DISABLED)
        self.conversation_display.see(tk.END)
    
    def run(self):
        """Run the GUI."""
        self.root.mainloop()


def main():
    """Main entry point for GUI."""
    app = SaraGUI()
    app.run()


if __name__ == "__main__":
    main()
