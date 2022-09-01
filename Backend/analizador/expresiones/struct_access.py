from ..abstract.expresiones import *
from ..abstract.retorno import *

class Struct_access(Expresion):
    def __init__(self, linea, columna, id, atributo):
        super().__init__(linea, columna)
        self.id = id
        self.atributo = atributo

    def Ejecutar(self,environment):
        print("EJECUTANDO STRUCT ACCESS")
