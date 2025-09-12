# 🤖 SaraAI 5.0
**A Multi-Language, Offline AI Assistant**

SaraAI 5.0 is a Jarvis-like desktop assistant designed to work completely offline. It demonstrates versatility, system-level control, and modular design by utilizing multiple programming languages, each chosen for their specific strengths.

## 🚀 Features

- 🎙️ **Offline Speech Recognition** - Fast, local voice-to-text conversion
- 🔊 **Natural Text-to-Speech** - Human-like voice responses
- ⚙️ **System Control** - Direct OS integration and automation
- 📚 **Knowledge Base** - Fast local search and information retrieval
- 🧠 **AI Orchestration** - Intelligent command routing and decision making
- 🌐 **Interactive Dashboard** - Real-time web-based user interface

## 🛠️ Tech Stack

| Module | Language | Purpose | Key Libraries |
|--------|----------|---------|---------------|
| **Core Orchestrator** | Python | Command handling, AI logic | asyncio, fastapi, pydantic |
| **Speech-to-Text** | C++ | Fast, offline voice recognition | Whisper.cpp, Vosk |
| **Text-to-Speech** | Java | Natural voice responses | MaryTTS, FreeTTS |
| **System Control** | C# | OS integration (Windows) | Windows API, .NET |
| **Knowledge & Search** | Rust + SQLite | Fast local knowledge base | sqlx, tokio, serde |
| **Dashboard** | JavaScript | Web-based UI | WebSocket, HTML5, CSS3 |

## ⚡ Architecture & Data Flow

```
🎙️ User speaks → STT (C++) converts voice to text
                        ↓
🧠 Python core receives text and decides the task
                        ↓
    ┌─────────────────────────────────────────┐
    │                                         │
    ▼                    ▼                    ▼
🔊 TTS (Java)    ⚙️ System (C#)    📚 Search (Rust)
Response needed   System command    Knowledge query
    │                    │                    │
    └─────────────────────────────────────────┘
                        ▼
🌐 Dashboard (JavaScript) updates in real-time
```

## 📁 Project Structure

```
saraai-5.0/
├── core-python/           # 🧠 Main orchestrator and AI logic
│   ├── src/
│   ├── requirements.txt
│   └── main.py
├── speech-cpp/            # 🎙️ Speech-to-text processing
│   ├── src/
│   ├── include/
│   └── CMakeLists.txt
├── tts-java/             # 🔊 Text-to-speech generation
│   ├── src/
│   ├── pom.xml
│   └── build.gradle
├── system-csharp/        # ⚙️ Windows system integration
│   ├── src/
│   └── SystemControl.csproj
├── knowledge-rust/       # 📚 Knowledge base and search
│   ├── src/
│   ├── Cargo.toml
│   └── database/
├── dashboard-js/         # 🌐 Web-based user interface
│   ├── public/
│   ├── src/
│   └── package.json
├── config/              # ⚙️ Configuration files
├── docs/                # 📖 Documentation
├── scripts/             # 🔧 Build and deployment scripts
└── README.md
```

## 🚦 Getting Started

### Prerequisites

- **Python 3.9+** - Core orchestrator
- **C++ Compiler** (GCC/MSVC) - Speech recognition
- **Java 11+** - Text-to-speech
- **C# .NET 6.0+** - System control
- **Rust 1.70+** - Knowledge base
- **Node.js 18+** - Dashboard

### Quick Setup

1. **Clone and navigate to project:**
   ```bash
   git clone <repository-url>
   cd saraai-5.0
   ```

2. **Run the setup script:**
   ```bash
   # Windows
   .\scripts\setup.bat
   
   # Linux/Mac
   ./scripts/setup.sh
   ```

3. **Build all modules:**
   ```bash
   # Windows
   .\scripts\build.bat
   
   # Linux/Mac
   ./scripts/build.sh
   ```

4. **Start SaraAI:**
   ```bash
   python core-python/main.py
   ```

## 🔧 Module Details

### Core Python Orchestrator
- **Purpose**: Central command processing and AI decision making
- **Key Features**: Voice command interpretation, module coordination, task routing
- **Location**: `core-python/`

### C++ Speech Recognition
- **Purpose**: Fast, offline speech-to-text conversion
- **Key Features**: Real-time audio processing, multiple STT engine support
- **Location**: `speech-cpp/`

### Java Text-to-Speech
- **Purpose**: Natural voice response generation
- **Key Features**: Multiple voice options, offline TTS engines
- **Location**: `tts-java/`

### C# System Control
- **Purpose**: Windows system integration and automation
- **Key Features**: File operations, application control, system monitoring
- **Location**: `system-csharp/`

### Rust Knowledge Base
- **Purpose**: Fast local search and data retrieval
- **Key Features**: SQLite integration, full-text search, data indexing
- **Location**: `knowledge-rust/`

### JavaScript Dashboard
- **Purpose**: Real-time web interface
- **Key Features**: Voice visualization, system status, command history
- **Location**: `dashboard-js/`

## 🔗 Inter-Module Communication

SaraAI uses a combination of communication methods:
- **REST API** - HTTP-based requests between modules
- **WebSocket** - Real-time dashboard updates
- **Message Queue** - Asynchronous task processing
- **IPC** - Inter-process communication for system calls

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Whisper.cpp for offline speech recognition
- MaryTTS for text-to-speech synthesis
- SQLite for lightweight database functionality
- All open-source contributors who make projects like this possible

---

**Note**: This is a development project showcasing multi-language integration. Some features may require additional setup or dependencies based on your operating system.
