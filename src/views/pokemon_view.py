import os
from flask import request, json, Response, Blueprint, g
from ..models.pokemon import PokemonModel, PokemonSchema
import pokebase as pb

pokemon_api = Blueprint('pokemon', __name__)
pokemon_schema = PokemonSchema()

@pokemon_api.route('/populate_database', methods=['GET'])
def get_all():
    '''
    Get all pokemon
    '''

    if request.headers.get('populate_pokemon_token') == os.getenv('POPULATE_TOKEN'):
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

            

            pokeSchema, error = pokemon_schema.load(data)

            
            myPokemon = PokemonModel(pokeSchema)
            myPokemon.save()

        return 'Database Successfully Populated'
    else :
        return 'Get out of here!'


@pokemon_api.route('/test/<int:ident>')
def get_my_all(ident):
    myStuff = PokemonModel.get_one_pokemon(ident)

    return json.dumps(myStuff.to_dict())



@pokemon_api.route('/<int:number>', methods=['GET'])
def get_pokemon(number):
    new_pokemon = pb.pokemon(number)
    new_pokemon_species = pb.pokemon_species(number)
    pokemon_fte = new_pokemon_species.flavor_text_entries
    for fte in pokemon_fte:
            if fte.language.name =="en" and fte.version.name == "alpha-sapphire" or fte.language.name == "en" and fte.version.name == "ultra-sun":
                    new_pokemon_description = fte.flavor_text
    new_pokemon_name = new_pokemon.name
    new_pokemon_number = new_pokemon.id
    
    new_pokemon_image = new_pokemon.sprites.front_default


    # return f'{new_pokemon_name},\n{new_pokemon_description},\n{new_pokemon_image},\n{new_pokemon_number}'
    data = {
        "name": new_pokemon_name,
        "description": new_pokemon_description,
        "image": new_pokemon_image,
        "number": new_pokemon_number,
    }
    json_pokemon_info = json.dumps(data)
    return json_pokemon_info

@pokemon_api.route('/<string:name>', methods=['GET'])
def pokemon_info(name):
    new_name = name.lower()
    new_pokemon = pb.pokemon(new_name)
    new_pokemon_species = pb.pokemon_species(new_name)
    pokemon_fte = new_pokemon_species.flavor_text_entries
    for fte in pokemon_fte:
            if fte.language.name =="en" and fte.version.name == "alpha-sapphire" or fte.language.name == "en" and fte.version.name == "ultra-sun":
                    new_pokemon_description = fte.flavor_text
    new_pokemon_name = new_pokemon.name
    new_pokemon_number = new_pokemon.id
    
    new_pokemon_image = new_pokemon.sprites.front_default


    # return f'{new_pokemon_name},\n{new_pokemon_description},\n{new_pokemon_image},\n{new_pokemon_number}'
    data = {
        "name": new_pokemon_name,
        "description": new_pokemon_description,
        "image": new_pokemon_image,
        "number": new_pokemon_number,
    }
    json_pokemon_info = json.dumps(data)
    return json_pokemon_info



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

