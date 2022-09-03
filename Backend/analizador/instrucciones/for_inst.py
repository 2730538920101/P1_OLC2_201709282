from ..abstract.instrucciones import *
from ..abstract.retorno import *
from ..symbol.environment import *

class For(Instruccion):
    def __init__(self, linea, columna, iden, exp2, code):
        super().__init__(linea, columna)
        self.iden = iden
        self.exp2 = exp2
        self.code = code

    def Ejecutar(self,environment):
        print("EJECUTANDO SENTENCIA FOR IN")
        try:
            varlist = self.exp2.Ejecutar(environment)
            if varlist.tipado == Type.ARRAY or varlist.tipado == Type.VECTOR:
                for x in varlist.value.values:
                    environment.guardarVariables(self.iden, x.value, x.tipado, True)
                    element = self.code.Ejecutar(environment)
                    if element != None:
                        if element.tipado == Type.BREAK:
                            break
                        elif element.tipado == Type.CONTINUE:
                            continue
                        else:
                            break
            else:
                print("ERROR SEMANTICO, SOLO SE PUEDEN ITERAR EXPRESIONES DE TIPO ARRAY O VECTOR")
        except:
            print("ERROR SEMANTICO, LA SENTENCIA FOR IN NO ES VALIDA")