import os
from flask import request, json, Response, Blueprint, g
from ..models.pokemon import PokemonModel, PokemonSchema
import pokebase as pb

pokemon_api = Blueprint('pokemon', __name__)
pokemon_schema = PokemonSchema()

@pokemon_api.route('/number/<int:ident>')
def get_pokemon(ident):
    myStuff = PokemonModel.get_one_pokemon(ident)

    return json.dumps(myStuff.to_dict())

@pokemon_api.route('/name/<string:name>')
def get_pokemon_name(name):
    myStuff = PokemonModel.get_one_pokemon_by_name(name)

    return json.dumps(myStuff.to_dict())

# Create route for gettng by name

@pokemon_api.route('/create', methods=['POST'])
def create_pokemon():

    if request.headers.get('populate_pokemon_token') == os.getenv('POPULATE_TOKEN'):
        req_data = request.get_json()
        data, error = pokemon_schema.load(req_data)
        if error:
            return custom_response(error, 400)

        pokemon = PokemonModel(data)
        pokemon.save()

        ser_data = pokemon_schema.dump(pokemon).data
        return custom_response(ser_data, 201)
    else:
        return 'Get outta \'ere'

# @pokemon_api.route('/<string:name>', methods=['GET'])
# def pokemon_info(name):
#     new_name = name.lower()
#     new_pokemon = pb.pokemon(new_name)
#     new_pokemon_species = pb.pokemon_species(new_name)
#     pokemon_fte = new_pokemon_species.flavor_text_entries
#     for fte in pokemon_fte:
#             if fte.language.name =="en" and fte.version.name == "alpha-sapphire" or fte.language.name == "en" and fte.version.name == "ultra-sun":
#                     new_pokemon_description = fte.flavor_text
#     new_pokemon_name = new_pokemon.name
#     new_pokemon_number = new_pokemon.id
    
#     new_pokemon_image = new_pokemon.sprites.front_default


#     # return f'{new_pokemon_name},\n{new_pokemon_description},\n{new_pokemon_image},\n{new_pokemon_number}'
#     data = {
#         "name": new_pokemon_name,
#         "description": new_pokemon_description,
#         "image": new_pokemon_image,
#         "number": new_pokemon_number,
#     }
#     json_pokemon_info = json.dumps(data)
#     return json_pokemon_info



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

