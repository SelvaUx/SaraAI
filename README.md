# 🚀 Sara AI – Multi-Version Personal PC Assistant
Your voice-activated, offline desktop assistant for Windows.

---

## 📌 Table of Contents
- Introduction  
- Version Overview  
- Features  
- Command Cheat-Sheet  
- Installation  
- Usage  
- Developer Details  
- Troubleshooting  
- Contributing  
- License  

---

## 1️⃣ Introduction
Sara AI is a multi-version, voice-powered desktop assistant designed to make your PC experience smarter and more intuitive. With versions built in Python, C#, and now multi-language modular design, Sara AI can open apps, perform web searches, control media, take screenshots, manage files, and even generate code using voice commands.  

It is designed to run **offline**, ensuring **privacy and speed** while delivering a seamless experience.  

---

## 2️⃣ Version Overview
Sara AI has evolved through several versions, each adding more capabilities and features.  

- **v1 Basic**: Basic assistant features like launching apps, checking the time and date, taking screenshots, and Wikipedia summaries.  
- **v2.0 Wake-Word**: Adds wake-word activation, music control, and YouTube search for an enhanced voice experience.  
- **v2.0 Enhanced**: Further improvements with macros, file operations, face unlock, and gesture recognition.  
- **v3.0 LLM**: Introduces local language model support and voice-to-code functionality, allowing more advanced AI-powered actions.  
- **v4.0 C#**: Full Windows automation with a native `.exe` application for streamlined, efficient performance.  
- **v5.0 Multi-Language (Latest)**: A **Jarvis-like modular AI assistant** that uses **Python, C++, Java, C#, Rust, and JavaScript**. Includes:  
  - Offline speech recognition (C++ – Whisper.cpp, Vosk)  
  - Natural TTS (Java – MaryTTS, FreeTTS)  
  - System Control (C# – full OS integration)  
  - Knowledge base (Rust + SQLite)  
  - Real-time dashboard (JavaScript Web UI)  
  - AI orchestration (Python core with FastAPI)  

---

## 3️⃣ Features
### Core Features
- 🎙️ **Voice-Powered Control**: Control your computer completely via voice commands.  
- 💻 **System Automation**: Open apps, manage files, kill tasks, shutdown/restart/lock.  
- 🎶 **Media Control**: Play, pause, adjust volume, mute/unmute.  
- 📂 **File Management**: Create, delete, move, and organize folders/files.  
- 🔐 **Security & Biometrics**: Face unlock & gesture recognition (experimental).  
- 👩‍💻 **Voice-to-Code**: Dictate code in Python, HTML, C++, and more.  

### v5.0 Exclusive Features  
- ⚙️ **Multi-Language Modular Design** (Python, C++, Java, C#, Rust, JavaScript)  
- 🧠 **AI Orchestration** with intelligent command routing  
- 📚 **Local Knowledge Base** with fast search (Rust + SQLite)  
- 🔊 **Natural TTS** with multiple voices (Java)  
- 🌐 **Interactive Dashboard** (JavaScript Web UI with real-time updates)  
- 🚀 **Asynchronous Module Communication** via REST, WebSocket, and IPC  

---

## 4️⃣ Command Cheat-Sheet
### Web & Search  
- `search <query>` – Google search  
- `youtube <video name>` – Search YouTube  
- `open website <URL>` – Open a website  

### Apps & Windows  
- `open <app name>` – Launch an app  
- `kill task <task name>` – Force-close app  
- `list tasks` – List running processes  

### Code Writing  
- `create project <project name>` – New project folder  
- `write code <language>` – Code snippet generation  

### File Operations  
- `create folder <name>` – New folder  
- `move file <file> to <folder>` – Move file  
- `delete file <file>` – Delete file  

### Media Control  
- `play music`, `pause music`  
- `volume up`, `mute`  

### Power & Security  
- `shutdown now`, `restart pc`, `lock`  

### Experimental  
- `start gestures` – Gesture recognition  
- `face unlock` – Unlock via face  

---

## 5️⃣ Installation
### Prerequisites
- Python 3.11+ (Core logic)  
- .NET 6.0 SDK (C# modules)  
- C++ Compiler (Whisper.cpp / Vosk STT)  
- Java 11+ (MaryTTS / FreeTTS TTS)  
- Rust 1.70+ (Knowledge base)  
- Node.js 18+ (Dashboard)  

### Setup
```bash
git clone https://github.com/SelvaUx/SaraAI.git
cd SaraAI
````

Windows:

```bash
.\scripts\setup.bat
.\scripts\build.bat
python core-python/main.py
```

Linux/Mac:

```bash
./scripts/setup.sh
./scripts/build.sh
python core-python/main.py
```

Activate by saying: **"Hey Sara"**

---

## 6️⃣ Usage

* Activate with **wake word** (`Hey Sara`)
* Speak any command (from cheat sheet)
* Watch tasks update in the **real-time dashboard**

---

## 7️⃣ Developer Details

👨‍💻 **Selva Pandi**

* Innovator, Tech Developer, ECE Student
* Passion: Futuristic AI, Embedded Systems, Full PC Automation
* Inspiration: Iron Man’s JARVIS
* Vision: Build a **real-world intelligent assistant** that controls everything, offline, in real-time.

📧 Email: **[selva.ux@yahoo.com](mailto:selva.ux@yahoo.com)**
🐙 GitHub: **[SelvaUx](https://github.com/SelvaUx)**
📸 Instagram: **[selva.ux](https://instagram.com/selva.ux)**

---

## 8️⃣ Troubleshooting

* `cv2 not found`: `pip install opencv-python`
* Mic not detected: Windows troubleshooter
* `permission denied`: Run terminal as Admin
* Antivirus blocking: Add project to exclusions

---

## 9️⃣ Contributing

* Fork the repo
* Create feature branch
* Submit PR
* Follow PEP8 (Python), proper docs, and clean modular code

---

## 🔟 License

MIT License – see LICENSE file

---

## 💌 Quotes That Guide Me

*"Knowledge is my power. Code is my weapon. Kindness is my rule."* — Selva Pandi
*"Build your own lab. Code your own world. Create your own future."* — Inspired by Iron Man
*"The one who understands time can design the future."* — The Future Physicist in Me

✨ *Let’s build the impossible — together!*

```
