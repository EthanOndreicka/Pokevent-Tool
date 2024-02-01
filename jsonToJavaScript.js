// This file doesn't actually do anything, it was just for testing converting
// python data back to JS using JSON

const fs = require('fs').promises;

fs.readFile('event_details.json', 'utf8')
    .then(data => {
        const eventDetails = JSON.parse(data);
        console.log('JS Title: ', eventDetails.title);
        console.log('JS Description: ', eventDetails.description);
    })
    .catch(err => {
        console.error('Error reading event details: ', err);
    });
