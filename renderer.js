const { ipcRenderer } = require('electron');

document.getElementById('myForm').addEventListener('submit', (event) => {
    event.preventDefault();

    const name = document.getElementById('submit-link').value;

    // Handle the form data (e.g., send it to the main process)
    ipcRenderer.send('form-submission', { name });
});