from flask import (
    Blueprint,
    render_template,
    request,
    send_from_directory
)

import os

from flask_login import (
    login_required,
    current_user
)

from src.models.assessment import Assessment

from src.services.assessment_service import process_assessment

from src.rag.rag_service import ask_rag

from src.core.progress_engine import calculate_progress
from src.core.task_engine import generate_tasks
from src.core.timeline_engine import generate_timeline

from src.services.memory_service import load_memory


main = Blueprint("main", __name__)


# ----------------------------------------------------
# Home
# ----------------------------------------------------

@main.route("/")
def home():

    return render_template("index.html")


# ----------------------------------------------------
# Assessment
# ----------------------------------------------------

@main.route("/assessment", methods=["GET", "POST"])
@login_required
def assessment():

    if request.method == "POST":

        founder_data = process_assessment(
            request.form
        )

        return render_template(

            "dashboard.html",

            founder=founder_data,

            progress=calculate_progress(
                founder_data
            ),

            tasks=generate_tasks(
                founder_data
            ),

            timeline=generate_timeline(
                load_memory(current_user.username)
            )

        )

    return render_template(
        "assessment.html"
    )


# ----------------------------------------------------
# Dashboard
# ----------------------------------------------------

@main.route("/dashboard")
@login_required
def dashboard():

    latest = (

        Assessment.query

        .filter_by(
            user_id=current_user.id
        )

        .order_by(
            Assessment.created_at.desc()
        )

        .first()

    )

    if latest is None:

        return render_template(

            "dashboard.html",

            founder={

                "name": current_user.username,

                "startup_stage": current_user.startup_name,

                "score": 0,

                "programming": 0,

                "marketing": 0,

                "finance": 0,

                "leadership": 0,

                "communication": 0,

                "problem_solving": 0,

                "risk_tolerance": 0,

                "ai_advice": "Complete your first assessment to receive personalized recommendations."

            },

            progress={

                "founder_level": "New Founder",

                "execution_readiness": 0,

                "startup_health": {}

            },

            tasks={

                "tasks": []

            },

            timeline=[]

        )

    founder = {

        "name": current_user.username,

        "startup_stage": latest.startup_stage,

        "score": latest.founder_score,

        "programming": latest.programming,

        "marketing": latest.marketing,

        "finance": latest.finance,

        "leadership": latest.leadership,

        "communication": latest.communication,

        "problem_solving": latest.problem_solving,

        "risk_tolerance": latest.risk_tolerance,

        "ai_advice": latest.ai_advice,

        "report_path": latest.report_path

    }

    return render_template(

        "dashboard.html",

        founder=founder,

        progress=calculate_progress(
            founder
        ),

        tasks=generate_tasks(
            founder
        ),

        timeline=generate_timeline(
            load_memory(current_user.username)
        )

    )


# ----------------------------------------------------
# AI Chat
# ----------------------------------------------------

@main.route("/chat", methods=["GET", "POST"])
@login_required
def chat():

    if request.method == "POST":

        question = request.form.get(
            "question"
        )

        answer = ask_rag(question)

        return render_template(

            "chat.html",

            answer=answer

        )

    return render_template(
        "chat.html"
    )


# ----------------------------------------------------
# Reports
# ----------------------------------------------------

@main.route("/report")
@login_required
def report():

    return render_template(
        "report.html"
    )


# ----------------------------------------------------
# Download Report
# ----------------------------------------------------

@main.route("/reports/<path:filename>")
@login_required
def download_report(filename):

    return send_from_directory(

        os.path.join(
            os.getcwd(),
            "reports"
        ),

        filename

    )