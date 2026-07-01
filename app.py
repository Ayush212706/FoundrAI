from flask import Flask
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

from src.config import Config

from src.models.database import db
from src.models.user import User

from src.routes.main_routes import main
from src.routes.auth_routes import auth


# --------------------------------------------------
# Create Flask App
# --------------------------------------------------

app = Flask(__name__)

# --------------------------------------------------
# Load Configuration
# --------------------------------------------------

app.config.from_object(Config)


# --------------------------------------------------
# Initialize Database
# --------------------------------------------------

db.init_app(app)


# --------------------------------------------------
# Initialize Login Manager
# --------------------------------------------------

login_manager = LoginManager()

login_manager.login_view = "auth.login"

login_manager.login_message = "Please login to continue."

login_manager.login_message_category = "warning"

login_manager.init_app(app)


# --------------------------------------------------
# User Loader
# --------------------------------------------------

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# --------------------------------------------------
# Register Blueprints
# --------------------------------------------------

app.register_blueprint(main)

app.register_blueprint(auth)


# --------------------------------------------------
# Create Database Tables
# --------------------------------------------------

with app.app_context():

    db.create_all()

    # --------------------------------------------------
    # Create Default Admin (Only if it doesn't exist)
    # --------------------------------------------------

    admin = User.query.filter_by(
        email="admin@foundrai.ai"
    ).first()

    if admin is None:

        admin = User(
            username="admin",
            email="admin@foundrai.ai",
            password=generate_password_hash("admin123"),
            startup_name="FoundrAI",
            industry="Artificial Intelligence",
            role="admin",
        )

        db.session.add(admin)

        db.session.commit()

        print("\n====================================")
        print(" Default Admin Created")
        print(" Email    : admin@foundrai.ai")
        print(" Password : admin123")
        print("====================================\n")


# --------------------------------------------------
# Run Application
# --------------------------------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )