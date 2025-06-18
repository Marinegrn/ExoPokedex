from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Télécharger les données JSON depuis l'URL
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
response = requests.get(url)
data = response.json()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokedex', methods=['POST'])
def pokedex():
    nom_pokemon = request.form.get('pokemon-name')
    pokemon_info = get_pokemon_info(nom_pokemon)
    return jsonify(pokemon_info)

def get_pokemon_info(nom_pokemon):
    for pokemon in data['pokemon']:
        if pokemon['name'].lower() == nom_pokemon.lower():
            info = {
                'name': pokemon['name'],
                'id': pokemon['id'],
                'weight': pokemon['weight'],
                'height': pokemon['height'],
                'type': ', '.join(pokemon['type']),
                'weaknesses': ', '.join(pokemon['weaknesses']),
                'next_evolution': pokemon.get('next_evolution', []),
                'img': pokemon.get('img', '')
            }
            return info
    return {'error': 'Pokémon non trouvé'}

if __name__ == '__main__':
    app.run(debug=True)