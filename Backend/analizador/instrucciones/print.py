from ..abstract.instrucciones import *
from ..abstract.retorno import *
from ..symbol.array import *
from ..symbol.vector import *
from ..reportes.TablaSim import *

class Println(Instruccion):
    def __init__(self, linea, columna, exp):
        super().__init__(linea, columna)
        self.exp = exp

    def Ejecutar(self, environment):
        print("EJECUTANDO PRINTLN")
        for e in self.exp:
            aux = e.Ejecutar(environment)
            if isinstance(aux, Retorno):
                if isinstance(aux.value, Arreglo) or isinstance(aux.value, Vector):
                    self.Imprimir_arr(aux.value)
                else:
                    print(aux.value)
                    Prints.append(aux.value)

                


    def Imprimir_arr(self, arr):
        arr = arr.values
        for x in arr:
            if isinstance(x.value, Arreglo) or isinstance(x.value, Vector):
                self.Imprimir_arr(x.value)
            else:
                print(x.value)
                Prints.append(x.value)
        
