"""
Send Message Skill - Send messages via various platforms.

Example skill for messaging functionality.
"""

import logging
from .base_skill import BaseSkill, SkillMetadata, SkillResult

logger = logging.getLogger(__name__)


class SendMessageSkill(BaseSkill):
    """Send messages via WhatsApp, Telegram, etc."""
    
    def get_metadata(self) -> SkillMetadata:
        """Get skill metadata."""
        return SkillMetadata(
            name="Send Message",
            description="Send messages via WhatsApp, Telegram, or Signal",
            version="1.0.0",
            requires_internet=True,
            requires_permissions=["messaging"]
        )
    
    def validate_params(self, **kwargs) -> bool:
        """Validate parameters."""
        required = ['platform', 'contact', 'message']
        return all(param in kwargs for param in required)
    
    async def execute(self, **kwargs) -> SkillResult:
        """
        Execute message sending.
        
        Args:
            platform: Messaging platform (whatsapp, telegram, signal)
            contact: Contact name or number
            message: Message to send
            
        Returns:
            Skill result
        """
        try:
            if not self.validate_params(**kwargs):
                return SkillResult(
                    success=False,
                    error="Missing required parameters: platform, contact, message"
                )
            
            platform = kwargs['platform']
            contact = kwargs['contact']
            message = kwargs['message']
            
            # Import messaging connector
            from connectors.messaging import MessagingConnector, MessagingPlatform
            
            connector = MessagingConnector()
            
            # Convert platform string to enum
            platform_enum = MessagingPlatform(platform.lower())
            
            # Send message
            success = await connector.send_message(platform_enum, contact, message)
            
            if success:
                return SkillResult(
                    success=True,
                    message=f"Message sent to {contact} via {platform}",
                    data={'platform': platform, 'contact': contact}
                )
            else:
                return SkillResult(
                    success=False,
                    error=f"Failed to send message via {platform}"
                )
            
        except Exception as e:
            logger.error(f"Error sending message: {e}")
            return SkillResult(success=False, error=str(e))
