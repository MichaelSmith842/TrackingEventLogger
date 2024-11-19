from flask import Flask, render_template, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

JSON_FILE_PATH = "/Users/michael/Desktop/EventLogger/converted_data/data.JSON"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-events', methods=['GET'])
def get_events():
    if not os.path.exists(JSON_FILE_PATH):
        return jsonify({"error": "JSON file not found"}), 404
    with open(JSON_FILE_PATH, 'r') as json_file:
        data = json.load(json_file)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
