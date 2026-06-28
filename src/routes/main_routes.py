from flask import Blueprint, render_template, request, send_from_directory
import os

from src.services.assessment_service import process_assessment
from src.rag.rag_service import ask_rag

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


@main.route("/chat", methods=["GET", "POST"])
def chat():

    if request.method == "POST":

        question = request.form.get("question")

        answer = ask_rag(question)

        return render_template(
            "chat.html",
            answer=answer
        )

    return render_template("chat.html")


@main.route("/reports/<path:filename>")
def download_report(filename):

    return send_from_directory(
        os.path.join(os.getcwd(), "reports"),
        filename
    )