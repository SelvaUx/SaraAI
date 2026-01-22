"""
Security Manager - Permission system and audit logs.

This module handles all security and permission checks.
"""

import logging
import json
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class PermissionLevel(str, Enum):
    """Permission levels for actions."""
    
    OBSERVE = "observe"      # Read-only, no system changes
    LOW = "low"              # Minor changes (volume, etc.)
    MEDIUM = "medium"        # File operations, app control
    HIGH = "high"            # System shutdown, restart, etc.


class AuditEntry(BaseModel):
    """An entry in the audit log."""
    
    timestamp: str
    action: str
    permission_level: PermissionLevel
    approved: bool
    result: Optional[str] = None


class SecurityManager:
    """Manages permissions and audit logging."""
    
    def __init__(self, audit_log_path: str = "sara_audit.json"):
        """
        Initialize security manager.
        
        Args:
            audit_log_path: Path to audit log file
        """
        self.audit_log_path = Path(audit_log_path)
        self.audit_entries = []
        
        # Load existing audit log if it exists
        if self.audit_log_path.exists():
            try:
                with open(self.audit_log_path, 'r') as f:
                    data = json.load(f)
                    self.audit_entries = [AuditEntry(**entry) for entry in data]
            except Exception as e:
                logger.error(f"Error loading audit log: {e}")
        
        logger.info("Security manager initialized")
    
    def check_permission(self, action: str, level: PermissionLevel) -> bool:
        """
        Check if an action is permitted.
        
        Args:
            action: Description of the action
            level: Permission level required
            
        Returns:
            True if permitted, False otherwise
        """
        # In MVP, all actions are permitted
        # In production, implement fine-grained permission system
        
        logger.info(f"Permission check: {action} (level: {level})")
        
        # High-risk actions should always require explicit confirmation
        if level == PermissionLevel.HIGH:
            logger.warning(f"High-risk action requires confirmation: {action}")
            return True  # Will be confirmed in main loop
        
        return True
    
    def log_action(
        self, 
        action: str, 
        permission_level: PermissionLevel,
        approved: bool,
        result: Optional[str] = None
    ):
        """
        Log an action to the audit trail.
        
        Args:
            action: Description of the action
            permission_level: Permission level of the action
            approved: Whether the action was approved
            result: Result of the action (success/failure message)
        """
        entry = AuditEntry(
            timestamp=datetime.now().isoformat(),
            action=action,
            permission_level=permission_level,
            approved=approved,
            result=result
        )
        
        self.audit_entries.append(entry)
        logger.info(f"Audit log: {action} - Approved: {approved}")
        
        # Save to file
        self._save_audit_log()
    
    def _save_audit_log(self):
        """Save audit log to file."""
        try:
            with open(self.audit_log_path, 'w') as f:
                json.dump(
                    [entry.model_dump() for entry in self.audit_entries],
                    f,
                    indent=2
                )
        except Exception as e:
            logger.error(f"Error saving audit log: {e}")
    
    def get_recent_actions(self, count: int = 10) -> list:
        """
        Get recent audit entries.
        
        Args:
            count: Number of recent entries to return
            
        Returns:
            List of recent audit entries
        """
        return self.audit_entries[-count:]
