from ..abstract.expresiones import *
from ..abstract.retorno import *

class Array_type(Expresion):
    def __init__(self, linea, columna, tipado, index):
        super().__init__(linea, columna)
        self.tipado = tipado
        self.index = index

    def Ejecuta(self, environment):
        print("EJECUTANDO TYPE ARRAY")
        try:
            var = environment.getStruct(self.tipado)
            if var != None:
                if var.tipado == Type.STRUCT:
                    self.tipado = Type.STRUCT
                
        except:
            print("ERROR SEMANTICO, EL TIPO DEL ARRAY ES INVALIDO")
