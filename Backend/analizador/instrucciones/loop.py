from ..abstract.instrucciones import *
from ..symbol.environment import *

class Loop(Instruccion):
    def __init__(self, linea, columna, code):
        super().__init__(linea, columna)
        self.code = code

    def Ejecutar(self, environment):
        print("EJECUTANDO SENTENCIA LOOP")
        while True:
            self.code.Ejecutar(environment)
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
           

