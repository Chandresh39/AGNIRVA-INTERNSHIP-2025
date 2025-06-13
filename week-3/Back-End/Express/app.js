const express = require("express");
const app = express();

// Define a route
app.get("/", (req, res) => {
    res.send("Hello, World!");
});

// Start the server
const PORT = 4043;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});



// Run for this code: node app.js

// how to make json code: npm init
