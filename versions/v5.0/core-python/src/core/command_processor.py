"""
Command Processor Module
Executes AI responses by routing them to appropriate modules
"""

import logging
from typing import Dict, Any
from core.ai_brain import AIResponse
from config.settings import Settings


class CommandProcessor:
    """Processes and executes AI responses by routing to appropriate modules"""
    
    def __init__(self, settings: Settings, orchestrator):
        self.settings = settings
        self.orchestrator = orchestrator
        self.logger = logging.getLogger(__name__)
    
    async def execute_response(self, response: AIResponse) -> bool:
        """
        Execute an AI response by routing to the appropriate module
        
        Args:
            response: AI response to execute
            
        Returns:
            True if executed successfully, False otherwise
        """
        try:
            self.logger.info(f"Executing {response.action} on {response.module} module")
            
            if response.module == "tts":
                return await self._execute_tts_action(response)
            elif response.module == "system":
                return await self._execute_system_action(response)
            elif response.module == "knowledge":
                return await self._execute_knowledge_action(response)
            else:
                self.logger.warning(f"Unknown module: {response.module}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error executing response: {e}")
            return False
    
    async def _execute_tts_action(self, response: AIResponse) -> bool:
        """Execute text-to-speech actions"""
        if not self.orchestrator.tts_client:
            self.logger.warning("TTS client not available")
            return False
        
        try:
            text = response.params.get("text", response.response_text)
            voice = response.params.get("voice", "default")
            
            success = await self.orchestrator.tts_client.synthesize_speech(text, voice)
            
            if success:
                self.logger.info(f"🔊 TTS: '{text[:50]}...'")
            
            return success
            
        except Exception as e:
            self.logger.error(f"TTS execution error: {e}")
            return False
    
    async def _execute_system_action(self, response: AIResponse) -> bool:
        """Execute system control actions"""
        if not self.orchestrator.system_client:
            self.logger.warning("System client not available")
            return False
        
        try:
            action = response.action
            
            if action == "get_time":
                time_result = await self.orchestrator.system_client.get_system_time()
                if time_result:
                    await self._speak_result(f"The current time is {time_result}")
                    return True
            
            elif action == "get_date":
                # Get system info which should include date
                info = await self.orchestrator.system_client.get_system_info()
                if info.get("date"):
                    await self._speak_result(f"Today is {info['date']}")
                    return True
            
            elif action == "launch_app":
                app = response.params.get("app", "application")
                result = await self.orchestrator.system_client.execute_command(f"start {app}")
                if result.get("success"):
                    await self._speak_result(f"Opening {app}")
                    return True
                else:
                    await self._speak_result(f"Sorry, I couldn't open {app}")
                    return False
            
            elif action in ["volume_up", "volume_down", "mute"]:
                # System volume control commands
                if action == "volume_up":
                    cmd = "nircmd.exe changesysvolume 6553"  # Increase by ~10%
                elif action == "volume_down":
                    cmd = "nircmd.exe changesysvolume -6553"  # Decrease by ~10%
                else:  # mute
                    cmd = "nircmd.exe mutesysvolume 2"  # Toggle mute
                
                result = await self.orchestrator.system_client.execute_command(cmd)
                if result.get("success"):
                    await self._speak_result("Done")
                    return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"System action execution error: {e}")
            return False
    
    async def _execute_knowledge_action(self, response: AIResponse) -> bool:
        """Execute knowledge base actions"""
        if not self.orchestrator.knowledge_client:
            self.logger.warning("Knowledge client not available")
            return False
        
        try:
            action = response.action
            
            if action == "search":
                query = response.params.get("query", "")
                if query:
                    results = await self.orchestrator.knowledge_client.search(query)
                    if results:
                        # Format and speak the first result
                        first_result = results[0]
                        result_text = first_result.get("content", "No content available")
                        await self._speak_result(f"Here's what I found: {result_text[:200]}...")
                        return True
                    else:
                        await self._speak_result("I couldn't find any information about that.")
                        return False
            
            elif action == "get_weather":
                # For now, provide a placeholder response
                await self._speak_result("I don't have access to current weather data yet, but you can check your weather app or ask me to search for weather information.")
                return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"Knowledge action execution error: {e}")
            return False
    
    async def _speak_result(self, text: str):
        """Helper method to speak a result using TTS"""
        if self.orchestrator.tts_client:
            await self.orchestrator.tts_client.synthesize_speech(text)
        
        # Also send to dashboard
        if self.orchestrator.dashboard_server:
            await self.orchestrator.dashboard_server.broadcast_command_result(
                "", text, True
            )