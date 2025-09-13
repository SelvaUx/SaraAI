# 🤖 SaraAI 5.0 - How to Use Guide

Welcome to SaraAI 5.0, your offline AI assistant! This guide will help you get started and make the most of your AI companion.

## 🚀 Running SaraAI 5.0

This section provides detailed instructions on how to set up and run SaraAI 5.0 on your system.

### 1. Prerequisites

Before you begin, ensure you have the following software installed:

*   **Python**: Version 3.9 or higher.
*   **Node.js**: Version 18 or higher.
*   **Java Development Kit (JDK)**: Version 11 or higher.
*   **C# .NET SDK**: Version 6.0 or higher.
*   **Rust**: Version 1.70 or higher.
*   **C++ Compiler**: Such as MSVC (on Windows) or GCC (on Linux/macOS).
*   **CMake**: Version 3.16 or higher.
*   **Git**: For cloning the repository.

You can check your installed versions using commands like:
```bash
python --version
node --version
java --version
dotnet --version
rustc --version
cmake --version
git --version
```

### 2. Clone the Repository

If you haven't already, clone the SaraAI repository to your local machine:
```bash
git clone <repository-url>
cd saraai-5.0
```
*(Replace `<repository-url>` with the actual URL of the repository)*

### 3. Install Dependencies and Build Modules

SaraAI is a multi-module project. You need to install dependencies and build each module.

**For Windows users:**
Run the setup and build script:
```powershell
# Navigate to the project directory if you haven't already
# cd path/to/saraai-5.0

# Run the setup script (installs dependencies for all modules)
.\scripts\setup.ps1

# Build all modules
.\scripts\build.ps1
```

**For Linux/macOS users:**
Run the setup and build script:
```bash
# Navigate to the project directory if you haven't already
# cd path/to/saraai-5.0

# Run the setup script (installs dependencies for all modules)
./scripts/setup.sh

# Build all modules
./scripts/build.sh
```
*Note: The build process might take some time as it compiles code from multiple languages.*

### 4. Start SaraAI

Once the build is complete, you can start the SaraAI assistant. The `.\run.ps1` (Windows) or `./run.sh` (Linux/macOS) script will start all necessary modules.

**Recommended way to start:**
```powershell
# Windows
.\run.ps1

# Linux/macOS
./run.sh
```

Alternatively, you can start the core orchestrator manually, which will then attempt to communicate with other running modules:
```bash
# Navigate to the core-python directory
cd core-python

# Activate Python virtual environment (if you created one during setup)
# Windows: .\venv\Scripts\Activate.ps1
# Linux/macOS: source venv/bin/activate

# Run the main orchestrator script
python main.py
```

### 5. Verify Installation and Access Dashboard

After starting SaraAI, you should see startup messages in your terminal indicating that modules are initializing and connecting.

**Verification Steps:**
1.  **Check Terminal Output**: Look for messages confirming that all modules have started successfully (e.g., `✅ All modules started successfully`).
2.  **Open the Dashboard**: Open your web browser and navigate to `http://localhost:3000`. You should see the SaraAI dashboard interface.
3.  **Wake Word Activation**: Listen for SaraAI to indicate that wake word detection is active. You can then try saying a wake word like "Hey Sara" followed by a command.

### Customizing Wake Word Settings

You can adjust wake word behavior using environment variables before starting SaraAI:

```bash
# Example for Windows PowerShell:
$env:SARAIA_WAKE_WORD_SENSITIVITY=0.8
$env:SARAIA_WAKE_WORD_ENABLED=true
python core-python/main.py

# Example for Linux/macOS:
export SARAIA_WAKE_WORD_SENSITIVITY=0.8
export SARAIA_WAKE_WORD_ENABLED=true
python core-python/main.py
```

## 🎙️ Using Voice Commands

### Wake Words
SaraAI uses wake words to know when you want to talk to it. Say one of these to get its attention:

- **"Sara"**
- **"Hey Sara"**  
- **"Computer"**
- **"Assistant"**

### How Voice Interaction Works

1. **Say a Wake Word**: "Hey Sara"
2. **Wait for Response**: SaraAI will say "Yes?" to confirm it's listening
3. **Give Your Command**: Speak your request clearly
4. **Get Your Answer**: SaraAI will respond and perform the action

### Example Conversation
```
You: "Hey Sara"
SaraAI: "Yes?"
You: "What time is it?"
SaraAI: "The current time is 3:30 PM."
You: "Tell me a joke."
SaraAI: "Why don't scientists trust atoms? Because they make up everything!"
You: "Search for the latest advancements in AI."
SaraAI: "Searching for the latest advancements in AI. I found several articles. Would you like me to summarize them?"
You: "Yes, please."
SaraAI: "Okay, summarizing the top results..."
You: "Open Google Chrome."
SaraAI: "Opening Google Chrome."
```

## 🎯 What SaraAI Can Do

### ⏰ Time & Date
- "What time is it?"
- "What's the current time?"
- "Tell me the time"
- "What day is today?"
- "What's today's date?"
- "What is the date tomorrow?"

### 🌤️ Weather Information
- "What's the weather like in [city]?"
- "Tell me about the weather in London."
- "How's the temperature today?"
- "Will it rain tomorrow?"

### 🔍 Search & Information
- "Search for the latest news on AI."
- "Find information about the history of the internet."
- "Tell me about black holes."
- "Look up the definition of 'serendipity'."
- "What is the capital of Australia?"

### 🖥️ System Control
- "Open notepad."
- "Launch calculator."
- "Start Google Chrome."
- "Open File Explorer."
- "Close Notepad."
- "Show me my desktop."

### 🔊 Volume Control
- "Volume up."
- "Turn the volume louder."
- "Volume down."
- "Turn the volume quieter."
- "Mute the sound."
- "Unmute."

### 💬 Conversation & Fun
- "Hello."
- "Hi Sara."
- "Good morning."
- "How are you doing?"
- "Tell me a joke."
- "Sing a song."
- "Thank you."
- "Help."
- "What can you do?"

### 🚪 Ending Session
- "Goodbye."
- "Bye Sara."
- "Stop listening."
- "Exit."

## 🌐 Using the Dashboard

The web dashboard provides a visual interface to SaraAI:

### Accessing the Dashboard
1. Open your web browser
2. Go to `http://localhost:3000`
3. You'll see the real-time SaraAI interface

### Dashboard Features
- **Module Status**: See which modules are running
- **Wake Word Status**: Monitor wake word detection
- **Command History**: View recent voice commands
- **Manual Commands**: Type commands instead of speaking
- **System Information**: Check module health and performance

## ⚙️ Configuration

### Wake Word Settings
You can customize wake word behavior by setting environment variables:

```bash
# Enable/disable wake words
SARAAI_WAKE_WORD_ENABLED=true

# Adjust sensitivity (0.0 to 1.0)
SARAAI_WAKE_WORD_SENSITIVITY=0.6

# Set audio threshold
SARAAI_AUDIO_THRESHOLD=0.01
```

### Changing Ports
If you need to use different ports:

```bash
SARAAI_API_PORT=8000
SARAAI_SPEECH_PORT=8001
SARAAI_TTS_PORT=8002
SARAAI_SYSTEM_PORT=8003
SARAAI_KNOWLEDGE_PORT=8004
SARAAI_DASHBOARD_PORT=3000
```

## 🛠️ Troubleshooting

### Wake Words Not Working

**Problem**: SaraAI doesn't respond to wake words

**Solutions**:
1. Check your microphone is working and not muted
2. Try speaking more clearly or closer to the microphone
3. Verify wake word detection is enabled in startup messages
4. Check if the speech module is running (should show ✅ in startup)

### No Audio Response

**Problem**: SaraAI understands commands but doesn't speak back

**Solutions**:
1. Check your speakers/headphones are working
2. Verify the TTS (Text-to-Speech) module started successfully
3. Check Windows audio output settings
4. Try a volume control command: "Hey Sara, volume up"

### Dashboard Not Loading

**Problem**: Can't access the dashboard at localhost:3000

**Solutions**:
1. Verify the dashboard module started (look for ✅ Dashboard in startup)
2. Check if port 3000 is being used by another application
3. Try refreshing the page or clearing browser cache
4. Make sure your firewall isn't blocking the connection

### Commands Not Understood

**Problem**: SaraAI says "I'm not sure how to help with that"

**Solutions**:
1. Try rephrasing your command using the examples above
2. Speak more clearly and avoid background noise
3. Use simpler, more direct commands
4. Say "Help" to hear what SaraAI can do

### Module Connection Issues

**Problem**: Error messages about modules not responding

**Solutions**:
1. Run the build script again: `.\scripts\build.ps1`
2. Check that all required tools are installed (Python, Java, .NET, etc.)
3. Restart SaraAI completely
4. Check Windows Defender or antivirus isn't blocking the executables

## 🎭 Tips for Best Experience

### Speaking to SaraAI
- **Speak clearly** and at normal pace
- **Use simple commands** rather than complex sentences
- **Wait for the "Yes?" response** before giving your command
- **Avoid background noise** when possible

### Wake Word Tips
- **Say wake words distinctly** - "Hey Sara" works better than "HeyySara"
- **Don't rush** - pause briefly after the wake word
- **Try different wake words** if one isn't working well for you

### Command Tips
- **Be specific**: "Open calculator" vs "Open something"
- **Use natural language**: "What time is it?" vs "Time query execute"
- **Try synonyms**: "Launch browser" or "Start browser" or "Open browser"

## 📚 Advanced Usage

### Environment Variables
Create a `.env` file in the project root to customize settings:

```bash
# .env file
SARAAI_DEBUG=true
SARAAI_LOG_LEVEL=DEBUG
SARAAI_WAKE_WORD_ENABLED=true
SARAAI_WAKE_WORD_SENSITIVITY=0.8
```

### Manual Module Control
You can start individual modules for testing:

```bash
# Start just the speech module
cd speech-cpp/build
./saraai_speech.exe

# Start just the TTS module
cd tts-java
mvn spring-boot:run

# Start just the knowledge module
cd knowledge-rust
cargo run --bin knowledge-server
```

### Development Mode
For developers working on SaraAI:

```bash
# Enable debug logging
export SARAAI_DEBUG=true
export SARAAI_LOG_LEVEL=DEBUG

# Start with development settings
python core-python/main.py --debug
```

## 🆘 Getting Help

### In-App Help
- Say **"Help"** or **"What can you do?"** to hear SaraAI's capabilities
- Check the dashboard for module status and errors
- Look at the console output for detailed error messages

### Common Commands Reference Card

| Action | Say This |
|--------|----------|
| Get Attention | "Hey Sara" / "Computer" |
| Time | "What time is it?" |
| Date | "What's today's date?" |
| Weather | "How's the weather?" |
| Search | "Search for cats" |
| Open App | "Open calculator" |
| Volume | "Volume up" / "Mute" |
| Help | "Help" / "What can you do?" |
| Goodbye | "Goodbye" / "Stop listening" |

### Technical Support
If you encounter issues:

1. Check the `logs/` directory for detailed error messages
2. Run with debug mode: `SARAAI_DEBUG=true python core-python/main.py`
3. Verify all modules built successfully with `.\scripts\build.ps1`
4. Check the WARP.md file for developer information

## 🎉 Enjoy Your AI Assistant!

SaraAI is designed to be your helpful, offline AI companion. The more you use it, the better you'll understand its capabilities. Don't hesitate to experiment with different commands and phrases - SaraAI is designed to understand natural language!

Remember: SaraAI works completely offline, so your privacy is protected and it will work even without an internet connection.

**Have fun with your new AI assistant!** 🤖✨
