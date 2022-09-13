from ..abstract.instrucciones import *
from ..abstract.retorno import *
from ..expresiones.access import *
from ..reportes.TablaSim import *

class Push(Instruccion):
    def __init__(self, linea, columna, id, exp):
        super().__init__(linea, columna)
        self.id = id
        self.exp = exp

    def Ejecutar(self, environment):
        print("EJECUTANDO PUSH AL VECTOR")
        try:
            if isinstance(self.id, Access):
                self.id = self.id.id
            var = environment.getVariable(self.id)
            if var != None:
                if var.tipado == Type.VECTOR:
                    if var.mutabilidad == True:
                        val = self.exp.Ejecutar(environment)
                        if var.valor.capacidad > len(var.valor.values):
                            var.valor.values.append(val)
                        elif var.valor.capacidad == len(var.valor.values):
                            var.valor.capacidad = var.valor.capacidad * 2
                            var.valor.values.append(val)
                    else:
                        auxer = "ERROR SEMANTICO, LA VARIABLE NO ES MUTABLE"
                        print(auxer)
                        TablaErrores.append(auxer)
                        Prints.append(auxer)
                else:
                    auxer = "ERROR SEMANTICO, LA VARIABLE NO ES UN VECTOR"
                    print(auxer)
                    TablaErrores.append(auxer)
                    Prints.append(auxer)
            else:
                auxer = "ERROR SEMANTICO, LA VARIABLE NO HA SIDO DECLARADA"
                print(auxer)
                TablaErrores.append(auxer)
                Prints.append(auxer)
        except:
            auxer = "ERROR SEMANTICO, VECTOR INVALIDO"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)