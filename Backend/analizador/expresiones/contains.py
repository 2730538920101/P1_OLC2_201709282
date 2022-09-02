from ..abstract.expresiones import *
from ..abstract.retorno import *

class Contains(Expresion):
    def __init__(self, linea, columna, id, exp):
        super().__init__(linea, columna)
        self.id = id
        self.exp = exp

    def Ejecutar(self, environment):
        print("EJECUTANDO CONTAINS AL VECTOR")
        try:
            var = environment.getVariable(self.id)
            if var != None:
                if var.tipado == Type.VECTOR:
                    expresion = self.exp.Ejecutar(environment)
                    aux = Retorno()
                    for val in var.valor.values:
                        if val.value == expresion.value:
                            aux.tipado = Type.BOOL
                            aux.value = True
                            break
                        else:
                            aux.tipado = Type.BOOL
                            aux.value = False
                    return aux
                else:
                    print("ERROR SEMANTICO, LA VARIABLE NO ES UN VECTOR")
            else:
                print("ERROR SEMANTICO, LA VARIABLE NO HA SIDO DECLARADA")
        except:
            print("ERROR SEMANTICO, ERROR AL BUSCAR EN EL VECTOR LA EXPRESION")