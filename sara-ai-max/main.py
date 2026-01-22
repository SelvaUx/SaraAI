"""
Sara AI Max - Main Entry Point

A modular, secure, offline-first, voice-controlled desktop automation system.
"""

import asyncio
import logging
from pathlib import Path
from typing import Optional

from sara_core.voice_engine import VoiceEngine
from sara_core.nlu import NLUEngine
from sara_core.planner import Planner
from sara_core.executor import Executor
from sara_core.security import SecurityManager
from sara_core.context import ContextManager


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('sara_max.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class SaraMax:
    """Main Sara AI Max application controller."""
    
    def __init__(self):
        """Initialize Sara AI Max."""
        logger.info("Initializing Sara AI Max...")
        
        # Initialize core components
        self.context = ContextManager()
        self.security = SecurityManager()
        self.voice = VoiceEngine()
        self.nlu = NLUEngine()
        self.planner = Planner(self.security)
        self.executor = Executor(self.security, self.context)
        
        self.running = False
        
        logger.info("Sara AI Max initialized successfully!")
    
    async def start(self):
        """Start Sara AI Max main loop."""
        self.running = True
        logger.info("Sara AI Max is now running. Say 'Hey Sara' to activate.")
        
        # Speak welcome message
        self.voice.speak("Sara AI Max initialized. I'm ready to help.")
        
        try:
            while self.running:
                # Listen for wake word
                if await self.voice.listen_for_wake_word():
                    logger.info("Wake word detected!")
                    self.voice.speak("Yes, I'm listening.")
                    
                    # Get command
                    command_text = await self.voice.listen_for_command()
                    
                    if command_text:
                        await self.process_command(command_text)
                    
                # Small delay to prevent CPU overuse
                await asyncio.sleep(0.1)
                
        except KeyboardInterrupt:
            logger.info("Shutting down Sara AI Max...")
            self.voice.speak("Goodbye!")
        finally:
            await self.shutdown()
    
    async def process_command(self, command_text: str):
        """
        Process a voice command through the full pipeline.
        
        Args:
            command_text: The recognized command text
        """
        logger.info(f"Processing command: {command_text}")
        
        try:
            # Step 1: Natural Language Understanding
            intent = self.nlu.parse(command_text)
            logger.info(f"Parsed intent: {intent.intent_type}")
            
            # Step 2: Create execution plan
            plan = self.planner.create_plan(intent)
            logger.info(f"Created plan with {len(plan.actions)} actions")
            
            # Step 3: Check permissions and get confirmation if needed
            if plan.requires_confirmation:
                self.voice.speak(f"This will {plan.description}. Confirm?")
                confirmation = await self.voice.listen_for_command(timeout=5)
                
                if not confirmation or 'yes' not in confirmation.lower():
                    self.voice.speak("Action cancelled.")
                    logger.info("User cancelled action")
                    return
            
            # Step 4: Execute the plan
            self.voice.speak(plan.before_message or "Executing...")
            result = await self.executor.execute(plan)
            
            # Step 5: Provide feedback
            if result.success:
                self.voice.speak(result.message or "Done!")
                logger.info(f"Command completed successfully: {result.message}")
            else:
                self.voice.speak(f"Sorry, {result.error}")
                logger.error(f"Command failed: {result.error}")
                
        except Exception as e:
            error_msg = f"An error occurred: {str(e)}"
            logger.error(error_msg, exc_info=True)
            self.voice.speak("Sorry, something went wrong.")
    
    async def shutdown(self):
        """Clean shutdown of Sara AI Max."""
        self.running = False
        self.voice.cleanup()
        logger.info("Sara AI Max shut down successfully")


async def main():
    """Main entry point."""
    sara = SaraMax()
    await sara.start()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nShutdown complete.")
