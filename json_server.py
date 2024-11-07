from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/metrics')
def get_metrics():
    with open('/tmp/enb_report.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

