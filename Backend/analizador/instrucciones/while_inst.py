from ..instrucciones.while_inst import *
from ..abstract.instrucciones import *
from ..symbol.environment import *

class While(Instruccion):
    def __init__(self, linea, columna, condicion, code):
        super().__init__(linea, columna)
        self.condicion = condicion
        self.code = code

    def Ejecutar(self, environment):  
        sigue = True
        while sigue == True:
            self.condicion.Ejecutar(environment)
            if self.condicion.Ejecutar(environment).tipado != Type.BOOL:
                if self.condicion.Ejecutar(environment).value:
                    element = self.code.Ejecutar(environment)
                    if element != None:
                        if element.tipado == Type.BREAK:
                            sigue = False
                            break
                        elif element.tipado == Type.CONTINUE:
                            continue
                        else:
                            sigue = False
                            break
                else:
                    sigue = False
            else:
                sigue = False        

