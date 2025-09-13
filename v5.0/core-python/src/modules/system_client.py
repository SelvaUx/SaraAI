"""
System Control Client Module
Handles communication with the C# system control module
"""

import aiohttp
import logging
from typing import Optional, Dict, Any

from config.settings import Settings


class SystemControlClient:
    """Client for communicating with the C# system control module"""
    
    def __init__(self, settings: Settings):
        self.settings = settings
        self.logger = logging.getLogger(__name__)
        self.base_url = f"http://{settings.system_config.host}:{settings.system_config.port}"
        self.session: Optional[aiohttp.ClientSession] = None
        
    async def start(self):
        """Initialize the system control client"""
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.settings.system_config.timeout)
        )
        self.logger.info(f"System control client initialized - {self.base_url}")
        
        try:
            await self.health_check()
            self.logger.info("✅ System control module is responsive")
        except Exception as e:
            self.logger.warning(f"⚠️ System control module health check failed: {e}")
    
    async def shutdown(self):
        """Clean up the system control client"""
        if self.session:
            await self.session.close()
        self.logger.info("System control client shut down")
    
    async def health_check(self) -> bool:
        """Check if the system control module is healthy"""
        try:
            if not self.session:
                return False
                
            async with self.session.get(f"{self.base_url}/health") as response:
                return response.status == 200
        except Exception as e:
            self.logger.debug(f"System control health check failed: {e}")
            return False
    
    async def get_system_time(self) -> Optional[str]:
        """Get current system time"""
        try:
            if not self.session:
                return None
            
            async with self.session.get(f"{self.base_url}/api/system/time") as response:
                if response.status == 200:
                    result = await response.json()
                    return result.get("time")
                    
        except Exception as e:
            self.logger.error(f"Error getting system time: {e}")
            
        return None
    
    async def execute_command(self, command: str) -> Dict[str, Any]:
        """
        Execute a system command
        
        Args:
            command: Command to execute
            
        Returns:
            Command execution result
        """
        try:
            if not self.session:
                return {"success": False, "error": "No session"}
            
            command_data = {
                "command": command,
                "timeout": 10
            }
            
            async with self.session.post(
                f"{self.base_url}/api/system/execute",
                json=command_data
            ) as response:
                
                if response.status == 200:
                    result = await response.json()
                    self.logger.info(f"⚙️ System command executed: '{command}'")
                    return result
                else:
                    return {"success": False, "error": f"HTTP {response.status}"}
                    
        except Exception as e:
            self.logger.error(f"System command execution error: {e}")
            return {"success": False, "error": str(e)}
    
    async def get_system_info(self) -> Dict[str, Any]:
        """Get system information"""
        try:
            if not self.session:
                return {}
            
            async with self.session.get(f"{self.base_url}/api/system/info") as response:
                if response.status == 200:
                    return await response.json()
                    
        except Exception as e:
            self.logger.error(f"Error getting system info: {e}")
            
        return {}