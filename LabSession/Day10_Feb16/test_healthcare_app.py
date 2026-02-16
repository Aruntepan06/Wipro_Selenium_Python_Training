import pytest
from healthcare_app import create_app

TOKEN = "test-token-123"

@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def auth_headers():
    return {"Authorization": f"Bearer {TOKEN}"}

def test_healthcare_workflow(client):
    # 1) Admin creates Doctor
    doc_payload = {"name": "Dr. Mehta", "specialization": "Cardiologist", "experience": 12}
    doc_res = client.post("/v1/doctors", json=doc_payload, headers=auth_headers())
    assert doc_res.status_code == 201
    doctor_id = doc_res.get_json()["doctor_id"]

    # 2) Patient registers
    pat_payload = {"name": "Arun", "age": 25, "email": "arun@mail.com", "phone": "9990001112"}
    pat_res = client.post("/v1/patients", json=pat_payload, headers=auth_headers())
    assert pat_res.status_code == 201
    patient_id = pat_res.get_json()["patient_id"]

    # 3) Patient books appointment
    appt_payload = {"patient_id": patient_id, "doctor_id": doctor_id, "date": "2026-03-10", "time": "10:00"}
    appt_res = client.post("/v1/appointments", json=appt_payload, headers=auth_headers())
    assert appt_res.status_code == 201
    appointment_id = appt_res.get_json()["appointment_id"]

    # 4) Patient views appointment
    view_res = client.get(f"/v1/appointments/{appointment_id}", headers=auth_headers())
    assert view_res.status_code == 200

    # 5) Patient reschedules appointment
    reschedule_payload = {"date": "2026-03-10", "time": "11:00"}
    put_res = client.put(f"/v1/appointments/{appointment_id}", json=reschedule_payload, headers=auth_headers())
    assert put_res.status_code == 200
    put_data = put_res.get_json()
    assert put_data["time"] == "11:00"

    # 6) Patient cancels appointment
    del_res = client.delete(f"/v1/appointments/{appointment_id}", headers=auth_headers())
    assert del_res.status_code == 204

    # After cancel, GET returns 404
    view_after = client.get(f"/v1/appointments/{appointment_id}", headers=auth_headers())
    assert view_after.status_code == 404

def test_patient_registration_edge_cases(client):
    # Invalid age (<0) -> 400
    bad_age = {"name": "X", "age": -1, "email": "x@mail.com", "phone": "9000000001"}
    r1 = client.post("/v1/patients", json=bad_age, headers=auth_headers())
    assert r1.status_code == 400

    # Missing email -> 400
    missing_email = {"name": "Y", "age": 10, "phone": "9000000002"}
    r2 = client.post("/v1/patients", json=missing_email, headers=auth_headers())
    assert r2.status_code == 400

    # Duplicate phone -> 409
    p1 = {"name": "A", "age": 20, "email": "a@mail.com", "phone": "9000000003"}
    p2 = {"name": "B", "age": 21, "email": "b@mail.com", "phone": "9000000003"}
    r3 = client.post("/v1/patients", json=p1, headers=auth_headers())
    assert r3.status_code == 201
    r4 = client.post("/v1/patients", json=p2, headers=auth_headers())
    assert r4.status_code == 409

def test_reschedule_conflict_keeps_old_slot(client):
    # Setup doctor + 2 patients + 2 appointments
    doc = client.post("/v1/doctors", json={"name": "Dr X", "specialization": "Cardio", "experience": 5}, headers=auth_headers()).get_json()
    did = doc["doctor_id"]

    p1 = client.post("/v1/patients", json={"name": "P1", "age": 30, "email": "p1@mail.com", "phone": "9111111111"}, headers=auth_headers()).get_json()
    p2 = client.post("/v1/patients", json={"name": "P2", "age": 31, "email": "p2@mail.com", "phone": "9222222222"}, headers=auth_headers()).get_json()

    a1 = client.post("/v1/appointments", json={"patient_id": p1["patient_id"], "doctor_id": did, "date": "2026-03-10", "time": "10:00"}, headers=auth_headers()).get_json()
    a2 = client.post("/v1/appointments", json={"patient_id": p2["patient_id"], "doctor_id": did, "date": "2026-03-10", "time": "11:00"}, headers=auth_headers()).get_json()

    # Try to move a1 into a2 slot -> 409, old slot unchanged
    conflict = client.put(f"/v1/appointments/{a1['appointment_id']}", json={"date": "2026-03-10", "time": "11:00"}, headers=auth_headers())
    assert conflict.status_code == 409

    # Verify a1 still at old slot
    a1_view = client.get(f"/v1/appointments/{a1['appointment_id']}", headers=auth_headers()).get_json()
    assert a1_view["time"] == "10:00"
