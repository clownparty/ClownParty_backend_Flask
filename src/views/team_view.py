from flask import request, json, Response, Blueprint, g
from ..models.team import TeamModel, TeamSchema
from ..shared.authentication import Auth


team_api = Blueprint('team', __name__)
team_schema = TeamSchema()


@team_api.route('/team/new', methods=['POST'])
# @Auth.auth_required
def create():
    '''
    Create endpoint for team api
    '''

    req_data = request.get_json()
    print(req_data)
    data, error = team_schema.load(req_data)
    print(data)

    if error:
        return custom_response(error, 400)

    # check if team already exists in db
    team_in_db = TeamModel.get_one_team(data.get('teamname'))
    if team_in_db:
        message = {'error': 'Team already exists, please supply another team name'}
        return custom_response(message, 400)

    team = TeamModel(data)
    team.save()

    ser_data = team_schema.dump(team).data


    return custom_response(ser_data, 201)


@team_api.route('/team/edit/<string:teamname>', methods=['DELETE'])
# @Auth.auth_required
def delete():
    '''
    Delete the team model
    if authenticated
    '''
    team = TeamModel.get_one_team(g.team.get("teamname"))
    team.delete()
    return custom_response({'message': 'deleted'}, 204)


@team_api.route('/team', methods=['GET'])
def get_all():
    '''
    Get all teams
    '''
    teams = TeamModel.get_all_teams()
    ser_teams = team_schema.dump(teams, many=True).data
    return custom_response(ser_teams, 200)


@team_api.route('/team/view/<teamname>', methods=['GET'])
def get_team(teamname):
    '''
    Get a single team
    '''
    team = TeamModel.get_one_team(teamname)
    if not team:
        return custom_response({'error': 'team not found'}, 404)

    ser_team = team_schema.dump(team).data
    return custom_response(ser_user, 200)


@team_api.route('/team/view', methods=['GET'])
def get_team_info():
    '''
    Get team information
    '''

    team = TeamModel.get_one_team(g.team.get('teamname'))
    ser_team = team_schema.dump(team).data
    return custom_response(ser_team, 200)



@team_api.route('/team/edit', methods=['PUT'])
@Auth.auth_required
def update():
    '''
    Allows owner of team (me)
    to update the team information
    '''

    req_data = request.get_json()
    data, error = team_schema.load(req_data, partial=True)
    if error:
        return custom_response(error, 400)

    team = TeamModel.get_one_team(g.team.get('id'))
    team.update(data)
    ser_team = team_schema.dump(team).data
    return custom_response(ser_team, 200)


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