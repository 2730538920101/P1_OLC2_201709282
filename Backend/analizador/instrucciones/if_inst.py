from ..abstract.instrucciones import *
from ..symbol.environment import *
from ..abstract.retorno import *

class If(Instruccion):
    def __init__(self, linea, columna, condicion, expif, expel = Type.NULL):
        super().__init__(linea, columna)
        self.condicion = condicion
        self.expif = expif
        self.expel = expel

    def Ejecutar(self, environment):
        print("EJECUTANDO SENTENCIA IF")
        cond = self.condicion.Ejecutar(environment)
        if cond.tipado != Type.BOOL:
            print("ERROR SEMANTICO, LA EXPRESION DEBE SER DE TIPO BOOL")
        else:
            if cond.value == True:
                element = self.expif.Ejecutar(environment)
                if element != None:
                    if element.tipado == Type.BREAK:
                        return element
                    elif element.tipado == Type.CONTINUE:
                        pass
                    else:
                        return element
            elif cond.value == False:
                if self.expel != Type.NULL:
                    elemento = self.expel.Ejecutar(environment)
                    if elemento != None:
                        if elemento.tipado == Type.BREAK:
                            return elemento
                        elif elemento.tipado == Type.CONTINUE:
                            pass
                        else:
                            return elemento
                    