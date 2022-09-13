from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..symbol.environment import *
from ..reportes.TablaSim import *

class Access(Expresion):
    def __init__(self, linea, columna, id):
        super().__init__(linea, columna)
        self.id = id

    def Ejecutar(self, environment):
        print("EJECUTANDO ACCESS")
        
        aux = Retorno()
        valor = environment.getVariable(self.id)
        if valor == None:
            auxer = "ERROR SEMANTICO, VARIABLE NO HA SIDO DECLARADA"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)
        else:
            aux.__init__(valor.valor, valor.tipado)
        return aux
        