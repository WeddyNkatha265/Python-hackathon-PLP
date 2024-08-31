from flask import Flask
from routes.issue_routes import issue_routes
from routes.alert_routes import alert_routes
from routes.response_routes import response_routes

app = Flask(__name__)

# Register blueprints for different routes
app.register_blueprint(issue_routes, url_prefix='/issues')
app.register_blueprint(alert_routes, url_prefix='/alerts')
app.register_blueprint(response_routes, url_prefix='/responses')

if __name__ == '__main__':
    app.run(debug=True)
