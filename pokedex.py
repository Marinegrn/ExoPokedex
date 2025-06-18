# Fichier sans l'interface graphique 
# # Charger et parser les données JSON
# import requests
# import json

# # Télécharger les données JSON depuis l'URL
# url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
# response = requests.get(url)
# data = response.json()

# # Afficher les données pour vérifier
# print(data)


# # Fonction pour répondre aux questions 
# def nombre_de_pokemon(data):
#     return len(data['pokemon'])

# def pokemon_poids_superieur_a_10_kg(data):
#     return [pokemon for pokemon in data['pokemon'] if pokemon['weight'] > '10 kg']

# def classer_par_poids_croissant(data):
#     pokemon_list = data['pokemon']
#     pokemon_list.sort(key=lambda x: float(x['weight'].split()[0]))
#     return pokemon_list

# # Exemple d'utilisation des fonctions
# print("Nombre de Pokemon:", nombre_de_pokemon(data))
# print("Pokemon dont le poids est supérieur à 10 kg:", pokemon_poids_superieur_a_10_kg(data))
# print("Pokemon classés par ordre croissant de poids:", classer_par_poids_croissant(data))

# # Fonction pour afficher les évolutions d'un Pokemon
# def afficher_evolutions(data, nom_pokemon):
#     for pokemon in data['pokemon']:
#         if pokemon['name'] == nom_pokemon:
#             evolutions = pokemon.get('next_evolution', [])
#             if evolutions:
#                 print(f"Les évolutions de {nom_pokemon} sont :")
#                 for evolution in evolutions:
#                     print(evolution['name'])
#             else:
#                 print(f"{nom_pokemon} n'a pas d'évolutions.")
#             return
#     print(f"Pokemon {nom_pokemon} non trouvé.")

# # Exemple d'utilisation de la fonction
# afficher_evolutions(data, 'Bulbasaur')

# # Création un Pokédex
# def pokedex(data, nom_pokemon):
#     for pokemon in data['pokemon']:
#         if pokemon['name'] == nom_pokemon:
#             print(f"Nom: {pokemon['name']}")
#             print(f"ID: {pokemon['id']}")
#             print(f"Poids: {pokemon['weight']}")
#             print(f"Taille: {pokemon['height']}")
#             print(f"Type(s): {', '.join(pokemon['type'])}")
#             print(f"Faiblesse(s): {', '.join(pokemon['weaknesses'])}")
#             evolutions = pokemon.get('next_evolution', [])
#             if evolutions:
#                 print("Évolutions possibles:")
#                 for evolution in evolutions:
#                     print(evolution['name'])
#             return
#     print(f"Pokemon {nom_pokemon} non trouvé.")

# # Exemple d'utilisation de la fonction
# pokedex(data, 'Pikachu')
