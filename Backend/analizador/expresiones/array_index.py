from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..symbol.environment import *
from ..symbol.array import *
from copy import copy


class Array_index(Expresion):
    def __init__(self, linea, columna, exp1, exp2):
        super().__init__(linea, columna)
        self.exp1 = exp1
        self.exp2 = exp2

    def Ejecutar(self, environment):
        print("EJECUTANDO INDEX ARRAY")
        aux = Arreglo()
        aux2 = Retorno()
        index = self.exp2.Ejecutar(environment)
        if index.tipado != Type.I64:
            print("ERROR SEMANTICO, EL INDICE NO ES UN VALOR NUMERICO")
        else:
            auxval = self.exp1.Ejecutar(environment)
            for val in range(index.value):
                aux.values.append(copy(auxval))
            aux.tipado = auxval.tipado
            aux2.value = aux
            aux2.tipado = Type.ARRAY
        return aux2
                
                



