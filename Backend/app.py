from flask import Flask, jsonify, request
from flask_cors import CORS
from analizador.abstract.retorno import *
import analizador.gramatica
from  analizador.symbol.environment import Entorno
from analizador.symbol.array import *
from analizador.reportes.TablaSim import *

import traductor.gramatica






app = Flask(__name__)
CORS(app)



@app.route('/ping')
def ping():
    return jsonify({'message':'PONG'})

@app.route('/analizar', methods=['POST'])
def Analizar():
    TablaErrores.clear()
    TablaSimbolos.clear()
    Prints.clear()
    aux = request.json
    entrada = aux['code']
    #analizador.gramatica.lexer.input(entrada) 
    resp = analizador.gramatica.parser.parse(entrada)
    env = Entorno()
    for elemento in resp:
        ejec = elemento.Ejecutar(env)
        if ejec != None:
            if isinstance(ejec.value, Retorno):
                print("EJECUCION ACTUAL: ", ejec.value.value)
            else:
                print("EJECUCION ACTUAL: ", ejec.value)
            
    #while True:
    #    tok = analizador.gramatica.lexer.token()
    #    if not tok: 
    #        break      # No more input
    #    print(tok)   
    print("SATISFACTORY ANALYSIS")
    return jsonify({"message":"SATISFACTORY ANALYSIS"})


@app.route('/traducir', methods = ['POST'])
def Traducir():
    aux = request.json
    entrada = aux['code']
    traductor.gramatica.parser.parse(entrada)            
    print("SATISFACTORY ANALYSIS")
    return jsonify({"message":"SATISFACTORY ANALYSIS"})


if __name__ == '__main__':
    app.run(debug=True, port=3000)