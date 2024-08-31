from flask import Blueprint, request, jsonify
from models import Alert, db

alert_routes = Blueprint('alert_routes', __name__)

@alert_routes.route('/', methods=['POST'])
def create_alert():
    data = request.json
    alert = Alert(
        title=data.get('title'),
        description=data.get('description'),
        level=data.get('level')
    )
    db.session.add(alert)
    db.session.commit()
    return jsonify({"message": "Alert created successfully"}), 201

@alert_routes.route('/', methods=['GET'])
def get_alerts():
    alerts = Alert.query.order_by(Alert.timestamp.desc()).all()
    return jsonify([{
        "id": alert.id,
        "title": alert.title,
        "description": alert.description,
        "level": alert.level,
        "timestamp": alert.timestamp
    } for alert in alerts])
