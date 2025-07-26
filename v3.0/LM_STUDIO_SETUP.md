# 🧠 LM Studio Integration Guide for Sara AI

This guide shows you how to integrate any local AI model from LM Studio with Sara AI for enhanced natural language understanding and conversations.

## 🚀 Quick Setup (5 Minutes)

> **📝 Note**: This guide is for **Full Mode** (`main.py`) only. 
> **Fast Mode** (`sara_fast.py`) uses rule-based responses for maximum speed and doesn't require AI models.

### Step 1: Download and Install LM Studio
1. **Download LM Studio**
   - Visit: https://lmstudio.ai/
   - Download for Windows
   - Install LM Studio

### Step 2: Download AI Models
You can use any of these popular models:

#### Recommended Models (by size/performance):

**🔥 Lightweight Models (4-8GB RAM)**
- `microsoft/DialoGPT-medium` (1.5GB)
- `TinyLlama/TinyLlama-1.1B-Chat-v1.0` (2.2GB)
- `microsoft/phi-2` (5.2GB)

**⚡ Balanced Models (8-16GB RAM)**
- `mistralai/Mistral-7B-Instruct-v0.1` (4.1GB)
- `microsoft/Phi-3-mini-4k-instruct` (7.6GB)
- `meta-llama/Llama-2-7b-chat-hf` (13.5GB)

**🚀 Powerful Models (16GB+ RAM)**
- `mistralai/Mixtral-8x7B-Instruct-v0.1` (26.4GB)
- `meta-llama/Llama-2-13b-chat-hf` (26GB)
- `codellama/CodeLlama-13b-Instruct-hf` (26GB)

### Step 3: Setup in LM Studio

1. **Open LM Studio**
2. **Go to "Discover" tab**
3. **Search for your chosen model** (e.g., "mistral-7b-instruct")
4. **Download the GGML/GGUF version** (these are optimized for local use)
5. **Wait for download to complete**

### Step 4: Start Local Server

1. **Go to "Local Server" tab in LM Studio**
2. **Load your downloaded model**
3. **Configure settings:**
   - Port: `1234` (default)
   - Context Length: `4096` (or higher)
   - Temperature: `0.7` (for balanced creativity)
4. **Click "Start Server"**
5. **Verify server is running** - you should see "Server running on localhost:1234"

### Step 5: Enable in Sara AI

1. **Edit `config.py`:**
   ```python
   # Enable AI features
   AI_SETTINGS = {
       'use_local_ai': True,        # Enable LM Studio integration
       'use_rule_based_only': False, # Use AI instead of just rules
       'lm_studio_url': 'http://localhost:1234/v1',
       'ai_timeout': 10.0,          # Increase timeout for AI responses
       'fallback_to_rules': True    # Fallback if AI fails
   }
   ```

2. **Run Sara AI:**
   ```bash
   # Full Mode with AI integration
   python main.py
   
   # Note: Fast Mode (sara_fast.py) doesn't use AI models
   # It's designed for speed and uses rule-based responses
   ```

## 🔧 Advanced Configuration

### Custom Model Configuration

Create a `models_config.json` file:

```json
{
  "models": {
    "mistral-7b": {
      "name": "Mistral 7B Instruct",
      "url": "http://localhost:1234/v1",
      "max_tokens": 4096,
      "temperature": 0.7,
      "system_prompt": "You are Sara, a helpful AI assistant. Be concise and direct."
    },
    "phi-3": {
      "name": "Microsoft Phi-3",
      "url": "http://localhost:1235/v1",
      "max_tokens": 2048,
      "temperature": 0.5,
      "system_prompt": "You are Sara, an AI assistant. Provide clear, helpful responses."
    }
  },
  "active_model": "mistral-7b"
}
```

### Performance Optimization

**For better performance, configure LM Studio:**

1. **GPU Settings:**
   - Enable GPU acceleration if you have NVIDIA GPU
   - Set GPU layers based on your VRAM

2. **CPU Settings:**
   - Set threads to your CPU core count
   - Enable CPU acceleration

3. **Memory Settings:**
   - Adjust context length based on available RAM
   - Enable memory mapping for large models

## 📋 Model Recommendations by Use Case

### 🎯 For Voice Assistant (Sara AI)
**Best: Mistral 7B Instruct**
- Excellent instruction following
- Good balance of speed/quality
- Works well with voice commands

**Alternative: Phi-3 Mini**
- Faster responses
- Lower memory usage
- Good for basic conversations

### 💻 For Code Generation
**Best: CodeLlama 7B/13B**
- Specialized for coding tasks
- Excellent code understanding
- Supports multiple languages

**Alternative: Mistral 7B**
- Good general coding ability
- Faster than CodeLlama
- Better for mixed tasks

### 🗣️ For Conversations
**Best: Llama-2 7B Chat**
- Excellent conversational ability
- Natural responses
- Good personality

**Alternative: Mixtral 8x7B** (if you have powerful hardware)
- Top-tier conversational AI
- Very intelligent responses
- Requires 16GB+ RAM

## 🔄 Multiple Model Setup

You can run multiple models simultaneously:

### Setup Multiple LM Studio Instances:

1. **First Instance (Port 1234):**
   - Load Mistral 7B for general tasks
   - Use for voice commands and chat

2. **Second Instance (Port 1235):**
   - Load CodeLlama for coding tasks
   - Use for code generation

3. **Configure Sara AI:**
   ```python
   # In config.py
   AI_SETTINGS = {
       'models': {
           'general': 'http://localhost:1234/v1',
           'coding': 'http://localhost:1235/v1'
       },
       'model_selection': 'auto'  # Auto-select based on command type
   }
   ```

## 🧪 Testing Your Setup

### Test 1: Basic Connection
```bash
# Test if LM Studio is responding
curl http://localhost:1234/v1/models
```

### Test 2: AI Response
```bash
# Run Sara AI and try:
python main.py

# Say: "Hey Sara, tell me about Python programming"
# Sara should give an AI-generated response
```

### Test 3: Performance Check
```bash
# Run performance test with AI enabled
python performance_test.py
```

## 🐛 Troubleshooting

### "LM Studio not connecting"
1. **Check if server is running:**
   - LM Studio should show "Server running on localhost:1234"
   - Try visiting http://localhost:1234 in browser

2. **Check firewall:**
   - Allow LM Studio through Windows Firewall
   - Temporarily disable antivirus if needed

3. **Check port conflicts:**
   - Make sure port 1234 isn't used by other apps
   - Try changing to port 1235 or 1236

### "AI responses are too slow"
1. **Reduce model size:**
   - Use Phi-3 Mini instead of Mistral 7B
   - Use TinyLlama for fastest responses

2. **Optimize LM Studio settings:**
   - Enable GPU acceleration
   - Reduce context length to 2048
   - Increase threads to match CPU cores

3. **Adjust Sara AI timeout:**
   ```python
   AI_SETTINGS = {
       'ai_timeout': 5.0,  # Reduce from 10.0
   }
   ```

### "Out of memory errors"
1. **Use smaller models:**
   - Phi-3 Mini (4GB) instead of Mistral 7B (8GB)
   - TinyLlama (2GB) for minimal systems

2. **Reduce context length:**
   - Set to 1024 or 2048 in LM Studio
   - This uses less RAM

3. **Close other applications:**
   - Free up RAM for the AI model

## 🎯 Model-Specific Instructions

### Mistral 7B Instruct
```python
# Optimal settings in LM Studio:
{
    "temperature": 0.7,
    "max_tokens": 150,
    "context_length": 4096,
    "system_prompt": "You are Sara, a helpful AI assistant. Be concise and direct in your responses."
}
```

### Microsoft Phi-3
```python
# Optimal settings in LM Studio:
{
    "temperature": 0.5,
    "max_tokens": 100,
    "context_length": 2048,
    "system_prompt": "You are Sara. Provide clear, helpful responses in 1-2 sentences."
}
```

### CodeLlama
```python
# Optimal settings for coding tasks:
{
    "temperature": 0.2,
    "max_tokens": 200,
    "context_length": 4096,
    "system_prompt": "You are Sara, an AI coding assistant. Provide code examples and explanations."
}
```

## 📈 Performance Expectations

| Model | RAM Usage | Response Time | Quality |
|-------|-----------|---------------|---------|
| TinyLlama 1B | 2-3GB | 1-2 seconds | Good |
| Phi-3 Mini | 4-6GB | 2-3 seconds | Very Good |
| Mistral 7B | 8-12GB | 3-5 seconds | Excellent |
| Llama-2 7B | 10-14GB | 4-6 seconds | Excellent |
| Mixtral 8x7B | 20-30GB | 8-15 seconds | Outstanding |

## 🔄 Switching Between Models

You can easily switch models in LM Studio:

1. **Stop current server**
2. **Load different model**
3. **Restart server**
4. **No changes needed in Sara AI** - it will automatically use the new model

## 🎨 Custom Prompts for Sara AI

Create specialized prompts for different scenarios:

```python
# In ai_engine.py, add custom prompts:
CUSTOM_PROMPTS = {
    'voice_command': "You are Sara, a voice assistant. Understand this command and respond briefly: ",
    'coding': "You are Sara, a coding assistant. Help with this programming request: ",
    'general': "You are Sara, a helpful AI assistant. Respond naturally to: ",
    'system': "You are Sara, a system assistant. Help with this computer task: "
}
```

## 🚀 Next Steps

1. **Start with Mistral 7B** - best balance of quality/performance
2. **Test with voice commands** - ensure low latency
3. **Experiment with different models** - find what works best for you
4. **Customize prompts** - make Sara respond the way you want
5. **Monitor performance** - use `performance_test.py` to optimize

---

> **🎉 Once set up, Sara AI will use your local AI model for natural language understanding, making conversations much more intelligent and context-aware!**
