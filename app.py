
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/data', methods=['GET'])

def get_data():
    data = {
        'key': 'value',
        'number': 1,
        'message': 'Seizure detected'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)