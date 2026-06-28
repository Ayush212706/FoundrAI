from src.models.database import db


class ChatMemory(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )

    role = db.Column(db.String(20))

    message = db.Column(db.Text)

    created_at = db.Column(db.DateTime, server_default=db.func.now())