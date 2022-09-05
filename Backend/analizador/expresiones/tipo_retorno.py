from ..abstract.expresiones import *
from ..abstract.retorno import *
class Tipo_retorno(Expresion):
    def __init__(self, linea, columna, tipado, isarray1D, isarrayMD, isvector, isstruct):
        super().__init__(linea,columna)
        self.tipado = tipado
        self.isarray1D = isarray1D
        self.isarrayMD = isarrayMD
        self.isvector = isvector
        self.isstruct = isstruct

    def Ejecutar(self, environment):
        try:
            print("EJECUTANDO EL TIPADO DEL RETORNO")
            val = environment.getStruct(self.tipado)
            if val != None:
                if val.tipado == Type.STRUCT:
                    self.isstruct = True
        except:
            print("ERROR SEMANTICO, EL TIPO DE DATO DE RETORNO DE LA FUNCION HA SIDO MAL DECLARADO")


