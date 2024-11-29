document.addEventListener("DOMContentLoaded", () => {
    const tweetsList = document.getElementById("tweets-list");

    // Consumir el endpoint para obtener los tweets
    fetch("/tweets/")
        .then(response => response.json())
        .then(data => {
            if (data.data) {
                data.data.forEach(tweet => {
                    const li = document.createElement("li");
                    li.innerHTML = `
                        <p>${tweet.text}</p>
                        <a href="https://twitter.com/i/web/status/${tweet.id}" target="_blank">Ver en Twitter</a>
                    `;
                    tweetsList.appendChild(li);
                });
            } else {
                tweetsList.innerHTML = "<p>No se pudieron cargar los tweets.</p>";
            }
        })
        .catch(error => {
            console.error("Error al obtener los tweets:", error);
            tweetsList.innerHTML = "<p>Error al cargar los tweets.</p>";
        });
});
