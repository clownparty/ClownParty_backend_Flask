import pokebase as pb
import json
import requests
URL = "https://pokemonteam-builder.herokuapp.com/api/v1/pokemon/create"
headers = {
    'populate_pokemon_token': 'testing',
    'Content-Type': 'application/json'
}
        
for i in range(1, 808):
    pokemon = pb.pokemon(i)
    species = pb.pokemon_species(i)
    description = ""
    for fte in species.flavor_text_entries:
        if fte.language.name =="en" and fte.version.name == "alpha-sapphire" or fte.language.name == "en" and fte.version.name == "ultra-sun":
            description = fte.flavor_text
                        
    data = {
    'name': pokemon.name,
    'pokemonnumber': pokemon.id,
    'pokemondescription': description,
    'pokemonimage': pokemon.sprites.front_default
    }

    data = json.dumps(data)
    requests.post(URL, data, headers=headers)
        
   





