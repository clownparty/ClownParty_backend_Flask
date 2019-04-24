from . import db
from datetime import datetime

from marshmallow import fields, Schema


class TeamModel(db.Model):
    '''
    Team Model
    '''

    __tablename__ = 'team'
    

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    teamname = db.Column(db.String(128), nullable=False)
    slot1 = db.Column(db.Integer, db.ForeignKey('pokemon.id'), nullable=True)
    slot2 = db.Column(db.Integer,db.ForeignKey('pokemon.id'), nullable=True)
    slot3 = db.Column(db.Integer, db.ForeignKey('pokemon.id'), nullable=True)
    slot4 = db.Column(db.Integer, db.ForeignKey('pokemon.id'), nullable=True)
    slot5 = db.Column(db.Integer, db.ForeignKey('pokemon.id'),  nullable=True)
    slot6 = db.Column(db.Integer, db.ForeignKey('pokemon.id'), nullable=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, data):
        '''
        Takes in a json request body
        as data and parses to
        instance attributes
        '''

        self.owner_id = data.get('owner_id')
        self.teamname = data.get('teamname')
        self.slot1 = data.get('slot1')
        self.slot2 = data.get('slot2')
        self.slot3 = data.get('slot3')
        self.slot4 = data.get('slot4')
        self.slot5 = data.get('slot5')
        self.slot6 = data.get('slot6')
        self.created_at = datetime.utcnow()
        self.modified_at = datetime.utcnow()

    def __repr__(self):
        return f'<id {self.id}>'

    def delete(self):
        '''
        deletes current model from database
        '''
        db.session.delete(self)
        db.session.commit()

    def save(self):
        '''
        saves new object to database
        '''
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        '''
        updates model after setting attributes
        and persists them to database
        '''
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.utcnow()
        db.session.commit()

    @staticmethod
    def get_all_teams():
        return TeamModel.query.all()

    @staticmethod
    def get_one_team(teamname):
        return TeamModel.query.filter_by(id=id).first()


class TeamSchema(Schema):
  """
  Team Schema
  """
  id = fields.Int(dump_only=True)
  teamname = fields.Str(required=True)
  slot1 = fields.Int(required=True)
  slot2 = fields.Int(required=True)
  slot3 = fields.Int(required=True)
  slot4 = fields.Int(required=True)
  slot5 = fields.Int(required=True)
  slot6 = fields.Int(required=True)
  owner_id = fields.Int(required=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)