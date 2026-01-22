# Sara AI Max API Documentation

This document describes Sara AI Max's programming interfaces for integration and customization.

## Core Modules

### Voice Engine

```python
from sara_core.voice_engine import VoiceEngine

engine = VoiceEngine()

# Listen for wake word
if await engine.listen_for_wake_word():
    print("Wake word detected!")

# Get voice command
command = await engine.listen_for_command()

# Speak response
engine.speak("Hello, I'm Sara!")
```

### NLU Engine

```python
from sara_core.nlu import NLUEngine, IntentType

nlu = NLUEngine()

# Parse command
intent = nlu.parse("open notepad")

print(f"Intent: {intent.intent_type}")  # IntentType.OPEN_APP
print(f"Entities: {intent.entities}")    # {'app_name': 'notepad'}
```

### Planner

```python
from sara_core.planner import Planner
from sara_core.security import SecurityManager

security = SecurityManager()
planner = Planner(security)

# Create execution plan
plan = planner.create_plan(intent)

print(f"Actions: {len(plan.actions)}")
print(f"Requires confirmation: {plan.requires_confirmation}")
```

### Executor

```python
from sara_core.executor import Executor

executor = Executor(security, context)

# Execute plan
result = await executor.execute(plan)

if result.success:
    print(f"Success: {result.message}")
else:
    print(f"Error: {result.error}")
```

## Skills

### Creating a Custom Skill

```python
from skills.base_skill import BaseSkill, SkillMetadata, SkillResult

class MyCustomSkill(BaseSkill):
    def get_metadata(self) -> SkillMetadata:
        return SkillMetadata(
            name="My Custom Skill",
            description="Does something amazing",
            version="1.0.0"
        )

    def validate_params(self, **kwargs) -> bool:
        return 'param1' in kwargs

    async def execute(self, **kwargs) -> SkillResult:
        # Your logic here
        return SkillResult(
            success=True,
            message="Skill executed!"
        )
```

## Plugins

### Plugin Development

```python
from plugins.sdk import Plugin, PluginMetadata

class MyPlugin(Plugin):
    def get_metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="My Plugin",
            version="1.0.0",
            author="Your Name",
            description="Custom Sara AI Max plugin"
        )

    def execute(self, **kwargs):
        self.sdk.log("Plugin executed!")

        return {
            'success': True,
            'data': kwargs
        }
```

## Connectors

### Browser Automation

```python
from connectors.browser import browser_session

async with browser_session() as browser:
    await browser.navigate("https://example.com")
    await browser.click("button.submit")
    text = await browser.get_text("h1")
    print(text)
```

### Email

```python
from connectors.email import EmailConnector

email = EmailConnector()

await email.send_email(
    to="recipient@example.com",
    subject="Hello",
    body="Message body",
    from_email="your@email.com",
    password="app_password"
)
```

### Office Automation

```python
from connectors.office import OfficeAutomation

office = OfficeAutomation()

# Create Word document
office.create_word_document(
    "report.docx",
    content=["Paragraph 1", "Paragraph 2"]
)

# Create Excel spreadsheet
office.create_excel_spreadsheet(
    "data.xlsx",
    data=[
        ["Name", "Age"],
        ["Alice", 30],
        ["Bob", 25]
    ]
)
```

## Vision

### OCR

```python
from vision.ocr import OCREngine

ocr = OCREngine()

# Read text from image
text = ocr.read_image("screenshot.png")

# Read text from screen region
text = ocr.read_screen_region(x=100, y=100, width=300, height=200)
```

### Screenshots

```python
from vision.screenshot import ScreenshotCapture

capture = ScreenshotCapture()

# Full screen
path = capture.capture_full_screen()

# Region
path = capture.capture_region(x=0, y=0, width=800, height=600)
```

## Complete Example

```python
import asyncio
from sara_core import (
    VoiceEngine, NLUEngine, Planner,
    Executor, SecurityManager, ContextManager
)

async def main():
    # Initialize
    voice = VoiceEngine()
    nlu = NLUEngine()
    security = SecurityManager()
    context = ContextManager()
    planner = Planner(security)
    executor = Executor(security, context)

    # Process command
    if await voice.listen_for_wake_word():
        voice.speak("Yes, I'm listening.")

        command = await voice.listen_for_command()

        intent = nlu.parse(command)
        plan = planner.create_plan(intent)
        result = await executor.execute(plan)

        voice.speak(result.message)

asyncio.run(main())
```

For more examples, see the `examples/` directory.
