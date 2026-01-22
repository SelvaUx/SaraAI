# 🤖 Sara AI Max - Voice-Controlled Desktop Automation

**MVP Version 1.0** - A modular, secure, offline-first voice assistant

Sara AI Max is an intelligent voice-controlled desktop automation system that can control your PC, manage files, launch applications, and perform various tasks through natural voice commands.

![Version](https://img.shields.io/badge/version-1.0--mvp-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

---

## ✨ Features (MVP)

### 🎤 Voice Intelligence

- **Wake Word Detection** - Activate with "Hey Sara"
- **Speech-to-Text** - Google Speech Recognition
- **Text-to-Speech** - Natural voice responses
- **Continuous Listening** - Always ready mode

### 🧠 Natural Language Understanding

- **Intent Parsing** - Understands natural commands
- **Entity Extraction** - Extracts app names, file names, etc.
- **25+ Intent Types** - System control, apps, files, utilities

### ⚙️ System Control

- **System Information** - Time, date, CPU, memory, disk usage
- **Volume Control** - Increase, decrease, mute
- **Power Management** - Shutdown, lock screen
- **Web Search** - Open Google searches

### 💻 Application Control

- **Open Apps** - Launch any Windows application
- **Close Apps** - Terminate running applications
- **Process Management** - Using psutil

### 📁 File Operations

- **Create Folders** - On Desktop or custom location
- **Create Files** - With optional content
- **Search Files** - Find files by name
- **Delete Files** - Safe file deletion

### 🔒 Security & Audit

- **Permission Levels** - OBSERVE, LOW, MEDIUM, HIGH
- **Audit Logging** - JSON-based audit trail
- **Confirmation Prompts** - For high-risk actions
- **Action History** - Complete audit log

### 🧩 Context Management

- **Session Memory** - Maintains conversation history
- **Context Variables** - Store session state
- **50-entry History** - Recent conversation tracking

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.9+**
- **Windows 10/11** (primary support)
- **Microphone** for voice input
- **Speakers** for audio output

### Installation

1. **Clone or navigate to the sara-ai-max folder**

   ```bash
   cd sara-ai-max
   ```

2. **Create virtual environment (recommended)**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Sara AI Max**
   ```bash
   python main.py
   ```

---

## 📖 Usage

### Starting Sara

```bash
python main.py
```

You'll see:

```
INFO - Sara AI Max initialized successfully!
INFO - Sara AI Max is now running. Say 'Hey Sara' to activate.
[Sara speaks: "Sara AI Max initialized. I'm ready to help."]
```

### Voice Commands

**Activate Sara:**

- Say: `"Hey Sara"`
- Sara responds: `"Yes, I'm listening."`

**Example Commands:**

```
"Hey Sara"
> "What time is it?"
Sara: "The current time is 9:30 PM"

"Hey Sara"
> "Open notepad"
Sara: "Opening notepad"

"Hey Sara"
> "Create a folder named TestProject"
Sara: "Created folder: TestProject"

"Hey Sara"
> "Search for Python tutorials"
Sara: "Searching for Python tutorials"

"Hey Sara"
> "What's the system info?"
Sara: "CPU usage: 25%, Memory usage: 60%, Disk usage: 45%"
```

---

## 📋 Supported Commands

### 🕐 Time & Date

- `"What time is it?"`
- `"What's the date?"`
- `"Tell me the current time"`

### 💻 Applications

- `"Open [app name]"` - Example: "Open Chrome", "Open Telegram"
- `"Close [app name]"` - Example: "Close Notepad"

### 📂 Files & Folders

- `"Create a folder named [name]"` - Creates on Desktop
- `"Create a file named [name]"` - Creates on Desktop
- `"Search for [filename]"` - Searches in home directory

### 🔊 System Control

- `"System info"` - CPU, memory, disk usage
- `"Increase volume"` / `"Decrease volume"` / `"Mute"`
- `"Lock screen"` / `"Lock computer"`
- `"Shutdown"` (requires confirmation)

### 🌐 Web

- `"Search for [query]"` - Opens Google search
- `"Google [query]"` - Same as above

### 🎭 Entertainment

- `"Tell me a joke"`

---

## 🏗️ Project Structure

```
sara-ai-max/
├── sara_core/              # Core intelligence
│   ├── voice_engine.py     # Wake word, STT, TTS
│   ├── nlu.py              # Intent parsing
│   ├── planner.py          # Action planning
│   ├── executor.py         # Action execution
│   ├── security.py         # Permissions & audit
│   └── context.py          # Session memory
│
├── automation/             # Automation modules
│   ├── app_controller.py   # App launching & control
│   ├── file_ops.py         # File operations
│   └── system.py           # System control
│
├── main.py                 # Main entry point
├── config.example.json     # Configuration template
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## ⚙️ Configuration

Copy `config.example.json` to `config.json` and customize:

```json
{
  "voice": {
    "wake_word": "hey sara",
    "language": "en-US",
    "tts_rate": 160
  },
  "security": {
    "require_confirmation_for_high_risk": true
  }
}
```

---

## 🛠️ Troubleshooting

### Microphone Not Working

- Check Windows microphone permissions
- Verify microphone is set as default device
- Test microphone in Windows settings

### PyAudio Installation Issues

```bash
# Install Visual C++ Build Tools first
# Then install PyAudio
pip install pipwin
pipwin install pyaudio
```

### "Module not found" Errors

```bash
pip install -r requirements.txt --upgrade
```

### Voice Recognition Not Responding

- Ensure stable internet (for Google Speech Recognition)
- Speak clearly and at moderate pace
- Reduce background noise

---

## 🔮 Roadmap

### Planned for Full Version

- **Visual Intelligence** - OCR, UI finding
- **Advanced Automation** - Macros, scheduled tasks
- **Plugin System** - Custom skills
- **Offline STT** - Vosk integration
- **Browser Control** - Playwright automation
- **Email Integration** - Gmail, Outlook
- **Messaging** - WhatsApp, Telegram
- **Office Automation** - Word, Excel, PowerPoint

See full [specification](README_FULL.md) for complete feature list.

---

## 📝 License

MIT License - see LICENSE for details

---

## 👤 Author

**Selva Pandi (Selva.Ux)**

- GitHub: [@SelvaUx](https://github.com/SelvaUx)
- Instagram: [@selva.ux](https://instagram.com/selva.ux)

---

<div align="center">

**Sara AI Max MVP** - Voice-controlled desktop automation 🎤🤖

_Say "Hey Sara" to get started!_

</div>
