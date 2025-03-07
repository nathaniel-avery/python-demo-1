from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def hello_world():
    """Default route that returns "Hello World"."""
    return jsonify({"message": "Hello World"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
