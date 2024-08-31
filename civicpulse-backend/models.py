from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255))
    status = db.Column(db.String(50), default="Open")

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    level = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alert_id = db.Column(db.Integer, db.ForeignKey('alert.id'), nullable=False)
    volunteer_name = db.Column(db.String(100), nullable=False)
    resources_provided = db.Column(db.String(255))
