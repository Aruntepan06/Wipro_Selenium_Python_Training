from flask import Flask, request, jsonify, abort

def create_app():
    app = Flask(__name__)

    customers = {}
    next_id = {"value": 1000}

    def _require_json():
        if not request.is_json:
            abort(400, description="Request must be JSON")

    @app.post("/customers")
    def create_customer():
        _require_json()
        payload = request.get_json()

        name = payload.get("name")
        email = payload.get("email")
        balance = payload.get("balance")

        if not name or not email or balance is None:
            return jsonify({"error": "name, email, balance are required"}), 400

        if not isinstance(balance, (int, float)) or balance < 0:
            return jsonify({"error": "balance must be a non-negative number"}), 400

        cid = next_id["value"]
        next_id["value"] += 1

        customer = {"id": cid, "name": name, "email": email, "balance": balance}
        customers[cid] = customer

        return jsonify(customer), 201

    @app.get("/customers/<int:customer_id>")
    def get_customer(customer_id):
        customer = customers.get(customer_id)
        if not customer:
            return jsonify({"error": "Customer not found"}), 404
        return jsonify(customer), 200

    @app.put("/customers/<int:customer_id>")
    def update_customer(customer_id):
        _require_json()
        customer = customers.get(customer_id)
        if not customer:
            return jsonify({"error": "Customer not found"}), 404

        payload = request.get_json()
        new_email = payload.get("email")
        if not new_email:
            return jsonify({"error": "email is required"}), 400

        customer["email"] = new_email
        customers[customer_id] = customer

        return jsonify(customer), 200

    @app.delete("/customers/<int:customer_id>")
    def delete_customer(customer_id):
        if customer_id not in customers:
            return jsonify({"error": "Customer not found"}), 404

        del customers[customer_id]
        return ("", 204)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
