from ..abstract.expresiones import *
from ..abstract.retorno import *

class Parametros_declaracion(Expresion):
    def __init__(self, linea, columna, id, tipado):
        super().__init__(linea, columna)
        self.id = id
        self.tipado = tipado

    def Ejecutar(self, environment):
        print("EJECUTANDO PARAMETROS DE FUNCION")
        try:
            self.tipado.Ejecutar(environment)
        except:
            print("ERROR SEMANTICO, NO SE PUEDE DECLARAR EL PARAMETRO")
