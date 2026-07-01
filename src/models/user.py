from flask_login import UserMixin
from src.models.database import db


class User(UserMixin, db.Model):
    assessments = db.relationship(
    "Assessment",
    backref="user",
    lazy=True,
    cascade="all, delete-orphan"
)

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    startup_name = db.Column(
        db.String(150),
        default=""
    )

    industry = db.Column(
        db.String(100),
        default=""
    )

    role = db.Column(
        db.String(20),
        nullable=False,
        default="founder"
    )

    is_active_user = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    last_login = db.Column(
        db.DateTime
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def get_id(self):
        return str(self.id)

    def is_admin(self):
        return self.role == "admin"

    def __repr__(self):
        return f"<User {self.username}>"