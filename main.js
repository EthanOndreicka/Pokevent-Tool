const { app, BrowserWindow } = require('electron');
require('electron-reload')(__dirname);
const path = require('path');

app.on('ready', () => {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    icon: path.join(__dirname, 'assets', 'icon.png'),
  });

  mainWindow.loadFile('index.html'); // Load your HTML file here
});


// npx electron main.js