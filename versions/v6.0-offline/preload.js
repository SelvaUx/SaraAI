const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('saraAPI', {
    minimizeWindow: () => ipcRenderer.send('window-control', 'minimize'),
    closeWindow: () => ipcRenderer.send('window-control', 'close'),
    sendVoiceCommand: (text) => ipcRenderer.invoke('process-voice-command', text)
});