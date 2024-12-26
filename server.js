const express = require('express');
const fs = require('fs');
const app = express();

// Middleware to get IP address
app.use((req, res, next) => {
    req.clientIp = req.headers['x-forwarded-for'] || req.socket.remoteAddress;
    next();
});

// Route to handle IP logging
app.post('/log-ip', (req, res) => {
    const ip = req.clientIp;
    console.log(`Logging IP: ${ip}`); // For debugging
    fs.appendFile('ips.txt', ip + '\n', (err) => {
        if (err) {
            console.error(err);
            res.status(500).send('Error logging IP');
        } else {
            res.send('Your IP has been logged!');
        }
    });
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
