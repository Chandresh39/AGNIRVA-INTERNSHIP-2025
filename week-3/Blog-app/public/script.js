document.getElementById('postForm').addEventListener('submit', async function (event) {
  event.preventDefault();

  const title = document.getElementById('title').value.trim();
  const content = document.getElementById('content').value.trim();

  if (!title || !content) {
    alert('Both fields are required!');
    return;
  }

  // POST to backend
  const res = await fetch('/posts', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ title, content })
  });

  if (res.ok) {
    document.getElementById('title').value = '';
    document.getElementById('content').value = '';
    loadPosts(); // refresh the post list
  } else {
    alert('Something went wrong!');
  }
});

async function loadPosts() {
  const res = await fetch('/posts');
  const posts = await res.json();

  const postsContainer = document.getElementById('posts');
  postsContainer.innerHTML = '';

  posts.forEach(post => {
    const postDiv = document.createElement('div');
    postDiv.classList.add('post');
    postDiv.innerHTML = `
      <h3>${post.title}</h3>
      <p>${post.content}</p>
      <button onclick="deletePost(${post.id})">Delete</button>
    `;
    postsContainer.appendChild(postDiv);
  });
}

async function deletePost(id) {
  const res = await fetch(`/posts/${id}`, {
    method: 'DELETE'
  });

  if (res.ok) {
    loadPosts();
  } else {
    alert('Could not delete the post!');
  }
}

// Load all posts when page loads
window.onload = loadPosts;
