from ..instrucciones.while_inst import *
from ..abstract.instrucciones import *
from ..symbol.environment import *

class While(Instruccion):
    def __init__(self, linea, columna, condicion, code):
        super().__init__(linea, columna)
        self.condicion = condicion
        self.code = code

    def Ejecutar(self, environment):
        print("EJECUTANDO SENTENCIA WHILE")  
        sigue = True
        while sigue == True:
            cond = self.condicion.Ejecutar(environment)
            if cond.tipado == Type.BOOL:
                if cond.value:
                    element = self.code.Ejecutar(environment)
                    if element != None:
                        if element.tipado == Type.BREAK:
                            sigue = False
                            break
                        elif element.tipado == Type.CONTINUE:
                            sigue = True
                            continue
                        elif element.tipado == Type.RETURN:
                            sigue = False
                            return element
                        else:
                            sigue = False
                            return element
                else:
                    sigue = False
                    break
            else:
                sigue = False
                break        

