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
            try:
                element = instr.Ejecutar(env)
                if element != None:
                    return element
            except:
                print("ERROR DE SEMANTICO EN EL ENTORNO")

