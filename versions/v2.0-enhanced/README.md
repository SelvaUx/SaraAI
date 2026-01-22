# 🚀 Sara AI v2.0 Enhanced - Advanced Desktop Assistant

**Code Generation & Biometrics** - Experimental features with voice-to-code capabilities

Sara AI v2.0 Enhanced pushes boundaries with experimental biometrics, voice-to-code generation, and comprehensive file/task management.

![Version](https://img.shields.io/badge/version-2.0--enhanced-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

---

## 🔥 What's New in Enhanced Edition

### ✍️ **Voice-to-Code**

- Dictate Python, HTML, or C++ snippets directly into Notepad
- Pre-built code templates for common tasks
- Project structure creation

### 🔒 **Experimental Biometrics**

- Face unlock (experimental)
- Gesture recognition
- Webcam-based controls

### 💾 **Advanced File Operations**

- Create, move, delete files
- Folder management
- File listing and organization

### 🎛️ **System Control**

- Power management (shutdown, restart, lock)
- Process management
- Task control

### 🎵 **Enhanced Media Control**

- Play, pause, resume
- Next/previous track
- Volume and brightness control

---

## 🗣️ Complete Command Reference

### 1️⃣ **Web & Search**

| Command        | Example                           | Result                   |
| -------------- | --------------------------------- | ------------------------ |
| Google Search  | `search for climate change`       | Opens Google search      |
| YouTube Search | `youtube never gonna give you up` | Auto-plays first video   |
| Open Website   | `open website stackoverflow.com`  | Launches site in browser |

### 2️⃣ **Apps & Windows**

| Command      | Example                | Result               |
| ------------ | ---------------------- | -------------------- |
| Open App     | `open notepad`         | Opens via Start menu |
| Kill App     | `kill task chrome.exe` | Force-closes app     |
| List Running | `list tasks`           | Lists all processes  |

### 3️⃣ **Code Writing Assistant**

| Command        | Example                   | Result                         |
| -------------- | ------------------------- | ------------------------------ |
| Create Project | `create project MySite`   | Creates folder on Desktop      |
| Write Snippet  | `write code login page`   | Types HTML login form          |
| Dictate Python | `write code hello python` | Types `print('Hello, world!')` |
| Auto-C++       | `write code cpp main`     | Types minimal `main.cpp`       |

### 4️⃣ **File & Folder**

| Command       | Example                         | Result                       |
| ------------- | ------------------------------- | ---------------------------- |
| Create Folder | `create folder Reports`         | Creates new folder           |
| Create File   | `create file todo.txt`          | Creates empty file           |
| List Files    | `list files`                    | Prints directory contents    |
| Move File     | `move file todo.txt to Reports` | Relocates file               |
| Delete File   | `delete file old.docx`          | **Permanently deletes** file |

### 5️⃣ **Media & System**

| Command       | Example                         | Result                  |
| ------------- | ------------------------------- | ----------------------- |
| Play Music    | `play music`                    | Plays first audio file  |
| Pause/Resume  | `pause music` / `resume music`  | Toggles playback        |
| Next/Previous | `next track` / `previous track` | Skips songs             |
| Volume        | `volume up` / `volume down`     | Adjusts volume          |
| Mute          | `mute`                          | Toggles mute            |
| Brightness    | `brightness 60`                 | Sets brightness (0-100) |

### 6️⃣ **Power & Security**

| Command     | Example        | Result                             |
| ----------- | -------------- | ---------------------------------- |
| Shutdown    | `shutdown now` | Powers off PC                      |
| Restart     | `restart pc`   | Reboots computer                   |
| Lock Screen | `lock`         | Locks screen                       |
| Face Unlock | `face unlock`  | (Experimental) Webcam-based unlock |

### 7️⃣ **Gestures & Experimental**

| Command        | Example          | Result                                |
| -------------- | ---------------- | ------------------------------------- |
| Start Gestures | `start gestures` | (Experimental) Hand-gesture detection |

### 8️⃣ **Classic Utilities**

| Command    | Example      | Result                |
| ---------- | ------------ | --------------------- |
| Screenshot | `screenshot` | Saves PNG to Pictures |
| Time       | `time`       | Tells current time    |
| Date       | `date`       | Tells current date    |

---

## 🛠️ Quick Start

### Prerequisites

- **Python 3.7+**
- **Windows 10/11**
- **Microphone**
- **Webcam** (for biometric features)

### Installation

```bash
# Clone the repository
git clone https://github.com/SelvaUx/SaraAI.git
cd SaraAI/versions/v2.0-enhanced

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py

# Activate by saying: "Hey Sara"
```

---

## 🧩 Requirements

Key dependencies (see `requirements.txt`):

- `pyautogui` - Desktop automation
- `opencv-python` - Webcam and computer vision
- `mediapipe` - Hand gesture recognition
- `wikipedia` - Information retrieval
- `pyjokes` - Entertainment
- `pyttsx3` - Text-to-speech
- `SpeechRecognition` - Voice recognition

---

## 📁 Project Structure

```
v2.0-enhanced/
├── main.py                  # Main application controller
├── voice_input.py          # Voice recognition system
├── tts.py                  # Text-to-speech engine
├── utils.py                # Utility functions
├── application_handler.py  # App launching
├── browser_handler.py      # Web browser control
├── music_player.py         # Media playback
├── code_writer.py          # Code generation module
├── file_handler.py         # File operations
├── task_manager.py         # Process management
├── face_unlock.py          # Biometric authentication (experimental)
├── gesture_handler.py      # Gesture recognition (experimental)
├── requirements.txt        # Python dependencies
├── LICENSE.txt            # MIT License
└── README.md              # This file
```

---

## 💻 Code Generation Examples

### Python Code

```
You: "Hey Sara, write code hello python"
Sara: [Types into Notepad]
print('Hello, world!')
```

### HTML Login Page

```
You: "Hey Sara, write code login page"
Sara: [Creates complete HTML login form with CSS]
```

### C++ Main Function

```
You: "Hey Sara, write code cpp main"
Sara: [Types basic C++ template]
#include <iostream>
int main() {
    return 0;
}
```

---

## 🔐 Experimental Features

### Face Unlock

- Uses webcam for facial recognition
- Experimental feature - requires training
- Uses OpenCV for face detection

### Gesture Recognition

- Hand tracking using MediaPipe
- Control system with hand gestures
- Experimental webcam-based controls

> **Note**: Experimental features require webcam and may need calibration

---

## 🎯 Key Features

### Wording Flexibility

Commands are flexible: "Hey Sara, open vs-code" works the same as "launch visual studio code"

### Extensibility

New code templates can be added to `code_writer.py`

### Offline Capable

Works without internet (except Google Speech Recognition)

---

## 📊 Comparison with v2.0

| Feature           | v2.0  | v2.0 Enhanced        |
| ----------------- | ----- | -------------------- |
| Voice Recognition | ✅    | ✅                   |
| Code Generation   | ❌    | ✅ Python, HTML, C++ |
| File Management   | Basic | ✅ Advanced          |
| Biometrics        | ❌    | ✅ Experimental      |
| Gesture Control   | ❌    | ✅ Experimental      |
| Media Control     | Basic | ✅ Advanced          |
| Power Management  | ❌    | ✅ Full support      |

---

## 🛠️ Troubleshooting

### Webcam Issues

- Check webcam permissions in Windows settings
- Ensure OpenCV can access camera
- Test webcam with other applications

### Code Generation Not Working

- Verify Notepad opens correctly
- Check clipboard permissions
- Ensure `code_writer.py` has proper templates

### Gesture Recognition Problems

- Ensure good lighting for webcam
- Keep hands visible in frame
- Calibrate MediaPipe settings

---

## 📝 Notes

- **Wording is flexible**: Natural language understanding
- **Extensibility**: Easy to add new templates and commands
- **Windows Focus**: Optimized for Windows 10/11
- **Experimental Features**: Biometrics and gestures need fine-tuning

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

---

## 👤 Author

**Selva Pandi (Selva.Ux)**

- GitHub: [@SelvaUx](https://github.com/SelvaUx)
- Instagram: [@selva.ux](https://instagram.com/selva.ux)
- Email: selva.ux@yahoo.com

---

<div align="center">
  <p><strong>Code Meets Voice 💻🎤</strong></p>
  <p>Made with ❤️ by Selva.Ux</p>
</div>
