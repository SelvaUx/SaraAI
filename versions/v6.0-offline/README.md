# 🌌 SARA AI 6.0 — OFFLINE EDITION
### *“Just a rather very intelligent system.”*

A futuristic offline voice assistant for Windows — fast, lightweight, and built entirely with **Electron + Node.js**, inspired by JARVIS but engineered to run without cloud, Python, or heavy dependencies.

<p align="center">
  <img src="https://via.placeholder.com/1600x500/0a0a0f/00f7ff?text=SARA+AI+6.0+OFFLINE" width="100%" alt="SARA AI Banner"/>
</p>

---

## ✨ Features

### ⚡ Offline Automation Core
- **Universal App Launcher** — “Open Chrome”, “Open VS Code”, “Open Notepad”.
- **Native Windows Control** using auto-generated `.vbs` scripts.
- **Screenshots** saved instantly to your Pictures folder.
- **Zero external dependencies** — no Python required.

### 🧠 Knowledge Engine
- Offline utilities: **Time**, **Date**, **Random Jokes**.
- **Wikipedia summaries** via public API calls.

### 🎙️ Interaction Modes
- **Voice Mode** — responds to “Hey Sara” or “Sara”.
- **Text Command Mode** — silent typing control.
- **Speech Output** through Windows built-in TTS.

### 🎨 Selva.UX Futuristic Interface
- **Arc Reactor Visualizer** (reactive animation).
- **Glassmorphism UI** — frameless neon-cyan look.
- **System Tray Mode** — runs quietly in background.

---

## 🛠️ Project Structure

```
sara-ai-offline/
│
├── automation.vbs          # Auto-generated scripts for OS automation
├── main.js                 # Backend brain (logic, commands, APIs)
├── preload.js              # Secure bridge between UI <-> backend
│
├── renderer/               # Frontend UI
│   ├── index.html          # Arc Reactor UI layout
│   ├── renderer.js         # Voice engine + UI logic
│   └── styles.css          # Neon UI / Cyberpunk visuals
│
└── package.json            # App configuration & dependencies
```

---

## 🚀 Installation

### **Prerequisite**
- Node.js (latest LTS recommended)

---

### **1. Clone Repository**
```bash
git clone https://github.com/your-username/sara-ai-offline.git
cd sara-ai-offline
```

### **2. Install Dependencies**
```bash
npm install
```

### **3. Run SARA**
```bash
npm start
```

### **4. Build Windows Executable (Optional)**
```bash
npm run dist
```

---

## 🗣️ Example Commands

### 🔧 System Control
| Command            | Action                          |
|-------------------|----------------------------------|
| `Open Chrome`      | Launches Google Chrome           |
| `Open VS Code`     | Opens Visual Studio Code         |
| `Take Screenshot`  | Saves screenshot to Pictures     |
| `Minimize Yourself`| Minimizes SARA                   |
| `Close Yourself`   | Exits application                |

---

### 🌐 Web & Info
| Command                | Action                     |
|------------------------|----------------------------|
| `Search PCB design`    | Performs Google Search     |
| `Open youtube.com`     | Opens website              |
| `Wikipedia Iron Man`   | Reads topic summary        |
| `What is the time?`    | Announces system time      |
| `Tell me a joke`       | Random programming joke    |

---

## 👨‍💻 About the Developer

### **Selva Pandi (Francis)**
**Electronics & Communication Engineering**  
Dr. G.U. Pope College of Engineering — Tamil Nadu, India

A creator driven by curiosity, circuits, and imagination.  
Exploring the future through **AI systems, embedded hardware, custom OS design,  
and cyberpunk-inspired UI engineering**.

**Motto:**  
*“I don’t just write code; I build systems.”*

---

## 📄 License
Released under the **MIT License** — free to use and innovate.
