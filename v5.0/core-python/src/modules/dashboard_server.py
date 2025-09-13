"""
Dashboard Server Module
Provides WebSocket communication with the JavaScript dashboard
"""

import asyncio
import logging
import json
from typing import Optional, Dict, Any, Set
import websockets
from websockets.server import WebSocketServerProtocol

from config.settings import Settings


class DashboardServer:
    """WebSocket server for communicating with the dashboard"""
    
    def __init__(self, settings: Settings, orchestrator):
        self.settings = settings
        self.orchestrator = orchestrator
        self.logger = logging.getLogger(__name__)
        self.server = None
        self.clients: Set[WebSocketServerProtocol] = set()
        
    async def start(self):
        """Start the WebSocket server"""
        try:
            self.server = await websockets.serve(
                self._handle_client,
                self.settings.dashboard_host,
                8080  # WebSocket port from config
            )
            self.logger.info(f"✅ Dashboard WebSocket server started on {self.settings.dashboard_host}:8080")
        except Exception as e:
            self.logger.error(f"Failed to start dashboard server: {e}")
            raise
    
    async def shutdown(self):
        """Shutdown the WebSocket server"""
        if self.server:
            self.server.close()
            await self.server.wait_closed()
        self.logger.info("Dashboard server shut down")
    
    async def _handle_client(self, websocket: WebSocketServerProtocol, path: str):
        """Handle new WebSocket client connections"""
        self.clients.add(websocket)
        self.logger.info(f"Dashboard client connected from {websocket.remote_address}")
        
        try:
            # Send initial status
            await self._send_to_client(websocket, {
                "type": "status",
                "data": {
                    "connected": True,
                    "modules": await self._get_module_status()
                }
            })
            
            # Handle client messages
            async for message in websocket:
                try:
                    data = json.loads(message)
                    await self._handle_client_message(websocket, data)
                except json.JSONDecodeError:
                    await self._send_error(websocket, "Invalid JSON")
                except Exception as e:
                    self.logger.error(f"Error handling client message: {e}")
                    await self._send_error(websocket, str(e))
                    
        except websockets.exceptions.ConnectionClosed:
            self.logger.info("Dashboard client disconnected")
        except Exception as e:
            self.logger.error(f"Dashboard client error: {e}")
        finally:
            self.clients.discard(websocket)
    
    async def _handle_client_message(self, websocket: WebSocketServerProtocol, data: Dict[str, Any]):
        """Handle messages from dashboard clients"""
        message_type = data.get("type")
        
        if message_type == "get_status":
            await self._send_to_client(websocket, {
                "type": "status",
                "data": {
                    "modules": await self._get_module_status(),
                    "wake_word": self._get_wake_word_status()
                }
            })
        elif message_type == "send_command":
            command = data.get("command", "")
            if command:
                # Add command to orchestrator task queue
                await self.orchestrator.task_queue.put({
                    "type": "voice_command",
                    "text": command,
                    "source": "dashboard",
                    "timestamp": asyncio.get_event_loop().time()
                })
                await self._send_to_client(websocket, {
                    "type": "command_received",
                    "data": {"command": command}
                })
        else:
            await self._send_error(websocket, f"Unknown message type: {message_type}")
    
    async def _get_module_status(self) -> Dict[str, Any]:
        """Get status of all modules"""
        status = {}
        
        for module_name, module_status in self.orchestrator.module_status.items():
            status[module_name] = {
                "active": module_status.active,
                "last_health_check": module_status.last_health_check,
                "error_count": module_status.error_count
            }
        
        return status
    
    def _get_wake_word_status(self) -> Dict[str, Any]:
        """Get wake word detector status"""
        if hasattr(self.orchestrator, 'wake_word_detector'):
            return self.orchestrator.wake_word_detector.get_status()
        return {"listening": False, "active": False}
    
    async def _send_to_client(self, websocket: WebSocketServerProtocol, message: Dict[str, Any]):
        """Send message to a specific client"""
        try:
            await websocket.send(json.dumps(message))
        except Exception as e:
            self.logger.error(f"Error sending to client: {e}")
    
    async def _send_error(self, websocket: WebSocketServerProtocol, error: str):
        """Send error message to client"""
        await self._send_to_client(websocket, {
            "type": "error",
            "data": {"message": error}
        })
    
    async def broadcast(self, message: Dict[str, Any]):
        """Broadcast message to all connected clients"""
        if not self.clients:
            return
        
        message_json = json.dumps(message)
        disconnected = set()
        
        for client in self.clients:
            try:
                await client.send(message_json)
            except Exception as e:
                self.logger.debug(f"Failed to send to client: {e}")
                disconnected.add(client)
        
        # Remove disconnected clients
        self.clients -= disconnected
    
    async def broadcast_wake_word_event(self, wake_word: str, confidence: float):
        """Broadcast wake word detection to dashboard"""
        await self.broadcast({
            "type": "wake_word_detected",
            "data": {
                "wake_word": wake_word,
                "confidence": confidence,
                "timestamp": asyncio.get_event_loop().time()
            }
        })
    
    async def broadcast_command_result(self, command: str, result: str, success: bool):
        """Broadcast command execution result to dashboard"""
        await self.broadcast({
            "type": "command_result",
            "data": {
                "command": command,
                "result": result,
                "success": success,
                "timestamp": asyncio.get_event_loop().time()
            }
        })
    
    async def health_check(self) -> bool:
        """Check if dashboard server is healthy"""
        return self.server is not None and not self.server.is_serving()