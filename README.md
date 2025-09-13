# 🤖 SaraAI – Multi-Version Personal PC Assistant
Your **Jarvis-like, voice-activated, offline desktop assistant** for Windows.  
Multi-language, modular, and designed for **real-time PC automation**.

---

## 📋 Table of Contents

  * [Introduction](https://www.google.com/search?q=%23introduction)
  * [Version Overview](https://www.google.com/search?q=%23version-overview)
  * [Features](https://www.google.com/search?q=%23features)
  * [Architecture & Data Flow](https://www.google.com/search?q=%23architecture--data-flow)
  * [Project Structure](https://www.google.com/search?q=%23project-structure)
  * [Command Cheat-Sheet](https://www.google.com/search?q=%23command-cheat-sheet)
  * [Installation](https://www.google.com/search?q=%23installation)
  * [Usage](https://www.google.com/search?q=%23usage)
  * [Developer Details](https://www.google.com/search?q=%23developer-details)
  * [Troubleshooting](https://www.google.com/search?q=%23troubleshooting)
  * [Contributing](https://www.google.com/search?q=%23contributing)
  * [License](https://www.google.com/search?q=%23license)
  * [Quotes That Guide Me](https://www.google.com/search?q=%23quotes-that-guide-me)

-----

## 1️⃣ Introduction

Sara AI is a multi-version, voice-powered desktop assistant designed to make your PC experience smarter and more intuitive.

Built across **Python, C\#, C++, Java, Rust, and JavaScript**, Sara AI evolves from simple offline commands to a **multi-language modular ecosystem** with **real-time dashboards, knowledge bases, and natural speech**.

It runs **fully offline**, ensuring **privacy, speed, and control**.

-----

## 2️⃣ Version Overview

Sara AI has evolved through several versions, each adding more capabilities:

  * **v1.0 Basic** → Launch apps, check time/date, screenshots, Wikipedia summaries.
  * **v2.0 Wake-Word** → Wake-word activation, music control, YouTube search.
  * **v2.0 Enhanced** → Macros, file operations, face unlock, gesture recognition.
  * **v3.0 LLM** → Local LLM integration, voice-to-code functionality.
  * **v4.0 C\#** → Full Windows automation with a `.exe` app.
  * **v5.0 Multi-Language (Latest)** → Complete **modular AI system**:
      * 🎙️ **C++ Speech-to-Text** (Whisper.cpp, Vosk)
      * 🔊 **Java Text-to-Speech** (MaryTTS, FreeTTS)
      * ⚙️ **C\# System Control** (Windows API)
      * 📚 **Rust Knowledge Base** (SQLite full-text search)
      * 🌐 **JavaScript Dashboard** (WebSocket real-time UI)
      * 🧠 **Python Core Orchestrator** (FastAPI, asyncio)

-----

## 3️⃣ Features

### Core Features (all versions)

  * 🎙️ **Voice-Powered Control** – Full PC control via voice
  * 💻 **System Automation** – Open apps, manage files, shutdown/restart
  * 🎶 **Media Control** – Play, pause, adjust volume, mute
  * 📂 **File Management** – Create, move, delete files & folders
  * 🔐 **Biometric Security** – Face unlock, gesture recognition (experimental)
  * 👩‍💻 **Voice-to-Code** – Generate code in Python, HTML, C++

### v5.0 Exclusive

  * ⚙️ **Multi-Language Modular Design**
  * 🧠 **AI Orchestration** (intelligent command routing)
  * 📚 **Local Knowledge Base** (Rust + SQLite)
  * 🔊 **Natural Speech Responses** (Java TTS)
  * 🌐 **Interactive Web Dashboard** (JavaScript UI)
  * 🚀 **Asynchronous Communication** (REST, WebSocket, IPC, Message Queues)

-----

## 4️⃣ Architecture & Data Flow

```
User speaks (🎙️)
       ↓
STT (C++) converts voice to text
       ↓
Python Core (🧠) receives text and decides the task
       ↓
┌────────────┬─────────────┬───────────┐
│            │             │           │
▼            ▼             ▼           ▼
TTS (Java)   System (C#)   Search (Rust)
Response     System        Knowledge
needed       command       query
│            │             │
└────────────┴─────────────┴───────────┘
       ↓
Dashboard (🌐) updates in real-time
```

-----

## 5️⃣ Project Structure

```text
saraai-5.0/
├── core-python/        # 🧠 Main orchestrator & AI logic
│   ├── src/
│   ├── requirements.txt
│   └── main.py
├── speech-cpp/         # 🎙️ Speech-to-text processing
│   ├── src/
│   ├── include/
│   └── CMakeLists.txt
├── tts-java/           # 🔊 Text-to-speech generation
│   ├── src/
│   ├── pom.xml
│   └── build.gradle
├── system-csharp/      # ⚙️ Windows system integration
│   ├── src/
│   └── SystemControl.csproj
├── knowledge-rust/     # 📚 Knowledge base and search
│   ├── src/
│   ├── Cargo.toml
│   └── database/
├── dashboard-js/       # 🌐 Web-based UI
│   ├── public/
│   ├── src/
│   └── package.json
├── config/             # ⚙️ Config files
├── docs/               # 📖 Documentation
├── scripts/            # 🔧 Build & setup scripts
└── README.md
```

-----

## 6️⃣ Command Cheat-Sheet

### Web & Search

```
search <query> → Google search
youtube <video> → YouTube search
open website <url> → Open site
```

### Apps & Windows

```
open <app> → Launch app
kill task <name> → Force-close app
list tasks → Show processes
```

### Files

```
create folder <name>
move file <src> to <dest>
delete file <name>
```

### Media

```
play music, pause music
volume up, mute
```

### Power & Security

```
shutdown now, restart pc, lock
```

### Experimental

```
start gestures → Gesture control
face unlock → Unlock via face
```

-----

## 7️⃣ Installation

### Prerequisites

  * **Python 3.11+**
  * **.NET 6.0 SDK**
  * **C++ Compiler** (MSVC/GCC)
  * **Java 11+**
  * **Rust 1.70+**
  * **Node.js 18+**

### Setup

1.  Clone the repository and navigate into the directory.

<!-- end list -->

```
git clone https://github.com/SelvaUx/SaraAI.git
cd SaraAI
```

2.  Run the setup and build scripts based on your OS.

**Windows:**

```
.\scripts\setup.bat
.\scripts\build.bat
```

**Linux/Mac:**

```
./scripts/setup.sh
./scripts/build.sh
```

3.  Launch the main Python script.

<!-- end list -->

```
python core-python/main.py
```

Wake with: `"Hey Sara"`

-----

## 8️⃣ Usage

  * Speak a command → Sara executes instantly.
  * Live updates on dashboard UI.
  * Works fully offline.

-----

## 9️⃣ Developer Details

  * **👨‍💻 Name:** Selva Pandi
  * **Role:** Innovator | Tech Developer | ECE Student
  * **Inspiration:** Iron Man’s JARVIS
  * **Vision:** A real-world AI operating system
  * **📧 Email:** selva.ux@yahoo.com
  * **🐙 GitHub:** [SelvaUx](https://www.google.com/search?q=https://github.com/SelvaUx)
  * **📸 Instagram:** [selva.ux](https://www.google.com/search?q=https://instagram.com/selva.ux)

-----

## 🔟 Troubleshooting

  * **`cv2 not found`** → `pip install opencv-python`
  * **`Mic not detected`** → Use the Windows Troubleshooter.
  * **`permission denied`** → Run terminal as Administrator.
  * **`Antivirus blocks`** → Add to exclusions.

-----

## 1️⃣1️⃣ Contributing

  * Fork the repo.
  * Create feature branch.
  * Submit PR.
  * Follow PEP8, modular code, and docs.

-----

## 1️⃣2️⃣ License

Distributed under the MIT License. See the `LICENSE` file for more information.

-----

## 💌 Quotes That Guide Me

> "Knowledge is my power. Code is my weapon. Kindness is my rule." — Selva Pandi
> "Build your own lab. Code your own world. Create your own future." — Inspired by Iron Man
> "The one who understands time can design the future." — The Future Physicist in Me

-----

## ✨ Let's build the impossible — together\!
