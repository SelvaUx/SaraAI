"""Test Core - Tests for core Sara AI Max modules."""

import pytest
import asyncio
from sara_core.nlu import NLUEngine, IntentType
from sara_core.context import ContextManager
from sara_core.security import SecurityManager, PermissionLevel


class TestNLU:
    """Test Natural Language Understanding."""
    
    def test_parse_time_intent(self):
        """Test parsing time query."""
        nlu = NLUEngine()
        intent = nlu.parse("what time is it?")
        
        assert intent.intent_type == IntentType.TIME
        assert intent.confidence > 0.5
    
    def test_parse_open_app_intent(self):
        """Test parsing app open command."""
        nlu = NLUEngine()
        intent = nlu.parse("open notepad")
        
        assert intent.intent_type == IntentType.OPEN_APP
        assert 'app_name' in intent.entities
        assert intent.entities['app_name'] == "notepad"
    
    def test_parse_create_folder_intent(self):
        """Test parsing folder creation."""
        nlu = NLUEngine()
        intent = nlu.parse("create a folder named TestFolder")
        
        assert intent.intent_type == IntentType.CREATE_FOLDER
        assert 'folder_name' in intent.entities
        assert intent.entities['folder_name'] == "TestFolder"
    
    def test_unknown_intent(self):
        """Test unknown command."""
        nlu = NLUEngine()
        intent = nlu.parse("xyz random gibberish abc")
        
        assert intent.intent_type == IntentType.UNKNOWN
        assert intent.confidence == 0.0


class TestContext:
    """Test Context Manager."""
    
    def test_add_user_message(self):
        """Test adding user message."""
        context = ContextManager()
        context.add_user_message("Hello Sara")
        
        history = context.get_recent_context(count=1)
        assert len(history) == 1
        assert history[0].role == "user"
        assert history[0].content == "Hello Sara"
    
    def test_set_get_variable(self):
        """Test context variables."""
        context = ContextManager()
        context.set_variable("test_key", "test_value")
        
        value = context.get_variable("test_key")
        assert value == "test_value"
    
    def test_clear_context(self):
        """Test clearing context."""
        context = ContextManager()
        context.add_user_message("Test")
        context.set_variable("key", "value")
        
        context.clear_context()
        
        assert len(context.history) == 0
        assert len(context.context_variables) == 0


class TestSecurity:
    """Test Security Manager."""
    
    def test_permission_check(self):
        """Test permission checking."""
        security = SecurityManager()
        
        # Low-level actions should be permitted
        allowed = security.check_permission("Test action", PermissionLevel.LOW)
        assert allowed is True
    
    def test_audit_logging(self):
        """Test audit log creation."""
        security = SecurityManager()
        
        security.log_action(
            "Test action",
            PermissionLevel.MEDIUM,
            approved=True,
            result="Success"
        )
        
        recent = security.get_recent_actions(count=1)
        assert len(recent) == 1
        assert recent[0].action == "Test action"
        assert recent[0].approved is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
