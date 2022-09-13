from ..symbol.symbol import Symbol
from ..abstract.instrucciones import *
from ..abstract.retorno import *
from ..symbol.array import * 
from ..symbol.vector import *
from ..reportes.TablaSim import *

class Access_assigment(Instruccion):
    def __init__(self, linea, columna, id, indices, exp):
        super().__init__(linea, columna)
        self.id = id
        self.indices = indices
        self.exp = exp

    def Ejecutar(self, environment):
        print("EJECUTANDO ACCESS ASSIGMENT")
        try:
            expaux = self.exp.Ejecutar(environment)
            val = environment.getVariable(self.id)
            if val.tipado == Type.VECTOR or val.tipado == Type.ARRAY:
                if val.mutabilidad == True:
                    auxval = val.valor
                    for x in range(len(self.indices)):
                        tip = self.indices[x].Ejecutar(environment)
                        if tip.tipado == Type.I64 or tip.tipado == Type.USIZE:
                            if len(self.indices) == 1:
                                auxval.values[tip.value] = expaux
                            else:
                                if x <= len(self.indices)-2:
                                    auxval = auxval.values[tip.value].value
                                else:
                                    auxval.values[tip.value] = expaux
                        else:
                            auxer = "ERROR SEMANTICO, EL INDICE DEBE SER DE TIPO I64"
                            print(auxer)
                            TablaErrores.append(auxer)
                            Prints.append(auxer)
                else:
                    auxer = "ERROR SEMANTICO, EL ARREGLO O VECTOR NO ES MUTABLE"
                    print(auxer)
                    TablaErrores.append(auxer)
                    Prints.append(auxer)
            else:
                auxer = "ERROR SEMANTICO, EL ARREGLO O VECTOR NO ES VALIDO"
                print(auxer)
                TablaErrores.append(auxer)
                Prints.append(auxer)
        except:
            auxer = "ERROR SEMANTICO, NO SE PUEDE ASIGNAR UN VALOR AL ARREGLO O VECTOR"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)


   