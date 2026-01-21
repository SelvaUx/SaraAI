"""
Knowledge Base Client Module
Handles communication with the Rust knowledge module
"""

import aiohttp
import logging
from typing import Optional, Dict, Any, List

from config.settings import Settings


class KnowledgeClient:
    """Client for communicating with the Rust knowledge module"""
    
    def __init__(self, settings: Settings):
        self.settings = settings
        self.logger = logging.getLogger(__name__)
        self.base_url = f"http://{settings.knowledge_config.host}:{settings.knowledge_config.port}"
        self.session: Optional[aiohttp.ClientSession] = None
        
    async def start(self):
        """Initialize the knowledge client"""
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.settings.knowledge_config.timeout)
        )
        self.logger.info(f"Knowledge client initialized - {self.base_url}")
        
        try:
            await self.health_check()
            self.logger.info("✅ Knowledge module is responsive")
        except Exception as e:
            self.logger.warning(f"⚠️ Knowledge module health check failed: {e}")
    
    async def shutdown(self):
        """Clean up the knowledge client"""
        if self.session:
            await self.session.close()
        self.logger.info("Knowledge client shut down")
    
    async def health_check(self) -> bool:
        """Check if the knowledge module is healthy"""
        try:
            if not self.session:
                return False
                
            async with self.session.get(f"{self.base_url}/health") as response:
                return response.status == 200
        except Exception as e:
            self.logger.debug(f"Knowledge health check failed: {e}")
            return False
    
    async def search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Search the knowledge base
        
        Args:
            query: Search query
            limit: Maximum number of results
            
        Returns:
            List of search results
        """
        try:
            if not self.session:
                return []
            
            search_params = {
                "q": query,
                "limit": limit
            }
            
            async with self.session.get(
                f"{self.base_url}/api/search",
                params=search_params
            ) as response:
                
                if response.status == 200:
                    result = await response.json()
                    results = result.get("results", [])
                    self.logger.info(f"📚 Knowledge search: '{query}' - {len(results)} results")
                    return results
                else:
                    self.logger.error(f"Knowledge search failed: {response.status}")
                    return []
                    
        except Exception as e:
            self.logger.error(f"Knowledge search error: {e}")
            return []