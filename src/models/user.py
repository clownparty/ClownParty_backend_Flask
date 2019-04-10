import datetime
from marshmallow import fields, Schema

from . import db
from ..app import bcrypt

from .team import UserTeamSchema

class UserModel(db.Model):
    '''
    User Model
    __tablename__ defines the
    database tables name on migration
    class attributes are for declaring
    the database columns
    '''

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    bio = db.Column(db.String(128), nullable=False)
    teams = db.Column(db.Integer, nullable=False)
    fav_poke = db.Column(db.Integer, nullable=False)
    # foreign key

    def __init__(self, data):
        '''
        takes in a json request body
        and parses to instance attributes
        password gets generated into a bcrypt
        hash before storage
        '''

        self.name = data.get('name')
        self.email = data.get('email')
        self.password = self._generate_hash(data.get('password'))
        self.bio = data.get('bio')
        self.teams= data.get('teams')
        self.fav_poke = data.get('fav_pokemon')


    def __repr__(self):
        return f'<id {self.id}>'

    def _generate_hash(self, password):
        return bcrypt.generate_password_hash(password, rounds=10).decode('utf-8')

    def check_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def delete(self):
        '''deletes row from db'''
        db.session.delete(self)
        db.session.commit()

    def save(self):
        '''saves current state of model to db'''
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        '''takes in data to modify model'''
        for key, item in data.items():
            if key == 'password':
                self.password = self._generate_hash(value)
            setattr(self, key, item)
        db.session.commit()

    @staticmethod
    def get_all_users():
        return UserModel.query.all()

    @staticmethod
    def get_user_by_email(value):
        return UserModel.query.filter_by(email=value).first()

    @staticmethod
    def get_one_user(id):
        return UserModel.query.get(id)


class UserSchema(Schema):
    '''
    Schema for User Models
    '''

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    bio = fields.Str(required=True)
    fav_poke = fields.Int(required=True)
    teams = fields.Nested(UserTeamSchema, many=True)