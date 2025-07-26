# 🚀 **Sara AI – Multi-Version Personal PC Assistant**
*Your voice-activated, offline desktop assistant for Windows.*

---

## 📌 Table of Contents
1. [Introduction](#introduction)
2. [Version Overview](#version-overview)
3. [Features](#features)
4. [Command Cheat-Sheet](#command-cheat-sheet)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Developer Details](#developer-details)
8. [Troubleshooting](#troubleshooting)
9. [Contributing](#contributing)
10. [License](#license)
11. [GitHub Stats](#github-stats)

---

## 1️⃣ Introduction
Sara AI is a multi-version, Python and C# based desktop assistant that responds to text commands to perform tasks like opening apps, searching Google, checking time and date, reading Wikipedia summaries, telling jokes, and taking screenshots. It includes text-to-speech feedback for a smart assistant experience.

---

## 2️⃣ Version Overview
Sara AI evolves across five major versions, each with unique capabilities:

| Version | Language | Core Features | Superpowers |
|---|---|---|---|
| **v1 Basic** | Python 3.11 | App launching, time, date, screenshot, Wikipedia | Basic commands |
| **v2.0 Wake-Word** | Python 3.11 | Wake-word, music, YouTube | Voice activation |
| **2.0 Enhanced** | Python 3.11 | Macros, file ops, face unlock, gestures | Enhanced control |
| **v3.0 LLM** | Python 3.11 | Local LLM, voice-to-code | Advanced AI |
| **v4.0 C#** | C# .NET 8 | Native .exe, full Windows automation | Full PC automation |

---

## 3️⃣ Features
- **Voice-Powered Control**: Use voice commands to perform tasks.
- **Voice-to-Code**: Dictate code snippets into editors.
- **Experimental Biometrics**: Face unlock and gesture recognition.
- **File & Task Operations**: Manage files and system processes.
- **Media Control**: Control media playback with voice commands.
- **Power Management**: Shutdown, restart, or lock your computer.

---

### 4️⃣ Command Cheat-Sheet
Say **“Hey Sara”** (in v2+) and then any phrase below.

| Category | Command | Example | Result |
|---|---|---|---|
| **Web & Search** | `search climate change` | Google search |
|  | `youtube never gonna give you up` | YouTube search |
|  | `open website stackoverflow.com` | Browser launch |
| **Apps & Windows** | `open notepad` | App opening |
|  | `kill task chrome.exe` | Force-close app |
|  | `list tasks` | Process list |
| **Code Writing Assistant** | `create project MySite` | Folder creation |
|  | `write code login page` | HTML in Notepad |
|  | `write code hello python` | Python code |
|  | `write code cpp main` | C++ main |
| **File & Folder** | `create folder Reports` | Folder creation |
|  | `create file todo.txt` | File creation |
|  | `list files` | Directory listing |
|  | `move file todo.txt to Reports` | File relocation |
|  | `delete file old.docx` | File deletion |
| **Media & System** | `play music` | Music playback |
|  | `pause music` | Playback toggle |
|  | `next track` | Song skip |
|  | `volume up` | Volume adjust |
|  | `mute` | Mute toggle |
|  | `brightness 60` | Brightness adjust |
| **Power & Security** | `shutdown now` | Shutdown |
|  | `restart pc` | Reboot |
|  | `lock` | Screen lock |
|  | `face unlock` | Face unlock |
| **Gestures & Experimental** | `start gestures` | Gesture start |
| **Classic Utilities** | `screenshot` | Screen capture |
|  | `time` | Time display |
|  | `date` | Date display |

---

### 5️⃣ Installation
#### Prerequisites
- **Python 3.11** (or later) for Python versions
- **.NET 6.0 SDK** for C# version
- **pip** (Python package manager)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/SelvaUx/SaraAI.git
   cd SaraAI
   ```

2. **Create a Virtual Environment (optional but recommended)**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python main.py
   ```

5. **Activate by Saying: "Hey Sara"**

---

### 6️⃣ Usage
Activate Sara AI by saying "Hey Sara" and then follow with any command from the [Command Cheat-Sheet](#command-cheat-sheet).

---

### 7️⃣ Developer Details
**Selva Pandi Francis**  
*ECE Student | Innovator | Futuristic Tech Developer*

- **Passion**: Futuristic AI, embedded systems, and full PC automation.
- **Inspiration**: Iron Man’s JARVIS.
- **Vision**: Building a real-world intelligent assistant that controls everything—offline, real-time, and voice-first.

**Connect with Selva:**
- 📧 **Email**: selva.ux@yahoo.com
- 🐙 **GitHub**: [SelvaUx](https://github.com/SelvaUx)
- 📸 **Instagram**: [selva.ux](https://www.instagram.com/selva.ux/)

---

## 8️⃣ Troubleshooting
### Common Issues
| Error | Fix |
|---|---|
| `cv2 not found` | `pip install opencv-python` |
| `microphone not detected` | Run Windows mic troubleshooter |
| `permission denied` | Launch terminal as Administrator |
| `antivirus blocks` | Add project folder to exclusions |

---

### 9️⃣ Contributing
Feel free to fork the repository, make changes, and create pull requests. Contributions are always welcome!

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Code Style
- Follow PEP 8 guidelines
- Use type hints where possible
- Add docstrings to functions
- Keep functions focused and small

---

### 🔟 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

"Join the journey of creating a real-world intelligent assistant that controls everything—offline, real-time, and voice-first. Let's build the future together!"

Love,

Selva Pandi & the Sara AI Team ✨

---

**Enjoy your personal AI assistant! 🤖**
