from ..abstract.instrucciones import *
from ..symbol.environment import *
from ..abstract.retorno import *

class Break(Instruccion):
    def __init__(self, linea, columna, exp, tipado):
        super().__init__(linea, columna)
        self.exp = exp
        self.tipado = tipado
    
    def Ejecutar(self, environment):
        aux = Retorno()
        if self.exp != None:
            val = self.exp.Ejecutar(environment)
            aux.tipado = self.tipado
            aux.value = val
            return aux
        
        