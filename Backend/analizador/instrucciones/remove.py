from ..abstract.instrucciones import *
from ..abstract.retorno import *
from ..expresiones.access import *

class Remove(Instruccion):
    def __init__(self, linea, columna, id, exp):
        super().__init__(linea, columna)
        self.id = id
        self.exp = exp

    def Ejecutar(self, environment):
        print("EJECUTANDO REMOVE AL VECTOR")
        try:
            if isinstance(self.id, Access):
                self.id = self.id.id
            var = environment.getVariable(self.id)
            if var != None:
                if var.tipado == Type.VECTOR:
                    if var.mutabilidad == True:
                        val = self.exp.Ejecutar(environment)
                        if val.tipado == Type.I64:
                            var.valor.values.pop(val.value)
                        else:
                            auxer = "ERROR SEMANTICO, EL INDICE DEBE SER DE TIPO I64"
                            print(auxer)
                            TablaErrores.append(auxer)
                            Prints.append(auxer)
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
            auxer = "ERROR SEMANTICO, VECTOR INVALIDO O EL INDICE SOBREPASA LA CAPACIDAD"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)