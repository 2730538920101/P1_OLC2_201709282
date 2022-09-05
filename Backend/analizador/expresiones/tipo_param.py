from ..abstract.expresiones import *
from ..abstract.retorno import *
class Tipo_param(Expresion):
    def __init__(self, linea, columna, tipado, isarray1D, isarrayMD, isvector, isstruct):
        super().__init__(linea,columna)
        self.tipado = tipado
        self.isarray1D = isarray1D
        self.isarrayMD = isarrayMD
        self.isvector = isvector
        self.isstruct = isstruct

    def Ejecutar(self, environment):
        try:
            print("EJECUTANDO EL TIPADO DEL PARAMETRO")
            val = environment.getVariable(self.tipado)
            if val != None:
                if val.tipado == Type.STRUCT:
                    self.isstruct = True

        except:
            print("ERROR SEMANTICO, EL TIPO DE DATO DEL ATRIBUTO HA SIDO MAL DECLARADO")


