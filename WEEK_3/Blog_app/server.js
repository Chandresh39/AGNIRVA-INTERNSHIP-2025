// Import necessary modules
const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");

// Create the Express app
const app = express();

// Enable CORS to allow front-end access
app.use(cors());

// Parse incoming JSON data
app.use(bodyParser.json());

// In-memory storage for blog posts
let posts = [];

// Route to fetch all posts
app.get("/posts", (req, res) => {
    res.json(posts);
});

// Route to create a new post
app.post("/posts", (req, res) => {
    const { title, content } = req.body; // Extract title and content from the request
    const id = posts.length + 1; // Assign a unique ID to the post
    posts.push({ id, title, content }); // Add the post to the storage
    res.status(201).json({ message: "Post created successfully" }); // Respond with success
});

// Route to delete a post by ID
app.delete("/posts/:id", (req, res) => {
    const id = parseInt(req.params.id); // Extract the ID from the route parameter
    posts = posts.filter((post) => post.id !== id); // Remove the post with the given ID
    res.json({ message: "Post deleted successfully" }); // Respond with success
});

// Start the server on port 5000
const PORT = 5000;
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));