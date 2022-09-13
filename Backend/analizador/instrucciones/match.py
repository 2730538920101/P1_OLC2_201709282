from .case import *
from ..abstract.instrucciones import *
from ..abstract.retorno import *
from ..symbol.environment import *

class Match(Instruccion):
    def __init__(self, linea, columna, cambio, casos):
        super().__init__(linea, columna)
        self.cambio = cambio
        self.casos = casos

    def Ejecutar(self, environment):
        print("EJECUTANDO MATCH")
        val = self.cambio.Ejecutar(environment)
        for caso in self.casos:
            c = caso.Ejecutar(environment)
            for ex in c.exp:
                if ex != "_":
                    e = ex.Ejecutar(environment)
                    if e.value == val.value:
                        element = c.code.Ejecutar(environment)
                        if isinstance(element, Retorno):
                            if element.tipado == Type.BREAK:
                                break
                            elif element.tipado == Type.RETURN:
                                return element
                            elif element.tipado == Type.CONTINUE:
                                continue

                else:
                    element = c.code.Ejecutar(environment)
                    if isinstance(element, Retorno):
                        if element.tipado == Type.BREAK:
                            break
                        elif element.tipado == Type.RETURN:
                            return element
                        elif element.tipado == Type.CONTINUE:
                            continue
                    