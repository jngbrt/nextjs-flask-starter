from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/cluster', methods=['POST'])
def cluster():
    data = request.json.get('input', [])
    # Beispiel: Rückgabe eines statischen Clusters
    return jsonify({"clusters": ["Cluster1", "Cluster2", "Cluster3"]})

@app.route('/api/network', methods=['GET'])
def network():
    # Beispiel: Rückgabe eines statischen Netzwerks
    return jsonify({"nodes": ["Node1", "Node2"], "edges": [["Node1", "Node2"]]})

@app.route('/api/ideas', methods=['POST'])
def ideas():
    input_data = request.json.get('input', [])
    # Beispiel: Generiere eine Idee basierend auf der Eingabe
    idea = f"Basierend auf {', '.join(input_data)}: Eine innovative Lösung entsteht."
    return jsonify({"idea": idea})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
