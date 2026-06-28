from flask import Blueprint, render_template, request

from src.services.assessment_service import process_assessment

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/assessment", methods=["GET", "POST"])
def assessment():

    if request.method == "POST":

        founder_data = process_assessment(request.form)

        return render_template(
            "dashboard.html",
            founder=founder_data
        )

    return render_template("assessment.html")


@main.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@main.route("/report")
def report():
    return render_template("report.html")