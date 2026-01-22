# 🤖 Sara AI v2.0 - Enhanced Voice Assistant

**Wake Word Detection** - Continuous voice recognition with "Hey Sara" activation

Sara AI v2.0 introduces true voice interaction with wake word detection, making it a hands-free voice assistant that's always listening for your commands.

![Version](https://img.shields.io/badge/version-2.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

---

## 🚀 What's New in v2.0

### 🎤 **Voice Recognition Breakthrough**

- **Wake Word Detection**: Activate with "Hey Sara"
- **Continuous Listening**: Always ready to respond
- **Google Speech Recognition**: Accurate voice-to-text
- **Ambient Noise Adjustment**: Auto-adjusts for background noise

### 🎵 **Music Player**

- Play music from your Music folder
- Automatic music file detection
- Default player integration

### 🔧 **Enhanced Architecture**

- **Modular Design**: Clean, organized codebase
- **Robust Error Handling**: Better microphone and PyAudio management
- **Professional TTS**: Dynamic voice selection with Jarvis-like patterns
- **Improved Windows Integration**: Seamless Start Menu integration

---

## ✨ Core Features

### 🗣️ **Text-to-Speech (TTS)**

- Professional Jarvis-like voice
- Automatic voice selection (female voice preferred)
- Customizable speech rate (160 WPM default)
- Real-time audio feedback

### 🌐 **Web & Search**

- Google Search integration
- Wikipedia 2-sentence summaries
- Browser control & automation
- Smart query processing

### 💻 **System Control**

- Application launcher (any Windows app)
- Screenshot capture with auto-save
- Windows Search integration
- System information (time, date)

### 🎵 **Entertainment**

- Music playback from Music folder
- Random programming jokes
- Smart file detection

---

## 📋 Complete Command Reference

### 🔍 **Search Commands**

| Command          | Example                          | Description              |
| ---------------- | -------------------------------- | ------------------------ |
| `search [query]` | `search artificial intelligence` | Searches Google          |
| `search [topic]` | `search Python programming`      | Opens results in browser |

### 🚀 **Application Commands**

| Command      | Example           | Description       |
| ------------ | ----------------- | ----------------- |
| `open [app]` | `open notepad`    | Opens application |
| `open [app]` | `open chrome`     | Launches Chrome   |
| `open [app]` | `open telegram`   | Opens Telegram    |
| `open [app]` | `open calculator` | Opens Calculator  |

### 📚 **Information Commands**

| Command              | Example                      | Description             |
| -------------------- | ---------------------------- | ----------------------- |
| `wikipedia [topic]`  | `wikipedia machine learning` | Reads Wikipedia summary |
| `wikipedia [person]` | `wikipedia Albert Einstein`  | Gets biography          |
| `time`               | `time`                       | Tells current time      |
| `date`               | `date`                       | Tells current date      |

### 📸 **Utility Commands**

| Command      | Example      | Description                   |
| ------------ | ------------ | ----------------------------- |
| `screenshot` | `screenshot` | Saves to Pictures folder      |
| `play music` | `play music` | Plays music from Music folder |
| `joke`       | `joke`       | Tells random joke             |

---

## 🛠️ Installation

### Prerequisites

- **Python 3.7+**
- **Windows 10/11**
- **Microphone** for voice input
- **Speakers/Headphones** for audio output
- **Internet Connection** for Google Speech Recognition

### Setup Steps

1. **Clone Repository**

   ```bash
   git clone https://github.com/SelvaUx/SaraAI.git
   cd SaraAI/versions/v2.0
   ```

2. **Create Virtual Environment (Recommended)**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   **Required Packages:**
   - `pyttsx3` - Text-to-Speech engine
   - `speechrecognition` - Voice recognition
   - `pyaudio` - Audio input/output
   - `pyautogui` - GUI automation and screenshots
   - `wikipedia` - Wikipedia API integration
   - `pyjokes` - Random joke generation

4. **Run Sara AI v2.0**
   ```bash
   python main.py
   ```

---

## 🎯 Usage Examples

### Basic Interaction Flow

1. **Start the application**: `python main.py`
2. **Wait for prompt**: `"🎤 Waiting for wake word: 'Hey Sara'..."`
3. **Say wake word**: "Hey Sara"
4. **Give command**: Sara responds "Yes, I'm listening."
5. **Voice command**: Speak any supported command
6. **Get response**: Sara executes and provides audio feedback

### Example Conversations

**🔍 Web Search:**

```
You: "Hey Sara"
Sara: "Yes, I'm listening."
You: "search Python tutorials"
Sara: "Searching for Python tutorials in Google."
[Opens Google search results]
```

**📱 Application Launch:**

```
You: "Hey Sara"
Sara: "Yes, I'm listening."
You: "open notepad"
Sara: "Opening notepad using Windows search."
[Notepad launches]
```

**📚 Wikipedia:**

```
You: "Hey Sara"
Sara: "Yes, I'm listening."
You: "wikipedia artificial intelligence"
Sara: "Here's what I found on Wikipedia: [Reads 2-sentence summary]"
```

**⏰ Time & Date:**

```
You: "Hey Sara"
Sara: "Yes, I'm listening."
You: "time"
Sara: "The current time is 02:30:45 PM"
```

**🎵 Music:**

```
You: "Hey Sara"
Sara: "Yes, I'm listening."
You: "play music"
Sara: "Playing music from your Music folder."
[First music file starts playing]
```

---

## 🏗️ Project Architecture

### Core Modules

**`main.py`** - Main application controller

- Command routing and processing
- Main application loop
- Integration of all modules

**`voice_input.py`** - Voice recognition system

- Wake word detection ("Hey Sara")
- Google Speech Recognition integration
- Ambient noise adjustment
- Error handling for microphone issues

**`tts.py`** - Text-to-Speech engine

- Professional voice configuration
- Dynamic voice selection
- Speech rate and volume optimization
- Jarvis-like speaking experience

**`utils.py`** - Utility functions

- Wikipedia search integration
- Time and date functions
- Random joke generation
- Error handling for API calls

**`application_handler.py`** - System application control

- Windows Search integration
- Application launching
- Screenshot functionality
- GUI automation

**`browser_handler.py`** - Web browser control

- Google search functionality
- URL handling
- Browser automation
- Search query processing

**`music_player.py`** - Music playback system

- Music folder detection
- File existence checking
- Default music player integration
- Cross-platform compatibility (Windows focus)

**`app_control.py`** - Alternative application control

- Letter-by-letter typing simulation
- Enhanced application search
- Backup application launching method

---

## 🔧 Configuration Options

### TTS Settings (tts.py)

```python
engine.setProperty('rate', 160)     # Speech speed (words per minute)
engine.setProperty('volume', 1)     # Volume level (0.0 to 1.0)
# Voice selection: Female voice preferred, falls back to available voice
```

### Wake Word Configuration (voice_input.py)

```python
WAKE_WORD = "hey sara"  # Customizable wake word
```

### File Paths

- **Screenshots**: `~/Pictures/screenshot.png`
- **Music**: `~/Music/` (first file in folder)

---

## 🛠️ Troubleshooting

### Microphone Not Working

- Check Windows microphone permissions
- Verify microphone is set as default device
- Test microphone in Windows settings

### Voice Recognition Issues

- Ensure stable internet connection (for Google Speech Recognition)
- Speak clearly and distinctly
- Reduce background noise
- Check microphone calibration

### Application Launch Failures

- Verify app is installed and in Start Menu
- Check Windows Search functionality
- Run as administrator if needed

### PyAudio Installation Issues

- Install Microsoft C++ Build Tools
- Use pre-compiled PyAudio wheel for Windows

---

## 🎯 Key Improvements Over v1.0

| Feature              | v1.0         | v2.0                    |
| -------------------- | ------------ | ----------------------- |
| Voice Input          | ❌ Text only | ✅ Voice with wake word |
| Continuous Listening | ❌           | ✅ Always ready         |
| Music Player         | ❌           | ✅ Full support         |
| Modular Architecture | Partial      | ✅ Complete             |
| Error Handling       | Basic        | ✅ Robust               |
| TTS Quality          | Basic        | ✅ Professional         |

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

---

## 👤 Author

**Selva Pandi (Selva.Ux)**

- GitHub: [@SelvaUx](https://github.com/SelvaUx)
- Instagram: [@selva.ux](https://instagram.com/selva.ux)
- Email: selva.ux@yahoo.com

---

<div align="center">
  <p><strong>The Voice Revolution 🎤</strong></p>
  <p>Made with ❤️ by Selva.Ux</p>
</div>
