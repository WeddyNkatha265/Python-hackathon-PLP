from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///civicpulse.db'
    db.init_app(app)
    with app.app_context():
        db.create_all()
