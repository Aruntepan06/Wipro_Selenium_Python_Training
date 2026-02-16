from flask import Flask, request, jsonify

def create_app():
    app = Flask(__name__)

    AUTH_TOKEN = "test-token-123"

    doctors = {}
    patients = {}
    appointments = {}

    next_ids = {"doctor": 500, "patient": 100, "appointment": 900}

    def require_auth():
        auth = request.headers.get("Authorization", "")
        if auth != f"Bearer {AUTH_TOKEN}":
            return jsonify({"error": "Unauthorized"}), 401
        return None

    def require_json():
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400
        return None

    @app.post("/v1/doctors")
    def create_doctor():
        auth_err = require_auth()
        if auth_err:
            return auth_err

        json_err = require_json()
        if json_err:
            return json_err

        payload = request.get_json()
        name = payload.get("name")
        specialization = payload.get("specialization")
        experience = payload.get("experience")

        if not name or not specialization or experience is None:
            return jsonify({"error": "name, specialization, experience are required"}), 400

        if not isinstance(experience, int) or experience < 0:
            return jsonify({"error": "experience must be a non-negative integer"}), 400

        did = next_ids["doctor"]
        next_ids["doctor"] += 1
        doctors[did] = {
            "doctor_id": did,
            "name": name,
            "specialization": specialization,
            "experience": experience
        }
        return jsonify(doctors[did]), 201

    @app.post("/v1/patients")
    def register_patient():
        auth_err = require_auth()
        if auth_err:
            return auth_err

        json_err = require_json()
        if json_err:
            return json_err

        payload = request.get_json()
        name = payload.get("name")
        age = payload.get("age")
        email = payload.get("email")
        phone = payload.get("phone")

        if not name or age is None or phone is None:
            return jsonify({"error": "name, age, phone are required"}), 400

        if not isinstance(age, int) or age < 0:
            return jsonify({"error": "Invalid age"}), 400

        if not email:
            return jsonify({"error": "Missing email"}), 400

        for p in patients.values():
            if p["phone"] == phone:
                return jsonify({"error": "Duplicate phone number"}), 409

        pid = next_ids["patient"]
        next_ids["patient"] += 1
        patients[pid] = {"patient_id": pid, "name": name, "age": age, "email": email, "phone": phone}
        return jsonify(patients[pid]), 201

    def slot_key(doctor_id, date, time):
        return f"{doctor_id}|{date}|{time}"

    @app.post("/v1/appointments")
    def book_appointment():
        auth_err = require_auth()
        if auth_err:
            return auth_err

        json_err = require_json()
        if json_err:
            return json_err

        payload = request.get_json()
        patient_id = payload.get("patient_id")
        doctor_id = payload.get("doctor_id")
        date = payload.get("date")
        time = payload.get("time")

        if patient_id is None or doctor_id is None or not date or not time:
            return jsonify({"error": "patient_id, doctor_id, date, time are required"}), 400

        if patient_id not in patients:
            return jsonify({"error": "Patient not found"}), 404
        if doctor_id not in doctors:
            return jsonify({"error": "Doctor not found"}), 404

        wanted = slot_key(doctor_id, date, time)
        for appt in appointments.values():
            if appt["status"] == "active" and slot_key(appt["doctor_id"], appt["date"], appt["time"]) == wanted:
                return jsonify({"error": "Time slot already booked"}), 409

        aid = next_ids["appointment"]
        next_ids["appointment"] += 1
        appointments[aid] = {
            "appointment_id": aid,
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "date": date,
            "time": time,
            "status": "active"
        }
        return jsonify(appointments[aid]), 201

    @app.get("/v1/appointments/<int:appointment_id>")
    def view_appointment(appointment_id):
        auth_err = require_auth()
        if auth_err:
            return auth_err

        appt = appointments.get(appointment_id)
        if not appt or appt["status"] != "active":
            return jsonify({"error": "Appointment not found"}), 404
        return jsonify(appt), 200

    @app.put("/v1/appointments/<int:appointment_id>")
    def reschedule_appointment(appointment_id):
        auth_err = require_auth()
        if auth_err:
            return auth_err

        json_err = require_json()
        if json_err:
            return json_err

        appt = appointments.get(appointment_id)
        if not appt or appt["status"] != "active":
            return jsonify({"error": "Appointment not found"}), 404

        payload = request.get_json()
        new_date = payload.get("date")
        new_time = payload.get("time")
        if not new_date or not new_time:
            return jsonify({"error": "date and time are required"}), 400

        wanted = slot_key(appt["doctor_id"], new_date, new_time)
        for other_id, other in appointments.items():
            if other_id == appointment_id:
                continue
            if other["status"] == "active" and slot_key(other["doctor_id"], other["date"], other["time"]) == wanted:
                return jsonify({"error": "Time slot already booked"}), 409

        appt["date"] = new_date
        appt["time"] = new_time
        appointments[appointment_id] = appt
        return jsonify(appt), 200

    @app.delete("/v1/appointments/<int:appointment_id>")
    def cancel_appointment(appointment_id):
        auth_err = require_auth()
        if auth_err:
            return auth_err

        appt = appointments.get(appointment_id)
        if not appt or appt["status"] != "active":
            return jsonify({"error": "Appointment not found"}), 404

        appt["status"] = "cancelled"
        appointments[appointment_id] = appt
        return ("", 204)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
