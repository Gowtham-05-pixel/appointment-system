from flask import Flask, render_template
import sqlite3
from pathlib import Path

app = Flask(__name__)

# Read the same database used by Version 1
DB_PATH = Path(__file__).resolve().parent.parent / "appointments.db"


@app.route("/")
def view_bookings():
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        appointments = con.execute("""
            SELECT * FROM appointments
            ORDER BY appointment_date, appointment_time
        """).fetchall()

    return render_template("view.html", appointments=appointments)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)