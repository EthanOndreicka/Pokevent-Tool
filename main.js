const { app, BrowserWindow, ipcMain } = require('electron');
const { spawn } = require('child_process');
require('electron-reload')(__dirname);
const path = require('path');

app.on('ready', () => {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 765,
    resizeable: false,
    webPreferences: {
        nodeIntegration: true,
        contextIsolation: false
    },
    title: 'Pokevent Tool',
    icon: path.join(__dirname, 'assets', 'icon.png'),
  });

  mainWindow.on('will-resize', (event, newBounds) => {
    event.preventDefault();
  })
  mainWindow.loadFile('index.html'); // Load your HTML file here

  ipcMain.on('form-submission', (event, FormData) => {
    console.log('Form Data: ', FormData);

    // Convert the form data to JSON string
    const formDataJson = JSON.stringify(FormData);

    // Execute the Python script with the form data
    const pythonProcess = spawn('python3', ['process_data.py', formDataJson]);

    // Handle the output of the Python script
    pythonProcess.stdout.on('data', (data) => {
      console.log(`Python script output: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
      console.error(`Error in Python script: ${data}`);
    });
  });
});


// npx electron main.js