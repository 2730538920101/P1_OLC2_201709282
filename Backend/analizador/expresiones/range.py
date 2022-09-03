from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..symbol.array import *

class Range(Expresion):
    def __init__(self, linea, columna, exp1, exp2):
        super().__init__(linea, columna)
        self.exp1 = exp1
        self.exp2 = exp2

    def Ejecutar(self, environment):
        print("EJECUTANDO RANGE")
        try:
            val1 = self.exp1.Ejecutar(environment)
            val2 = self.exp2.Ejecutar(environment)
            if val1 != None and val2 != None:
                if val1.tipado == Type.I64 and val2.tipado == Type.I64:
                    aux = Retorno()
                    arr = Arreglo()
                    valaux = list(range(val1.value, val2.value))
                    for val in valaux:
                        ret = Retorno()
                        ret.tipado = Type.I64
                        ret.value = val
                        arr.values.append(ret)
                    arr.tipado = Type.I64
                    aux.value = arr
                    aux.tipado = Type.ARRAY
                    return aux
                else:
                    print("ERROR SEMANTICO, LAS EXPRESIONES INGRESADAS DEBEN DE SER DE TIPO I64")
            else:
                print("ERROR SEMANTICO, LAS EXPRESIONES INGRESADAS NO SON VALIDAS")
        except:
            print("ERROR SEMANTICO, NO SE PUEDE EJECUTAR EL RANGE")