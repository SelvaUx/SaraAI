#!/usr/bin/env python3
"""
Sara AI Engine
Handles local LLM integration and natural language understanding
"""

import os
import re
import json
import logging
import requests
from typing import Dict, Tuple, List, Optional

# Try importing transformers for local models
try:
    from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False
    print("⚠️ Transformers not available, using rule-based NLU")

class AIEngine:
    def __init__(self):
        """Initialize AI engine with local model support"""
        self.logger = logging.getLogger('AIEngine')
        
        # LM Studio API settings (for local model serving)
        self.lm_studio_url = "http://localhost:1234/v1"
        self.lm_studio_available = False
        
        # Initialize local model if available
        self.local_model = None
        self.local_tokenizer = None
        
        # Command patterns for rule-based understanding
        self.command_patterns = self.load_command_patterns()
        
        # Check available AI backends
        self.check_available_backends()
        
        print("🧠 AI Engine initialized")
        
    def check_available_backends(self):
        """Check which AI backends are available"""
        # Check LM Studio
        try:
            response = requests.get(f"{self.lm_studio_url}/models", timeout=3)
            if response.status_code == 200:
                self.lm_studio_available = True
                # Get available models
                models_data = response.json()
                if 'data' in models_data and models_data['data']:
                    model_name = models_data['data'][0].get('id', 'Unknown')
                    print(f"✅ LM Studio connected - Model: {model_name}")
                else:
                    print("✅ LM Studio connected - No models loaded")
            else:
                print("⚠️ LM Studio not responding")
        except requests.exceptions.ConnectionError:
            print("⚠️ LM Studio not running (start server on localhost:1234)")
        except Exception as e:
            print(f"⚠️ LM Studio connection failed: {str(e)[:50]}")
            
        # Check local transformers
        if TRANSFORMERS_AVAILABLE:
            print("✅ Transformers library available")
        else:
            print("⚠️ Transformers library not available")
            
    def load_command_patterns(self) -> Dict:
        """Load command patterns for intent recognition"""
        return {
            "browser_search": [
                r"search (?:for |about )?(.+)",
                r"look up (.+)",
                r"find (.+)",
                r"google (.+)",
                r"browse (.+)",
                r"(.+) in browser"
            ],
            "open_app": [
                r"open (.+)",
                r"launch (.+)",
                r"start (.+)",
                r"run (.+)"
            ],
            "write_code": [
                r"write (.+) code",
                r"create (.+) (?:file|template)",
                r"generate (.+) code",
                r"code (?:for |a )?(.+)"
            ],
            "play_music": [
                r"play music",
                r"start music",
                r"turn on music",
                r"music on"
            ],
            "pause_music": [
                r"pause music",
                r"stop music",
                r"music off",
                r"turn off music"
            ],
            "system_shutdown": [
                r"shutdown",
                r"turn off",
                r"power off",
                r"shut down"
            ],
            "system_lock": [
                r"lock (?:the )?(?:screen|computer|pc)",
                r"lock system",
                r"secure (?:the )?(?:screen|computer)"
            ],
            "create_file": [
                r"create (?:a )?file (?:called |named )?(.+)",
                r"make (?:a )?file (?:called |named )?(.+)",
                r"new file (?:called |named )?(.+)"
            ],
            "create_folder": [
                r"create (?:a )?folder (?:called |named )?(.+)",
                r"make (?:a )?folder (?:called |named )?(.+)",
                r"new folder (?:called |named )?(.+)"
            ],
            "take_screenshot": [
                r"take (?:a )?screenshot",
                r"capture (?:the )?screen",
                r"screenshot"
            ],
            "volume_control": [
                r"volume (up|down|mute)",
                r"turn volume (up|down)",
                r"(increase|decrease) volume",
                r"(mute|unmute)"
            ],
            "uninstall_app": [
                r"uninstall (.+)",
                r"remove (.+)",
                r"delete (.+) (?:app|application|program)"
            ]
        }
        
    def understand_command(self, command: str) -> Tuple[str, Dict]:
        """
        Understand command intent and extract entities
        Returns: (intent, entities)
        """
        command = command.lower().strip()
        
        # Try AI-powered understanding first
        if self.lm_studio_available or self.local_model:
            try:
                return self.ai_understand_command(command)
            except Exception as e:
                self.logger.warning(f"AI understanding failed, falling back to rules: {e}")
        
        # Fallback to rule-based understanding
        return self.rule_based_understand(command)
        
    def ai_understand_command(self, command: str) -> Tuple[str, Dict]:
        """Use AI model to understand command intent"""
        # Create prompt for intent classification
        prompt = f"""
Classify the following voice command into one of these intents and extract entities:

Intents:
- browser_search: searching for information online
- open_app: opening applications or software
- write_code: writing or generating code
- play_music: playing music or audio
- pause_music: pausing or stopping music
- system_shutdown: shutting down the system
- system_lock: locking the screen or system
- create_file: creating new files
- create_folder: creating new folders
- take_screenshot: taking screenshots
- volume_control: controlling system volume
- uninstall_app: uninstalling applications
- general_chat: general conversation or questions

Command: "{command}"

Response format:
Intent: [intent_name]
Entities: {{"key": "value"}}
"""

        if self.lm_studio_available:
            response = self.query_lm_studio(prompt)
        else:
            response = self.query_local_model(prompt)
            
        return self.parse_ai_response(response, command)
        
    def query_lm_studio(self, prompt: str) -> str:
        """Query LM Studio API"""
        try:
            data = {
                "model": "local-model",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.1,
                "max_tokens": 150
            }
            
            response = requests.post(
                f"{self.lm_studio_url}/chat/completions",
                json=data,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content']
            else:
                raise Exception(f"LM Studio error: {response.status_code}")
                
        except Exception as e:
            self.logger.error(f"LM Studio query failed: {e}")
            raise
            
    def query_local_model(self, prompt: str) -> str:
        """Query local transformers model"""
        try:
            if not self.local_model:
                self.load_local_model()
                
            # Generate response
            inputs = self.local_tokenizer.encode(prompt, return_tensors="pt")
            outputs = self.local_model.generate(
                inputs,
                max_length=inputs.shape[1] + 100,
                temperature=0.1,
                pad_token_id=self.local_tokenizer.eos_token_id
            )
            
            response = self.local_tokenizer.decode(outputs[0], skip_special_tokens=True)
            return response[len(prompt):].strip()
            
        except Exception as e:
            self.logger.error(f"Local model query failed: {e}")
            raise
            
    def load_local_model(self):
        """Load local transformer model"""
        try:
            model_name = "microsoft/DialoGPT-medium"  # Lightweight model
            self.local_tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.local_model = AutoModelForCausalLM.from_pretrained(model_name)
            print("✅ Local model loaded")
            
        except Exception as e:
            self.logger.error(f"Failed to load local model: {e}")
            raise
            
    def parse_ai_response(self, response: str, original_command: str) -> Tuple[str, Dict]:
        """Parse AI model response to extract intent and entities"""
        try:
            # Extract intent
            intent_match = re.search(r"Intent:\s*([a-zA-Z_]+)", response)
            intent = intent_match.group(1) if intent_match else "general_chat"
            
            # Extract entities
            entities = {}
            entities_match = re.search(r"Entities:\s*({.*?})", response, re.DOTALL)
            if entities_match:
                try:
                    entities = json.loads(entities_match.group(1))
                except (json.JSONDecodeError, ValueError):
                    entities = {}
                    
            return intent, entities
            
        except Exception as e:
            self.logger.error(f"Error parsing AI response: {e}")
            return "general_chat", {}
            
    def rule_based_understand(self, command: str) -> Tuple[str, Dict]:
        """Rule-based command understanding as fallback"""
        entities = {}
        
        # Check each intent pattern
        for intent, patterns in self.command_patterns.items():
            for pattern in patterns:
                match = re.search(pattern, command, re.IGNORECASE)
                if match:
                    # Extract entities based on intent
                    if intent == "browser_search":
                        entities["query"] = match.group(1) if match.groups() else command
                    elif intent == "open_app":
                        entities["app_name"] = match.group(1) if match.groups() else command
                    elif intent == "write_code":
                        entities["code_type"] = match.group(1) if match.groups() else "html"
                    elif intent == "create_file":
                        entities["filename"] = match.group(1) if match.groups() else "new_file.txt"
                    elif intent == "create_folder":
                        entities["foldername"] = match.group(1) if match.groups() else "new_folder"
                    elif intent == "volume_control":
                        entities["action"] = match.group(1) if match.groups() else "up"
                    elif intent == "uninstall_app":
                        entities["app_name"] = match.group(1) if match.groups() else command
                        
                    return intent, entities
                    
        # Default to general chat if no pattern matches
        return "general_chat", {}
        
    def generate_response(self, query: str) -> str:
        """Generate conversational response"""
        try:
            if self.lm_studio_available:
                return self.generate_with_lm_studio(query)
            elif self.local_model:
                return self.generate_with_local_model(query)
            else:
                return self.generate_simple_response(query)
                
        except Exception as e:
            self.logger.error(f"Error generating response: {e}")
            return "I'm sorry, I couldn't process that request right now."
            
    def generate_with_lm_studio(self, query: str) -> str:
        """Generate response using LM Studio"""
        try:
            prompt = f"You are Sara, a helpful AI assistant. Respond naturally and concisely to: {query}"
            
            data = {
                "model": "local-model",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 100
            }
            
            response = requests.post(
                f"{self.lm_studio_url}/chat/completions",
                json=data,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content'].strip()
            else:
                raise Exception("LM Studio request failed")
                
        except Exception as e:
            self.logger.error(f"LM Studio generation failed: {e}")
            return self.generate_simple_response(query)
            
    def generate_with_local_model(self, query: str) -> str:
        """Generate response using local model"""
        try:
            prompt = f"Sara: {query}\nResponse:"
            
            inputs = self.local_tokenizer.encode(prompt, return_tensors="pt")
            outputs = self.local_model.generate(
                inputs,
                max_length=inputs.shape[1] + 50,
                temperature=0.7,
                pad_token_id=self.local_tokenizer.eos_token_id,
                do_sample=True
            )
            
            response = self.local_tokenizer.decode(outputs[0], skip_special_tokens=True)
            return response[len(prompt):].strip()
            
        except Exception as e:
            self.logger.error(f"Local model generation failed: {e}")
            return self.generate_simple_response(query)
            
    def generate_simple_response(self, query: str) -> str:
        """Generate simple rule-based response"""
        query = query.lower()
        
        # Simple response patterns
        if "hello" in query or "hi" in query:
            return "Hello! I'm Sara, your AI assistant. How can I help you today?"
        elif "how are you" in query:
            return "I'm doing well, thank you for asking! Ready to assist you."
        elif "what can you do" in query or "help" in query:
            return "I can help you search the web, open applications, play music, manage files, and much more. Just ask me!"
        elif "time" in query:
            from datetime import datetime
            return f"The current time is {datetime.now().strftime('%I:%M %p')}"
        elif "date" in query:
            from datetime import datetime
            return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}"
        else:
            return "I understand you're asking about something, but I'm not sure how to help with that specific request."

def main():
    """Test the AI engine"""
    engine = AIEngine()
    
    # Test commands
    test_commands = [
        "search for Python tutorials",
        "open notepad",
        "write HTML code",
        "play some music",
        "create a file called test.txt",
        "what time is it?"
    ]
    
    for command in test_commands:
        print(f"\nCommand: {command}")
        intent, entities = engine.understand_command(command)
        print(f"Intent: {intent}")
        print(f"Entities: {entities}")
        
        if intent == "general_chat":
            response = engine.generate_response(command)
            print(f"Response: {response}")

if __name__ == "__main__":
    main()
