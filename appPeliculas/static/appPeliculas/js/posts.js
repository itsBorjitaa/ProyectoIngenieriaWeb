document.addEventListener("DOMContentLoaded", () => {
    fetch('/api/posts/') //endpoint de los posts
        .then(response => response.json())
        .then(posts => {
            const postsContainer = document.getElementById('posts-container');
            posts.forEach(post => {
                const postElement = document.createElement('div');
                postElement.classList.add('post');
                postElement.innerHTML = `
                    <h3>${post.titulo}</h3>
                    <p>${post.contenido}</p>
                    <small>Publicado el: ${new Date(post.fecha_publicacion).toLocaleDateString()}</small>
                `;
                postsContainer.appendChild(postElement);
            });
        })
        .catch(error => console.error('Error al obtener los posts:', error));
});
