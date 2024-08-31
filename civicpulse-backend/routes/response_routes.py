from flask import Blueprint, request, jsonify
from models import Response, db

response_routes = Blueprint('response_routes', __name__)

@response_routes.route('/', methods=['POST'])
def create_response():
    data = request.json
    response = Response(
        alert_id=data.get('alert_id'),
        volunteer_name=data.get('volunteer_name'),
        resources_provided=data.get('resources_provided')
    )
    db.session.add(response)
    db.session.commit()
    return jsonify({"message": "Response recorded successfully"}), 201

@response_routes.route('/', methods=['GET'])
def get_responses():
    responses = Response.query.all()
    return jsonify([{
        "id": response.id,
        "alert_id": response.alert_id,
        "volunteer_name": response.volunteer_name,
        "resources_provided": response.resources_provided
    } for response in responses])
