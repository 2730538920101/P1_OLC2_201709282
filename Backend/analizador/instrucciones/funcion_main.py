from ..abstract.instrucciones import *

class Funcion_main(Instruccion):
    def __init__(self, linea, columna, code):
        super().__init__(linea, columna)
        self.code = code

    def Ejecutar(self, environment):
        print("EJECUTANDO FUNCION MAIN")
        self.code.Ejecutar(environment)
        