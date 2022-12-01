from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "flask"

mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/info")
def info():
    return render_template("info.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        email = request.form.get("email")
        subject = request.form.get("subject")
        description = request.form.get("description")
        cur = mysql.connection.cursor()
        cur.execute(
            f"INSERT INTO user(email, subject, description) VALUES ('{email}', '{subject}', '{description}');"
        )
        mysql.connection.commit()

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(port=2000, debug=True)
