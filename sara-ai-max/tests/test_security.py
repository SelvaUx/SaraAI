"""Test Security - Tests for security and audit system."""

import pytest
from sara_core.security import SecurityManager, PermissionLevel
from pathlib import Path
import json


class TestSecurityManager:
    """Test security manager."""
    
    def test_audit_log_file_creation(self, tmp_path):
        """Test audit log file is created."""
        audit_path = tmp_path / "test_audit.json"
        security = SecurityManager(str(audit_path))
        
        security.log_action("Test", PermissionLevel.LOW, True)
        
        assert audit_path.exists()
    
    def test_audit_log_persistence(self, tmp_path):
        """Test audit log persists across instances."""
        audit_path = tmp_path / "test_audit.json"
        
        # First instance
        security1 = SecurityManager(str(audit_path))
        security1.log_action("Action 1", PermissionLevel.LOW, True)
        
        # Second instance
        security2 = SecurityManager(str(audit_path))
        
        # Should load previous entry
        recent = security2.get_recent_actions(count=1)
        assert len(recent) == 1
        assert recent[0].action == "Action 1"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
