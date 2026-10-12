from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample fitness programs
FITNESS_PROGRAMS = [
    {"id": 1, "name": "Weight Loss", "duration_weeks": 8},
    {"id": 2, "name": "Muscle Building", "duration_weeks": 12},
    {"id": 3, "name": "General Fitness", "duration_weeks": 6},
]

# In-memory member records for our initial version
members = []
next_member_id = 1


@app.route("/")
def home():
    return jsonify({
        "application": "ACEest Fitness & Gym",
        "message": "Welcome to ACEest Fitness!",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/programs", methods=["GET"])
def get_programs():
    return jsonify(FITNESS_PROGRAMS), 200


@app.route("/members", methods=["GET"])
def get_members():
    return jsonify(members), 200


@app.route("/members", methods=["POST"])
def add_member():
    global next_member_id

    data = request.get_json(silent=True)

    if not data or not isinstance(data, dict):
        return jsonify({"error": "A JSON request body is required"}), 400

    name = data.get("name")

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Member name is required"}), 400

    member = {
        "id": next_member_id,
        "name": name.strip()
    }

    members.append(member)
    next_member_id += 1

    return jsonify(member), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)