from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)

    # Initialize Migrate
    migrate = Migrate(app, db)

    with app.app_context():
        # Register blueprints
        from app.views import trigger_blueprint, event_blueprint
        app.register_blueprint(trigger_blueprint)
        app.register_blueprint(event_blueprint)

        # Skip creating the 'trigger' table since it already exists manually
        # Use migrations instead if required
        # db.create_all()  # Remove or comment this line if 'trigger' table already exists

    return app
