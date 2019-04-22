from flask import request, json, Response, Blueprint, g
from ..models.pokemon import PokemonModel, PokemonSchema

pokemon_api = Blueprint('pokemon', __name__)
pokemon_schema = PokemonSchema()

@pokemon_api.route('/all', methods=['GET'])
def get_all():
    '''
    Get all pokemon
    '''
    pokemons = PokemonModel.get_all_pokemon()
    ser_pokemon = pokemon_schema.dump(pokemons, many=True).data
    return custom_response(ser_pokemon, 200)

@pokemon_api.route('/<int:pokemonnumber>', methods=['GET'])
def get_pokemon(pokemonnumber):
    '''
    Get a single pokemon
    '''
    pokemon = PokemonModel.get_pokemon_by_name(pokemonnumber)
    # print(pokemon)
    if not pokemon:
        return custom_response({'error': 'Pokemon not found'}, 404)

    ser_pokemon = pokemon_schema.dump(pokemon).data
    return custom_response(ser_pokemon, 200)

@pokemon_api.route('/<str:name>', methods=['GET'])
def get_pokemon_name(name):
    '''
    Get a single pokemon
    '''
    pokemon = PokemonModel.get_one_pokemon(pokemonnumber)
    print(pokemon)
    if not pokemon:
        return custom_response({'error': 'Pokemon not found'}, 404)

    ser_pokemon = pokemon_schema.dump(pokemon).data
    return custom_response(ser_pokemon, 200)

# @pokemon_api.route('/create', methods=['POST'])
# def create_pokemon():
   
#     req_data = request.get_json()
#     data, error = pokemon_schema.load(req_data)
#     print('Printing data')
#     print(data, error)
#     if error:
#         return custom_response(error, 400)

#     pokemon = PokemonModel(data)
#     print(pokemon)
#     pokemon.save()

#     ser_data = pokemon_schema.dump(pokemon).data
#     return custom_response(ser_data, 201)

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

