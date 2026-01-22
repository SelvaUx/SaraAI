# Developer Guide

Learn how to extend and customize Sara AI Max.

## Architecture Overview

```
User Voice → Voice Engine → NLU → Planner → Security → Executor → Actions
                                      ↓
                                  Context Manager
```

## Adding New Intents

### 1. Define Intent Type

Edit `sara_core/nlu.py`:

```python
class IntentType(str, Enum):
    # ... existing intents ...
    MY_NEW_INTENT = "my_new_intent"
```

### 2. Add Pattern Matching

```python
def _build_patterns(self):
    return {
        # ... existing patterns ...
        IntentType.MY_NEW_INTENT: [
            r"do something with (.+)",
            r"perform (.+) action",
        ]
    }
```

### 3. Create Plan

Edit `sara_core/planner.py`:

```python
def create_plan(self, intent: Intent) -> Plan:
    # ... existing routing ...
    elif intent.intent_type == IntentType.MY_NEW_INTENT:
        return self._plan_my_action(intent.entities)

def _plan_my_action(self, entities):
    return Plan(
        actions=[
            Action(
                action_type=ActionType.MY_ACTION,
                parameters=entities,
                permission_level=PermissionLevel.MEDIUM
            )
        ],
        description="do my custom action"
    )
```

### 4. Implement Executor

Edit `sara_core/executor.py`:

```python
async def _execute_action(self, action: Action):
    # ... existing routing ...
    elif action.action_type == ActionType.MY_ACTION:
        return await self._handle_my_action(action)

async def _handle_my_action(self, action: Action):
    # Your implementation
    return ExecutionResult(success=True, message="Done!")
```

## Creating Custom Skills

Skills are reusable, modular components.

### Skill Template

```python
from skills.base_skill import BaseSkill, SkillMetadata, SkillResult

class WeatherSkill(BaseSkill):
    """Get weather information."""

    def get_metadata(self) -> SkillMetadata:
        return SkillMetadata(
            name="Weather",
            description="Get current weather",
            version="1.0.0",
            requires_internet=True
        )

    def validate_params(self, **kwargs) -> bool:
        return 'location' in kwargs

    async def execute(self, **kwargs) -> SkillResult:
        location = kwargs['location']

        # Fetch weather data
        weather = self._get_weather(location)

        return SkillResult(
            success=True,
            message=f"Weather in {location}: {weather}",
            data={'location': location, 'weather': weather}
        )

    def _get_weather(self, location):
        # Implementation
        return "Sunny, 72°F"
```

## Building Plugins

Plugins extend Sara AI Max with new capabilities.

### Plugin Structure

```
my_plugin.py:
- Inherits from Plugin
- Implements get_metadata()
- Implements execute()
- Optional: on_load(), on_unload()
```

### Example Plugin

```python
from plugins.sdk import Plugin, PluginMetadata

class TranslatorPlugin(Plugin):
    def get_metadata(self):
        return PluginMetadata(
            name="Translator",
            version="1.0.0",
            author="Your Name",
            description="Translate text between languages",
            requires=["googletrans"]
        )

    def execute(self, **kwargs):
        text = kwargs.get('text', '')
        target_lang = kwargs.get('lang', 'en')

        # Translation logic
        translated = self._translate(text, target_lang)

        return {
            'success': True,
            'original': text,
            'translated': translated
        }
```

## Testing

### Running Tests

```bash
# All tests
pytest tests/ -v

# Specific test file
pytest tests/test_core.py -v

# With coverage
pytest tests/ --cov=sara_core --cov-report=html
```

### Writing Tests

```python
import pytest
from sara_core.nlu import NLUEngine

class TestMyFeature:
    def test_something(self):
        # Arrange
        nlu = NLUEngine()

        # Act
        result = nlu.parse("test command")

        # Assert
        assert result.intent_type == IntentType.EXPECTED
```

## Best Practices

1. **Use Type Hints**: Always annotate function signatures
2. **Log Everything**: Use logger for debugging
3. **Handle Errors**: Try-except with specific error messages
4. **Write Tests**: Test new features before merging
5. **Document Code**: Add docstrings to functions and classes

## CLI Development

### Using saractl

```bash
# Start Sara
saractl start

# View logs
saractl logs --tail 50

# Manage plugins
saractl plugins list
saractl plugins load my_plugin

# Run tests
saractl test
```

## Debugging

### Enable Debug Logging

Set log level in `Sara_Max.py`:

```python
logging.basicConfig(level=logging.DEBUG)
```

### Check Audit Log

View `sara_audit.json` for action history.

### Inspect Context

Access conversation history via Context Manager.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Add tests
5. Submit PR

---

Happy coding! If you have questions, check the API documentation or open an issue.
