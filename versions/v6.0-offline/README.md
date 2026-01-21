# SARA AI 6.0 [OFFLINE] 🤖

![Version](https://img.shields.io/badge/version-6.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)

A powerful desktop AI assistant built with Electron and Python, featuring voice commands, desktop automation, and intelligent task handling.

## 🌟 Features

### Voice Commands

- **Wake Word Detection**: Activate with "Hey Sara" or "Sara"
- **Natural Language Processing**: Understands conversational commands
- **Multi-function Support**: Open apps, search web, control system, and more

### Application Control

- Open applications via Windows Search
- Smart application launching with typing simulation
- Window management (minimize, close)

### Web Integration

- Google search directly from voice commands
- Open websites by URL or name
- Quick access to YouTube, Google, and other popular sites
- Wikipedia integration with article summaries

### Desktop Automation

- **Screenshots**: Capture and save screenshots to Pictures folder
- **WhatsApp Messaging**: Send messages via WhatsApp desktop app
- **System Control**: Time, date, and system information

### Utilities

- Built-in joke library for entertainment
- Real-time clock and calendar
- Wikipedia API integration for quick information

## 🚀 Getting Started

### Prerequisites

- **Node.js** (v14 or higher)
- **Python** (v3.7 or higher)
- **Windows OS** (Required for automation features)
- **npm** or **yarn** package manager

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/SelvaUx/SaraAI.git
   cd SaraAI/versions/v6.0-offline
   ```

2. **Install Node.js dependencies**

   ```bash
   npm install
   ```

3. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables** (Optional)
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

### Running the Application

#### Development Mode

```bash
npm start
```

#### Build for Production

```bash
# Build for Windows (all architectures)
npm run dist

# Build for Windows x64 only
npm run dist:win:x64
```

The built application will be available in the `dist` folder.

## 📖 Usage

### Voice Commands

Once the application is running, you can use the following voice commands:

#### Basic Commands

- `"Hey Sara"` or `"Sara"` - Wake up the assistant
- `"Minimize"` or `"Minimize yourself"` - Minimize the window
- `"Close"` or `"Go to sleep"` - Close the application

#### Web & Search

- `"Search [query]"` - Search Google for the query
- `"Open YouTube"` - Open YouTube
- `"Open Google"` - Open Google
- `"Open [website].com"` - Open any website
- `"Wikipedia [topic]"` - Get Wikipedia summary or open article

#### Applications

- `"Open [app name]"` - Open any Windows application
  - Examples: "Open Chrome", "Open Notepad", "Open Telegram"

#### Utilities

- `"What's the time?"` - Get current time
- `"What's the date?"` - Get current date
- `"Tell me a joke"` - Hear a random joke
- `"Screenshot"` - Take a screenshot (saved to Pictures folder)

#### Messaging

- `"Send [message] to [contact] in WhatsApp"` - Send WhatsApp message
  - Example: "Send hello to John in WhatsApp"

## 🏗️ Project Structure

```
v6.0-offline/
├── renderer/              # Frontend files
│   ├── index.html        # Main UI
│   ├── renderer.js       # Frontend logic
│   └── styles.css        # Styling
├── automation.py         # Python automation scripts
├── command-handler.js    # Voice command processing
├── main.js              # Electron main process
├── preload.js           # Electron preload script
├── package.json         # Node.js dependencies
└── requirements.txt     # Python dependencies
```

## 🛠️ Technologies Used

### Frontend

- **Electron** - Desktop application framework
- **HTML/CSS/JavaScript** - User interface
- **Web Speech API** - Voice recognition

### Backend

- **Node.js** - Runtime environment
- **Python** - Automation scripts
- **PyAutoGUI** - Desktop automation
- **node-fetch** - HTTP requests

### APIs & Services

- **Wikipedia API** - Information retrieval
- **Google Search** - Web search integration

## 🔧 Configuration

### Build Configuration

The application uses `electron-builder` for packaging. Configuration can be found in `package.json` under the `build` section.

### Python Automation

The `automation.py` script provides three main functions:

- `open_application(app_name)` - Opens Windows applications
- `screenshot()` - Takes and saves screenshots
- `send_whatsapp_message(contact, message)` - Sends WhatsApp messages

## 🐛 Troubleshooting

### Python not found

Ensure Python is installed and added to your system PATH. You can test this by running:

```bash
python --version
```

### Voice recognition not working

- Check microphone permissions in Windows settings
- Ensure you're using a supported browser engine (Chromium/Chrome)
- Test microphone with other applications

### Application won't open apps

- Ensure the application name is correct
- Check Windows Search is functioning properly
- Run the application with administrator privileges if needed

### Screenshot fails

- Verify the Pictures folder exists in your user directory
- Check write permissions for the Pictures folder

## 📝 Development

### Adding New Commands

1. Open `command-handler.js`
2. Add your command pattern in the `processCommand` method
3. Implement the command logic
4. Update the README with the new command

### Adding Python Automation

1. Open `automation.py`
2. Create a new function for your automation
3. Add command-line argument handling in the `if __name__ == "__main__"` block
4. Call it from `command-handler.js` using `runPythonAutomation()`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Selva.Ux**

- GitHub: [@SelvaUx](https://github.com/SelvaUx)
- Instagram: [@selva.ux](https://instagram.com/selva.ux)

## 🙏 Acknowledgments

- Thanks to the Electron community for the amazing framework
- PyAutoGUI for powerful automation capabilities
- Wikipedia API for knowledge integration

---

<div align="center">
  Made with ❤️ by Selva.Ux
</div>
