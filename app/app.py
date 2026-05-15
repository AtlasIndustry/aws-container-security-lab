from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "AWS Container Security Lab",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}

    username = data.get("username", "unknown")
    password = data.get("password", "")

    print(f"[LOGIN_ATTEMPT] user={username} ip={request.remote_addr}", flush=True)

    if username == "admin" and password == "password123":
        print(f"[LOGIN_SUCCESS] user={username} ip={request.remote_addr}", flush=True)
        return jsonify({"message": "Login successful"})

    print(f"[LOGIN_FAILURE] user={username} ip={request.remote_addr}", flush=True)
    return jsonify({"message": "Invalid credentials"}), 401

@app.route("/admin")
def admin():
    print(f"[ADMIN_ACCESS_ATTEMPT] ip={request.remote_addr} user_agent={request.headers.get('User-Agent')}",flush=True)
    return jsonify({
        "message": "Admin endpoint accessed",
        "warning": "This endpoint is being monitored"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)