from flask import Flask, request, jsonify, send_from_directory
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)

db_url = os.getenv("MONGO_URI", "mongodb://localhost:27017")  # Default fallback for local testing

client = MongoClient(db_url)

db = client["mydatabase"]
collection = db["mycollection"]

@app.route('/')
def serve_frontend():
    return send_from_directory('templates', 'index.html')

@app.route('/api', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome to the Flask API!"})

@app.route('/api/data', methods=['POST'])
def add_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    try:
        inserted_id = collection.insert_one(data).inserted_id
        return jsonify({"message": "Data added", "id": str(inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        data = list(collection.find())
        for item in data:
            item["_id"] = str(item["_id"])
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)