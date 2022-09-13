from ..abstract.instrucciones import *
from ..abstract.retorno import *


class Struct_assigment(Instruccion):
    def __init__(self, linea, columna, expl, exp):
        super().__init__(linea, columna)
        self.expl = expl
        self.exp = exp 

    def Ejecutar(self, environment):
        print("EJECUTANDO STRUCT ASSIGMENT")
        for e1 in self.exp1:
            print(e1)
        
        for e2 in self.exp:
            print(e2)
