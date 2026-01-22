# 🤖 SARA AI - Intelligent Desktop Assistant Evolution

![Latest Version](https://img.shields.io/badge/latest-v6.0--offline-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![Stars](https://img.shields.io/github/stars/SelvaUx/SaraAI?style=social)

**SARA AI** is an evolving intelligent desktop assistant that has grown from basic voice commands to a sophisticated multi-platform automation system. This repository showcases the complete evolution of SARA across **7 distinct versions**, each building upon the previous with enhanced features and architectural innovations.

---

## 📚 Table of Contents

- [Version Overview](#-version-overview)
- [Quick Start](#-quick-start)
- [Version Details](#-version-details)
- [Feature Comparison](#-feature-comparison)
- [Technologies](#-technologies-used)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 🎯 Version Overview

| Version                            | Status    | Description                 | Key Innovation                                |
| ---------------------------------- | --------- | --------------------------- | --------------------------------------------- |
| [**v6.0-offline**](#v60-offline)   | ✅ Latest | Electron desktop app        | Modern UI + Python automation                 |
| [**v5.0**](#v50)                   | 📦 Stable | Multi-language architecture | 6 languages (Python, C++, Java, C#, Rust, JS) |
| [**v4.0**](#v40)                   | 📦 Stable | C# enterprise edition       | LM Studio AI integration                      |
| [**v3.0**](#v30)                   | 📦 Stable | Offline AI assistant        | Local LLM support + Fast mode                 |
| [**v2.0-enhanced**](#v20-enhanced) | 📦 Stable | Advanced desktop control    | Code generation + Biometrics                  |
| [**v2.0**](#v20)                   | 📦 Stable | Voice assistant 2.0         | Wake word detection + Music player            |
| [**v1-basic**](#v1-basic)          | 📦 Legacy | Foundation                  | Basic voice assistant (Python)                |

---

## 🚀 Quick Start

### Choose Your Version

```bash
# Clone the repository
git clone https://github.com/SelvaUx/SaraAI.git
cd sara-ai-desktop

# Navigate to your preferred version
cd versions/v6.0-offline  # Latest Electron app
# OR
cd versions/v4.0          # Enterprise C# version
# OR
cd versions/v3.0          # Python with AI integration

# Follow version-specific README for installation
```

### Recommended Version for Different Use Cases

- **🎯 General Users**: [v6.0-offline](#v60-offline) - Modern UI, easy to use
- **💼 Enterprise/Advanced**: [v4.0](#v40) - C# with LM Studio integration
- **🧠 AI Enthusiasts**: [v3.0](#v30) - Local AI models + Fast mode
- **👨‍💻 Developers**: [v5.0](#v50) - Multi-language architecture study

---

## 📖 Version Details

### v6.0-offline

> 🎯 **Focus**: Modern desktop app with Electron + Python automation

**Location**: `/versions/v6.0-offline/`

#### Highlights

- ✅ **Electron Framework** - Native desktop experience
- ✅ **Web Speech API** - Browser-based voice recognition
- ✅ **Python Automation** - PyAutoGUI for desktop control
- ✅ **WhatsApp Integration** - Send messages via desktop app
- ✅ **Wikipedia Lookup** - Quick information retrieval
- ✅ **Modern UI** - Clean, responsive interface

#### Tech Stack

- **Frontend**: Electron, HTML/CSS/JavaScript
- **Backend**: Node.js, Python 3.7+
- **Automation**: PyAutoGUI
- **APIs**: Wikipedia API, Web Speech API

#### Quick Start

```bash
cd versions/v6.0-offline
npm install
pip install -r requirements.txt
npm start
```

**[📖 Full v6.0 Documentation →](versions/v6.0-offline/README.md)**

---

### v5.0

> 🎯 **Focus**: Multi-language architecture demonstration

**Location**: `/versions/v5.0/`

#### Highlights

- ✅ **6 Programming Languages** - Python, C++, Java, C#, Rust, JavaScript
- ✅ **C++ STT** - Fast offline speech recognition (Whisper.cpp/Vosk)
- ✅ **Java TTS** - Natural voice responses (MaryTTS/FreeTTS)
- ✅ **C# System Control** - Deep Windows integration
- ✅ **Rust Knowledge Base** - Lightning-fast SQLite queries
- ✅ **React Dashboard** - Real-time web interface

#### Architecture

```
🎙️ C++ STT → 🧠 Python Core → 🔊 Java TTS
                    ↓
          ⚙️ C# System Control
          📚 Rust Knowledge Base
          🌐 JS Dashboard
```

#### Tech Stack

Each language chosen for its strengths:

- **Python**: AI orchestration & command routing
- **C++**: Real-time audio processing (<100ms latency)
- **Java**: Cross-platform TTS generation
- **C#**: Native Windows system control
- **Rust**: Memory-safe database operations
- **JavaScript**: Universal web UI

**[📖 Full v5.0 Documentation →](versions/v5.0/README.md)**

---

### v4.0

> 🎯 **Focus**: Enterprise C# rewrite with AI integration

**Location**: `/versions/v4.0/`

#### Highlights

- ✅ **Complete C# Rewrite** - .NET 6.0 architecture
- ✅ **LM Studio Integration** - Local AI chat & code generation
- ✅ **Windows Search Simulation** - Jarvis-like app launching
- ✅ **50+ Commands** - Comprehensive voice control
- ✅ **Offline NLP** - No internet required for basic functions
- ✅ **Professional Architecture** - Modular, extensible design

#### Tech Stack

- **Language**: C# (.NET 6.0)
- **Speech**: System.Speech.Synthesis + NAudio
- **Automation**: UIAutomation, Input Simulator
- **AI**: LM Studio local server integration

#### Key Features

- Voice recognition accuracy: 95%+ in quiet environments
- Command response time: <500ms average
- Memory usage: ~50-100MB
- 50+ built-in commands, fully extensible

**[📖 Full v4.0 Documentation →](versions/v4.0/README.md)**

---

### v3.0

> 🎯 **Focus**: Offline AI assistant with local LLM support

**Location**: `/versions/v3.0/`

#### Highlights

- ✅ **Local AI Models** - LM Studio integration (Llama, Mistral)
- ✅ **Fast Mode** - 2-3 second startup (`sara_fast.py`)
- ✅ **Offline STT** - Vosk speech recognition
- ✅ **Advanced NLP** - Context-aware responses
- ✅ **Code Generation** - Multi-language templates
- ✅ **Highly Configurable** - Extensive `config.py`

#### Modes

```bash
python main.py         # Full mode with AI
python sara_fast.py    # Fast mode (2-3s startup)
python main.py --text  # Text mode for testing
```

#### Tech Stack

- **Core**: Python 3.8+
- **AI**: LM Studio, Transformers, GGUF models
- **STT**: Vosk (offline) + Google (online fallback)
- **TTS**: pyttsx3 with dynamic voice selection

**[📖 Full v3.0 Documentation →](versions/v3.0/README.md)**

---

### v2.0-enhanced

> 🎯 **Focus**: Advanced desktop control & experimental features

**Location**: `/versions/v2.0-enhanced/`

#### Highlights

- ✅ **Voice-to-Code** - Dictate Python, HTML, C++ snippets
- ✅ **Experimental Biometrics** - Face unlock & gesture recognition
- ✅ **File Management** - Create, move, delete files/folders
- ✅ **Power Management** - Shutdown, restart, lock commands
- ✅ **Enhanced Media Control** - Play, pause, volume, brightness
- ✅ **Task Manager Integration** - Process control

#### Tech Stack

- **Core**: Python 3.7+
- **Vision**: OpenCV, MediaPipe
- **Automation**: PyAutoGUI
- **Code Gen**: Pre-built templates in `code_writer.py`

**[📖 Full v2.0-enhanced Documentation →](versions/v2.0-enhanced/README.md)**

---

### v2.0

> 🎯 **Focus**: Wake word detection & continuous listening

**Location**: `/versions/v2.0/`

#### Highlights

- ✅ **Wake Word Detection** - "Hey Sara" activation
- ✅ **Continuous Listening** - Always ready mode
- ✅ **Google Speech Recognition** - Accurate voice-to-text
- ✅ **Music Player** - Play from Music folder
- ✅ **Modular Architecture** - Clean, organized codebase
- ✅ **Enhanced TTS** - Jarvis-like voice (160 WPM)

#### Tech Stack

- **Core**: Python 3.7+
- **Speech**: SpeechRecognition, PyAudio
- **TTS**: pyttsx3 (dynamic voice selection)
- **Automation**: PyAutoGUI

**[📖 Full v2.0 Documentation →](versions/v2.0/README.md)**

---

### v1-basic

> 🎯 **Focus**: Foundation - Basic voice assistant

**Location**: `/versions/v1-basic/`

#### Highlights

- ✅ **Text-to-Speech** - Jarvis-like responses
- ✅ **Google Search** - Web search integration
- ✅ **Wikipedia** - Article summaries
- ✅ **App Launcher** - Windows Search integration
- ✅ **Utilities** - Time, date, jokes, screenshots

#### Tech Stack

- **Core**: Python 3.7+
- **TTS**: pyttsx3
- **Automation**: PyAutoGUI
- **APIs**: Wikipedia API

**[📖 Full v1-basic Documentation →](versions/v1-basic/README.md)**

---

## 📊 Feature Comparison

| Feature           | v1  | v2.0 | v2.0-E | v3.0 | v4.0 | v5.0 | v6.0 |
| ----------------- | --- | ---- | ------ | ---- | ---- | ---- | ---- |
| Voice Recognition | ✅  | ✅   | ✅     | ✅   | ✅   | ✅   | ✅   |
| Wake Word         | ❌  | ✅   | ✅     | ✅   | ✅   | ✅   | ✅   |
| TTS Engine        | ✅  | ✅   | ✅     | ✅   | ✅   | ✅   | ✅   |
| App Launcher      | ✅  | ✅   | ✅     | ✅   | ✅   | ✅   | ✅   |
| Code Generation   | ❌  | ❌   | ✅     | ✅   | ✅   | ✅   | ❌   |
| Local AI          | ❌  | ❌   | ❌     | ✅   | ✅   | ✅   | ❌   |
| Offline Mode      | ✅  | ✅   | ✅     | ✅   | ✅   | ✅   | ✅   |
| File Management   | ❌  | ❌   | ✅     | ✅   | ✅   | ✅   | ❌   |
| Biometrics        | ❌  | ❌   | ✅†    | ❌   | ❌   | ❌   | ❌   |
| Music Player      | ❌  | ✅   | ✅     | ✅   | ✅   | ✅   | ❌   |
| WhatsApp          | ❌  | ❌   | ❌     | ❌   | ❌   | ❌   | ✅   |
| Wikipedia         | ✅  | ✅   | ✅     | ✅   | ✅   | ✅   | ✅   |
| Modern UI         | ❌  | ❌   | ❌     | ❌   | ❌   | ✅   | ✅   |
| Multi-Language    | ❌  | ❌   | ❌     | ❌   | ❌   | ✅   | ❌   |

_† Experimental feature_

---

## 🛠️ Technologies Used

### Core Technologies

#### Languages

- **Python** 🐍 - Core logic (v1-v3, v5, v6)
- **C#** 💜 - Enterprise version (v4, v5)
- **C++** ⚡ - High-performance STT (v5)
- **Java** ☕ - TTS services (v5)
- **Rust** 🦀 - Knowledge base (v5)
- **JavaScript** 💛 - UI & dashboards (v5, v6)

#### Frameworks

- **Electron** - Desktop apps (v6)
- **.NET 6.0** - C# framework (v4)
- **React** - Web UI (v5)
- **FastAPI** - REST APIs (v5)

#### Speech & Audio

- **Web Speech API** - Browser recognition (v6)
- **Google Speech Recognition** - Online STT (v1-v3)
- **Vosk** - Offline STT (v3, v5)
- **Whisper.cpp** - Fast offline STT (v5)
- **pyttsx3** - Python TTS (v1-v3)
- **MaryTTS/FreeTTS** - Java TTS (v5)
- **System.Speech** - .NET TTS (v4)

#### Automation & System

- **PyAutoGUI** - Desktop automation (v1-v6)
- **UIAutomation** - Windows control (v4)
- **OpenCV** - Computer vision (v2.0-enhanced, v5)
- **MediaPipe** - Gesture recognition (v2.0-enhanced)

#### AI & NLP

- **LM Studio** - Local LLM serving (v3, v4)
- **Transformers** - Hugging Face models (v3)
- **Custom NLP** - Rule-based + ML (v3, v4)

#### External APIs

- **Wikipedia API** - Knowledge retrieval
- **Google Search** - Web search
- **Gemini API** - AI capabilities (optional, v6)

---

## 📦 Installation Guide

### General Prerequisites

```bash
# Check Node.js (v14 or higher)
node --version

# Check Python (3.7 or higher)
python --version

# Check Git
git --version
```

### Version-Specific Setup

#### For Python Versions (v1, v2.0, v2.0-enhanced, v3.0)

```bash
cd versions/[version-name]
pip install -r requirements.txt
python main.py
```

#### For C# Version (v4.0)

```bash
cd versions/v4.0/SaraAI_CSharp
dotnet restore
dotnet build
dotnet run
```

#### For Multi-Language Version (v5.0)

```bash
cd versions/v5.0
./scripts/setup.bat    # Windows
./scripts/setup.sh     # Linux/Mac
python core-python/main.py
```

#### For Electron Version (v6.0-offline)

```bash
cd versions/v6.0-offline
npm install
pip install -r requirements.txt
npm start
```

---

## 🎨 Customization

### Adding Custom Commands

Each version has its own command handler. Example patterns:

**Python versions:**

```python
# In main.py or command handler
if "your command" in text.lower():
    speak("Your response")
    # Your logic here
```

**C# version (v4.0):**

```csharp
// In main.cs
if (command.Contains("your command"))
{
    Speak("Your response");
    // Your logic here
}
```

**Electron version (v6.0):**

```javascript
// In command-handler.js
if (cleanText.includes("your command")) {
  response.text = "Your response";
  // Your logic here
  return response;
}
```

---

## 🔮 Evolution Timeline

```
v1-basic (2023)
   └─→ Basic voice assistant foundation
         └─→ v2.0 (2023)
               └─→ Wake word + Continuous listening
                     └─→ v2.0-enhanced (2024)
                           └─→ Code gen + Biometrics
                                 ├─→ v3.0 (2024)
                                 │     └─→ Local AI + Offline STT
                                 │           └─→ v4.0 (2024)
                                 │                 └─→ C# rewrite + LM Studio
                                 └─→ v5.0 (2024)
                                       └─→ Multi-language architecture
                                             └─→ v6.0-offline (2025)
                                                   └─→ Modern Electron app
```

---

## 🐛 Troubleshooting

### Common Issues

#### Voice Recognition Not Working

- ✅ Check microphone permissions in Windows settings
- ✅ Verify microphone is set as default device
- ✅ Test microphone with other applications
- ✅ Ensure stable internet (for Google Speech Recognition)

#### Application Won't Start

- ✅ Install all dependencies (`pip install -r requirements.txt`)
- ✅ Check Node.js/Python version compatibility
- ✅ Review error logs in console
- ✅ Try running with administrator privileges

#### Python Not Found (v6.0)

- ✅ Verify Python is in system PATH
- ✅ Test with `python --version`
- ✅ Install Python 3.7+ from python.org

#### Build Errors (v4.0)

- ✅ Install .NET 6.0 SDK
- ✅ Run `dotnet restore`
- ✅ Check Visual Studio installation

#### LM Studio Connection (v3.0, v4.0)

- ✅ Verify LM Studio is running on `localhost:1234`
- ✅ Load a model in LM Studio
- ✅ Check firewall settings
- ✅ Test: `http://localhost:1234/v1/models`

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Contribution Guidelines

- Follow existing code style
- Add tests for new features
- Update documentation
- Keep commits atomic and descriptive

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### What This Means

- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ⚠️ No warranty provided

---

## 👤 Author

**Selva Pandi (Selva.Ux)**

**Tech Empire Builder | Knowledge Seeker | Virtual World Architect | Self-Made Innovator**

[![GitHub](https://img.shields.io/badge/GitHub-SelvaUx-181717?style=for-the-badge&logo=github)](https://github.com/SelvaUx)
[![Instagram](https://img.shields.io/badge/Instagram-selva.ux-E4405F?style=for-the-badge&logo=instagram)](https://instagram.com/selva.ux)

### Connect With Me

- 💼 GitHub: [@SelvaUx](https://github.com/SelvaUx)
- 📸 Instagram: [@selva.ux](https://instagram.com/selva.ux)
- 📧 Email: selva.ux@yahoo.com

---

## 🙏 Acknowledgments

Special thanks to:

- **Electron Team** - Amazing desktop framework
- **Python Community** - PyAutoGUI and automation tools
- **Microsoft** - .NET framework and C# language
- **LM Studio Team** - Local LLM serving
- **Wikipedia** - Free knowledge API
- **Open Source Community** - Continuous inspiration
- **All Contributors** - Who have helped improve SARA AI

---

## ⭐ Star History

If you find this project helpful, please consider giving it a star! ⭐

---

## 📞 Support

Need help? Here's how to get support:

1. **Documentation** - Check version-specific READMEs in each folder
2. **Issues** - [Open an issue](https://github.com/SelvaUx/SaraAI/issues)
3. **Discussions** - Join GitHub Discussions
4. **Email** - Contact the author directly

---

<div align="center">

### Made with ❤️ by Selva.Ux

**SARA AI** - _"Your Intelligent Desktop Companion"_

**7 Versions. Infinite Possibilities.**

[⬆ Back to Top](#-sara-ai---intelligent-desktop-assistant-evolution)

</div>
