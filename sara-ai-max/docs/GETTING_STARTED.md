# Getting Started with Sara AI Max

Welcome to Sara AI Max! This guide will help you get up and running quickly.

## Prerequisites

- **Python 3.9 or higher**
- **Windows 10/11** (primary support)
- **Microphone** for voice commands
- **Internet connection** (for online speech recognition)

## Quick Installation

### 1. Install Python Dependencies

```bash
cd sara-ai-max
pip install -r requirements.txt
```

### 2. Optional Dependencies

For advanced features, install optional packages:

```bash
# Browser automation
pip install playwright
playwright install chromium

# OCR capabilities
pip install pytesseract easyocr

# Office automation
pip install python-docx openpyxl python-pptx

# Messaging
pip install telethon selenium
```

### 3. Run Sara AI Max

```bash
python main.py
```

## First Steps

### Test Your Voice

1. Run Sara AI Max
2. Say: **"Hey Sara"**
3. Wait for response: **"Yes, I'm listening."**
4. Say: **"What time is it?"**
5. Sara should tell you the current time!

### Basic Commands

Try these commands to get familiar:

```
"Hey Sara, open Notepad"
"Hey Sara, create a folder named TestFolder"
"Hey Sara, search for Python tutorials"
"Hey Sara, what's the system info?"
"Hey Sara, tell me a joke"
```

## Configuration

Copy `config.example.json` to `config.json` and customize:

```json
{
  "voice": {
    "wake_word": "hey sara",
    "tts_rate": 160
  }
}
```

## Troubleshooting

**Microphone not working?**

- Check Windows microphone permissions
- Verify microphone is set as default device

**Voice not recognized?**

- Ensure stable internet connection
- Speak clearly and at moderate volume
- Reduce background noise

**Import errors?**

- Run: `pip install -r requirements.txt --upgrade`
- Check Python version: `python --version`

## Next Steps

- Read the [Developer Guide](developer_guide.md) to create custom skills
- Check the [API Documentation](API.md) for integrations
- Review the [Security Policy](security_policy.md) for permissions

Happy automating! 🎉
