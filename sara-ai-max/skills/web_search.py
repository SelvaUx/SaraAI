"""
Web Search Skill - Perform web searches.

Example skill demonstrating the skill framework.
"""

import logging
import webbrowser
from .base_skill import BaseSkill, SkillMetadata, SkillResult

logger = logging.getLogger(__name__)


class WebSearchSkill(BaseSkill):
    """Perform web searches."""
    
    def get_metadata(self) -> SkillMetadata:
        """Get skill metadata."""
        return SkillMetadata(
            name="Web Search",
            description="Search the web using Google",
            version="1.0.0",
            requires_internet=True
        )
    
    def validate_params(self, **kwargs) -> bool:
        """Validate parameters."""
        return 'query' in kwargs and kwargs['query']
    
    async def execute(self, **kwargs) -> SkillResult:
        """
        Execute web search.
        
        Args:
            query: Search query
            
        Returns:
            Skill result
        """
        try:
            if not self.validate_params(**kwargs):
                return SkillResult(
                    success=False,
                    error="Missing required parameter: query"
                )
            
            query = kwargs['query']
            search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            
            webbrowser.open(search_url)
            
            logger.info(f"Searched for: {query}")
            
            return SkillResult(
                success=True,
                message=f"Searching for: {query}",
                data={'query': query, 'url': search_url}
            )
            
        except Exception as e:
            logger.error(f"Error executing web search: {e}")
            return SkillResult(success=False, error=str(e))
