from ..abstract.instrucciones import *
from ..abstract.retorno import *
from ..symbol.environment import *
from ..reportes.TablaSim import *

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
                        elif element.tipado == Type.RETURN:
                            return element
                        else:
                            return element
            else:
                auxer = "ERROR SEMANTICO, SOLO SE PUEDEN ITERAR EXPRESIONES DE TIPO ARRAY O VECTOR"
                print(auxer)
                TablaErrores.append(auxer)
                Prints.append(auxer)
        except:
            auxer = "ERROR SEMANTICO, LA SENTENCIA FOR IN NO ES VALIDA"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)