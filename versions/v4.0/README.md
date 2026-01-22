# 🤖 Sara AI 4.0 (C# Edition) - Intelligent Voice-Controlled PC Assistant

**Complete C# Rewrite** - Enterprise-grade assistant with LM Studio integration

Sara AI 4.0 represents a complete architectural redesign using C# and .NET, delivering a futuristic, voice-enabled desktop assistant built for performance, reliability, and extensibility.

![Version](https://img.shields.io/badge/version-4.0-blue.svg)
![C#](https://img.shields.io/badge/C%23-.NET%206.0-purple.svg)
![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 👑 Developer - Selva Pandi (Selva.Ux)

**Tech Empire Builder | Knowledge Seeker | Virtual World Architect | Self-Made Innovator**

- 🧠 **ECE Student** passionate about VLSI, Embedded Systems, and AI
- 🔭 **Building SaraAI** - Personal AI Assistant (This Project!)
- 🌱 **Learning**: VLSI, Embedded Systems, Android AI/ML with Python, Quantum Physics & Time Travel
- 💡 **Dream**: Create tech empire and change the future using knowledge and innovation
- ⚡ **Fun Fact**: Building Iron Man world before getting driver's license!

**Connect with Selva:**

- 📧 **Email**: selva.ux@yahoo.com
- 🐙 **GitHub**: [SelvaUx](https://github.com/SelvaUx)
- 📸 **Instagram**: [selva.ux](https://www.instagram.com/selva.ux/)

**Empire Vision**: 🚩 Designing tools, machines, and realities that help humanity and expand imagination

---

## 🚀 Features (50+ Real-World Tasks)

### 🔊 Voice Interaction

- **Wake Word Support**: "Hey Sara"
- Understands multiple ways of saying commands
- Local NLP engine (no internet required)
- 95%+ voice recognition accuracy in quiet environments

### 🧠 Natural Language Understanding (NLP)

- Understand flexible, real-world instructions
- Contextual understanding & memory
- Command analysis and interpretation

### 🖥️ PC Control (Offline)

- Open any installed software via Windows Search (simulated typing)
- Search & Open websites through browser
- Create, delete, rename, move, and copy files/folders
- Lock/unlock the PC using voice
- Shutdown/restart/log off the system
- Control volume and brightness
- Toggle airplane mode/Wi-Fi/Bluetooth

### 🗂 File & Folder Operations

- Create project folders
- Create text/code files
- Write contents into Notepad
- Save and organize files automatically
- Delete specific files/folders via voice

### 🌐 Browsing and Web Interaction

- Open default browser using Windows Search
- Search any topic via browser
- Automatically click the first result
- Open specific websites (YouTube, Gmail, etc.)
- Search on YouTube and play first result

### 🎵 Media Features

- Play, pause, skip, and stop local songs
- Control Windows Media Player or Spotify
- Play video files using voice

### 📸 Screen & Display

- Take screenshots
- Start and stop screen recording
- Set wallpapers via voice
- Zoom in/out display

### 📅 Utilities

- Tell current time and date
- Set reminders and alarms
- Tell weather (if internet is available)
- Speak jokes and fun facts

### 📄 Document Tasks

- Open Word, Excel, PowerPoint using Windows Search
- Create basic documents with voice
- Save, name, and close documents

### 🛠 Developer Assistant

- Open Notepad via Windows Search
- Type full Python/C/C++ code as per user voice
- Create folder for code files automatically
- Run or compile basic programs

### 🔐 Security & Access

- Lock screen via voice
- Unlock PC via secure voice pattern (local model-based)

### 🤖 AI Integration (LM Studio)

- **Local AI Chat**: Engage with locally hosted LLM
- **Command Analysis**: AI analyzes and understands complex commands
- **Smart Code Generation**: Generate code in multiple languages
- **Contextual Responses**: Intelligent responses to any query
- **Conversation Memory**: AI remembers context across interactions
- **Offline Intelligence**: All AI processing happens locally

---

## 🔥 Unique Feature - Jarvis-like Realism

Every command executes only after simulating a Windows Search query.

**Example:**
🗣 "Open YouTube in browser" →

1. Opens Windows Search
2. Types "browser"
3. Selects the top browser app
4. Launches it
5. Types youtube.com and presses Enter
6. Done ✅

No shortcuts. It mimics how a human would interact manually with the system.

---

## 🧑‍💻 Technologies Used

- **💻 C# (.NET 6.0)**
- **🎤 System.Speech.Synthesis + NAudio** for TTS and voice recognition
- **🖱 Windows Input Simulator** or UIAutomation for cursor/mouse/keyboard actions
- **🧠 Custom local ML/NLP model** (trained for offline command understanding)
- **🔗 Integrated with LM Studio** for local AI chat and command analysis

---

## ⚙️ Quick Installation

### 📋 System Requirements

- **Operating System**: Windows 10 (version 1903+) or Windows 11
- **Architecture**: x64 (64-bit)
- **RAM**: Minimum 4GB, Recommended 8GB+
- **Storage**: 500MB free space
- **Audio**: Working microphone and speakers/headphones
- **Internet**: Optional (for initial setup only)

### 🛠️ Prerequisites Installation

#### 1. Install .NET 6.0 SDK

**Option A: Download from Microsoft**

- Visit: https://dotnet.microsoft.com/download/dotnet/6.0
- Download ".NET 6.0 SDK" for Windows x64
- Run installer and follow instructions

**Option B: Using Windows Package Manager**

```powershell
winget install Microsoft.DotNet.SDK.6
```

**Verify Installation:**

```bash
dotnet --version
# Should show: 6.0.x or higher
```

#### 2. Install Visual Studio (Choose One)

**Option A: Visual Studio 2022 Community (Recommended)**

- Download from: https://visualstudio.microsoft.com/vs/community/
- During installation, select:
  - ".NET desktop development" workload
  - "ASP.NET and web development" workload
  - Individual components: ".NET 6.0 Runtime"

**Option B: Visual Studio Code (Lightweight)**

- Download from: https://code.visualstudio.com/
- Install Extensions:
  - C# for Visual Studio Code
  - C# Extensions
  - .NET Install Tool

#### 3. Install LM Studio (Optional for AI Features)

- Download LM Studio from official source
- Run LM Studio on `http://localhost:1234` for local AI integration

#### 4. Configure Audio Permissions

1. **Windows Settings** → **Privacy & Security** → **Microphone**
2. Enable "Allow apps to access your microphone"
3. **Control Panel** → **Sound** → **Recording**
4. Set your microphone as "Default Device"
5. Test microphone: Right-click → "Test" → Speak and check levels

### 🚀 Project Setup

#### Method 1: Quick Start (Recommended)

1. **Download Project**

   ```bash
   git clone https://github.com/SelvaUx/SaraAI.git
   cd SaraAI/versions/v4.0/SaraAI_CSharp
   ```

2. **Auto-Build & Run**
   - **Windows**: Double-click `run.bat`
   - **PowerShell**: `./run.bat`
   - **Command Prompt**: `run.bat`

#### Method 2: Manual Setup

1. **Open Project**

   ```bash
   # Using Visual Studio
   start SaraAI4.0.sln

   # Using VS Code
   code .
   ```

2. **Restore NuGet Packages**

   ```bash
   dotnet restore
   ```

3. **Build Project**

   ```bash
   dotnet build --configuration Release
   ```

4. **Run Sara AI**

   ```bash
   dotnet run
   ```

   _Or press `F5` in Visual Studio_

---

## 💡 Sample Commands

- 🗣 "Hey Sara, open Notepad"
- 🗣 "Write Python code to print Hello World"
- 🗣 "Search about Elon Musk on Google"
- 🗣 "Create a folder named Project Alpha"
- 🗣 "Take a screenshot"
- 🗣 "Lock my screen"
- 🗣 "Play my favorite song"
- 🗣 "Open YouTube and search Top AI projects"
- 🗣 "Tell me a joke"
- 🗣 "What time is it?"
- 🗣 "Increase volume"
- 🗣 "Open calculator"
- 🗣 "Chat with AI about weather forecasts"
- 🗣 "Generate code in C# for file operations"

---

## 🎯 How to Use

1. **Start the Application**: Run the program and wait for initialization
2. **Wake Word**: Say "Hey Sara" to activate the assistant
3. **Give Commands**: Speak your command clearly
4. **Wait for Response**: Sara will acknowledge and execute your command
5. **Continue**: Give more commands or press 'Q' to quit

---

## 🛠 Troubleshooting

### Common Issues

**Microphone Not Working**

- Check Windows microphone permissions
- Verify microphone is set as default
- Update audio drivers

**Voice Recognition Not Responding**

- Speak clearly at moderate pace
- Reduce background noise
- Adjust confidence threshold in code
- Train Windows Speech Recognition

**Applications Not Opening**

- Verify apps are installed
- Test Windows Search manually
- Run as Administrator
- Update Windows Search indexing

**Build Errors**

```bash
dotnet --list-sdks  # Verify .NET 6.0
dotnet restore --force
dotnet clean
dotnet build
```

**LM Studio Connection Issues**

- Verify LM Studio is running
- Check firewall settings
- Test connection: `http://localhost:1234/v1/models`
- Ensure model is loaded

---

## 📁 Project Structure

```
v4.0/
├── SaraAI4.0.sln           # Visual Studio solution
├── SaraAI_CSharp/
│   ├── main.cs             # Entry point (Sara listener and router)
│   ├── modules/
│   │   ├── OpenApp.cs      # Application launching via Windows Search
│   │   ├── Music.cs        # Music controls
│   │   ├── Browser.cs      # Web browsing and search
│   │   ├── FileOps.cs      # File/folder operations
│   │   ├── Screen.cs       # Screenshot and screen recording
│   │   ├── Developer.cs    # Code writing to Notepad
│   │   ├── Utilities.cs    # Time/date/jokes
│   │   └── LMStudio.cs     # Local AI integration
│   ├── assets/
│   │   └── voiceModels/    # Local voice models and NLP data
│   ├── SaraAI.csproj      # Project file
│   └── run.bat            # Quick build and run script
└── README.md              # This file
```

---

## 📊 Performance Metrics

- **Voice Recognition Accuracy**: 95%+ in quiet environments
- **Command Response Time**: <500ms average
- **Memory Usage**: ~50-100MB during operation
- **CPU Usage**: <5% when idle, 10-15% during active use
- **Supported Commands**: 50+ built-in, extensible
- **Languages**: English (US) - More coming soon

---

## 🔮 Future Roadmap

### Version 4.1

- Cross-platform support (macOS, Linux)
- Face Recognition Login
- GUI dashboard
- Smart home integration

### Version 4.2

- Multi-language support
- Voice biometric authentication
- AI-powered project management
- Plugin architecture

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Selva Pandi (Selva.Ux)**

- GitHub: [@SelvaUx](https://github.com/SelvaUx)
- Instagram: [@selva.ux](https://instagram.com/selva.ux)
- Email: selva.ux@yahoo.com

---

<div align="center">
  <p><strong>Enjoy your personal AI assistant! 🤖✨</strong></p>
  <p>Made with ❤️ by Selva.Ux</p>
</div>
