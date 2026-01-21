
const { app, BrowserWindow, ipcMain, shell, Tray, Menu } = require('electron');
const path = require('path');
const CommandHandler = require('./command-handler');

// --- CONFIGURATION ---
let mainWindow;
let tray;
const APP_NAME = "SARA AI 6.0 [OFFLINE]";
const commandHandler = new CommandHandler(null);

// --- WINDOW MANAGEMENT ---
function createWindow() {
    mainWindow = new BrowserWindow({
        width: 450,
        height: 700,
        resizable: false,
        frame: false,
        transparent: true,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            contextIsolation: true,
            nodeIntegration: false,
            sandbox: false
        },
        icon: path.join(__dirname, 'icon.ico')
    });
    mainWindow.loadFile(path.join(__dirname, 'renderer/index.html'));

    // Update the command handler with the window instance
    commandHandler.mainWindow = mainWindow;
}

function createTray() {
    try {
        tray = new Tray(path.join(__dirname, 'icon.ico'));
        const contextMenu = Menu.buildFromTemplate([
            { label: 'Show Sara', click: () => mainWindow.show() },
            { label: 'Quit', click: () => app.quit() }
        ]);
        tray.setToolTip(APP_NAME);
        tray.setContextMenu(contextMenu);
    } catch (e) { }
}

// --- IPC COMMAND HANDLER ---
ipcMain.handle('process-voice-command', async (event, fullText) => {
    return await commandHandler.processCommand(fullText);
});

// --- LIFECYCLE ---
ipcMain.on('window-control', (e, act) => {
    if (act === 'minimize') mainWindow.minimize();
    if (act === 'close') mainWindow.hide();
});

app.whenReady().then(() => {
    createWindow();
    createTray();
});
app.on('window-all-closed', () => { if (process.platform !== 'darwin') app.quit(); });