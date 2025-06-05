# Import necessary modules
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)
CORS(app)

# In-memory storage for blog posts
posts = []

# Route to fetch all posts
@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify(posts)

# Route to create a new post
@app.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()  # Parse incoming JSON data
    post = {
        "id": len(posts) + 1,  # Assign a unique ID to the post
        "title": data["title"],  # Extract title
        "content": data["content"],  # Extract content
    }
    posts.append(post)  # Add the post to the storage
    return jsonify({"message": "Post created successfully"}), 201

# Route to delete a post by ID
@app.route("/posts/<int:id>", methods=["DELETE"])
def delete_post(id):
    global posts
    posts = [post for post in posts if post["id"] != id]  # Remove the post with the given ID
    return jsonify({"message": "Post deleted successfully"})

# Start the server
if __name__ == "__main__":
    app.run(debug=True, port=5000)