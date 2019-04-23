import os
from flask import request, json, Response, Blueprint, g
from ..models.pokemon import PokemonModel, PokemonSchema
import pokebase as pb

pokemon_api = Blueprint('pokemon', __name__)
pokemon_schema = PokemonSchema()

@pokemon_api.route('/number/<int:ident>')
def get_pokemon(ident):
    pokemon = PokemonModel.get_one_pokemon(ident)
    poke_info = pokemon_schema.dump(pokemon).data

    return custom_response(poke_info, 200)

@pokemon_api.route('/name/<string:name>')
def get_pokemon_name(name):
    
    pokemon = PokemonModel.get_pokemon_by_name(name)
    if not pokemon:
        return custom_response({'error': 'no pokemon found'}, 404)
    poke_info = pokemon_schema.dump(pokemon).data

    return custom_response(poke_info, 200)

@pokemon_api.route('/all', methods=['GET'])
def get_all_pokemon():
    pokedex = PokemonModel.get_all_pokemon()

    pokedex_info = pokemon_schema.dump(pokedex, many=True).data
    return custom_response(pokedex_info, 200)

def custom_response(res, status_code):
    '''
    Creates a custom json response
    for proper status messages
    '''

    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )

