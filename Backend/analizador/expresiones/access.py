from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..symbol.environment import *


class Access(Expresion):
    def __init__(self, linea, columna, id):
        super().__init__(linea, columna)
        self.id = id

    def Ejecutar(self, environment):
        print("EJECUTANDO ACCESS")
        aux = Retorno()
        if self.id == "_":
            return None
        else:
            valor = environment.getVariable(self.id)
            if valor == None:
                print("ERROR SEMANTICO, VARIABLE NO HA SIDO DECLARADA")
            else:
                aux.__init__(valor.valor, valor.tipado)
            return aux
        