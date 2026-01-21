# 🎯 Sara AI 3.0 - Complete Command Examples

This document provides comprehensive examples of all voice commands supported by Sara AI 3.0, organized by category with expected behaviors and variations.

## 🚀 Fast Mode vs Full Mode

Sara AI 3.0 has two operation modes:

- **🚀 Fast Mode** (`sara_fast.py`) - 2-3 second startup, essential commands only
- **🔥 Full Mode** (`main.py`) - Complete feature set with AI integration

---

## 🚀 Fast Mode Commands (sara_fast.py)

### 📸 Screenshot Commands
```
"Hey Sara, take a screenshot"
"Hey Sara, capture screen"
"Hey Sara, screenshot"
"Hey Sara, take a picture of the screen"
```

**Expected Behavior:**
1. Captures full screen instantly
2. Auto-creates `screenshots/` directory
3. Saves as `screenshot_YYYYMMDD_HHMMSS.png`
4. Confirms save with voice feedback

### 🚀 Application Launcher (Fast Mode)
```
"Hey Sara, open calculator"
"Hey Sara, open notepad"
"Hey Sara, open chrome"
"Hey Sara, open firefox"
"Hey Sara, open paint"
"Hey Sara, open file explorer"
"Hey Sara, open task manager"
```

**Expected Behavior:**
1. Opens Windows Search (Win key)
2. Types application name
3. Launches application
4. Voice confirmation

### 🔊 Volume & System Controls
```
"Hey Sara, volume up"
"Hey Sara, volume down"
"Hey Sara, lock screen"
"Hey Sara, system info"
"Hey Sara, system information"
```

**Expected Behavior:**
- **Volume**: Adjusts by 3 steps
- **Lock**: Immediately locks screen (Win+L)
- **System Info**: Reports CPU, memory, disk usage

### 🌐 Web Search (Fast Mode)
```
"Hey Sara, search for Python"
"Hey Sara, search for machine learning"
"Hey Sara, look up JavaScript"
```

**Expected Behavior:**
1. Opens Chrome via Windows Search
2. Navigates to Google
3. Performs search with proper URL encoding
4. Voice confirmation

### ⏰ Time & Date
```
"Hey Sara, what time is it?"
"Hey Sara, what's the date?"
"Hey Sara, what's the date today?"
```

**Expected Response:**
- **Time**: "The time is 2:30 PM"
- **Date**: "Today is Saturday, January 26, 2025"

### 📋 Help & Exit
```
"Hey Sara, help"
"Hey Sara, what can you do?"
"Hey Sara, commands"
"Hey Sara, goodbye"
"Hey Sara, exit"
"Hey Sara, quit"
```

**Expected Behavior:**
- **Help**: Lists all available commands
- **Exit**: Clean shutdown with goodbye message

---

## 🔥 Full Mode Commands (main.py)

*All Fast Mode commands plus advanced features below:*

---

## 🎤 Wake Word Activation

### Basic Activation
```
"Hey Sara"
"Sara"
"Hey Sarah"
"Sarah"
```

**Expected Response:**
- Sara acknowledges with: *"Yes, I'm listening."*
- System waits for your command
- LED indicator (if available) shows active state

---

## 🌐 Browser & Web Search Commands

### Web Search Commands
```
"Hey Sara, search for Python tutorials"
"Hey Sara, look up machine learning"
"Hey Sara, find information about Tesla"
"Hey Sara, google JavaScript courses"
"Hey Sara, browse for coding bootcamps"
"Hey Sara, search about climate change"
```

**Expected Behavior:**
1. Opens Windows Search (Win key)
2. Types "chrome" (or default browser)
3. Launches browser
4. Navigates to address bar (Ctrl+L)
5. Types search query in Google
6. Presses Enter to search

### Website Navigation
```
"Hey Sara, open YouTube"
"Hey Sara, go to GitHub"
"Hey Sara, visit Wikipedia"
"Hey Sara, open Facebook"
"Hey Sara, browse to Stack Overflow"
```

**Expected Behavior:**
1. Opens browser
2. Types website URL in address bar
3. Navigates to the specified website

### YouTube Commands
```
"Hey Sara, search for Python tutorial on YouTube"
"Hey Sara, play music on YouTube"
"Hey Sara, find funny videos"
"Hey Sara, YouTube search for cooking recipes"
```

**Expected Behavior:**
1. Opens browser
2. Navigates to YouTube
3. Searches for specified content
4. Attempts to click first video result

---

## 🚀 Application Launcher Commands

### Text Editors & IDEs
```
"Hey Sara, open Notepad"
"Hey Sara, launch Visual Studio Code"
"Hey Sara, start VS Code"
"Hey Sara, open text editor"
"Hey Sara, run Visual Studio"
"Hey Sara, launch Sublime Text"
```

**Expected Behavior:**
1. Opens Windows Search
2. Types application name
3. Launches the requested application

### Browsers
```
"Hey Sara, open Chrome"
"Hey Sara, launch Firefox"
"Hey Sara, start Edge"
"Hey Sara, open browser"
"Hey Sara, launch Internet Explorer"
```

### Office Applications
```
"Hey Sara, open Word"
"Hey Sara, launch Excel"
"Hey Sara, start PowerPoint"
"Hey Sara, open Microsoft Office"
"Hey Sara, launch Outlook"
```

### Media Players
```
"Hey Sara, open VLC"
"Hey Sara, launch Spotify"
"Hey Sara, start music player"
"Hey Sara, open Windows Media Player"
"Hey Sara, launch YouTube Music"
```

### System Tools
```
"Hey Sara, open Calculator"
"Hey Sara, launch Task Manager"
"Hey Sara, start Control Panel"
"Hey Sara, open Settings"
"Hey Sara, launch Command Prompt"
"Hey Sara, open PowerShell"
"Hey Sara, start File Explorer"
```

### Development Tools
```
"Hey Sara, open GitHub Desktop"
"Hey Sara, launch Docker"
"Hey Sara, start Postman"
"Hey Sara, open Git Bash"
```

### Graphics & Design
```
"Hey Sara, open Paint"
"Hey Sara, launch Photoshop"
"Hey Sara, start GIMP"
"Hey Sara, open Illustrator"
```

---

## 💻 Code Writing Commands

### HTML Code Generation
```
"Hey Sara, write HTML code"
"Hey Sara, create a login page"
"Hey Sara, write a signup form"
"Hey Sara, generate web page code"
"Hey Sara, create HTML template"
```

**Expected Behavior:**
1. Opens Notepad via Windows Search
2. Types complete HTML code (login/signup page)
3. Includes CSS styling
4. Ready for saving

### Python Code Generation
```
"Hey Sara, write Python code"
"Hey Sara, create Python program"
"Hey Sara, write a calculator in Python"
"Hey Sara, generate Python script"
"Hey Sara, create hello world Python"
```

**Expected Behavior:**
1. Opens Notepad
2. Types Python code template
3. Includes proper structure and comments

### C++ Code Generation
```
"Hey Sara, write C++ code"
"Hey Sara, create C++ program"
"Hey Sara, write C++ hello world"
"Hey Sara, generate C++ calculator"
```

### Java Code Generation
```
"Hey Sara, write Java code"
"Hey Sara, create Java program"
"Hey Sara, write Java hello world"
"Hey Sara, generate Java class"
```

### Custom Code Templates
```
"Hey Sara, write login page code"
"Hey Sara, create signup form"
"Hey Sara, generate calculator code"
"Hey Sara, write hello world program"
```

---

## ⚙️ System Control Commands

### Power Management
```
"Hey Sara, shutdown the computer"
"Hey Sara, turn off the PC"
"Hey Sara, power off the system"
"Hey Sara, shut down"
"Hey Sara, restart the computer"
"Hey Sara, reboot the system"
"Hey Sara, restart PC"
```

**Expected Behavior:**
- **Shutdown**: Executes `shutdown /s /t 10` (10-second delay)
- **Restart**: Executes `shutdown /r /t 10`
- Provides voice confirmation before execution

### Screen & Security
```
"Hey Sara, lock the screen"
"Hey Sara, lock the computer"
"Hey Sara, secure the PC"
"Hey Sara, lock system"
```

**Expected Behavior:**
1. Presses Win+L
2. Screen locks immediately
3. Confirms action with voice

### Sleep & Hibernate
```
"Hey Sara, put the computer to sleep"
"Hey Sara, hibernate the system"
"Hey Sara, sleep mode"
```

---

## 🔊 Volume & Audio Control

### Volume Adjustment
```
"Hey Sara, volume up"
"Hey Sara, increase volume"
"Hey Sara, turn volume up"
"Hey Sara, raise volume"
"Hey Sara, volume down"
"Hey Sara, decrease volume"
"Hey Sara, lower volume"
"Hey Sara, turn volume down"
```

**Expected Behavior:**
- Adjusts volume by ~10% increments
- Uses system volume keys
- Provides audio feedback

### Mute Control
```
"Hey Sara, mute"
"Hey Sara, silence"
"Hey Sara, turn off sound"
"Hey Sara, unmute"
```

**Expected Behavior:**
- Toggles mute state
- Uses system mute key

---

## 📸 Screenshot & Media Commands

### Screenshot Commands
```
"Hey Sara, take a screenshot"
"Hey Sara, capture the screen"
"Hey Sara, screenshot"
"Hey Sara, take a picture of the screen"
```

**Expected Behavior:**
1. Captures full screen instantly
2. Auto-creates `screenshots/` directory if needed
3. Saves with timestamp: `screenshot_YYYYMMDD_HHMMSS.png`
4. Voice confirmation with filename
5. Works in both Fast Mode and Full Mode

---

## 📁 File & Folder Management

### File Creation
```
"Hey Sara, create a file called test.txt"
"Hey Sara, make a file named document.doc"
"Hey Sara, new file called notes.txt"
"Hey Sara, create file report.pdf"
```

**Expected Behavior:**
1. Creates file in current directory
2. Uses specified filename
3. Confirms creation

### Folder Creation
```
"Hey Sara, create a folder called Projects"
"Hey Sara, make a folder named Documents"
"Hey Sara, new folder called Images"
"Hey Sara, create directory called Downloads"
```

**Expected Behavior:**
1. Creates folder in current directory
2. Uses specified folder name
3. Confirms creation

---

## 🗑️ Application Management

### Closing Applications
```
"Hey Sara, close this application"
"Hey Sara, close the current window"
"Hey Sara, exit this program"
```

**Expected Behavior:**
1. Presses Alt+F4
2. Closes active window
3. Confirms closure

### Uninstalling Software
```
"Hey Sara, uninstall Chrome"
"Hey Sara, remove Microsoft Word"
"Hey Sara, delete Spotify app"
"Hey Sara, uninstall this program"
```

**Expected Behavior:**
1. Opens Control Panel
2. Navigates to Programs & Features
3. Searches for specified application
4. Initiates uninstall process

---

## 🎵 Music & Media Control

### Music Playback (Coming Soon)
```
"Hey Sara, play music"
"Hey Sara, start music"
"Hey Sara, turn on music"
"Hey Sara, music on"
"Hey Sara, pause music"
"Hey Sara, stop music"
"Hey Sara, music off"
"Hey Sara, next song"
"Hey Sara, previous track"
```

---

## 🖱️ Window Management

### Window Operations
```
"Hey Sara, minimize all windows"
"Hey Sara, show desktop"
"Hey Sara, switch applications"
"Hey Sara, alt tab"
```

**Expected Behavior:**
- **Minimize all**: Win+D
- **Switch apps**: Alt+Tab
- **Show desktop**: Win+D

---

## 💬 Conversational Commands

### General Questions
```
"Hey Sara, what time is it?"
"Hey Sara, what's the date today?"
"Hey Sara, how are you?"
"Hey Sara, hello"
"Hey Sara, good morning"
"Hey Sara, what can you do?"
"Hey Sara, help me"
```

**Expected Responses:**
- **Time**: "The current time is 2:30 PM"
- **Date**: "Today is Friday, January 25, 2025"
- **Greeting**: "Hello! I'm Sara, your AI assistant. How can I help you today?"
- **Capabilities**: Lists available features and commands

### System Information
```
"Hey Sara, what's my computer name?"
"Hey Sara, system information"
"Hey Sara, computer specs"
"Hey Sara, battery status"
"Hey Sara, check battery"
```

**Expected Behavior:**
1. Retrieves system information via PowerShell
2. Reports computer name, OS, memory, etc.
3. Shows battery level (if laptop)

---

## 🔧 Advanced Commands

### Task Management
```
"Hey Sara, open Task Manager"
"Hey Sara, show running applications"
"Hey Sara, list running tasks"
"Hey Sara, kill Chrome process"
"Hey Sara, end Notepad task"
```

### System Cleanup
```
"Hey Sara, empty recycle bin"
"Hey Sara, clear trash"
"Hey Sara, clean recycle bin"
```

---

## 🎯 Command Variations & Natural Language

Sara AI understands flexible phrasing. These variations work for most commands:

### Flexible Phrasing Examples
```
"Hey Sara, I want to browse the internet" → Opens browser
"Hey Sara, can you search for Python?" → Performs web search  
"Hey Sara, I need to write some code" → Opens Notepad for coding
"Hey Sara, please take a screenshot" → Captures screen
"Hey Sara, could you lock my computer?" → Locks screen
"Hey Sara, I'd like to open Calculator" → Launches Calculator
```

### Indirect Commands
```
"Hey Sara, I want to browse" → Opens browser
"Hey Sara, I need to code" → Opens Notepad
"Hey Sara, time to sleep" → Puts computer to sleep
"Hey Sara, picture time" → Takes screenshot
"Hey Sara, secure my PC" → Locks screen
```

---

## ⚠️ Error Handling Examples

### When Commands Fail
```
User: "Hey Sara, open XYZ application"
Sara: "I couldn't find that application. Could you try a different name?"

User: "Hey Sara, delete system32"  
Sara: "I can't perform that action for security reasons."

User: "Hey Sara, [unclear audio]"
Sara: "I didn't catch that. Could you repeat?"
```

### Clarification Requests
```
User: "Hey Sara, open that thing"
Sara: "Which application would you like me to open?"

User: "Hey Sara, do the thing"
Sara: "I'm not sure what you're referring to. Could you be more specific?"
```

---

## 🎪 Demo Sequence Examples

### Complete Workflow Examples

**Workflow 1: Research and Code**
```
1. "Hey Sara, search for Python tutorials"
   → Opens browser, searches for Python tutorials
   
2. "Hey Sara, open Notepad"  
   → Opens Notepad for coding
   
3. "Hey Sara, write Python code"
   → Types Python hello world program
   
4. "Hey Sara, take a screenshot"
   → Captures screen showing the code
```

**Workflow 2: System Management**
```
1. "Hey Sara, what time is it?"
   → Reports current time
   
2. "Hey Sara, take a screenshot"
   → Captures desktop
   
3. "Hey Sara, volume up"
   → Increases system volume
   
4. "Hey Sara, lock the screen"
   → Secures the computer
```

**Workflow 3: Application Management**
```
1. "Hey Sara, open Calculator"
   → Launches Calculator app
   
2. "Hey Sara, open Notepad"
   → Launches Notepad
   
3. "Hey Sara, minimize all windows"
   → Shows desktop
   
4. "Hey Sara, show running applications"
   → Lists active processes
```

---

## 📋 Success Indicators

### Visual Feedback
- ✅ Applications launch successfully
- ✅ Code appears in Notepad
- ✅ Browser navigates to correct pages
- ✅ Screenshots saved in screenshots folder
- ✅ System responds to power commands

### Audio Feedback
- 🔊 Sara confirms each action with voice
- 🔊 Error messages are spoken clearly
- 🔊 Status updates provided during long operations

### System Responses
- 📱 Windows Search opens and closes appropriately
- 📱 Applications appear in taskbar
- 📱 Files created in correct locations
- 📱 System commands execute with proper delays

---

## 🚀 Performance Tips

### For Best Results
1. **Speak Clearly**: Enunciate commands clearly
2. **Wait for Response**: Let Sara acknowledge before next command
3. **Use Natural Language**: Don't worry about exact syntax
4. **Check Microphone**: Ensure good audio input
5. **Run as Administrator**: For system-level operations

### Troubleshooting Commands
```
"Hey Sara, test voice system" → Runs voice system test
"Hey Sara, check microphone" → Tests audio input
"Hey Sara, system status" → Reports system health
```

---

## 🧪 Testing Your Setup

### Quick Test Commands (Fast Mode)
```bash
# 1. Test installation
python test_all_features.py

# 2. Start Fast Mode
python sara_fast.py

# 3. Test these commands in order:
"Hey Sara"                    # Should respond "Yes?"
"help"                        # Should list commands
"take a screenshot"           # Should save to screenshots/
"what time is it?"           # Should tell current time
"system info"                # Should report system stats
"goodbye"                    # Should exit cleanly
```

### Verification Checklist
- ✅ Wake word detection works
- ✅ Screenshot saves to `screenshots/screenshot_YYYYMMDD_HHMMSS.png`
- ✅ Applications launch via Windows search
- ✅ Voice feedback is clear
- ✅ System commands execute properly
- ✅ Help command shows available options
- ✅ Exit command shuts down cleanly

---

**🎯 Total Commands Supported: 100+ variations across 15+ categories**

**💡 Pro Tips**: 
- Use **Fast Mode** for daily use (2-3 second startup)
- Use **Full Mode** for advanced AI features
- Say "help" anytime to see available commands
- Screenshots are automatically timestamped and organized

---

> **"Experience the power of voice-controlled computing with Sara AI 3.0 - Your personal offline JARVIS!"** 🤖✨
