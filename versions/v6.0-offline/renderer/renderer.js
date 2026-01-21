const statusText = document.getElementById('status');
const userTranscript = document.getElementById('user-transcript');
const coreStatus = document.getElementById('core-status');
const micBtn = document.getElementById('mic-btn');
const textModeBtn = document.getElementById('text-mode-btn');
const inputArea = document.getElementById('input-area');
const commandInput = document.getElementById('command-input');
const sendBtn = document.getElementById('send-btn');

document.getElementById('min-btn').addEventListener('click', () => window.saraAPI.minimizeWindow());
document.getElementById('close-btn').addEventListener('click', () => window.saraAPI.closeWindow());

// --- STATE ---
let isTextMode = false;
let isListening = false;
let isProcessing = false;

// --- MODES ---
function setMode(mode) {
    if (mode === 'text') {
        isTextMode = true;
        inputArea.style.display = 'flex';
        textModeBtn.classList.add('active');
        micBtn.classList.remove('active');
        stopListening();
        updateUI('TEXT MODE', 'blue');
        commandInput.focus();
    } else {
        isTextMode = false;
        inputArea.style.display = 'none';
        textModeBtn.classList.remove('active');
        micBtn.classList.add('active');
        updateUI('ONLINE', 'blue');
        startListening();
    }
}

textModeBtn.addEventListener('click', () => { isTextMode ? setMode('voice') : setMode('text'); });

micBtn.addEventListener('click', () => {
    if (isTextMode) setMode('voice');
    else isListening ? stopListening() : startListening();
});

// --- SEND LOGIC ---
sendBtn.addEventListener('click', () => {
    const text = commandInput.value;
    if (text) {
        userTranscript.textContent = `"${text}"`;
        processCommand(text);
        commandInput.value = '';
    }
});
commandInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') sendBtn.click(); });

// --- VOICE RECOGNITION ---
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
let recognition;

if (SpeechRecognition) {
    recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.lang = 'en-US';
    recognition.interimResults = false;

    recognition.onstart = () => { isListening = true; updateUI('LISTENING', 'blue'); };
    
    recognition.onend = () => { 
        isListening = false;
        if (!isProcessing && !isTextMode) startListening(); // Auto-restart (Always Listening)
        else if (isTextMode) updateUI('TEXT MODE', 'blue');
        else updateUI('PROCESSING', 'purple');
    };

    recognition.onresult = async (event) => {
        const transcript = event.results[0][0].transcript.trim();
        userTranscript.textContent = `"${transcript}"`;
        
        // Process EVERYTHING heard. 
        // Logic in main.js handles if it's a valid command or just noise.
        await processCommand(transcript);
    };
    
    startListening();
} else {
    statusText.textContent = "NO VOICE API";
}

function startListening() { try { if(!isListening && !isTextMode) recognition.start(); } catch (e) {} }
function stopListening() { try { recognition.stop(); } catch(e) {} }

// --- CORE PROCESSING ---
async function processCommand(text) {
    isProcessing = true;
    updateUI('PROCESSING', 'purple');
    
    try {
        const response = await window.saraAPI.sendVoiceCommand(text);
        
        // ALWAYS SPEAK THE RESPONSE
        if (response.text) {
            userTranscript.textContent = `SARA: ${response.text}`;
            speak(response.text);
        }
    } catch (error) {
        speak("System error.");
    } finally {
        isProcessing = false;
        // Don't restart here, onend handles it
    }
}

function speak(text) {
    updateUI('SPEAKING', 'cyan');
    const utterance = new SpeechSynthesisUtterance(text);
    const voices = window.speechSynthesis.getVoices();
    // Try to get a specific female voice, or fallback to default
    const saraVoice = voices.find(v => v.name.includes('Zira') || v.name.includes('Google US English') || v.name.includes('Female'));
    if (saraVoice) utterance.voice = saraVoice;
    
    utterance.pitch = 1.0;
    utterance.rate = 1.0;

    utterance.onend = () => { 
        updateUI(isTextMode ? 'TEXT MODE' : 'ONLINE', 'blue');
        if (!isTextMode) startListening(); // Ensure listening resumes after speaking
    };
    
    window.speechSynthesis.speak(utterance);
}

function updateUI(status, color) {
    statusText.textContent = status;
    statusText.style.color = color === 'blue' ? '#00f7ff' : (color === 'purple' ? '#b642f5' : '#00f7ff');
    
    if (status === 'SPEAKING' || status === 'PROCESSING') {
        coreStatus.classList.add('pulsing');
        coreStatus.style.boxShadow = `0 0 30px ${color === 'blue' ? '#00f7ff' : '#b642f5'}`;
    } else {
        coreStatus.classList.remove('pulsing');
        coreStatus.style.boxShadow = "0 0 15px #00f7ff";
    }
}