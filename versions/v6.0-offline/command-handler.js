const { shell, app } = require('electron');
const path = require('path');
const { exec } = require('child_process');
const fetch = require('node-fetch');

class CommandHandler {
    constructor(mainWindow) {
        this.mainWindow = mainWindow;
        this.jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "I told my computer I needed a break, and now it won't stop sending me Kit-Kats.",
            "Hardware: The part of a computer you can kick.",
            "Artificial intelligence is no match for natural stupidity.",
            "Why was the cell phone wearing glasses? It lost its contacts."
        ];
    }

    async processCommand(fullText) {
        console.log(`Raw Input: ${fullText}`);

        // 1. CLEAN INPUT
        let cleanText = fullText.toLowerCase().replace(/^hey sara\s*/, '').replace(/^sara\s*/, '').trim();
        let response = { text: "", action: null };

        // --- A. WAKE WORD ONLY ---
        if (cleanText === "" || cleanText === "hey" || cleanText === "hi") {
            const greetings = ["Online, Sir.", "Ready, sir.", "Listening.", "At your service."];
            response.text = greetings[Math.floor(Math.random() * greetings.length)];
            return response;
        }

        // --- B. WINDOW CONTROL ---
        if (cleanText.includes('minimize yourself') || cleanText === 'minimize') {
            response.text = "Minimizing interface Sir.";
            this.mainWindow.minimize();
            return response;
        }
        if (cleanText.includes('close yourself') || cleanText.includes('go to sleep') || cleanText === 'close') {
            response.text = "Closing SARA systems. Goodbye Sir Miss You.";
            setTimeout(() => this.mainWindow.hide(), 2000);
            return response;
        }

        // --- C. SEARCH GOOGLE ---
        if (cleanText.startsWith('search ')) {
            const query = cleanText.substring(7).trim();
            response.text = `Searching Google for ${query} Sir`;
            shell.openExternal(`https://google.com/search?q=${query}`);
            return response;
        }

        // --- D. OPEN WEBSITE ---
        if (cleanText.includes('.com') || cleanText.includes('.org') || cleanText.includes('.net')) {
            let url = cleanText.replace('open ', '').trim();
            if (!url.startsWith('http')) url = 'https://' + url;
            response.text = `Opening requested website Sir.`;
            shell.openExternal(url);
            return response;
        }
        if (cleanText.startsWith('open youtube')) {
            response.text = "Opening YouTube.";
            shell.openExternal('https://youtube.com');
            return response;
        }
        if (cleanText.startsWith('open google')) {
            response.text = "Opening Google.";
            shell.openExternal('https://google.com');
            return response;
        }

        // --- E. OPEN APP (Python Automation) ---
        if (cleanText.startsWith('open ')) {
            const appName = cleanText.substring(5).trim();
            response.text = `Accessing protocols. Opening ${appName}.`;
            this.runPythonAutomation('open', appName);
            return response;
        }

        // --- F. UTILITIES ---
        if (cleanText.includes('time')) {
            const now = new Date();
            response.text = `The time is ${now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}`;
            return response;
        }
        if (cleanText.includes('date')) {
            const now = new Date();
            response.text = `Today is ${now.toLocaleDateString(undefined, { weekday: 'long', month: 'long', day: 'numeric' })}`;
            return response;
        }
        if (cleanText.includes('joke')) {
            response.text = this.jokes[Math.floor(Math.random() * this.jokes.length)];
            return response;
        }

        // --- G. SCREENSHOT (Python Automation) ---
        if (cleanText.includes('screenshot')) {
            response.text = "Capturing screen now Sir.";
            this.runPythonAutomation('screenshot');
            return response;
        }

        // --- H. WHATSAPP MESSAGING ---
        // Pattern: "send [message] to [contact] in whatsapp"
        const whatsappMatch = cleanText.match(/send (.+) to (.+) in whatsapp/);
        if (whatsappMatch) {
            const message = whatsappMatch[1];
            const contact = whatsappMatch[2];
            response.text = `Sending message to ${contact} on WhatsApp.`;
            // Pass arguments as a single string, separated by a delimiter that is unlikely to be in the message
            // or handle it carefully in Python. Here we'll pass them as separate arguments.
            // We need to be careful about quoting in the shell command.
            this.runPythonAutomation('whatsapp', `"${contact}" "${message}"`);
            return response;
        }

        // --- I. WIKIPEDIA ---
        if (cleanText.startsWith('wikipedia ')) {
            const query = cleanText.substring(10).trim();
            try {
                const api = `https://en.wikipedia.org/api/rest_v1/page/summary/${encodeURIComponent(query)}`;
                const res = await fetch(api);
                const data = await res.json();

                if (data.extract) {
                    response.text = data.extract.split('.').slice(0, 2).join('.') + '.';
                } else {
                    response.text = `Opening Wikipedia article for ${query}.`;
                    shell.openExternal(`https://en.wikipedia.org/wiki/${query}`);
                }
            } catch (e) {
                response.text = "Network error. Unable to reach Wikipedia Sir.";
            }
            return response;
        }

        // --- I. UNKNOWN ---
        response.text = "I didn't catch that command, Sir.";
        return response;
    }

    runPythonAutomation(command, args = '') {
        const scriptPath = path.join(__dirname, 'automation.py');
        // Use 'python' assuming it's in PATH. If not, might need full path or 'py'.
        // Also quoting script path just in case.
        const cmd = `python "${scriptPath}" ${command} ${args}`;
        console.log(`Executing: ${cmd}`);

        exec(cmd, (error, stdout, stderr) => {
            if (error) {
                console.error(`exec error: ${error}`);
                return;
            }
            if (stderr) console.error(`stderr: ${stderr}`);
            console.log(`stdout: ${stdout}`);
        });
    }
}

module.exports = CommandHandler;
