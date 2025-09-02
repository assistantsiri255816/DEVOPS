from flask import Flask, jsonify, request
import os
import psycopg2
import json

app = Flask(__name__)
DB_URL = os.environ.get("DATABASE_URL")  # e.g. postgres://user:pass@host:5432/dbname

def get_db_count():
    if not DB_URL:
        return {"warning": "DATABASE_URL not set"}
    try:
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM users;")
        count = cur.fetchone()[0]
        cur.close()
        conn.close()
        return {"users_count": count}
    except Exception as e:
        return {"db_error": str(e)}

@app.route("/api/data", methods=["GET"])
def data():
    info = {
        "message": "Hello from backend",
        "env": {"SERVICE": os.environ.get("SERVICE_NAME","backend")},
        "db": get_db_count()
    }
    # Optionally emit a simple log file that logger can consume (in real setup you'd use a queue)
    try:
        with open("/tmp/backend_events.log", "a") as f:
            f.write(json.dumps({"path": "/api/data", "payload": {}, "remote": request.remote_addr}) + "\n")
    except Exception:
        pass
    return jsonify(info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
