from ..abstract.instrucciones import *
from ..abstract.retorno import *
from ..symbol.environment import *

class For(Instruccion):
    def __init__(self, linea, columna, iden, exp2, code):
        super().__init__(linea, columna)
        self.iden = iden
        self.exp2 = exp2
        self.code = code

    def Ejecutar(environment):
        print("EJECUTANDO SENTENCIA FOR IN")