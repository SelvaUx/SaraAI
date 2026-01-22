"""
Planner - Converts intents into executable action plans.

This module creates safe, structured execution plans from user intents.
"""

import logging
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel

from .nlu import Intent, IntentType
from .security import SecurityManager, PermissionLevel

logger = logging.getLogger(__name__)


class ActionType(str, Enum):
    """Types of actions Sara can execute."""
    
    # System actions
    SYSTEM_INFO = "system_info"
    VOLUME_SET = "volume_set"
    BRIGHTNESS_SET = "brightness_set"
    SYSTEM_SHUTDOWN = "system_shutdown"
    SYSTEM_RESTART = "system_restart"
    SYSTEM_LOCK = "system_lock"
    
    # Application actions
    APP_OPEN = "app_open"
    APP_CLOSE = "app_close"
    APP_SWITCH = "app_switch"
    
    # File actions
    FILE_CREATE = "file_create"
    FILE_DELETE = "file_delete"
    FOLDER_CREATE = "folder_create"
    FOLDER_DELETE = "folder_delete"
    FILE_SEARCH = "file_search"
    
    # Utility actions
    SPEAK = "speak"
    WEB_SEARCH = "web_search"


class Action(BaseModel):
    """A single executable action."""
    
    action_type: ActionType
    parameters: dict = {}
    permission_level: PermissionLevel = PermissionLevel.LOW
    description: str = ""


class Plan(BaseModel):
    """A structured execution plan."""
    
    actions: List[Action]
    description: str
    requires_confirmation: bool = False
    before_message: Optional[str] = None
    success_message: Optional[str] = None


class Planner:
    """Creates execution plans from intents."""
    
    def __init__(self, security: SecurityManager):
        """
        Initialize planner.
        
        Args:
            security: Security manager for permission checks
        """
        self.security = security
        logger.info("Planner initialized")
    
    def create_plan(self, intent: Intent) -> Plan:
        """
        Create an execution plan from an intent.
        
        Args:
            intent: Parsed user intent
            
        Returns:
            Execution plan
        """
        logger.info(f"Creating plan for intent: {intent.intent_type}")
        
        # Route to appropriate plan creator
        if intent.intent_type == IntentType.TIME:
            return self._plan_time()
        elif intent.intent_type == IntentType.DATE:
            return self._plan_date()
        elif intent.intent_type == IntentType.OPEN_APP:
            return self._plan_open_app(intent.entities.get('app_name', ''))
        elif intent.intent_type == IntentType.CLOSE_APP:
            return self._plan_close_app(intent.entities.get('app_name', ''))
        elif intent.intent_type == IntentType.VOLUME_CONTROL:
            return self._plan_volume(intent.entities.get('action', 'increase'))
        elif intent.intent_type == IntentType.BRIGHTNESS_CONTROL:
            return self._plan_brightness(intent.entities.get('action', 'increase'))
        elif intent.intent_type == IntentType.CREATE_FOLDER:
            return self._plan_create_folder(intent.entities.get('folder_name', ''))
        elif intent.intent_type == IntentType.SEARCH_WEB:
            return self._plan_web_search(intent.entities.get('query', ''))
        elif intent.intent_type == IntentType.SYSTEM_INFO:
            return self._plan_system_info()
        elif intent.intent_type == IntentType.SHUTDOWN:
            return self._plan_shutdown()
        elif intent.intent_type == IntentType.LOCK:
            return self._plan_lock()
        elif intent.intent_type == IntentType.JOKE:
            return self._plan_joke()
        else:
            return self._plan_unknown(intent.raw_text)
    
    def _plan_time(self) -> Plan:
        """Plan for telling the time."""
        return Plan(
            actions=[
                Action(
                    action_type=ActionType.SYSTEM_INFO,
                    parameters={'info_type': 'time'},
                    permission_level=PermissionLevel.OBSERVE,
                    description="Get current time"
                )
            ],
            description="tell you the current time",
            requires_confirmation=False
        )
    
    def _plan_date(self) -> Plan:
        """Plan for telling the date."""
        return Plan(
            actions=[
                Action(
                    action_type=ActionType.SYSTEM_INFO,
                    parameters={'info_type': 'date'},
                    permission_level=PermissionLevel.OBSERVE,
                    description="Get current date"
                )
            ],
            description="tell you the current date",
            requires_confirmation=False
        )
    
    def _plan_open_app(self, app_name: str) -> Plan:
        """Plan for opening an application."""
        return Plan(
            actions=[
                Action(
                    action_type=ActionType.APP_OPEN,
                    parameters={'app_name': app_name},
                    permission_level=PermissionLevel.MEDIUM,
                    description=f"Open {app_name}"
                )
            ],
            description=f"open {app_name}",
            requires_confirmation=False,
            before_message=f"Opening {app_name}"
        )
    
    def _plan_close_app(self, app_name: str) -> Plan:
        """Plan for closing an application."""
        return Plan(
            actions=[
                Action(
                    action_type=ActionType.APP_CLOSE,
                    parameters={'app_name': app_name},
                    permission_level=PermissionLevel.MEDIUM,
                    description=f"Close {app_name}"
                )
            ],
            description=f"close {app_name}",
            requires_confirmation=False,
            before_message=f"Closing {app_name}"
        )
    
    def _plan_volume(self, action: str) -> Plan:
        """Plan for volume control."""
        return Plan(
            actions=[
                Action(
                    action_type=ActionType.VOLUME_SET,
                    parameters={'action': action},
                    permission_level=PermissionLevel.LOW,
                    description=f"{action.capitalize()} volume"
                )
            ],
            description=f"{action} the volume",
            requires_confirmation=False
        )
    
    def _plan_brightness(self, action: str) -> Plan:
        """Plan for brightness control."""
        return Plan(
            actions=[
                Action(
                    action_type=ActionType.BRIGHTNESS_SET,
                    parameters={'action': action},
                    permission_level=PermissionLevel.LOW,
                    description=f"{action.capitalize()} brightness"
                )
            ],
            description=f"{action} the brightness",
            requires_confirmation=False
        )
    
    def _plan_create_folder(self, folder_name: str) -> Plan:
        """Plan for creating a folder."""
        return Plan(
            actions=[
                Action(
                    action_type=ActionType.FOLDER_CREATE,
                    parameters={'folder_name': folder_name},
                    permission_level=PermissionLevel.MEDIUM,
                    description=f"Create folder '{folder_name}'"
                )
            ],
            description=f"create a folder named {folder_name}",
            requires_confirmation=False,
            success_message=f"Folder {folder_name} created successfully"
        )
    
    def _plan_web_search(self, query: str) -> Plan:
        """Plan for web search."""
        return Plan(
            actions=[
                Action(
                    action_type=ActionType.WEB_SEARCH,
                    parameters={'query': query},
                    permission_level=PermissionLevel.LOW,
                    description=f"Search web for '{query}'"
                )
            ],
            description=f"search for {query}",
            requires_confirmation=False,
            before_message=f"Searching for {query}"
        )
   
    def _plan_system_info(self) -> Plan:
        """Plan for system information."""
        return Plan(
            actions=[
                Action(
                    action_type=ActionType.SYSTEM_INFO,
                    parameters={'info_type': 'system'},
                    permission_level=PermissionLevel.OBSERVE,
                    description="Get system information"
                )
            ],
            description="get system information",
            requires_confirmation=False
        )
    
    def _plan_shutdown(self) -> Plan:
        """Plan for system shutdown."""
        return Plan(
            actions=[
                Action(
                    action_type=ActionType.SYSTEM_SHUTDOWN,
                    parameters={},
                    permission_level=PermissionLevel.HIGH,
                    description="Shutdown computer"
                )
            ],
            description="shutdown your computer",
            requires_confirmation=True,  # High risk
            before_message="Shutting down now"
        )
    
    def _plan_lock(self) -> Plan:
        """Plan for locking the screen."""
        return Plan(
            actions=[
                Action(
                    action_type=ActionType.SYSTEM_LOCK,
                    parameters={},
                    permission_level=PermissionLevel.MEDIUM,
                    description="Lock screen"
                )
            ],
            description="lock your screen",
            requires_confirmation=False,
            before_message="Locking screen"
        )
    
    def _plan_joke(self) -> Plan:
        """Plan for telling a joke."""
        return Plan(
            actions=[
                Action(
                    action_type=ActionType.SPEAK,
                    parameters={'text': 'Why did the programmer quit his job? Because he didnt get arrays!'},
                    permission_level=PermissionLevel.OBSERVE,
                    description="Tell a joke"
                )
            ],
            description="tell you a joke",
            requires_confirmation=False
        )
    
    def _plan_unknown(self, text: str) -> Plan:
        """Plan for unknown intent."""
        return Plan(
            actions=[
                Action(
                    action_type=ActionType.SPEAK,
                    parameters={'text': f"I'm not sure how to help with: {text}"},
                    permission_level=PermissionLevel.OBSERVE,
                    description="Respond to unknown command"
                )
            ],
            description="respond that I don't understand",
            requires_confirmation=False
        )
