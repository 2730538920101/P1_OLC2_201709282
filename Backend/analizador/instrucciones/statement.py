from ..abstract.instrucciones import *
from ..symbol.environment import *
from ..reportes.TablaSim import *

class Statement(Instruccion):
    def __init__(self, linea, columna, code):
        super().__init__(linea, columna)
        self.code = code

    def Ejecutar(self, environment):
        print("EJECUTANDO STATEMENT")
        env = Entorno(environment)
        for instr in self.code:
            if instr != None:
                if isinstance(instr, list):
                    for x in instr:
                        if x != None:
                            el = x.Ejecutar(env)
                            if isinstance(el, Retorno):
                                return el
                else:
                    element = instr.Ejecutar(env)
                    if isinstance(element, Retorno):
                        return element
        

