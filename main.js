const { app, BrowserWindow, ipcMain } = require('electron');
require('electron-reload')(__dirname);
const path = require('path');

app.on('ready', () => {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
        nodeIntegration: true,
        contextIsolation: false
    },
    title:'Pokevent Tool',

    icon: path.join(__dirname, 'assets', 'icon.png'),
  });

  mainWindow.loadFile('index.html'); // Load your HTML file here

  ipcMain.on('form-submission', (event, FormData) => {
    console.log('Form Data: ', FormData);
  });
});


// npx electron main.js