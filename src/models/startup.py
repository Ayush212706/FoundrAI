from src.models.database import db


class Startup(db.Model):

    __tablename__ = "startups"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    name = db.Column(db.String(150), nullable=False)

    industry = db.Column(db.String(100))

    stage = db.Column(db.String(50))

    budget = db.Column(db.Integer)

    team_size = db.Column(db.Integer)

    description = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )