from ..abstract.instrucciones import *
from ..abstract.retorno import *

class Push(Instruccion):
    def __init__(self, linea, columna, id, exp):
        super().__init__(linea, columna)
        self.id = id
        self.exp = exp

    def Ejecutar(self, environment):
        print("EJECUTANDO PUSH AL VECTOR")
        try:
            var = environment.getVariable(self.id)
            if var != None:
                if var.tipado == Type.VECTOR:
                    if var.mutabilidad == True:
                        val = self.exp.Ejecutar(environment)
                        if val.tipado == var.valor.tipado:
                            if var.valor.capacidad > len(var.valor.values):
                                var.valor.values.append(val)
                            elif var.valor.capacidad == len(var.valor.values):
                                var.valor.capacidad = var.valor.capacidad * 2
                                var.valor.values.append(val)
                        else:
                            print("ERROR SEMANTICO, LA EXPRESION DEBE SER DEL MISMO TIPO DE LA VARIABLE")
                    else:
                        print("ERROR SEMANTICO, LA VARIABLE NO ES MUTABLE")
                else:
                    print("ERROR SEMANTICO, LA VARIABLE NO ES UN VECTOR")
            else:
                print("ERROR SEMANTICO, LA VARIABLE NO HA SIDO DECLARADA")
        except:
            print("ERROR SEMANTICO, VECTOR INVALIDO")