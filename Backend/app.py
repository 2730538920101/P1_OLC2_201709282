from flask import Flask, jsonify, request
from flask_cors import CORS
import analizador.gramatica
from  analizador.symbol.environment import Entorno 



app = Flask(__name__)
CORS(app)

@app.route('/ping')
def ping():
    return jsonify({'message':'PONG'})

@app.route('/analizar', methods=['POST'])
def Analizar():
    aux = request.json
    entrada = aux['code']
    #analizador.gramatica.lexer.input(entrada) 
    resp = analizador.gramatica.parser.parse(entrada)
    env = Entorno()
    for elemento in resp:
        ejec = elemento.Ejecutar(env)
        if ejec != None:
            print(ejec.value)
            
    #while True:
    #    tok = analizador.gramatica.lexer.token()
    #    if not tok: 
    #        break      # No more input
    #    print(tok)   
    print("SATISFACTORY ANALYSIS")
    return jsonify({"message":"SATISFACTORY ANALYSIS"})

if __name__ == '__main__':
    app.run(debug=True, port=3000)