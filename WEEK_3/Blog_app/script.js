document.getElementById('postForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;
    
    // Simple validation
    if (!title || !content) {
        alert('Please fill in both fields');
        return;
    }

    // Construct the post object
    const post = { title, content };

    // Simulate adding to a server
    addPost(post);
    displayPosts();
});

function addPost(post) {
    // Assuming posts array is declared globally or retrieved from a server
    posts.push(post);
}

function displayPosts() {
    const postsContainer = document.getElementById('posts');
    postsContainer.innerHTML = ''; // Clear previous posts
    posts.forEach((post, index) => {
        const postElement = document.createElement('div');
        postElement.className = 'post';
        postElement.innerHTML = `
            <h3>${post.title}</h3>
            <p>${post.content}</p>
            <button onclick="deletePost(${index})">Delete</button>
        `;
        postsContainer.appendChild(postElement);
    });
}

function deletePost(index) {
    posts.splice(index, 1); // Remove the post from the array
    displayPosts(); // Re-display posts after deletion
}