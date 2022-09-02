from ..abstract.expresiones import *
from ..abstract.retorno import *

class Capacity(Expresion):
    def __init__(self, linea, columna, id):
        super().__init__(linea, columna)
        self.id = id

    def Ejecutar(self, environment):
        print("EJECUTANDO CAPACITY AL VECTOR")
        try:
            var = environment.getVariable(self.id)
            if var != None:
                if var.tipado == Type.VECTOR:
                    aux = Retorno()
                    aux.value = var.valor.capacidad
                    aux.tipado = Type.I64
                    return aux
                else:
                    print("ERROR SEMANTICO, LA VARIABLE NO ES UN VECTOR")
            else:
                print("ERROR SEMANTICO, LA VARIABLE NO HA SIDO DECLARADA")
        except:
            print("ERROR SEMANTICO, VECTOR INVALIDO")