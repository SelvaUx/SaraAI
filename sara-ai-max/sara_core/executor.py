"""
Executor - Executes action plans safely.

This module executes the actions created by the planner.
"""

import logging
import asyncio
from typing import Optional
from pydantic import BaseModel

from .planner import Plan, Action, ActionType
from .security import SecurityManager
from .context import ContextManager
from automation import app_controller, file_ops, system

logger = logging.getLogger(__name__)


class ExecutionResult(BaseModel):
    """Result of executing a plan."""
    
    success: bool
    message: Optional[str] = None
    error: Optional[str] = None
    data: dict = {}


class Executor:
    """Executes action plans safely."""
    
    def __init__(self, security: SecurityManager, context: ContextManager):
        """
        Initialize executor.
        
        Args:
            security: Security manager for permission checks and auditing
            context: Context manager for session state
        """
        self.security = security
        self.context = context
        logger.info("Executor initialized")
    
    async def execute(self, plan: Plan) -> ExecutionResult:
        """
        Execute a plan.
        
        Args:
            plan: The plan to execute
            
        Returns:
            ExecutionResult with success status and message
        """
        logger.info(f"Executing plan: {plan.description}")
        
        try:
            # Execute all actions in the plan
            for action in plan.actions:
                # Check permissions
                if not self.security.check_permission(
                    action.description,
                    action.permission_level
                ):
                    error_msg = f"Permission denied for: {action.description}"
                    logger.error(error_msg)
                    self.security.log_action(
                        action.description,
                        action.permission_level,
                        approved= False,
                        result="Permission denied"
                    )
                    return ExecutionResult(success=False, error=error_msg)
                
                # Execute the action
                result = await self._execute_action(action)
                
                # Log to audit trail
                self.security.log_action(
                    action.description,
                    action.permission_level,
                    approved=True,
                    result="Success" if result.success else result.error
                )
                
                # If any action fails, stop execution
                if not result.success:
                    return result
            
            # All actions succeeded
            return ExecutionResult(
                success=True,
                message=plan.success_message or "Successfully completed"
            )
            
        except Exception as e:
            error_msg = f"Error executing plan: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return ExecutionResult(success=False, error=error_msg)
    
    async def _execute_action(self, action: Action) -> ExecutionResult:
        """
        Execute a single action.
        
        Args:
            action: The action to execute
            
        Returns:
            ExecutionResult
        """
        logger.info(f"Executing action: {action.action_type}")
        
        try:
            # Route to appropriate handler
            if action.action_type == ActionType.SYSTEM_INFO:
                return await self._handle_system_info(action)
            elif action.action_type == ActionType.VOLUME_SET:
                return await self._handle_volume(action)
            elif action.action_type == ActionType.BRIGHTNESS_SET:
                return await self._handle_brightness(action)
            elif action.action_type == ActionType.APP_OPEN:
                return await self._handle_app_open(action)
            elif action.action_type == ActionType.APP_CLOSE:
                return await self._handle_app_close(action)
            elif action.action_type == ActionType.FOLDER_CREATE:
                return await self._handle_folder_create(action)
            elif action.action_type == ActionType.WEB_SEARCH:
                return await self._handle_web_search(action)
            elif action.action_type == ActionType.SYSTEM_SHUTDOWN:
                return await self._handle_shutdown(action)
            elif action.action_type == ActionType.SYSTEM_LOCK:
                return await self._handle_lock(action)
            elif action.action_type == ActionType.SPEAK:
                return await self._handle_speak(action)
            else:
                return ExecutionResult(
                    success=False,
                    error=f"Unknown action type: {action.action_type}"
                )
                
        except Exception as e:
            logger.error(f"Error executing action: {e}", exc_info=True)
            return ExecutionResult(success=False, error=str(e))
    
    async def _handle_system_info(self, action: Action) -> ExecutionResult:
        """Handle system information requests."""
        info_type = action.parameters.get('info_type', 'system')
        message = system.get_system_info(info_type)
        return ExecutionResult(success=True, message=message)
    
    async def _handle_volume(self, action: Action) -> ExecutionResult:
        """Handle volume control."""
        volume_action = action.parameters.get('action', 'increase')
        result = system.control_volume(volume_action)
        return ExecutionResult(success=result, message=f"Volume {volume_action}d")
    
    async def _handle_brightness(self, action: Action) -> ExecutionResult:
        """Handle brightness control."""
        brightness_action = action.parameters.get('action', 'increase')
        result = system.control_brightness(brightness_action)
        return ExecutionResult(success=result, message=f"Brightness {brightness_action}d")
    
    async def _handle_app_open(self, action: Action) -> ExecutionResult:
        """Handle opening an application."""
        app_name = action.parameters.get('app_name', '')
        result = app_controller.open_app(app_name)
        if result:
            return ExecutionResult(success=True, message=f"Opened {app_name}")
        else:
            return ExecutionResult(success=False, error=f"Could not open {app_name}")
    
    async def _handle_app_close(self, action: Action) -> ExecutionResult:
        """Handle closing an application."""
        app_name = action.parameters.get('app_name', '')
        result = app_controller.close_app(app_name)
        if result:
            return ExecutionResult(success=True, message=f"Closed {app_name}")
        else:
            return ExecutionResult(success=False, error=f"Could not close {app_name}")
    
    async def _handle_folder_create(self, action: Action) -> ExecutionResult:
        """Handle folder creation."""
        folder_name = action.parameters.get('folder_name', '')
        result = file_ops.create_folder(folder_name)
        if result:
            return ExecutionResult(success=True, message=f"Created folder: {folder_name}")
        else:
            return ExecutionResult(success=False, error=f"Could not create folder: {folder_name}")
    
    async def _handle_web_search(self, action: Action) -> ExecutionResult:
        """Handle web search."""
        query = action.parameters.get('query', '')
        result = system.web_search(query)
        if result:
            return ExecutionResult(success=True, message=f"Searching for: {query}")
        else:
            return ExecutionResult(success=False, error="Could not perform search")
    
    async def _handle_shutdown(self, action: Action) -> ExecutionResult:
        """Handle system shutdown."""
        system.shutdown()
        return ExecutionResult(success=True, message="Shutting down")
    
    async def _handle_lock(self, action: Action) -> ExecutionResult:
        """Handle screen lock."""
        system.lock_screen()
        return ExecutionResult(success=True, message="Screen locked")
    
    async def _handle_speak(self, action: Action) -> ExecutionResult:
        """Handle speaking text."""
        text = action.parameters.get('text', '')
        # This will be spoken by the voice engine in the main loop
        return ExecutionResult(success=True, message=text)
