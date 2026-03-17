from flask import Flask, render_template, request
from db_connect import get_connection

app = Flask(__name__)

def predict_career(maths, science, english, interest,
                   computer, economics, creativity, communication):

    interest = interest.lower()

    # Tech
    if maths >= 75 and computer >= 70 and interest == "technology":
        return "Software Engineer / Data Analyst"

    # Medical
    elif science >= 75 and interest == "medical":
        return "Doctor"

    # Teaching
    elif english >= 65 and communication >= 7 and interest == "teaching":
        return "Teacher / Professor"

    # Acting
    elif creativity >= 8 and interest == "acting":
        return "Actor / Theatre Artist"

    # Journalism
    elif english >= 70 and communication >= 8 and interest == "journalism":
        return "Journalist / Reporter"

    # Business
    elif economics >= 70 and interest == "business":
        return "Entrepreneur / Manager"

    # Designing
    elif creativity >= 7 and interest == "arts":
        return "Designer / Content Creator"

    else:
        return "General Graduation + Skill Development"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    name = request.form["name"]
    maths = int(request.form["maths"])
    science = int(request.form["science"])
    english = int(request.form["english"])
    interest = request.form["interest"]
    computer = int(request.form["computer"])
    economics = int(request.form["economics"])
    creativity = int(request.form["creativity"])
    communication = int(request.form["communication"])  

    career = predict_career(maths, science, english, interest, computer , economics, creativity, communication)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
    "INSERT INTO students (name, maths, science, english, interest, career, computer, economics, creativity, communication) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
    (name, maths, science, english, interest, career, computer, economics, creativity, communication)
)

    conn.commit()
    conn.close()

    return render_template("result.html", career=career)


# 🔥 Dashboard route yaha hona chahiye (run se upar)
@app.route("/dashboard")
def dashboard():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    return render_template("dashboard.html", total=total, students=students)


if __name__ == "__main__":
    app.run(debug=True)