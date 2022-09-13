from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..symbol.environment import *
from ..symbol.vector import *
from copy import copy


class Vector_index(Expresion):
    def __init__(self, linea, columna, exp1, exp2):
        super().__init__(linea, columna)
        self.exp1 = exp1
        self.exp2 = exp2

    def Ejecutar(self, environment):
        print("EJECUTANDO INDEX VECTOR")
        aux = Vector()
        aux2 = Retorno()
        index = self.exp2.Ejecutar(environment)
        auxval = self.exp1.Ejecutar(environment)   
        for val in range(index.value):
            aux.values.append(copy(auxval))
        aux.tipado = auxval.tipado
        aux.capacidad = index.value
        aux2.value = aux
        aux2.tipado = Type.VECTOR
        return aux2
                
                



