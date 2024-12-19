from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/cluster', methods=['POST'])
def cluster():
    data = request.json
    if not data or 'inputs' not in data:
        return jsonify({"error": "No inputs provided"}), 400

    inputs = data['inputs']
    clusters = {"Cluster 1": inputs[:len(inputs)//2], "Cluster 2": inputs[len(inputs)//2:]}

    return jsonify(clusters)

@app.route('/api/network', methods=['POST'])
def network():
    data = request.json
    if not data or 'nodes' not in data:
        return jsonify({"error": "No nodes provided"}), 400

    nodes = data['nodes']
    network = {"nodes": nodes, "edges": [[nodes[i], nodes[i+1]] for i in range(len(nodes)-1)]}

    return jsonify(network)

@app.route('/api/ideas', methods=['POST'])
def ideas():
    data = request.json
    if not data or 'themes' not in data:
        return jsonify({"error": "No themes provided"}), 400

    themes = data['themes']
    ideas = [f"Innovative idea based on {theme}" for theme in themes]

    return jsonify({"ideas": ideas})

if __name__ == '__main__':
    app.run(debug=True)