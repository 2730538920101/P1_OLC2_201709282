from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..reportes.TablaSim import *

class Parametro_llamada(Expresion):
    def __init__(self, linea, columna, exp, isref):
        super().__init__(linea, columna)
        self.exp = exp
        self.isref = isref

    def Ejecutar(self, environment):
        print("EJECUTANDO PARAMETRO LLAMADA")
        try:
            val = self.exp.Ejecutar(environment)
            if (val.tipado == Type.ARRAY) or (val.tipado == Type.VECTOR) or (val.tipado == Type.STRUCT):
                if self.isref == True:
                    return self
                else:
                    return None
            elif (val.tipado == Type.I64) or (val.tipado == Type.F64) or (val.tipado == Type.STRING) or (val.tipado == Type.STR) or (val.tipado == Type.CHAR) or (val.tipado == Type.BOOL) or (val.tipado == Type.USIZE): 
                if self.isref == False:
                    return self
                else:
                    return None
        except:
            auxer = "ERROR SEMANTICO, PARAMETRO INVALIDO"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)
