# 🛠️ Sara AI 3.0 - Installation Guide

This guide provides step-by-step instructions for installing Sara AI 3.0 on Windows systems.

---

## 📋 System Requirements

### Minimum Requirements
- **Operating System**: Windows 10 (64-bit) or Windows 11
- **Python**: 3.8 or higher (3.10+ recommended)
- **RAM**: 4 GB minimum (8 GB recommended)
- **Storage**: 2 GB free space
- **Microphone**: Any USB or built-in microphone
- **Internet**: Required for initial setup and online features

### Recommended Requirements
- **Operating System**: Windows 11 (latest updates)
- **Python**: 3.10 or 3.11
- **RAM**: 16 GB (for local AI models)
- **Storage**: 10 GB free space (for models and data)
- **Microphone**: High-quality USB microphone
- **Internet**: Stable broadband connection

---

## 🚀 Quick Installation (Recommended)

### Option 1: Fast Mode Setup
Perfect for first-time users who want to try Sara AI quickly.

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/SaraAI3.0.git
cd SaraAI3.0

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run Fast Mode
python sara_fast.py
```

### Option 2: Full Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/SaraAI3.0.git
cd SaraAI3.0

# 2. Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run Sara AI
python main.py
```

---

## 🔧 Detailed Installation Steps

### Step 1: Python Setup

#### Install Python (if not already installed)
1. Download Python from [python.org](https://www.python.org/downloads/)
2. **Important**: Check "Add Python to PATH" during installation
3. Verify installation:
   ```bash
   python --version
   pip --version
   ```

### Step 2: Clone Repository
```bash
git clone https://github.com/yourusername/SaraAI3.0.git
cd SaraAI3.0
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Test Installation
```bash
# Test with text mode (no microphone required)
python main.py --text

# Test voice mode
python main.py

# Test fast mode
python sara_fast.py
```

---

## 🤖 AI Model Setup (Optional)

### LM Studio Setup (Recommended)

1. **Download LM Studio**
   - Visit: https://lmstudio.ai/
   - Download and install for Windows

2. **Download a Model**
   - Open LM Studio
   - Go to "Discover" tab
   - Search for "mistral-7b-instruct" or "llama-2-7b-chat"
   - Download GGML version (4-bit quantized recommended)

3. **Start Local Server**
   - In LM Studio, go to "Local Server" tab
   - Load your downloaded model
   - Start server on `localhost:1234`
   - Sara AI will automatically detect it

---

## 🔧 Configuration

Sara AI can be customized through `config.py`:

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

## 🛠️ Troubleshooting

### Common Issues

#### Python PATH Issues
```bash
# Check if Python is in PATH
where python
where pip

# If not found, reinstall Python with "Add to PATH" checked
```

#### Permission Errors
```bash
# Run as administrator or use --user flag
pip install --user -r requirements.txt
```

#### Microphone Issues
1. Check Windows microphone permissions
2. Go to Settings > Privacy > Microphone
3. Allow apps to access microphone
4. Test with: `python main.py --text` first

#### Performance Issues
1. Use Fast Mode: `python sara_fast.py`
2. Disable unused features in `config.py`
3. Close unnecessary applications
4. Check system resources

---

## 📦 Dependencies

### Core Dependencies
- `speech-recognition` - Voice recognition
- `pyttsx3` - Text-to-speech
- `pyautogui` - GUI automation
- `keyboard` - Keyboard control
- `psutil` - System monitoring
- `requests` - HTTP requests
- `pywin32` - Windows API access

### Optional Dependencies
- `transformers` - AI model support
- `torch` - Machine learning framework
- `vosk` - Offline speech recognition
- `pygame` - Audio playback

---

## 🧪 Testing Installation

### Basic Test
```bash
python -c "
from main import SaraAI
sara = SaraAI(text_mode=True)
print('✅ Sara AI installed successfully!')
"
```

### Voice Test
```bash
# Test microphone
python -c "
import speech_recognition as sr
r = sr.Recognizer()
m = sr.Microphone()
print('✅ Microphone detected:', sr.Microphone.list_microphone_names())
"
```

---

## 📞 Support

If you encounter issues:

1. **Check logs**: Look in `logs/` directory for error messages
2. **GitHub Issues**: [Report bugs](https://github.com/yourusername/SaraAI3.0/issues)
3. **Documentation**: [Check Wiki](https://github.com/yourusername/SaraAI3.0/wiki)
4. **Discussions**: [Community help](https://github.com/yourusername/SaraAI3.0/discussions)

---

## ✅ Installation Checklist

- [ ] Python 3.8+ installed with PATH configured
- [ ] Repository cloned successfully
- [ ] Dependencies installed
- [ ] Microphone permissions granted
- [ ] Basic functionality tested
- [ ] Configuration customized (optional)
- [ ] AI models downloaded (optional)

---

**Installation complete! 🎉**

Run `python sara_fast.py` to start your Sara AI experience!