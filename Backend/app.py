from flask import Flask, jsonify, request
from flask_cors import CORS
import ply.lex as lex
from analizador.parser.gramatica import *
lexer = lex.lex()

app = Flask(__name__)
CORS(app)

@app.route('/ping')
def ping():
    return jsonify({'message':'PONG'})

@app.route('/analizar', methods=['POST'])
def Analizar():
    aux = request.json
    entrada = aux['code']
    lexer.input(entrada) 
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)   
    print(entrada)
    return jsonify({"message":"SUCCESS"})

if __name__ == '__main__':
    app.run(debug=True, port=3000)