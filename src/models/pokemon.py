from marshmallow import fields, Schema

from . import db
from ..app import bcrypt

class PokemonModel(db.Model):
    '''
    Pokemon Model
    '''
    __tablename__ = 'pokemon'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    pokemonnumber = db.Column(db.Integer, nullable = False)
    # pokemontype1 = db.Column(db.String(128), nullable = False)
    # pokemontype2 = db.Column(db.String(128), nullable = True)
    pokemondescription = db.Column(db.Text, nullable = False)
    pokemonimage = db.Column(db.String(128), nullable = False)


    def __init__(self, data):
        '''
        Takes in a json request body
        as data and parses to
        instance attributes
        '''
        
        self.name = data.get('name')
        self.pokemonnumber = data.get('pokemonnumber')
        # self.pokemontype1 = data.get('pokemontype1')
        # self.pokemontype2 = data.get('pokemontype2')
        self.pokemondescription = data.get('pokemondescription')
        self.pokemonimage = data.get('pokemonimage')

    def __repr__(self):
        return f'<id {self.id}>'
    
    def save(self):
        '''
        saves new pokemon to database
        '''
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_pokemon():
        return PokemonModel.query.all()

    @staticmethod
    def get_one_pokemon(pokemonnumber):
        return PokemonModel.query.get(pokemonnumber)
    @staticmethod
    def get_pokemon_by_name(name):
        return PokemonModel.query.get(name)
    
    @staticmethod
    def get_pokemon_by_type(pokemontype1):
        return PokemonModel.query.filter_by(pokemontype1).all()

class PokemonSchema(Schema):
    '''
    Pokemon Schema
    '''
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    pokemonnumber = fields.Int(required=True)
    # pokemontype1 = fields.Str(required=True)
    # pokemontype2 = fields.Str(required= False)
    pokemondescription = fields.Str(required=True)
    pokemonimage = fields.Str(required=True)
