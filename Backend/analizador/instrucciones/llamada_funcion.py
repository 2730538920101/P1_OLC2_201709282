from ..abstract.instrucciones import *
from ..abstract.retorno import *

class Llamada_funcion(Instruccion):
    def __init__(self, linea, columna, id, params):
        super().__init__(linea, columna)
        self.id = id
        self.params = params

    def Ejecutar(self, environment):
        print("EJECUTANDO LLAMADA A FUNCION")
        for p in self.params:
            p.Ejecutar(environment)
        
        fun = environment.getFuncion(self.id)
        print(fun)
