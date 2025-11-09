

## 📖 Documentation

- **[Getting Started Guide](docs/GETTING_STARTED.md)** - Complete installation and setup
- **[API Documentation](docs/API.md)** - Build custom skills and integrations
- **[Developer Guide](docs/developer_guide.md)** - Development workflow
- **[Security Policy](docs/security_policy.md)** - Permission levels and security model
- **[WARP.md](WARP.md)** - Warp AI development guide
- **[GUI README](GUI_README.md)** - Details on the graphical interface

## 🏗️ Project Structure

```
sara-max/
├── sara_core/          # Core: NLU, Planner, Executor, Security
├── automation/         # File ops, archives, media, system control
├── connectors/         # Email, browser, messaging, office automation
├── vision/             # OCR, screenshots, UI finding
├── skills/             # Example skills (web search, send message)
├── plugins/            # Plugin SDK for custom skills
├── cli/                # CLI tools (saractl)
├── tests/              # Comprehensive test suite
├── docs/               # Full documentation
├── main.py             # Main application entry point
└── config.example.json # Example configuration
```

## 🎯 Detailed Capabilities

### 1️⃣ Core Voice Intelligence
Continuous wake-word listener (“Hey Sara”) with noise suppression, VAD, multilingual speech-to-text (Vosk / Whisper). Real-time command parsing, punctuation, and context memory. Natural TTS replies using pyttsx3 or edge-tts with adjustable tone, gender, and speed. Multi-user voice profiles; optional speaker recognition for personalization.

### 2️⃣ System & File Automation
Launch, close, minimize, resize, switch, and monitor applications. Navigate folders, copy / move / rename / delete / recover files. Compress / extract ZIP / 7Z / RAR / TAR archives with auto-destination logic. Create backups and timed snapshots (shadow-copy or rsync). Search by name, type, or content; tag and catalog files. Bulk actions: “Clean Downloads older than 30 days,” “Organize photos by month.” Undo or rollback every destructive step; all deletions go to a safe vault.

### 3️⃣ Application Integration
Browsers: Chrome / Edge / Firefox control via Playwright. Messaging: WhatsApp Web, Telegram Desktop, Signal Desktop. Email: Gmail IMAP/SMTP and Outlook via exchangelib. Office: Word / Excel / PowerPoint automation (win32com / pyautogui). Media: YouTube, Spotify, VLC — play, pause, queue, adjust volume. Development: VS Code, PyCharm, Terminal, Git, build & test automation. Creative: Photoshop / GIMP keyboard macro support; paste & export images.

### 4️⃣ Network & Hardware Control
Toggle Wi-Fi, Bluetooth, airplane-mode, tethering. Adjust brightness, volume, microphone gain, input / output devices. Capture camera feed, take photos or screenshots. Communicate with Arduino / ESP32 / Raspberry Pi over serial / Wi-Fi for IoT. System information & diagnostics (“Check CPU temperature,” “Show RAM usage”).

### 5️⃣ Automation Engine & Planner
Deterministic intent → plan → atomic actions pipeline. Every plan can simulate, explain, then execute. Step safety levels: observe | low | medium | high-risk. Two-step confirmations and spoken OTPs for high-risk tasks. Action queue with timeouts, retries, and concurrency control. Undo stack & versioned history for full reversibility.

### 6️⃣ Visual Intelligence
Screen OCR (Tesseract / easyocr) to read text on screen. Template & object detection (OpenCV) to find icons, buttons, or windows. Fallback hierarchy: Accessibility → Selector → Template → OCR → User prompt. Dynamic element recognition even after UI changes.

### 7️⃣ Communication & Productivity
Compose, read, and summarize emails. Draft documents and presentations by voice. Translate text, detect language automatically. Summarize webpages, PDFs, or clipboard text. Manage calendar, set reminders, alarms, timers. Take notes, todo lists, and convert speech → Markdown.

### 8️⃣ API Autodetection Layer
Scan environment and config for valid API keys (GEMINI_KEY, OPENAI_API_KEY, etc.). Ping endpoints concurrently, benchmark latency, cache results. Route tasks by capability: reasoning → Gemini, summarization → OpenAI, translation → local. Never transmit private data without voice or UI approval. Securely store credentials in OS keyring, not plain files. Full provider report: name, latency, cost, allowed capabilities.

### 9️⃣ Macro & Skill System
Record any manual session → save as macro.yml. Replay macros by name (“Run macro morning setup”). Convert macros to Python Skill modules with parameters. Hot-reload skills without restart. Plugin SDK with signed manifests; sandbox each plugin with resource limits. Local plugin marketplace & dependency installer.

### 🔟 Security, Privacy & Audit
Mandatory permission checks for all actions. Signed plugins only; sandbox for third-party code (no network, limited CPU/RAM). Full audit log in SQLite + human-readable journal. Privacy vault encrypts tokens / credentials / personal data. Voice confirmations for dangerous actions. “Strict mode” = no cloud, no disk writes outside user folder. “Trusted mode” = auto-approve known safe actions.

### 11️⃣ User Experience & Interface
Voice + optional GUI dashboard showing live actions, logs, and abort controls. Real-time subtitles of Sara’s speech & recognized commands. Desktop notifications and toast pop-ups for status. Theming: light/dark, accent color linked to wallpaper. Multi-language interface; easy language switch. Accessibility features for hands-free & eyes-free operation.

### 12️⃣ Intelligence Enhancements (without built-in LLM)
Deterministic templates for common reasoning patterns. Optional cloud reasoning when APIs allowed. Local embedding & search (FAISS / Chroma) for offline document recall. Rule-based habit detection: auto-suggest new macros. Context memory of recent sessions; can forget on command.

### 13️⃣ Developer & Admin Tools
CLI tool `saractl` for build, test, install, or control Sara Max. Integrated test runner & logger viewer. API for remote control via WebSocket / HTTP. One-click Windows service installer, autostart config, updater. Complete docs generator (mkdocs / Sphinx). Continuous-integration pipeline: lint → type-check → unit → integration → security scan.

### 14️⃣ Special Extreme Features
1. Rollback Snapshots: automatic pre-action backups with restore menu.
2. Visual Flow Player: replay actions like a movie for debugging.
3. Adaptive Profiles: per-user, per-time, or per-app trust levels.
4. Omnibox Composer: type or speak to build structured commands visually.
5. Smart Attachment Manager: detect duplicates, auto-compress, generate thumbnails.
6. Offline News & Knowledge Feed: local cached summaries of chosen sources.
7. Energy-aware Mode: pause background tasks on battery.
8. Multimodal Context: combine microphone + camera + screen input for richer commands (“Read the number on this page and email it”).
9. Time-Safe Scheduling: future or recurring tasks with dry-run previews.
10. Developer Rehearsal Mode: step-through execution with breakpoints.

### 15️⃣ Deployment & Maintenance
Packaged via PyInstaller (Windows) / Briefcase (cross-platform). Installer auto-downloads models (Vosk / Whisper) and checks microphone. Autoupdater with cryptographic signature verification. Logs rotate and compress automatically; telemetry is opt-in only. Config and models stored under `~/.sara_max/`.

## 🧩 Summary

Sara Max is:

> A modular, secure, offline-first, voice-controlled operating system that automates every digital task on a PC — from file management to web browsing, from coding to messaging — while protecting privacy, auditing every step, and growing through signed plugins and macros. She can hear, speak, see, plan, and act — all in Python.

## 📦 Dependencies

### Core
- `pydantic` - Data validation
- `keyring` - Secure credential storage
- `psutil` - System information

### Optional
- `pillow` - Image processing
- `pytesseract` - OCR
- `playwright` - Browser automation
- `openpyxl`, `python-docx`, `python-pptx` - Office automation
- `telethon` - Telegram integration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

MIT License - see LICENSE for details

## 🙏 Acknowledgments

- Built with Python 3.11+ type hints
- Designed for offline-first privacy
- Inspired by voice assistant systems and desktop automation tools

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-repo/sara-max/issues)
- **Documentation**: [Full Docs](docs/)
- **Discussions**: [GitHub Discussions](https://github.com/your-repo/sara-max/discussions)

---

**Sara AI Max** - Voice-driven desktop automation, your way. 🎤🤖
