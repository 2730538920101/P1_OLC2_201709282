from ..symbol.symbol import Symbol
from ..abstract.instrucciones import *
from ..abstract.retorno import *
from ..symbol.array import * 
from ..symbol.vector import *

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
                        if self.indices[x].tipado == Type.I64:
                            if len(self.indices) == 1:
                                auxval[self.indices[x].valor] = expaux
                            else:
                                auxval = auxval[self.indices[x].valor]
                                if auxval.tipado == Type.ARRAY or auxval.tipado == Type.VECTOR:
                                    auxval = auxval.value.values
                                else:
                                    auxval.value = expaux.value
                        else:
                            print("ERROR SEMANTICO, EL INDICE DEBE SER DE TIPO I64")
                else:
                    print("ERROR SEMANTICO, EL ARREGLO O VECTOR NO ES MUTABLE")
            else:
                print("ERROR SEMANTICO, EL ARREGLO O VECTOR NO ES VALIDO")
        except:
            print("ERROR SEMANTICO, NO SE PUEDE ASIGNAR UN VALOR AL ARREGLO O VECTOR")


   