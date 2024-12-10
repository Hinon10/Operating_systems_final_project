from flask import Flask, render_template, request
import pg8000

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        level = request.form["level"]
        return render_template("courses.html", level=level)
    return render_template("index.html")

@app.route("/courses", methods=["GET"])
def courses():
    level = request.args.get("level")

    conn = pg8000.connect(user="postgres", password="postgres", host="host.docker.internal", port=7001, database="anton")
    cur = conn.cursor()

    query = f"SELECT * FROM courses WHERE level = {level};"
    cur.execute(query)
    rows = cur.fetchall()
    message = "No data found for this course code." if not rows else None
    return render_template("courses.html", data=rows, message=message, level=level)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')