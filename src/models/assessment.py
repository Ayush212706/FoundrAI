from src.models.database import db


class Assessment(db.Model):
    """
    Stores every assessment completed by a founder.
    One User -> Many Assessments
    """

    __tablename__ = "assessments"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # ----------------------------------
    # Relationship
    # ----------------------------------

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    # ----------------------------------
    # Founder Information
    # ----------------------------------

    age = db.Column(
        db.Integer,
        nullable=False
    )

    education = db.Column(
        db.String(100),
        nullable=False
    )

    occupation = db.Column(
        db.String(100),
        nullable=False
    )

    # ----------------------------------
    # Startup Information
    # ----------------------------------

    startup_stage = db.Column(
        db.String(50),
        nullable=False
    )

    budget = db.Column(
        db.Integer,
        nullable=False
    )

    team_size = db.Column(
        db.Integer,
        nullable=False
    )

    # ----------------------------------
    # Skills
    # ----------------------------------

    programming = db.Column(
        db.Integer,
        nullable=False
    )

    marketing = db.Column(
        db.Integer,
        nullable=False
    )

    finance = db.Column(
        db.Integer,
        nullable=False
    )

    leadership = db.Column(
        db.Integer,
        nullable=False
    )

    communication = db.Column(
        db.Integer,
        nullable=False
    )

    problem_solving = db.Column(
        db.Integer,
        nullable=False
    )

    risk_tolerance = db.Column(
        db.Integer,
        nullable=False
    )

    # ----------------------------------
    # AI Output
    # ----------------------------------

    founder_score = db.Column(
        db.Float,
        nullable=False
    )

    ai_advice = db.Column(
        db.Text,
        nullable=False
    )

    report_path = db.Column(
        db.String(255)
    )

    # ----------------------------------
    # Analytics
    # ----------------------------------

    success_probability = db.Column(
        db.Float,
        default=0
    )

    founder_level = db.Column(
        db.String(50),
        default="Beginner"
    )

    execution_readiness = db.Column(
        db.Float,
        default=0
    )

    # ----------------------------------
    # Metadata
    # ----------------------------------

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )

    def to_dict(self):
        return {

            "id": self.id,

            "user_id": self.user_id,

            "age": self.age,

            "education": self.education,

            "occupation": self.occupation,

            "startup_stage": self.startup_stage,

            "budget": self.budget,

            "team_size": self.team_size,

            "programming": self.programming,

            "marketing": self.marketing,

            "finance": self.finance,

            "leadership": self.leadership,

            "communication": self.communication,

            "problem_solving": self.problem_solving,

            "risk_tolerance": self.risk_tolerance,

            "score": self.founder_score,

            "ai_advice": self.ai_advice,

            "report_path": self.report_path,

            "success_probability": self.success_probability,

            "founder_level": self.founder_level,

            "execution_readiness": self.execution_readiness,

            "created_at": self.created_at

        }

    def __repr__(self):

        return (
            f"<Assessment "
            f"id={self.id} "
            f"user={self.user_id} "
            f"score={self.founder_score}>"
        )