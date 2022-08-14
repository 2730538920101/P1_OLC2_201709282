from ..abstract.instrucciones import *
from ..symbol.environment import ClaseSym

class Funcion(Instruccion):
    def __init__(self, linea, columna, id, tipado, statement, parametros):
        super().__init__(linea,columna)
        self.id = id
        self.tipado = tipado
        self.statement = statement
        self.parametros = parametros

    def Ejecutar(self, environment):
        print("EJECUTANDO FUNCION")
        environment.guardarFunciones(self.id, self)
