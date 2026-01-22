# Security Policy

Sara AI Max implements a comprehensive security model to protect users and their data.

## Permission System

### Permission Levels

Sara AI Max uses a 4-level permission system:

| Level       | Description           | Examples                 | Confirmation Required |
| ----------- | --------------------- | ------------------------ | --------------------- |
| **OBSERVE** | Read-only, no changes | Time, date, system info  | No                    |
| **LOW**     | Minor system changes  | Volume, brightness       | No                    |
| **MEDIUM**  | File & app operations | Create files, open apps  | No (by default)       |
| **HIGH**    | Critical operations   | Shutdown, system changes | Yes (always)          |

### Permission Assignment

Every action is assigned a permission level in the Planner:

```python
Action(
    action_type=ActionType.SYSTEM_SHUTDOWN,
    permission_level=PermissionLevel.HIGH  # Requires confirmation
)
```

## Audit Logging

All actions are logged to `sara_audit.json`:

```json
{
  "timestamp": "2026-01-22T21:30:00",
  "action": "Open notepad",
  "permission_level": "medium",
  "approved": true,
  "result": "Success"
}
```

### Accessing Audit Logs

```python
from sara_core.security import SecurityManager

security = SecurityManager()
recent = security.get_recent_actions(count=10)

for entry in recent:
    print(f"{entry.timestamp}: {entry.action} - {entry.result}")
```

## Confirmations

High-risk actions require voice confirmation:

```
Sara: "This will shutdown your computer. Confirm?"
User: "Yes"
Sara: "Shutting down now..."
```

## Data Privacy

### What Data is Stored

- **Conversation History**: Last 50 interactions (in-memory)
- **Audit Log**: All actions with timestamps (local file)
- **Context Variables**: Session-specific data (in-memory)

### What is NOT Stored

- Voice recordings (deleted after processing)
- Passwords or sensitive credentials
- Personal information unless explicitly saved

### Data Location

- Audit log: `sara_audit.json` (local)
- Screenshots: `~/Pictures/Sara_Screenshots/`
- Configuration: `config.json` (local)

## Credential Management

### Secure Storage

Use Python's `keyring` for credentials:

```python
import keyring

# Store
keyring.set_password("sara_max", "email_password", "your_password")

# Retrieve
password = keyring.get_password("sara_max", "email_password")
```

### Never Hardcode

❌ **Bad**:

```python
password = "my_password_123"
```

✅ **Good**:

```python
password = keyring.get_password("sara_max", "service_name")
```

## Plugin Security

### Plugin Sandboxing

Plugins run with limited permissions:

- No network access by default
- Limited file system access
- Resource limits (CPU, memory)

### Plugin Validation

Before loading, plugins are:

1. **Signature Verified**: Check author signature
2. **Code Scanned**: Basic security scan
3. **Metadata Validated**: Check required fields
4. **Permissions Checked**: Verify requested permissions

### Trusted Plugins Only

Configure trusted plugin sources in `config.json`:

```json
{
  "plugins": {
    "trusted_sources": ["official_plugin_store", "verified_authors"],
    "allow_unsigned": false
  }
}
```

## Network Security

### API Keys

Store API keys securely:

```bash
# .env file (never commit!)
GEMINI_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
```

Load with:

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
```

### HTTPS Only

All network requests use HTTPS.

## Best Practices

### For Users

1. **Review Audit Logs**: Check `sara_audit.json` regularly
2. **Use Confirmations**: Don't disable high-risk confirmations
3. **Update Regularly**: Keep Sara AI Max updated
4. **Trust Plugins**: Only install plugins from trusted sources

### For Developers

1. **Validate Input**: Never trust user input
2. **Log Actions**: Use SecurityManager for all operations
3. **Handle Errors**: Catch and log exceptions
4. **Test Security**: Include security tests in test suite

## Reporting Security Issues

If you discover a security vulnerability:

1. **Do NOT** open a public issue
2. Email: security@saraai.example.com
3. Include:
   - Description of vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

We aim to respond within 48 hours.

## Compliance

Sara AI Max is designed to comply with:

- **GDPR**: Personal data protection
- **CCPA**: California Consumer Privacy Act
- **SOC 2**: Security controls

## Security Updates

We release security patches as needed. Enable auto-updates:

```json
{
  "auto_update": {
    "enabled": true,
    "check_interval": "daily"
  }
}
```

---

**Last Updated**: January 22, 2026  
**Version**: 1.0.0
