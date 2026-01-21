# 🚀 **SaraAI 2.0 Enhanced**  
*Your fully-offline, Jarvis-style desktop assistant.*

---

## 🔥 Core Features
| Feature | Description |
|---|---|
| 🎤 **Voice-Powered Control** | Uses voice commands to perform a wide range of tasks on your desktop. |
| ✍️ **Voice-to-Code** | Dictate Python, HTML, or C++ snippets directly into Notepad. |
| 🔒 **Experimental Biometrics** | Features experimental face unlock and gesture recognition capabilities. |
| 💾 **File & Task Operations** | Create, move, delete files, and manage system processes. |
| 🎵 **Media Control** | Control media playback with commands for play, pause, next, and previous. |
| 🛡️ **Power Management** | Shutdown, restart, or lock your computer with simple voice commands. |

---

## 🗣️ **Command Reference**  
> Say **“Hey Sara”** first, then any phrase below.

### 1️⃣ Web & Search
| Command | Example | Result |
|---|---|---|
| Google Search | `search for climate change` | Opens a Google search in your browser. |
| YouTube Search | `youtube never gonna give you up` | Performs a YouTube search and auto-plays the first video. |
| Open Website | `open website stackoverflow.com` | Launches the specified site in your default browser. |

---

### 2️⃣ Apps & Windows
| Command | Example | Result |
|---|---|---|
| Open App | `open notepad` | Opens an application using the Start-menu search. |
| Kill App | `kill task chrome.exe` | Force-closes the specified application. |
| List Running | `list tasks` | Prints a list of all running processes. |

---

### 3️⃣ Code Writing Assistant
| Command | Example | Result |
|---|---|---|
| Create Project | `create project MySite` | Creates a new folder on your Desktop. |
| Write Snippet | `write code login page` | Types an HTML login form into a new Notepad window. |
| Dictate Python | `write code hello python` | Types `print('Hello, world!')` into Notepad. |
| Auto-C++ | `write code cpp main` | Types a minimal `main.cpp` file into Notepad. |

---

### 4️⃣ File & Folder
| Command | Example | Result |
|---|---|---|
| Create Folder | `create folder Reports` | Creates a new folder named 'Reports' on your Desktop. |
| Create File | `create file todo.txt` | Creates a new empty file on your Desktop. |
| List Files | `list files` | Prints the files in the current directory. |
| Move File | `move file todo.txt to Reports` | Relocates the specified file. |
| Delete File | `delete file old.docx` | **Permanently deletes** the specified file. |

---

### 5️⃣ Media & System
| Command | Example | Result |
|---|---|---|
| Play Music | `play music` | Plays the first supported audio file in your Music folder. |
| Pause / Resume | `pause music` / `resume music` | Toggles media playback. |
| Next / Previous | `next track` / `previous track` | Skips to the next or previous song. |
| Volume | `volume up` / `volume down` | Adjusts the system volume. |
| Mute | `mute` | Toggles system mute. |
| Brightness | `brightness 60` | Adjusts the display brightness (0-100). |

---

### 6️⃣ Power & Security
| Command | Example | Result |
|---|---|---|
| Shutdown | `shutdown now` | Powers off the computer. |
| Restart | `restart pc` | Reboots the computer. |
| Lock Screen | `lock` | Locks the computer screen. |
| Face Unlock | `face unlock` | (Experimental) Uses the webcam to scan for a face to unlock the PC. |

---

### 7️⃣ Gestures & Experimental
| Command | Example | Result |
|---|---|---|
| Start Gestures | `start gestures` | (Experimental) Starts the hand-gesture detection loop. |

---

### 8️⃣ Classic Utilities
| Command | Example | Result |
|---|---|---|
| Screenshot | `screenshot` | Saves a PNG of your screen to the Pictures folder. |
| Time | `time` | Tells you the current time. |
| Date | `date` | Tells you the current date. |

---

## 🛠️ Quick-Start
```bash
# Clone the repository
git clone https://github.com/SelvaUx/SaraAI.git
cd SaraAI

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py

# Activate by saying: "Hey Sara"
```

---

## 🧩 Requirements
A `requirements.txt` file is included. Key dependencies are:
- `pyautogui`
- `opencv-python`
- `mediapipe`
- `wikipedia`
- `pyjokes`
- Speech and audio libraries (`pyttsx3`, `SpeechRecognition`, etc.)

---

### 📝 Notes
- **Wording is flexible**: “Hey Sara, open vs-code” works the same as “launch visual studio code”.  
- **Extensibility**: New code templates can be added to `code_writer.py`.

---

**License**: MIT
