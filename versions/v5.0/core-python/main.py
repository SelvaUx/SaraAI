#!/usr/bin/env python3
"""
SaraAI 5.0 - Main Orchestrator
Entry point for the multi-language AI assistant
"""

import asyncio
import sys
import logging
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.core.orchestrator import SaraAIOrchestrator
from src.config.settings import load_settings
from src.utils.logger import setup_logging


async def main():
    """Main entry point for SaraAI"""
    print("🤖 Starting SaraAI 5.0 - Multi-Language AI Assistant")
    
    # Load configuration
    settings = load_settings()
    
    # Setup logging
    logger = setup_logging(settings.log_level)
    logger.info("SaraAI 5.0 initializing...")
    
    try:
        # Initialize the orchestrator
        orchestrator = SaraAIOrchestrator(settings)
        
        # Start all modules
        await orchestrator.start()
        
        logger.info("🎉 SaraAI 5.0 is now running!")
        
        # Show wake word status
        if settings.wake_word_enabled:
            wake_words_str = ", ".join([f"'{word}'" for word in settings.wake_words])
            print(f"✨ SaraAI is ready! Say {wake_words_str} to get my attention.")
            print(f"🎧 Wake word detection is active (sensitivity: {settings.wake_word_sensitivity})")
        else:
            print("✨ SaraAI is ready! Wake word detection is disabled.")
        
        print(f"🌐 Dashboard available at: http://localhost:{settings.dashboard_port}")
        print("💵 Press Ctrl+C to stop")
        
        # Keep running until interrupted
        await orchestrator.run_forever()
        
    except KeyboardInterrupt:
        logger.info("Received shutdown signal...")
        print("\n👋 Shutting down SaraAI...")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        print(f"❌ Error starting SaraAI: {e}")
    finally:
        if 'orchestrator' in locals():
            await orchestrator.shutdown()
        print("🔌 SaraAI has shut down gracefully.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")