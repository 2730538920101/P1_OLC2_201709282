from ..abstract.instrucciones import *
from ..abstract.retorno import *

class Remove(Instruccion):
    def __init__(self, linea, columna, id, exp):
        super().__init__(linea, columna)
        self.id = id
        self.exp = exp

    def Ejecutar(self, environment):
        print("EJECUTANDO REMOVE AL VECTOR")
        try:
            var = environment.getVariable(self.id)
            if var != None:
                if var.tipado == Type.VECTOR:
                    if var.mutabilidad == True:
                        val = self.exp.Ejecutar(environment)
                        if val.tipado == Type.I64:
                            var.valor.values.pop(val.value)
                        else:
                            print("ERROR SEMANTICO, EL INDICE DEBE SER DE TIPO I64")
                    else:
                        print("ERROR SEMANTICO, LA VARIABLE NO ES MUTABLE")
                else:
                    print("ERROR SEMANTICO, LA VARIABLE NO ES UN VECTOR")
            else:
                print("ERROR SEMANTICO, LA VARIABLE NO HA SIDO DECLARADA")
        except:
            print("ERROR SEMANTICO, VECTOR INVALIDO O EL INDICE SOBREPASA LA CAPACIDAD")