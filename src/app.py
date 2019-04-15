from flask import Flask

from .config import app_config
from .models import db, bcrypt
from .models import user

from .views.user_view import user_api as user_blueprint
from .views.pokemon_view import pokemon_api as pokemon_blueprint
from .views.team_view import team_api as team_blueprint
from flask_cors import CORS


def create_app(env_name='development'):
    '''Create app context'''

    app = Flask(__name__)

    CORS(app)

    app.config.from_object(app_config[env_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
    app.register_blueprint(pokemon_blueprint, url_prefix='/api/v1/pokemon')
    app.register_blueprint(team_blueprint, url_prefix='/api/v1/teams')
    

    bcrypt.init_app(app)
    db.init_app(app)


    @app.route('/', methods=['GET'])
    def index():
        '''example endpoint'''
        return 'Test Successful'

    return app