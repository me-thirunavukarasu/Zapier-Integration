from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object("app.config.Config")

    # Enable CORS
    CORS(app)

    # Register routes
    from app.routes import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
