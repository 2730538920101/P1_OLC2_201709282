from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/ping')
def ping():
    return jsonify({'message':'PONG'})

@app.route('/analizar', methods=['POST'])
def Analizar():
    aux = request.json
    print(aux['code'])
    return jsonify({"message":"SUCCESS"})

if __name__ == '__main__':
    app.run(debug=True, port=3000)