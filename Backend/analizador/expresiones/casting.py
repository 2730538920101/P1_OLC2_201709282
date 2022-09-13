from .access import Access
from ..abstract.expresiones import *
from ..symbol.environment import *
from ..abstract.retorno import *
from ..reportes.TablaSim import *

class Casting(Expresion):
    def __init__(self, linea, columna, exp, tipado):
        super().__init__(linea, columna)
        self.exp = exp
        self.tipado = tipado

    def Ejecutar(self, environment):
        print("EJECUTANDO UN CASTING")
        val = self.exp.Ejecutar(environment)
        aux = Retorno()
        if self.tipado == Type.I64:
            if val.tipado == self.tipado:
                auxer = "ERROR SEMANTICO, NO PUEDE CONVERTIR EL VALOR SI YA POSEE EL TIPO DE DATO ESPECIFICADO"
                print(auxer)
                TablaErrores.append(auxer)
                Prints.append(auxer)
            elif val.tipado == Type.F64:
                aux.tipado = Type.I64
                aux.value = int(val.value)
        elif self.tipado == Type.F64:
            if val.tipado == self.tipado:
                auxer = "ERROR SEMANTICO, NO PUEDE CONVERTIR EL VALOR SI YA POSEE EL TIPO DE DATO ESPECIFICADO"
                print(auxer)
                TablaErrores.append(auxer)
                Prints.append(auxer)
            elif val.tipado == Type.I64:
                aux.tipado = Type.F64
                aux.value = float(val.value)
        else:
            auxer = "ERROR SEMANTICO, NO SE PUEDE CASTEAR ENTRE EL TIPO DE DATO DE LA EXPRESION Y EL TIPO DE DATO INDICADO"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)
        return aux