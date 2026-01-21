"""
SaraAI Core Orchestrator
Main coordination system for all language modules
"""

import asyncio
import logging
from typing import Dict, Any, Optional
from dataclasses import dataclass

from config.settings import Settings
from modules.speech_client import SpeechToTextClient
from modules.tts_client import TextToSpeechClient
from modules.system_client import SystemControlClient
from modules.knowledge_client import KnowledgeClient
from modules.dashboard_server import DashboardServer
from core.command_processor import CommandProcessor
from core.ai_brain import AIBrain
from core.wake_word_detector import WakeWordDetector, WakeWordEvent


@dataclass
class ModuleStatus:
    """Status of each module"""
    name: str
    active: bool = False
    last_health_check: Optional[float] = None
    error_count: int = 0


class SaraAIOrchestrator:
    """Main orchestrator for coordinating all SaraAI modules"""
    
    def __init__(self, settings: Settings):
        self.settings = settings
        self.logger = logging.getLogger(__name__)
        self.running = False
        
        # Module clients
        self.speech_client: Optional[SpeechToTextClient] = None
        self.tts_client: Optional[TextToSpeechClient] = None
        self.system_client: Optional[SystemControlClient] = None
        self.knowledge_client: Optional[KnowledgeClient] = None
        self.dashboard_server: Optional[DashboardServer] = None
        
        # Core processing components
        self.command_processor: Optional[CommandProcessor] = None
        self.ai_brain: Optional[AIBrain] = None
        self.wake_word_detector: Optional[WakeWordDetector] = None
        
        # Module status tracking
        self.module_status: Dict[str, ModuleStatus] = {}
        
        # Task queue for async operations
        self.task_queue: asyncio.Queue = asyncio.Queue()
        
    async def start(self):
        """Initialize and start all modules"""
        self.logger.info("🚀 Starting SaraAI orchestrator...")
        
        try:
            # Initialize core components
            await self._initialize_core_components()
            
            # Start external module clients
            await self._start_module_clients()
            
            # Start dashboard server
            await self._start_dashboard_server()
            
            # Start background tasks
            await self._start_background_tasks()
            
            self.running = True
            self.logger.info("✅ All modules started successfully")
            
        except Exception as e:
            self.logger.error(f"❌ Failed to start orchestrator: {e}")
            await self.shutdown()
            raise
    
    async def _initialize_core_components(self):
        """Initialize the AI brain, command processor, and wake word detector"""
        self.logger.info("🧠 Initializing AI brain...")
        self.ai_brain = AIBrain(self.settings)
        
        self.logger.info("⚙️ Initializing command processor...")
        self.command_processor = CommandProcessor(self.settings, self)
        
        self.logger.info("👂 Initializing wake word detector...")
        self.wake_word_detector = WakeWordDetector(self.settings)
        self.wake_word_detector.set_wake_word_callback(self._handle_wake_word_detected)
        
    async def _start_module_clients(self):
        """Start all external module clients"""
        modules_to_start = [
            (\"speech\", SpeechToTextClient, \"🎙️ Starting speech recognition...\"),
            (\"tts\", TextToSpeechClient, \"🔊 Starting text-to-speech...\"),
            (\"system\", SystemControlClient, \"⚙️ Starting system control...\"),
            (\"knowledge\", KnowledgeClient, \"📚 Starting knowledge base...\")
        ]
        
        for name, client_class, message in modules_to_start:
            try:
                self.logger.info(message)
                client = client_class(self.settings)
                await client.start()
                
                # Store client reference
                setattr(self, f\"{name}_client\", client)
                
                # Track status
                self.module_status[name] = ModuleStatus(name=name, active=True)
                
            except Exception as e:
                self.logger.warning(f\"⚠️ Failed to start {name} module: {e}\")
                self.module_status[name] = ModuleStatus(name=name, active=False)
    
    async def _start_dashboard_server(self):
        """Start the web dashboard server"""
        try:
            self.logger.info(\"🌐 Starting dashboard server...\")
            self.dashboard_server = DashboardServer(self.settings, self)
            await self.dashboard_server.start()
            self.module_status[\"dashboard\"] = ModuleStatus(name=\"dashboard\", active=True)
        except Exception as e:
            self.logger.warning(f\"⚠️ Failed to start dashboard: {e}\")
            self.module_status[\"dashboard\"] = ModuleStatus(name=\"dashboard\", active=False)
    
    async def _start_background_tasks(self):
        \"\"\"Start background monitoring and processing tasks\"\"\"
        # Health check task
        asyncio.create_task(self._health_check_loop())
        
        # Task processing loop
        asyncio.create_task(self._process_task_queue())
        
        # Start wake word detection (if enabled and speech module is active)
        if (self.speech_client and self.module_status.get("speech", {}).active and 
            self.settings.wake_word_enabled):
            asyncio.create_task(self._wake_word_listening_loop())
        
        # Voice listening loop (fallback if wake words disabled)
        elif self.speech_client and self.module_status.get("speech", {}).active:
            asyncio.create_task(self._voice_listening_loop())
    
    async def _health_check_loop(self):
        \"\"\"Periodic health check of all modules\"\"\"
        while self.running:
            try:
                await self._perform_health_checks()
                await asyncio.sleep(30)  # Check every 30 seconds
            except Exception as e:
                self.logger.error(f\"Health check error: {e}\")
    
    async def _perform_health_checks(self):
        \"\"\"Check the health of all modules\"\"\"
        for name, status in self.module_status.items():
            if status.active:
                try:
                    client = getattr(self, f\"{name}_client\", None) or getattr(self, f\"{name}_server\", None)
                    if client and hasattr(client, 'health_check'):
                        await client.health_check()
                        status.error_count = 0
                except Exception as e:
                    status.error_count += 1
                    self.logger.warning(f\"Health check failed for {name}: {e}\")
                    
                    if status.error_count > 3:
                        self.logger.error(f\"Module {name} appears to be down\")
                        status.active = False
    
    async def _process_task_queue(self):
        \"\"\"Process tasks from the async queue\"\"\"
        while self.running:
            try:
                task = await asyncio.wait_for(self.task_queue.get(), timeout=1.0)
                await self._handle_task(task)
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                self.logger.error(f\"Task processing error: {e}\")
    
    async def _handle_task(self, task: Dict[str, Any]):
        \"\"\"Handle a specific task\"\"\"
        task_type = task.get(\"type\")
        
        if task_type == \"voice_command\":
            await self._handle_voice_command(task[\"text\"])
        elif task_type == \"system_command\":
            await self._handle_system_command(task[\"command\"])
        elif task_type == \"knowledge_query\":
            await self._handle_knowledge_query(task[\"query\"])
        else:
            self.logger.warning(f\"Unknown task type: {task_type}\")
    
    async def _voice_listening_loop(self):
        \"\"\"Continuous voice listening and processing\"\"\"
        while self.running and self.speech_client:
            try:
                # Listen for voice input
                text = await self.speech_client.listen_for_speech()
                
                if text and text.strip():
                    self.logger.info(f\"🎙️ Heard: {text}\")
                    
                    # Add to task queue for processing
                    await self.task_queue.put({
                        "type": "voice_command",
                        "text": text,
                        "timestamp": asyncio.get_event_loop().time()
                    })
                    
            except Exception as e:
                self.logger.error(f\"Voice listening error: {e}\")
                await asyncio.sleep(1)  # Brief pause before retry
    
    async def _handle_voice_command(self, text: str):
        \"\"\"Process a voice command through the AI brain\"\"\"
        try:
            # Process through AI brain
            response = await self.ai_brain.process_command(text)
            
            # Execute the response
            await self.command_processor.execute_response(response)
            
            # Send to dashboard for display
            if self.dashboard_server:
                await self.dashboard_server.broadcast_message({
                    \"type\": \"voice_command\",
                    \"input\": text,
                    \"response\": response.dict()
                })
                
        except Exception as e:
            self.logger.error(f\"Error processing voice command: {e}\")
    
    async def _handle_system_command(self, command: str):
        \"\"\"Handle system control commands\"\"\"
        if self.system_client:
            try:
                result = await self.system_client.execute_command(command)
                self.logger.info(f\"System command result: {result}\")
            except Exception as e:
                self.logger.error(f\"System command error: {e}\")
    
    async def _handle_knowledge_query(self, query: str):
        \"\"\"Handle knowledge base queries\"\"\"
        if self.knowledge_client:
            try:
                result = await self.knowledge_client.search(query)
                self.logger.info(f\"Knowledge query result: {result}\")
                return result
            except Exception as e:
                self.logger.error(f\"Knowledge query error: {e}\")
        return None
    
    async def run_forever(self):
        \"\"\"Keep the orchestrator running\"\"\"
        while self.running:
            await asyncio.sleep(1)
    
    async def shutdown(self):
        \"\"\"Gracefully shutdown all modules\"\"\"
        self.logger.info(\"🔌 Shutting down SaraAI orchestrator...\")
        self.running = False
        
        # Shutdown all clients
        clients = [
            self.speech_client,
            self.tts_client, 
            self.system_client,
            self.knowledge_client,
            self.dashboard_server
        ]
        
        for client in clients:
            if client and hasattr(client, 'shutdown'):
                try:
                    await client.shutdown()
                except Exception as e:
                    self.logger.error(f\"Error shutting down client: {e}\")
        
        self.logger.info(\"✅ Orchestrator shutdown complete\")
    
    def get_status(self) -> Dict[str, Any]:
        \"\"\"Get current status of all modules\"\"\"
        return {
            "running": self.running,
            "modules": {name: {
                "active": status.active,
                "error_count": status.error_count
            } for name, status in self.module_status.items()}
        }
    
    async def _wake_word_listening_loop(self):
        """Continuous wake word detection loop"""
        if not self.wake_word_detector or not self.speech_client:
            return
        
        self.wake_word_detector.start_listening()
        
        while self.running and self.speech_client:
            try:
                # Listen for any speech
                text = await self.speech_client.listen_for_speech(timeout=2.0)
                
                if text and text.strip():
                    # Process through wake word detector
                    wake_word_event = await self.wake_word_detector.process_audio_text(text)
                    
                    # If wake word not detected, continue listening
                    if not wake_word_event:
                        continue
                    
                    # Wake word detected - now listen for command
                    await self._handle_wake_word_detected(wake_word_event)
                    
            except Exception as e:
                self.logger.debug(f"Wake word listening error: {e}")
                await asyncio.sleep(0.5)
    
    async def _handle_wake_word_detected(self, event: WakeWordEvent):
        """Handle wake word detection event"""
        self.logger.info(f"✨ Wake word detected: '{event.wake_word}' (confidence: {event.confidence:.2f})")
        
        # Notify dashboard
        if self.dashboard_server:
            await self.dashboard_server.broadcast_wake_word_event(
                event.wake_word, event.confidence
            )
        
        # Give audio feedback
        if self.tts_client:
            await self.tts_client.synthesize_speech("Yes?")
        
        # Listen for command after wake word
        if self.speech_client:
            try:
                self.logger.info("🎧 Listening for command...")
                command_text = await self.speech_client.start_command_listening(
                    timeout=self.settings.wake_word_timeout
                )
                
                if command_text:
                    self.logger.info(f"📝 Command received: '{command_text}'")
                    
                    # Process the command
                    await self.task_queue.put({
                        "type": "voice_command",
                        "text": command_text,
                        "wake_word": event.wake_word,
                        "timestamp": asyncio.get_event_loop().time()
                    })
                else:
                    self.logger.info("No command received after wake word")
                    if self.tts_client:
                        await self.tts_client.synthesize_speech("I didn't hear anything. Try again.")
                        
            except Exception as e:
                self.logger.error(f"Error listening for command after wake word: {e}")
