print("app.py is running!")
from flask import Flask, render_template, request

app = Flask(__name__)

def generate_plan(subjects, hours):
    subjects = subjects.split(",")
    subjects = [s.strip() for s in subjects]
    hours = int(hours)

    per_subject = max(1, hours // len(subjects))

    plan = []
    for subject in subjects:
        plan.append(f"{subject}: {per_subject} hour(s)")

    return plan

@app.route("/", methods=["GET", "POST"])
def home():
    plan = []
    if request.method == "POST":
        subjects = request.form["subjects"]
        hours = request.form["hours"]
        plan = generate_plan(subjects, hours)
    return render_template("index.html", plan=plan)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
