# 🤖 Sara AI v1.0 - Basic Voice Assistant

**The Foundation** - A simple yet functional Python-based voice assistant

Sara AI v1.0 is the foundational version that demonstrates core voice assistant capabilities with Python. It provides basic voice recognition, text-to-speech, and essential PC automation features.

![Version](https://img.shields.io/badge/version-1.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

---

## ✨ Features

### 🎤 **Voice Interaction**

- Text-based command input (foundation for voice)
- **Jarvis-like Text-to-Speech** responses
- Professional voice feedback for all commands

### 🌐 **Web & Search**

- **Google Search**: Search any query on Google
- **Website Launcher**: Open websites directly in default browser
- **Wikipedia Integration**: Get article summaries with voice feedback

### 💻 **Application Control**

- **Windows Search Integration**: Open any installed application
- Simulates native Windows application launching
- Works with all apps in Start Menu

### 🛠️ **Utilities**

- **Time & Date**: Get current time and date
- **Screenshot**: Capture and save to Pictures folder
- **Jokes**: Random joke generator for entertainment

---

## 📋 Command Reference

### Search Commands

| Command          | Example                | Description                        |
| ---------------- | ---------------------- | ---------------------------------- |
| `search [query]` | `search AI technology` | Searches Google for the query      |
| `open [website]` | `open youtube.com`     | Opens specified website in browser |

### Application Commands

| Command      | Example         | Description                          |
| ------------ | --------------- | ------------------------------------ |
| `open [app]` | `open notepad`  | Opens application via Windows Search |
| `open [app]` | `open telegram` | Works with any installed application |

### Utility Commands

| Command             | Example            | Description            |
| ------------------- | ------------------ | ---------------------- |
| `time`              | `time`             | Tells current time     |
| `date`              | `date`             | Tells current date     |
| `joke`              | `joke`             | Tells a random joke    |
| `screenshot`        | `screenshot`       | Takes screenshot       |
| `wikipedia [query]` | `wikipedia Python` | Gets Wikipedia summary |

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.7+**
- **Windows 10/11**
- **Microphone** (for future voice input)
- **Internet Connection** (for Wikipedia & Google Search)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/SelvaUx/SaraAI.git
   cd SaraAI/versions/v1-basic
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   **Required Packages:**
   - `pyttsx3` - Text-to-Speech engine
   - `pyautogui` - GUI automation
   - `wikipedia` - Wikipedia API
   - `pyjokes` - Joke generator

3. **Run Sara AI**
   ```bash
   python main.py
   ```

---

## 💡 Usage Examples

**Search the web:**

```
Sara > search machine learning
🔊 "Searching for machine learning in Google."
[Opens Google search in browser]
```

**Open an application:**

```
Sara > open chrome
🔊 "Opening chrome using Windows search."
[Chrome browser launches]
```

**Get Wikipedia information:**

```
Sara > wikipedia Python programming
🔊 "Here's what I found on Wikipedia: [Reads summary]"
```

**Take a screenshot:**

```
Sara > screenshot
🔊 "Screenshot taken and saved in your Pictures folder."
```

---

## 📁 Project Structure

```
v1-basic/
├── main.py                  # Main application entry point
├── tts.py                   # Text-to-Speech engine
├── utils.py                 # Utility functions (time, date, jokes)
├── application_handler.py   # Application launching logic
├── browser_handler.py       # Web browser and search control
├── app_control.py          # Alternative app control methods
├── requirements.txt         # Python dependencies
├── LICENSE.txt             # MIT License
└── README.md               # This file
```

---

## 🔧 How It Works

1. **Command Input**: User types commands in the console
2. **Text-to-Speech**: Sara speaks the response using pyttsx3
3. **Application Launch**: Uses Windows Search simulation to open apps
4. **Web Integration**: Opens URLs and Google searches via default browser
5. **Wikipedia Search**: Fetches article summaries using Wikipedia API

---

## 🛠️ Troubleshooting

### TTS Not Working

- Ensure `pyttsx3` is properly installed
- Check Windows audio drivers
- Verify speakers/headphones are working

### Application Won't Open

- Verify app is installed and appears in Windows Start Menu
- Try running with administrator privileges
- Check app name spelling

### Wikipedia Errors

- Ensure internet connection is active
- Check if Wikipedia is accessible
- Try different search queries

---

## 🎯 Key Highlights

- **Simple Architecture**: Easy to understand and extend
- **No External APIs**: Uses local Python libraries
- **Windows Integration**: Native Start Menu search
- **Voice Feedback**: Professional Jarvis-like responses
- **Modular Design**: Separate files for different features

---

## 🔮 Evolution Path

**This is version 1.0** - The foundation that evolved into more advanced versions:

- **v2.0**: Added wake word detection and continuous listening
- **v2.0-enhanced**: Added code generation and system control
- **v3.0**: Integrated local AI models and NLP
- **v4.0**: Complete C# rewrite with LM Studio integration
- **v5.0**: Multi-language architecture (Python, C++, Java, C#, Rust, JS)
- **v6.0**: Electron-based desktop app with modern UI

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
  <p><strong>The Foundation of Sara AI 🚀</strong></p>
  <p>Made with ❤️ by Selva.Ux</p>
</div>
