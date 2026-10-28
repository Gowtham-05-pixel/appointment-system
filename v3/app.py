from flask import Flask, render_template, redirect, url_for, request
import sqlite3
from pathlib import Path

app = Flask(__name__)

# Share the database used by v1 and v2
DB_PATH = Path(__file__).resolve().parent.parent / "appointments.db"


@app.route("/", methods=["GET", "POST"])
def cancel_appointment():
    message = ""

    if request.method == "POST":
        appointment_id = request.form.get("appointment_id", "").strip()

        if appointment_id.isdigit():
            with sqlite3.connect(DB_PATH) as con:
                cursor = con.execute(
                    "DELETE FROM appointments WHERE id = ?",
                    (int(appointment_id),)
                )

                if cursor.rowcount > 0:
                    message = f"Appointment {appointment_id} cancelled successfully!"
                else:
                    message = "Appointment ID not found."
        else:
            message = "Enter a valid appointment ID."

    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        appointments = con.execute("""
            SELECT * FROM appointments
            ORDER BY appointment_date, appointment_time
        """).fetchall()

    return render_template(
        "cancel.html",
        appointments=appointments,
        message=message
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=False)