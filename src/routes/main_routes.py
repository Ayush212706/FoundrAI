from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/assessment", methods=["GET", "POST"])
def assessment():

    if request.method == "POST":

        name = request.form.get("name")
        age = request.form.get("age")
        budget = request.form.get("budget")
        occupation = request.form.get("occupation")
        skill = request.form.get("skill")

        print("\n========== Founder Assessment ==========")
        print(f"Name       : {name}")
        print(f"Age        : {age}")
        print(f"Budget     : ₹{budget}")
        print(f"Occupation : {occupation}")
        print(f"Skill      : {skill}")
        print("========================================\n")

        return render_template("dashboard.html")

    return render_template("assessment.html")


@main.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@main.route("/report")
def report():
    return render_template("report.html")