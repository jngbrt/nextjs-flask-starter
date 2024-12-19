from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/cluster', methods=['POST'])
def cluster():
    data = request.json.get('input', [])
    return jsonify({"clusters": ["Cluster1", "Cluster2", "Cluster3"]})

@app.route('/api/network', methods=['GET'])
def network():
    return jsonify({"nodes": ["Node1", "Node2"], "edges": [["Node1", "Node2"]]})

@app.route('/api/ideas', methods=['POST'])
def ideas():
    input_data = request.json.get('input', [])
    idea = f"Basierend auf {', '.join(input_data)}: Eine innovative Lösung entsteht."
    return jsonify({"idea": idea})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
