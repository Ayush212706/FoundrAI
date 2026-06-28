from flask import Flask
from flask_login import LoginManager

from src.models.database import db
from src.models.user import User

from src.routes.main_routes import main
from src.routes.auth_routes import auth

from src.services.auth_service import bcrypt

app = Flask(__name__)

app.config["SECRET_KEY"] = "foundrai-secret-key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///foundrai.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

bcrypt.init_app(app)

login_manager = LoginManager()

login_manager.login_view = "auth.login"

login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app.register_blueprint(main)

app.register_blueprint(auth)


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)