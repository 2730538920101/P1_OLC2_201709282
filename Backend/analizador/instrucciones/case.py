from ..abstract.instrucciones import *
from ..symbol.environment import *

class Case(Instruccion):
    def __init__(self, linea, columna, exp, code):
        super().__init__(linea, columna)
        self.exp = exp
        self.code = code
    
    def Ejecutar(self, environment):
        print("EJECUTANDO CASE")    
        return self
    