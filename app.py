from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask import render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# MongoDB Connection
mongo_uri = os.getenv("MONGO_URI")

try:
    client = MongoClient(mongo_uri)
    db = client[os.getenv("DB_NAME")]
    collection = db[os.getenv("COLLECTION_NAME")]
    client.admin.command("ping")
    print("✅ MongoDB Connected Successfully")
except Exception as e:
    print("❌ MongoDB Connection Failed:", e)


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/webhook", methods=["POST"])
def webhook():
    event_type = request.headers.get("X-GitHub-Event")
    data = request.json

    if not data:
        return jsonify({"error": "No payload received"}), 400

    document = {}

    # PUSH EVENT
    if event_type == "push":
        document = {
            "request_id": data.get("after"),
            "author": data.get("pusher", {}).get("name"),
            "action": "PUSH",
            "from_branch": None,
            "to_branch": data.get("ref").split("/")[-1],
            "timestamp": data.get("head_commit", {}).get("timestamp")
        }

    # PULL REQUEST EVENT
    elif event_type == "pull_request":
        pr = data.get("pull_request", {})

        # MERGE
        if pr.get("merged") == True:
            document = {
                "request_id": str(pr.get("id")),
                "author": pr.get("user", {}).get("login"),
                "action": "MERGE",
                "from_branch": pr.get("head", {}).get("ref"),
                "to_branch": pr.get("base", {}).get("ref"),
                "timestamp": pr.get("merged_at")
            }

        # NORMAL PR OPEN
        else:
            document = {
                "request_id": str(pr.get("id")),
                "author": pr.get("user", {}).get("login"),
                "action": "PULL_REQUEST",
                "from_branch": pr.get("head", {}).get("ref"),
                "to_branch": pr.get("base", {}).get("ref"),
                "timestamp": pr.get("created_at")
            }

    else:
        return jsonify({"message": "Event ignored"}), 200

    collection.insert_one(document)

    return jsonify({"message": "Event stored"}), 200


@app.route("/events", methods=["GET"])
def get_events():
    events = list(collection.find({}, {"_id": 0}).sort("timestamp", -1).limit(10))
    return jsonify(events)


if __name__ == "__main__":
    app.run(port=5000, debug=True)