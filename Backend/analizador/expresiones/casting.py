from .access import Access
from ..abstract.expresiones import *
from ..symbol.environment import *
from ..abstract.retorno import *

class Casting(Expresion):
    def __init__(self, linea, columna, exp, tipado):
        super().__init__(linea, columna)
        self.exp = exp
        self.tipado = tipado

    def Ejecutar(self, environment):
        print("EJECUTANDO UN CASTING")
        if isinstance(self.exp, Access):
            val = self.exp.Ejecutar(environment).value
        else:
            val = self.exp.Ejecutar(environment)
        aux = Retorno()
        if self.tipado == Type.I64:
            if val.tipado == self.tipado:
                print("ERROR SEMANTICO, NO PUEDE CONVERTIR EL VALOR SI YA POSEE EL TIPO DE DATO ESPECIFICADO")
            elif val.tipado == Type.F64:
                aux.tipado = Type.I64
                aux.value = int(val.value)
        elif self.tipado == Type.F64:
            if val.tipado == self.tipado:
                print("ERROR SEMANTICO, NO PUEDE CONVERTIR EL VALOR SI YA POSEE EL TIPO DE DATO ESPECIFICADO")
            elif val.tipado == Type.I64:
                aux.tipado = Type.F64
                aux.value = float(val.value)
        else:
            print("ERROR SEMANTICO, NO SE PUEDE CASTEAR ENTRE EL TIPO DE DATO DE LA EXPRESION Y EL TIPO DE DATO INDICADO")
        return aux