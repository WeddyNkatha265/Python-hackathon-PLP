from flask import Blueprint, request, jsonify
from models import Issue, db

issue_routes = Blueprint('issue_routes', __name__)

@issue_routes.route('/', methods=['POST'])
def report_issue():
    data = request.json
    issue = Issue(
        description=data.get('description'),
        location=data.get('location'),
        image_url=data.get('image_url')
    )
    db.session.add(issue)
    db.session.commit()
    return jsonify({"message": "Issue reported successfully"}), 201

@issue_routes.route('/', methods=['GET'])
def get_issues():
    issues = Issue.query.all()
    return jsonify([{
        "id": issue.id,
        "description": issue.description,
        "location": issue.location,
        "image_url": issue.image_url,
        "status": issue.status
    } for issue in issues])
