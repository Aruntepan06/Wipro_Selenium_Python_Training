import pytest
from bank_app import create_app

@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_customer_lifecycle(client):
    create_payload = {"name": "Arun", "email": "arun@mail.com", "balance": 5000}

    # Step 1: POST
    post_res = client.post("/customers", json=create_payload)
    assert post_res.status_code == 201
    post_data = post_res.get_json()
    assert "id" in post_data
    assert post_data["name"] == create_payload["name"]
    customer_id = post_data["id"]

    # Step 2: GET
    get_res = client.get(f"/customers/{customer_id}")
    assert get_res.status_code == 200
    get_data = get_res.get_json()
    assert get_data["id"] == customer_id
    assert get_data["email"] == create_payload["email"]
    assert get_data["balance"] == create_payload["balance"]

    # Step 3: PUT
    update_payload = {"email": "arun.new@mail.com"}
    put_res = client.put(f"/customers/{customer_id}", json=update_payload)
    assert put_res.status_code == 200
    put_data = put_res.get_json()
    assert put_data["id"] == customer_id
    assert put_data["email"] == update_payload["email"]

    # Step 4: DELETE
    del_res = client.delete(f"/customers/{customer_id}")
    assert del_res.status_code == 204

    # GET after delete -> 404
    get_after_del = client.get(f"/customers/{customer_id}")
    assert get_after_del.status_code == 404
