# 🚀 **Sara AI – Multi-Version Personal PC Assistant**
*Your voice-activated, offline desktop assistant for Windows.*

---

## 📌 Table of Contents
1. [Introduction](#1️⃣-introduction)
2. [Version Overview](#2️⃣-version-overview)
3. [Features](#3️⃣-features)
4. [Command Cheat-Sheet](#4️⃣-command-cheat-sheet)
5. [Installation](#5️⃣-installation)
6. [Usage](#6️⃣-usage)
7. [Developer Details](#7️⃣-developer-details)
8. [Troubleshooting](#8️⃣-troubleshooting)
9. [Contributing](#9️⃣-contributing)
10. [License](#license)

---

## 1️⃣ Introduction
Sara AI is a multi-version, voice-powered desktop assistant designed to make your PC experience smarter and more intuitive. With versions built in Python and C#, Sara AI can open apps, perform web searches, control media, take screenshots, manage files, and even generate code using voice commands. It is designed to run offline, ensuring privacy while delivering a seamless experience.

---

## 2️⃣ Version Overview
Sara AI has evolved through several versions, each adding more capabilities and features. Here’s a summary of what each version offers:

- **v1 Basic**: Basic assistant features like launching apps, checking the time and date, taking screenshots, and Wikipedia summaries.
- **v2.0 Wake-Word**: Adds wake-word activation, music control, and YouTube search for an enhanced voice experience.
- **v2.0 Enhanced**: Further improvements with macros, file operations, face unlock, and gesture recognition.
- **v3.0 LLM**: Introduces local language model support, and voice-to-code functionality, allowing more advanced AI-powered actions.
- **v4.0 C#**: Full Windows automation with a native `.exe` application for streamlined, efficient performance.

---

## 3️⃣ Features
### **Core Features:**
- **Voice-Powered Control**: Control your computer completely via voice commands.
- **Voice-to-Code**: Dictate code directly into editors for Python, HTML, C++, and more.
- **Biometric Authentication**: Includes experimental features like face unlock and gesture recognition.
- **File & Task Management**: Create, delete, and move files or folders, and manage system processes.
- **Media Control**: Play, pause, and adjust the volume of music, videos, and more.
- **Power Management**: Safely shutdown, restart, or lock your computer with a single command.

---

## 4️⃣ Command Cheat-Sheet

**Activate Sara AI**: Say **"Hey Sara"** (in versions v2+), then follow with any of the commands below:

- **Web & Search**:
  - `search <query>` – Perform a Google search
  - `youtube <video name>` – Search YouTube
  - `open website <URL>` – Open a website in your browser
  
- **Apps & Windows**:
  - `open <app name>` – Launch an app (e.g., Notepad)
  - `kill task <task name>` – Force-close an app or task
  - `list tasks` – List running processes

- **Code Writing**:
  - `create project <project name>` – Create a new project folder
  - `write code <language>` – Create code snippets in Python, C++, HTML, etc.

- **File Operations**:
  - `create folder <folder name>` – Create a new folder
  - `move file <file> to <folder>` – Move a file to a folder
  - `delete file <file>` – Delete a file

- **Media Control**:
  - `play music` – Start playing music
  - `pause music` – Pause the current track
  - `volume up` – Increase volume
  - `mute` – Mute the sound
  
- **Power & Security**:
  - `shutdown now` – Shutdown the PC
  - `restart pc` – Reboot the computer
  - `lock` – Lock the screen
  
- **Experimental Features**:
  - `start gestures` – Begin gesture recognition
  - `face unlock` – Unlock PC using face recognition

---

## 5️⃣ Installation

### Prerequisites:
- **Python 3.11** (or later) for Python versions
- **.NET 6.0 SDK** for C# version
- **pip** (Python package manager)

### Installation Steps:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SelvaUx/SaraAI.git  
   cd SaraAI

2. **Set Up Virtual Environment (optional but recommended)**:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:

   ```bash
   python main.py
   ```

5. **Activate by Saying**: "Hey Sara"

---

## 6️⃣ Usage

Once installed, you can activate Sara AI by saying "Hey Sara", followed by any command from the [Command Cheat-Sheet](#command-cheat-sheet). Sara AI will respond to you, perform the requested tasks, and provide text-to-speech feedback.

---

## 7️⃣ Developer Details

**Selva Pandi**
*Innovator, Tech Developer, ECE Student*

* **Passion**: Futuristic AI, Embedded Systems, Full PC Automation
* **Inspiration**: Iron Man’s JARVIS
* **Vision**: Building a real-world intelligent assistant that can control everything—offline, real-time, and voice-first.

**Contact Information**:

* 📧 **Email**: [selva.ux@yahoo.com](mailto:selva.ux@yahoo.com)
* 🐙 **GitHub**: [SelvaUx](https://github.com/SelvaUx)
* 📸 **Instagram**: [selva.ux](https://www.instagram.com/selva.ux/)

---

## 8️⃣ Troubleshooting

### Common Issues and Fixes:

* **`cv2 not found`**:
  Run: `pip install opencv-python`
* **`microphone not detected`**:
  Use Windows troubleshooter for microphone issues.
* **`permission denied`**:
  Launch terminal as Administrator.
* **`antivirus blocks`**:
  Add the project folder to your antivirus exclusions.

---

## 9️⃣ Contributing

### How to Contribute:

1. **Fork the Repository**: Create a personal copy of the project.
2. **Create a Feature Branch**: Branch off from `main`.
3. **Make Changes**: Add your enhancements or bug fixes.
4. **Submit a Pull Request**: Create a PR with your changes.

### Code Style Guidelines:

* Follow **PEP 8** for Python code.
* Use **type hints** where applicable.
* Keep functions **small and focused**.
* Add **docstrings** to all functions and methods.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 💌 Quotes That Guide Me

> "Knowledge is my power. Code is my weapon. Kindness is my rule."  
— **Selva Pandi Francis**

> "Build your own lab. Code your own world. Create your own future."  
— *Inspired by Iron Man*

> "The one who understands time can design the future."  
— *The Future Physicist in Me*

Let’s build the impossible — together.

"Join us in building a world where technology makes life easier, smarter, and more efficient. Let's create the future together!"

Love,
**Selva Pandi & the Sara AI Team ✨**

---
