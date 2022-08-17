from ..abstract.instrucciones import *
from ..symbol.environment import *

class Case(Instruccion):
    def __init__(self, linea, columna, exp, code):
        super().__init__(linea, columna)
        self.exp = exp
        self.code = code
    
    def Ejecutar(self, environment):
        element = self.code.Ejecutar(environment)
        if element != None:
            return element

    def getExp(self):
        return self.exp

    
    