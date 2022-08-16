from ..instrucciones.while_inst import *
from ..abstract.instrucciones import *
from ..symbol.environment import *

class While(Instruccion):
    def __init__(self, linea, columna, condicion, code):
        super().__init__(linea, columna)
        self.condicion = condicion
        self.code = code

    def Ejecutar(self, environment):
        cond = self.condicion.Ejecutar(environment)
        if cond.tipado == Type.BOOL:
            print("ERROR SEMANTICO, NO SE PUEDE EJECUTAR UN CICLO WHILE CON UNA VARIABLE DE TIPO DIFERENTE DE BOOL")
        else:
            while cond.value == True:
                element = self.code.Ejecutar(environment)
                if element != None:
                    if element.tipado == Type.BREAK:
                        break
                    elif element.tipado == Type.CONTINUE:
                        continue
                    else:
                        return element
                cond = self.condicion.Ejecutar(environment)
                if cond.tipado != Type.BOOL:
                    print("ERROR SEMANTICO, NO SE PUEDE EJECUTAR UN CICLO WHILE CON UNA VARIABLE DE TIPO DIFERENTE DE BOOL")
                    

