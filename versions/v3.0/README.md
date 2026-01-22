# 🤖 Sara AI 3.0 - Your Personal Offline JARVIS

**Local AI Integration** - Advanced NLP with offline LLM support

Sara AI 3.0 is a powerful, offline-capable voice assistant that brings JARVIS-like functionality with advanced natural language processing and seamless integration with local AI models.

![Version](https://img.shields.io/badge/Version-3.0-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-lightblue?style=for-the-badge&logo=windows)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## 🌟 Key Features

### 🎤 **Advanced Voice Recognition**

- **Wake Word Detection**: "Hey Sara" or "Sara" activation
- **Offline STT Support**: Works with Vosk for complete offline operation
- **Online STT Fallback**: Google Speech Recognition when internet available
- **Natural Language Understanding**: Flexible command interpretation

### 🧠 **AI-Powered Intelligence**

- **Local LLM Integration**: Compatible with LM Studio and local models
- **Rule-Based Fallback**: Reliable operation without AI dependencies
- **Context-Aware Responses**: Understands intent and entities
- **Conversational Interface**: Natural dialogue capabilities

### 🚀 **System Control & Automation**

- **Application Launcher**: Open any Windows application by voice
- **System Operations**: Shutdown, restart, lock, sleep, hibernate
- **Volume Control**: Adjust system volume with voice commands
- **Screenshot Capture**: Instant screen capture with timestamp
- **File Management**: Create files and folders by voice

### 🌐 **Web & Browser Control**

- **Smart Web Search**: Intelligent search query processing
- **Browser Automation**: Open websites and perform searches
- **YouTube Integration**: Search and play videos by voice
- **Multi-Browser Support**: Chrome, Firefox, Edge compatibility

### 💻 **Code Generation**

- **Multi-Language Support**: HTML, Python, C++, Java, JavaScript
- **Template Generation**: Pre-built code templates and structures
- **Instant Code Creation**: Generate code files with voice commands
- **Development Workflow**: Streamlined coding assistance

### 🎵 **Media Control**

- **Music Playback**: Control music applications
- **Volume Management**: System-wide audio control
- **Media Integration**: Support for various media players

### ⚡ **Performance Optimized**

- **Fast Mode**: 2-3 second startup with essential features (`sara_fast.py`)
- **Full Mode**: Complete feature set with AI integration (`main.py`)
- **Memory Efficient**: Optimized resource usage
- **Configurable Features**: Enable/disable modules as needed

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** (Recommended: Python 3.10+)
- **Windows 10/11** (Primary support)
- **Microphone** (for voice commands)
- **Internet Connection** (for online features)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/SelvaUx/SaraAI.git
   cd SaraAI/versions/v3.0
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run Sara AI**

   ```bash
   # Full Mode (with AI features)
   python main.py

   # Fast Mode (essential features only)
   python sara_fast.py

   # Text Mode (for testing without microphone)
   python main.py --text
   ```

---

## 📖 Usage Examples

### Voice Commands

```
"Hey Sara, search for Python tutorials"
"Hey Sara, open Visual Studio Code"
"Hey Sara, write HTML code"
"Hey Sara, take a screenshot"
"Hey Sara, lock the screen"
"Hey Sara, what time is it?"
```

### Text Mode

```bash
python main.py --text
Sara> search for machine learning
Sara> open notepad
Sara> take a screenshot
```

---

## 🔧 Configuration

Sara AI 3.0 is highly configurable through `config.py`:

### Performance Settings

```python
VOICE_SETTINGS = {
    'wake_word_timeout': 0.5,
    'command_timeout': 5,
    'energy_threshold': 300
}

AI_SETTINGS = {
    'use_local_ai': False,
    'use_rule_based_only': True,
    'ai_timeout': 2.0
}
```

### Feature Toggles

```python
FEATURES = {
    'voice_commands': True,
    'app_launcher': True,
    'browser_control': True,
    'code_writer': True,
    'music_control': True,
    'ai_chat': False  # Disable for better performance
}
```

---

## 🤖 AI Integration

### Local LLM Support

Sara AI supports local language models through:

- **LM Studio**: Easy local model serving
- **Transformers**: Direct model integration
- **Custom Models**: GGUF and other formats

### Setup LM Studio

1. Download and install [LM Studio](https://lmstudio.ai/)
2. Load a compatible model (e.g., Llama, Mistral)
3. Start the local server on `localhost:1234`
4. Sara AI will automatically detect and use the local model

---

## 📁 Project Structure

```
v3.0/
├── main.py                 # Main application (Full Mode)
├── sara_fast.py            # Fast Mode launcher
├── voice_engine.py         # Voice recognition and TTS
├── ai_engine.py           # AI and NLP processing
├── config.py              # Configuration settings
├── browser_control/       # Web browser automation
├── code_writer/          # Code generation modules
├── music_control/        # Media control functionality
├── software_launcher/    # Application launcher
├── system_control/       # System operations
├── logs/                 # Application logs
├── screenshots/          # Screenshot storage
├── docs/                # Documentation
│   ├── CHANGELOG.md
│   ├── CONTRIBUTING.md
│   ├── EXAMPLES.md
│   ├── INSTALL.md
│   ├── LM_STUDIO_SETUP.md
│   └── PROJECT_STATUS.md
└── requirements.txt      # Python dependencies
```

---

## 🎯 Command Categories

### 🌐 Web & Search

- Web search queries
- Website navigation
- YouTube video search
- Browser control

### 🚀 Applications

- Launch any Windows application
- Open development tools
- Start media players
- System utilities

### 💻 Development

- Generate code templates
- Create project files
- Open IDEs and editors
- Development workflow automation

### ⚙️ System Control

- Power management
- Volume control
- Screen capture
- File operations

### 💬 Conversation

- Time and date queries
- System information
- General questions
- Help and assistance

---

## 🛠️ Troubleshooting

### Common Issues

**Microphone Not Working**

- Check microphone permissions
- Verify audio input device
- Run audio troubleshooter
- Try text mode: `python main.py --text`

**Voice Recognition Issues**

- Ensure stable internet connection
- Check microphone calibration
- Speak clearly and distinctly
- Reduce background noise

**Application Launch Failures**

- Verify application is installed
- Check Windows Search functionality
- Run as administrator if needed
- Update application paths in config

**Performance Issues**

- Use Fast Mode: `python sara_fast.py`
- Disable unused features in config
- Close unnecessary applications
- Check system resources

---

## 📊 Comparison with Previous Versions

| Feature           | v2.0 Enhanced | v3.0             |
| ----------------- | ------------- | ---------------- |
| Voice Recognition | Google only   | ✅ Vosk + Google |
| Local AI          | ❌            | ✅ LM Studio     |
| NLP               | Basic         | ✅ Advanced      |
| Fast Mode         | ❌            | ✅ 2-3s startup  |
| Configuration     | Limited       | ✅ Extensive     |
| Modular Design    | Partial       | ✅ Complete      |
| Documentation     | Basic         | ✅ Comprehensive |

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Code Style

- Follow PEP 8 guidelines
- Use type hints where possible
- Add docstrings to functions
- Keep functions focused and small

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **OpenAI** for inspiration from ChatGPT and GPT models
- **Google** for Speech Recognition API
- **Microsoft** for Windows Speech Platform
- **Vosk** for offline speech recognition
- **LM Studio** for local LLM serving
- **Python Community** for excellent libraries

---

## 🔮 Roadmap

### Version 3.1 (Coming Soon)

- [ ] Cross-platform support (macOS, Linux)
- [ ] Mobile app integration
- [ ] Cloud synchronization
- [ ] Advanced AI model support

### Version 3.2 (Future)

- [ ] Computer vision capabilities
- [ ] Smart home integration
- [ ] Multi-language support
- [ ] Voice cloning features

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/SelvaUx/SaraAI/issues)
- **Documentation**: See `docs/` folder for detailed guides

---

## 👤 Author

**Selva Pandi (Selva.Ux)**

- GitHub: [@SelvaUx](https://github.com/SelvaUx)
- Instagram: [@selva.ux](https://instagram.com/selva.ux)
- Email: selva.ux@yahoo.com

---

<div align="center">
  <p><strong>Transform your computer into an intelligent assistant with Sara AI 3.0! 🚀</strong></p>
  <p>Made with ❤️ by Selva.Ux</p>
</div>
