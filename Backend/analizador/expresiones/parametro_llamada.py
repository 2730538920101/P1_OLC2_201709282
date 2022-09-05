from ..abstract.expresiones import *
from ..abstract.retorno import *

class Parametro_llamada(Expresion):
    def __init__(self, linea, columna, exp, isref):
        super().__init__(linea, columna)
        self.exp = exp
        self.isref = isref

    def Ejecutar(self, environment):
        print("EJECUTANDO PARAMETRO LLAMADA")
        try:
            val = self.exp.Ejecutar(environment)
            if val.tipado == Type.ARRAY or val.tipado == Type.VECTOR or val.tipado == Type.STRUCT:
                if self.isref == True:
                    return self
                else:
                    print("ERROR SEMANTICO, SOLO LOS VECTORES, ARRAYS Y STRUCTS SON PASADOS COMO REFERENCIA")
            else:
                if self.isref == False:
                    return self
                else:
                    print("ERROR SEMANTICO, SOLO LOS VECTORES, ARRAYS Y STRUCTS SON PASADOS COMO REFERENCIA")
        except:
            print("ERROR SEMANTICO, PARAMETRO INVALIDO")
