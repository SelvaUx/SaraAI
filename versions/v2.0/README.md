# **SaraAI 2.0** 🤖

**SaraAI 2.0** is an advanced intelligent virtual assistant built with Python that provides a **Jarvis-like** experience. It combines voice recognition, text-to-speech, and automation capabilities to help you control your computer, search for information, and perform various tasks through natural voice commands.

---

## 🚀 **What's New in SaraAI 2.0**

- **Enhanced Voice Recognition**: Improved wake word detection with "Hey Sara"
- **Robust Error Handling**: Better microphone and PyAudio error management
- **Professional TTS Engine**: Dynamic voice selection with Jarvis-like speech patterns
- **Modular Architecture**: Clean, organized codebase with separate modules for different functionalities
- **Windows Integration**: Seamless integration with Windows Search and system applications
- **Smart Music Player**: Intelligent music folder detection and playback
- **Advanced Screenshot Functionality**: Automatic screenshot saving to Pictures folder

---

## ✨ **Core Features**

### 🎤 **Voice Recognition & Control**
- **Wake Word Activation**: Say "Hey Sara" to activate the assistant
- **Continuous Listening**: Always ready to respond to your commands
- **Google Speech Recognition**: Accurate voice-to-text conversion
- **Ambient Noise Adjustment**: Automatically adjusts for background noise

### 🗣️ **Text-to-Speech (TTS)**
- **Professional Voice**: Jarvis-like speaking experience
- **Dynamic Voice Selection**: Automatically selects the best available voice
- **Customizable Speech Rate**: Optimized for clarity and understanding
- **Real-time Feedback**: Immediate audio responses to all commands

### 🌐 **Web & Search Integration**
- **Google Search**: Direct web searches through voice commands
- **Wikipedia Integration**: Instant Wikipedia summaries with 2-sentence results
- **Browser Control**: Opens websites and search results in default browser
- **Smart Query Processing**: Intelligent extraction of search terms

### 💻 **System Control & Automation**
- **Application Launcher**: Open any Windows application via voice
- **Screenshot Capture**: Take and save screenshots instantly
- **Windows Search Integration**: Leverages Windows built-in search functionality
- **System Information**: Get current time and date on demand

### 🎵 **Entertainment Features**
- **Music Player**: Play music from your Music folder
- **Joke Generator**: Random programming and general jokes
- **Smart File Detection**: Automatically finds and plays available music files

## 📋 **Complete Command Reference**

### 🔍 **Search Commands**
| Command | Example | Description |
|---------|---------|-------------|
| `search [query]` | "search artificial intelligence" | Searches Google for the specified query |
| `search [topic]` | "search Python programming" | Opens Google search results in default browser |

### 🚀 **Application Commands**
| Command | Example | Description |
|---------|---------|-------------|
| `open [app]` | "open notepad" | Opens the specified application |
| `open [app]` | "open chrome" | Launches Chrome browser |
| `open [app]` | "open telegram" | Opens Telegram application |
| `open [app]` | "open calculator" | Opens Windows Calculator |

### 📚 **Information Commands**
| Command | Example | Description |
|---------|---------|-------------|
| `wikipedia [topic]` | "wikipedia machine learning" | Searches Wikipedia and reads summary |
| `wikipedia [person]` | "wikipedia Albert Einstein" | Gets biographical information |
| `time` | "time" | Tells current time in 12-hour format |
| `date` | "date" | Tells current date (DD/MM/YYYY format) |

### 📸 **Utility Commands**
| Command | Example | Description |
|---------|---------|-------------|
| `screenshot` | "screenshot" | Takes screenshot and saves to Pictures folder |
| `play music` | "play music" | Plays music from your Music folder |
| `joke` | "joke" | Tells a random programming or general joke |

## 🛠️ **Installation Guide**

### **Prerequisites**
- **Python 3.7+** installed on your system
- **Windows 10/11** (optimized for Windows)
- **Microphone** for voice input
- **Speakers/Headphones** for audio output
- **Internet connection** for Google Speech Recognition and Wikipedia

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/SelvaUx/SaraAI2.0.git
cd SaraAI2.0
```

### **Step 2: Create Virtual Environment (Recommended)**
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Required Dependencies:**
- `pyttsx3` - Text-to-Speech engine
- `speechrecognition` - Voice recognition
- `pyaudio` - Audio input/output
- `pyautogui` - GUI automation and screenshots
- `wikipedia` - Wikipedia API integration
- `pyjokes` - Random joke generation

### **Step 4: Run SaraAI 2.0**
```bash
python main.py
```

## 🎯 **Usage Examples**

### **Basic Interaction Flow**
1. **Start the application**: Run `python main.py`
2. **Wait for prompt**: "🎤 Waiting for wake word: 'Hey Sara'..."
3. **Say wake word**: "Hey Sara"
4. **Give command**: Sara responds "Yes, I'm listening."
5. **Voice command**: Say any supported command
6. **Get response**: Sara executes the command and provides audio feedback

### **Example Conversations**

**🔍 Web Search Example:**
```
You: "Hey Sara"
Sara: "Yes, I'm listening."
You: "search Python tutorials"
Sara: "Searching for Python tutorials in Google."
[Opens Google search results in browser]
```

**📱 Application Launch Example:**
```
You: "Hey Sara"
Sara: "Yes, I'm listening."
You: "open notepad"
Sara: "Opening notepad using Windows search."
[Notepad application opens]
```

**📚 Wikipedia Search Example:**
```
You: "Hey Sara"
Sara: "Yes, I'm listening."
You: "wikipedia artificial intelligence"
Sara: "Here's what I found on Wikipedia: [Reads 2-sentence summary]"
```

**⏰ Time & Date Example:**
```
You: "Hey Sara"
Sara: "Yes, I'm listening."
You: "time"
Sara: "The current time is 02:30:45 PM"
```

**📸 Screenshot Example:**
```
You: "Hey Sara"
Sara: "Yes, I'm listening."
You: "screenshot"
Sara: "Screenshot taken and saved in your Pictures folder."
```

**🎵 Music Example:**
```
You: "Hey Sara"
Sara: "Yes, I'm listening."
You: "play music"
Sara: "Playing music from your Music folder."
[First music file in Music folder starts playing]
```

## 🏗️ **Project Architecture**

### **Core Modules**

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

## 🔧 **Configuration Options**

### **TTS Settings (tts.py)**
```python
engine.setProperty('rate', 160)     # Speech speed (words per minute)
engine.setProperty('volume', 1)     # Volume level (0.0 to 1.0)
# Voice selection: Female voice preferred, falls back to available voice
```

### **Wake Word Configuration (voice_input.py)**
```python
WAKE_WORD = "hey sara"  # Customizable wake word
```

### **File Paths**
- **Screenshots**: `~/Pictures/screenshot.png`
- **Music**: `~/Music/` (first file in folder)

### **Troubleshooting**:

* If Sara AI is unable to find or open an application, make sure it’s correctly installed and appears in the **Windows Start Menu**.
* If speech is not working, make sure your audio device is properly configured and your **Python** environment has the required libraries installed.

---

### **Contributing**:

Feel free to fork the repository, make changes, and create pull requests. Contributions are always welcome!

### **License**:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
