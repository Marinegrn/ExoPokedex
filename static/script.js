        function afficherPokedex() {
            const nomPokemon = document.getElementById('pokemon-name').value;

            fetch('/pokedex', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `pokemon-name=${encodeURIComponent(nomPokemon)}`
            })

            .then(response => response.json())
            .then(data => {
            const pokemonInfoDiv = document.getElementById('pokemon-info');

            let imgTag = `<img id="pokemon-img" src="" alt="Image du Pokémon" style="display:none;"/><br/>`;

            if (data.error) {
                pokemonInfoDiv.innerHTML = imgTag + `<p>${data.error}</p>`;
                document.getElementById('pokemon-img').style.display = 'none';
            } else {
                let info = `
                <h2>${data.name}</h2>
                <p><strong>ID:</strong> ${data.id}</p>
                <p><strong>Poids:</strong> ${data.weight}</p>
                <p><strong>Taille:</strong> ${data.height}</p>
                <p><strong>Type(s):</strong> ${data.type}</p>
                <p><strong>Faiblesse(s):</strong> ${data.weaknesses}</p>
                `;

                if (data.next_evolution.length > 0) {
                    info += `<p><strong>Évolutions possibles:</strong></p><ul>`;

                    data.next_evolution.forEach(evolution => {
                        info += `<li>${evolution.name}</li>`;
                });

                info += `</ul>`;
                }

                pokemonInfoDiv.innerHTML = imgTag + info;

                const img = document.getElementById('pokemon-img');

                if (data.img) {
                    img.src = data.img;
                    img.style.display = 'block';
                } else {
                    img.style.display = 'none';
                }
            }
            })

            .catch(error => console.error('Erreur:', error));
        }