from ..abstract.instrucciones import *
from ..abstract.retorno import *
from ..symbol.environment import *

class Continue(Instruccion):
    def __init__(self, linea, columna, tipado):
        super().__init__(linea, columna)
        self.tipado = tipado

    def Ejecutar(self, environment):
        return {'linea': self.linea, 'columna' : self.columna, 'tipado': self.tipado}
    

