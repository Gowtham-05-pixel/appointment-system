from flask import Flask, render_template, request
import sqlite3
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "appointments.db"


def init_db():
    with sqlite3.connect(DB_PATH) as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT NOT NULL,
                appointment_date TEXT NOT NULL,
                appointment_time TEXT NOT NULL,
                reason TEXT NOT NULL
            )
        """)


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        name = request.form.get("patient_name", "").strip()
        date = request.form.get("appointment_date", "")
        time = request.form.get("appointment_time", "")
        reason = request.form.get("reason", "").strip()

        if name and date and time and reason:
            with sqlite3.connect(DB_PATH) as con:
                con.execute("""
                    INSERT INTO appointments
                    (patient_name, appointment_date,
                     appointment_time, reason)
                    VALUES (?, ?, ?, ?)
                """, (name, date, time, reason))

            message = "Appointment booked successfully!"
        else:
            message = "Please fill in all fields."

    return render_template("index.html", message=message)


init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)