from src.models.database import db


class FounderAnalysis(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )

    score = db.Column(db.Float)

    success_probability = db.Column(db.Float)

    startup_type = db.Column(db.String(100))

    funding_strategy = db.Column(db.String(100))

    strengths = db.Column(db.Text)

    weaknesses = db.Column(db.Text)

    roadmap = db.Column(db.Text)

    created_at = db.Column(db.DateTime, server_default=db.func.now())