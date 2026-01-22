# 🤖 SaraAI 5.0 - Multi-Language Powerhouse

**Polyglot Architecture** - A multi-language, offline AI assistant showcasing modular excellence

SaraAI 5.0 demonstrates versatility and system-level control by utilizing multiple programming languages, each chosen for their specific strengths. This is Sara AI at its most advanced architectural design.

![Version](https://img.shields.io/badge/version-5.0-blue.svg)
![Multi-Language](https://img.shields.io/badge/languages-6-purple.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 🚀 Features

- 🎙️ **Offline Speech Recognition** - Fast, local voice-to-text with Whisper.cpp/Vosk
- 🔊 **Natural Text-to-Speech** - Human-like voice responses via MaryTTS/FreeTTS
- ⚙️ **System Control** - Direct OS integration and automation
- 📚 **Knowledge Base** - Fast local search with Rust + SQLite
- 🧠 **AI Orchestration** - Intelligent command routing via Python core
- 🌐 **Interactive Dashboard** - Real-time web-based UI with WebSocket updates

---

## 🛠️ Tech Stack

| Module                 | Language      | Purpose                         | Key Libraries              |
| ---------------------- | ------------- | ------------------------------- | -------------------------- |
| **Core Orchestrator**  | Python        | Command handling, AI logic      | asyncio, fastapi, pydantic |
| **Speech-to-Text**     | C++           | Fast, offline voice recognition | Whisper.cpp, Vosk          |
| **Text-to-Speech**     | Java          | Natural voice responses         | MaryTTS, FreeTTS           |
| **System Control**     | C#            | OS integration (Windows)        | Windows API, .NET          |
| **Knowledge & Search** | Rust + SQLite | Fast local knowledge base       | sqlx, tokio, serde         |
| **Dashboard**          | JavaScript    | Web-based UI                    | WebSocket, HTML5, CSS3     |

---

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

---

## 📁 Project Structure

```
v5.0/
├── core-python/           # 🧠 Main orchestrator and AI logic
│   ├── src/
│   │   ├── main.py
│   │   ├── command_processor.py
│   │   └── module_coordinator.py
│   ├── requirements.txt
│   └── config/
├── speech-cpp/            # 🎙️ Speech-to-text processing
│   ├── src/
│   │   ├── stt_engine.cpp
│   │   └── audio_capture.cpp
│   ├── include/
│   └── CMakeLists.txt
├── tts-java/             # 🔊 Text-to-speech generation
│   ├── src/
│   │   └── com/saraai/tts/
│   ├── pom.xml
│   └── build.gradle
├── system-csharp/        # ⚙️ Windows system integration
│   ├── src/
│   │   ├── SystemController.cs
│   │   ├── FileManager.cs
│   │   └── AppLauncher.cs
│   └── SystemControl.csproj
├── knowledge-rust/       # 📚 Knowledge base and search
│   ├── src/
│   │   ├── main.rs
│   │   ├── database.rs
│   │   └── search_engine.rs
│   ├── Cargo.toml
│   └── database/
├── dashboard-js/         # 🌐 Web-based user interface
│   ├── public/
│   │   ├── index.html
│   │   └── assets/
│   ├── src/
│   │   ├── app.js
│   │   └── websocket.js
│   └── package.json
├── config/              # ⚙️ Configuration files
│   ├── app_config.json
│   └── module_settings.yaml
├── scripts/             # 🔧 Build and deployment scripts
│   ├── setup.bat / setup.sh
│   └── build.bat / build.sh
├── docs/                # 📖 Documentation
│   └── HOW_TO_USE.md
└── README.md            # This file
```

---

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
   git clone https://github.com/SelvaUx/SaraAI.git
   cd SaraAI/versions/v5.0
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

---

## 🔧 Module Details

### Core Python Orchestrator

- **Purpose**: Central command processing and AI decision making
- **Key Features**: Voice command interpretation, module coordination, task routing
- **Location**: `core-python/`
- **Dependencies**: asyncio, fastapi, pydantic

### C++ Speech Recognition

- **Purpose**: Fast, offline speech-to-text conversion
- **Key Features**: Real-time audio processing, multiple STT engine support
- **Location**: `speech-cpp/`
- **Dependencies**: Whisper.cpp, Vosk

### Java Text-to-Speech

- **Purpose**: Natural voice response generation
- **Key Features**: Multiple voice options, offline TTS engines
- **Location**: `tts-java/`
- **Dependencies**: MaryTTS, FreeTTS

### C# System Control

- **Purpose**: Windows system integration and automation
- **Key Features**: File operations, application control, system monitoring
- **Location**: `system-csharp/`
- **Dependencies**: Windows API, .NET

### Rust Knowledge Base

- **Purpose**: Fast local search and data retrieval
- **Key Features**: SQLite integration, full-text search, data indexing
- **Location**: `knowledge-rust/`
- **Dependencies**: sqlx, tokio, serde

### JavaScript Dashboard

- **Purpose**: Real-time web interface
- **Key Features**: Voice visualization, system status, command history
- **Location**: `dashboard-js/`
- **Dependencies**: WebSocket, HTML5, CSS3

---

## 🔗 Inter-Module Communication

SaraAI 5.0 uses a combination of communication methods:

- **REST API** - HTTP-based requests between modules
- **WebSocket** - Real-time dashboard updates
- **Message Queue** - Asynchronous task processing
- **IPC** - Inter-process communication for system calls

---

## 🎯 Why Multi-Language Architecture?

Each language was chosen for its strengths:

- **Python**: Perfect for AI orchestration and flexible scripting
- **C++**: Unmatched performance for real-time audio processing
- **Java**: Cross-platform TTS with excellent library support
- **C#**: Deep Windows integration and native system control
- **Rust**: Memory safety and blazing-fast database operations
- **JavaScript**: Universal web UI with real-time capabilities

This demonstrates that the **right tool for the right job** creates superior results.

---

## 📊 Performance Highlights

- **STT Latency**: <100ms (C++ processing)
- **Database Query**: <10ms (Rust + SQLite)
- **TTS Generation**: <200ms (Java MaryTTS)
- **System Commands**: <50ms (C# native calls)
- **Dashboard Update**: Real-time (WebSocket)

---

## 🛠️ Development

### Build Individual Modules

```bash
# Python Core
cd core-python && pip install -r requirements.txt

# C++ STT
cd speech-cpp && cmake . && make

# Java TTS
cd tts-java && mvn clean install

# C# System Control
cd system-csharp && dotnet build

# Rust Knowledge Base
cd knowledge-rust && cargo build --release

# JavaScript Dashboard
cd dashboard-js && npm install && npm run build
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Whisper.cpp** for offline speech recognition
- **MaryTTS** for text-to-speech synthesis
- **SQLite** for lightweight database functionality
- All open-source contributors who make projects like this possible

---

## 📝 Notes

**Note**: This is a development project showcasing multi-language integration. Some features may require additional setup or dependencies based on your operating system.

For detailed usage instructions, see [HOW_TO_USE.md](HOW_TO_USE.md)

---

## 👤 Author

**Selva Pandi (Selva.Ux)**

- GitHub: [@SelvaUx](https://github.com/SelvaUx)
- Instagram: [@selva.ux](https://instagram.com/selva.ux)
- Email: selva.ux@yahoo.com

---

<div align="center">
  <p><strong>Six Languages, One Vision 🌐</strong></p>
  <p>Made with ❤️ by Selva.Ux</p>
</div>
