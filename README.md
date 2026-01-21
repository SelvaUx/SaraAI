# SARA AI - Your Intelligent Desktop Assistant 🤖

![Latest Version](https://img.shields.io/badge/latest-v6.0--offline-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Node](https://img.shields.io/badge/node-14+-green.svg)

**SARA AI** is an evolving desktop AI assistant that has grown from basic voice commands to a sophisticated automation system. This repository contains the complete evolution of SARA across multiple versions, each building upon the previous with enhanced features and capabilities.

---

## 📚 Table of Contents

- [Version Overview](#-version-overview)
- [Quick Start](#-quick-start)
- [Version Details](#-version-details)
- [Feature Comparison](#-feature-comparison)
- [Technologies](#-technologies)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 🎯 Version Overview

| Version                                 | Status    | Description                     | Key Features                                            |
| --------------------------------------- | --------- | ------------------------------- | ------------------------------------------------------- |
| [**v6.0-offline**](#v60-offline-latest) | ✅ Latest | Fully offline desktop assistant | Voice commands, Desktop automation, WhatsApp, Wikipedia |
| [**v5.0**](#v50)                        | 📦 Stable | Advanced TTS & multi-language   | Text-to-Speech, Java integration, Enhanced UI           |
| [**v4.0**](#v40)                        | 📦 Stable | Android mobile version          | Mobile app, Touch interface, On-device processing       |
| [**v3.0**](#v30)                        | 📦 Stable | Web-based interface             | Browser-based, REST API, Cloud ready                    |
| [**v2.0-enhanced**](#v20-enhanced)      | 📦 Stable | Improved v2.0                   | Better UI, More commands, Bug fixes                     |
| [**v2.0**](#v20)                        | 📦 Stable | GUI introduction                | Graphical interface, Settings panel                     |
| [**v1-basic**](#v1-basic)               | 📦 Legacy | Command-line only               | Basic voice recognition, CLI                            |

---

## 🚀 Quick Start

### Choose Your Version

```bash
# Clone the repository
git clone https://github.com/SelvaUx/SaraAI.git
cd SaraAI

# Navigate to the version you want
cd versions/v6.0-offline  # or any other version

# Install dependencies
npm install
pip install -r requirements.txt  # if Python is used

# Run the application
npm start
```

---

## 📖 Version Details

### v6.0-offline (Latest)

> 🎯 **Focus:** Fully offline desktop assistant with voice commands and automation

**Location:** `/versions/v6.0-offline/`

#### Features

- ✅ **Offline Voice Recognition** - Works without internet
- ✅ **Desktop Automation** - Screenshot capture, app launching
- ✅ **WhatsApp Integration** - Send messages via desktop app
- ✅ **Wikipedia Lookup** - Quick information retrieval
- ✅ **Smart Web Search** - Google search integration
- ✅ **Application Control** - Open any Windows app
- ✅ **System Utilities** - Time, date, jokes

#### Tech Stack

- **Frontend:** Electron, HTML/CSS/JavaScript
- **Backend:** Node.js, Python
- **Automation:** PyAutoGUI
- **APIs:** Wikipedia API, Web Speech API

#### Quick Commands

```
"Hey Sara"                           - Wake up
"Open Chrome"                        - Launch apps
"Screenshot"                         - Capture screen
"Send hello to John in WhatsApp"     - Message
"Wikipedia Albert Einstein"          - Get info
"Search Python tutorials"            - Web search
```

#### Installation

```bash
cd versions/v6.0-offline
npm install
pip install -r requirements.txt
npm start
```

---

### v5.0

> 🎯 **Focus:** Advanced Text-to-Speech and multi-language support

**Location:** `/versions/v5.0/`

#### Features

- ✅ **Advanced TTS Engine** - Multiple voice options
- ✅ **Multi-language Support** - Supports multiple languages
- ✅ **Java TTS Integration** - Native Java TTS service
- ✅ **Enhanced UI** - Modern interface design
- ✅ **Voice Customization** - Pitch, speed, volume control
- ✅ **Audio Export** - Save responses as audio files

#### Tech Stack

- **Frontend:** Electron, React components
- **Backend:** Node.js, Java
- **TTS:** Java Sound API, FreeTTS
- **Build:** Gradle, Maven

#### Notable Additions

- Java-based TTS service for better voice quality
- Voice profile customization
- Audio file generation
- Improved response accuracy

---

### v4.0

> 🎯 **Focus:** Mobile Android application

**Location:** `/versions/v4.0/`

#### Features

- ✅ **Android Native App** - Full mobile experience
- ✅ **Touch Interface** - Tap and swipe controls
- ✅ **On-device Processing** - No cloud dependency
- ✅ **Mobile Optimized UI** - Responsive design
- ✅ **Background Service** - Always listening mode
- ✅ **Widget Support** - Quick access widget

#### Tech Stack

- **Platform:** Android (Java/Kotlin)
- **UI:** Material Design
- **Speech:** Android Speech Recognition
- **Storage:** SQLite

#### Mobile-Specific Features

- Voice activation without opening app
- Lock screen widget
- Battery optimization
- Offline mode

---

### v3.0

> 🎯 **Focus:** Web-based interface with REST API

**Location:** `/versions/v3.0/`

#### Features

- ✅ **Web Interface** - Browser-based access
- ✅ **REST API** - External integrations
- ✅ **Multi-user Support** - User accounts
- ✅ **Cloud Ready** - Deployable to cloud
- ✅ **Session Management** - Persistent conversations
- ✅ **Analytics Dashboard** - Usage statistics

#### Tech Stack

- **Frontend:** React, Bootstrap
- **Backend:** Express.js, MongoDB
- **API:** RESTful endpoints
- **Auth:** JWT tokens

#### API Endpoints

```
POST /api/command     - Send voice command
GET  /api/history     - Get command history
POST /api/settings    - Update preferences
GET  /api/stats       - Usage statistics
```

---

### v2.0-enhanced

> 🎯 **Focus:** Improved GUI and enhanced features from v2.0

**Location:** `/versions/v2.0-enhanced/`

#### Features

- ✅ **Polished GUI** - Refined visual design
- ✅ **More Commands** - Expanded command library
- ✅ **Settings Panel** - Customization options
- ✅ **Theme Support** - Light/Dark themes
- ✅ **Command History** - View past interactions
- ✅ **Bug Fixes** - Stability improvements

#### Improvements Over v2.0

- Better error handling
- Faster response times
- More intuitive UI
- Additional voice commands
- Enhanced logging

---

### v2.0

> 🎯 **Focus:** Introduction of graphical user interface

**Location:** `/versions/v2.0/`

#### Features

- ✅ **First GUI Version** - Visual interface
- ✅ **Settings Page** - Basic configuration
- ✅ **Visual Feedback** - Command status display
- ✅ **Tray Icon** - System tray integration
- ✅ **Window Management** - Minimize, maximize, close

#### Tech Stack

- **Frontend:** Electron, Vanilla JavaScript
- **Backend:** Node.js
- **UI:** Custom CSS

---

### v1-basic

> 🎯 **Focus:** Command-line voice assistant foundation

**Location:** `/versions/v1-basic/`

#### Features

- ✅ **Voice Recognition** - Basic speech-to-text
- ✅ **CLI Interface** - Terminal-based
- ✅ **Simple Commands** - Core functionality
- ✅ **Text Responses** - Console output

#### Tech Stack

- **Runtime:** Node.js
- **Speech:** Node speech recognition libraries
- **Interface:** Command-line

#### Basic Commands

```
"hello sara"    - Greeting
"time"          - Current time
"date"          - Current date
"exit"          - Close application
```

---

## 📊 Feature Comparison

| Feature            | v1  | v2.0 | v2.0-E | v3.0 | v4.0 | v5.0 | v6.0 |
| ------------------ | --- | ---- | ------ | ---- | ---- | ---- | ---- |
| Voice Recognition  | ✅  | ✅   | ✅     | ✅   | ✅   | ✅   | ✅   |
| GUI Interface      | ❌  | ✅   | ✅     | ✅   | ✅   | ✅   | ✅   |
| Desktop Automation | ❌  | ❌   | ❌     | ❌   | ❌   | ❌   | ✅   |
| Web Interface      | ❌  | ❌   | ❌     | ✅   | ❌   | ❌   | ❌   |
| Mobile App         | ❌  | ❌   | ❌     | ❌   | ✅   | ❌   | ❌   |
| TTS Engine         | ❌  | ❌   | ❌     | ❌   | ✅   | ✅   | ✅   |
| Multi-language     | ❌  | ❌   | ❌     | ❌   | ❌   | ✅   | ❌   |
| Offline Mode       | ✅  | ✅   | ✅     | ❌   | ✅   | ✅   | ✅   |
| WhatsApp           | ❌  | ❌   | ❌     | ❌   | ❌   | ❌   | ✅   |
| Wikipedia          | ❌  | ❌   | ❌     | ✅   | ✅   | ✅   | ✅   |
| Screenshot         | ❌  | ❌   | ❌     | ❌   | ✅   | ❌   | ✅   |
| REST API           | ❌  | ❌   | ❌     | ✅   | ❌   | ❌   | ❌   |

---

## 🛠️ Technologies

### Core Technologies Across Versions

#### Frontend

- **Electron** - Desktop app framework (v2.0+)
- **React** - UI components (v3.0, v5.0)
- **HTML/CSS/JavaScript** - Core web technologies
- **Material Design** - Android UI (v4.0)

#### Backend

- **Node.js** - JavaScript runtime
- **Python** - Automation scripts (v6.0)
- **Java** - TTS services (v5.0)
- **Express.js** - Web server (v3.0)

#### Speech & Audio

- **Web Speech API** - Browser speech recognition
- **PyAutoGUI** - Desktop automation (v6.0)
- **FreeTTS** - Java TTS (v5.0)
- **Android Speech** - Mobile recognition (v4.0)

#### External APIs

- **Wikipedia API** - Knowledge retrieval
- **Google Search** - Web search
- **Gemini API** - AI capabilities (optional)

---

## 📦 Installation Guide

### General Prerequisites

```bash
# Node.js (v14 or higher)
node --version

# Python 3.7+ (for v6.0-offline)
python --version

# Git
git --version
```

### Version-Specific Setup

#### For Desktop Versions (v2.0, v2.0-enhanced, v5.0, v6.0-offline)

```bash
cd versions/[version-name]
npm install
npm start
```

#### For v6.0-offline (with Python)

```bash
cd versions/v6.0-offline
npm install
pip install -r requirements.txt
npm start
```

#### For Web Version (v3.0)

```bash
cd versions/v3.0
npm install
npm run build
npm run serve
```

#### For Android (v4.0)

```bash
cd versions/v4.0
./gradlew build
./gradlew installDebug
```

---

## 🎨 Customization

### Adding Custom Commands

Each version has its own command handler. Example for v6.0-offline:

```javascript
// In command-handler.js
if (cleanText.includes("your custom command")) {
  response.text = "Your response";
  // Your custom logic here
  return response;
}
```

### Changing Voice Settings

Modify the voice configuration in the respective version's settings file.

---

## 🐛 Troubleshooting

### Common Issues

#### Voice Recognition Not Working

- Check microphone permissions
- Verify browser/system supports Web Speech API
- Test microphone with other apps

#### Application Won't Start

- Ensure all dependencies are installed
- Check Node.js version compatibility
- Review error logs in console

#### Python Scripts Failing (v6.0)

- Verify Python is in system PATH
- Install required packages: `pip install -r requirements.txt`
- Check PyAutoGUI compatibility with your OS

### Getting Help

- Check version-specific README in each folder
- Open an issue on GitHub
- Contact: [@SelvaUx](https://github.com/SelvaUx)

---

## 🔮 Future Roadmap

### Planned Features

- [ ] Cross-platform support (macOS, Linux)
- [ ] Cloud synchronization
- [ ] Plugin system for extensions
- [ ] Smart home integration
- [ ] Calendar and reminders
- [ ] Email management
- [ ] Custom wake words
- [ ] Machine learning improvements
- [ ] Multi-user profiles
- [ ] Voice biometrics

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

**Selva.Ux**

[![GitHub](https://img.shields.io/badge/GitHub-SelvaUx-181717?style=for-the-badge&logo=github)](https://github.com/SelvaUx)
[![Instagram](https://img.shields.io/badge/Instagram-selva.ux-E4405F?style=for-the-badge&logo=instagram)](https://instagram.com/selva.ux)

### Connect With Me

- 💼 GitHub: [@SelvaUx](https://github.com/SelvaUx)
- 📸 Instagram: [@selva.ux](https://instagram.com/selva.ux)
- 📧 Email: spt6421@gmail.com

---

## 🙏 Acknowledgments

Special thanks to:

- **Electron Team** - For the amazing desktop framework
- **Python Community** - For PyAutoGUI and automation tools
- **Node.js Contributors** - For the robust runtime
- **Wikipedia** - For the free knowledge API
- **Open Source Community** - For continuous inspiration
- **All Contributors** - Who have helped improve SARA AI

---

## ⭐ Star History

If you find this project helpful, please consider giving it a star! ⭐

---

## 📞 Support

Need help? Here's how to get support:

1. **Documentation** - Check version-specific READMEs
2. **Issues** - [Open an issue](https://github.com/SelvaUx/SaraAI/issues)
3. **Discussions** - Join GitHub Discussions
4. **Email** - Contact the author directly

---

## 📈 Project Stats

![GitHub stars](https://img.shields.io/github/stars/SelvaUx/SaraAI?style=social)
![GitHub forks](https://img.shields.io/github/forks/SelvaUx/SaraAI?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/SelvaUx/SaraAI?style=social)

---

<div align="center">

### Made with ❤️ by Selva.Ux

**SARA AI** - _"Just a rather very intelligent system."_

[⬆ Back to Top](#sara-ai---your-intelligent-desktop-assistant-)

</div>
