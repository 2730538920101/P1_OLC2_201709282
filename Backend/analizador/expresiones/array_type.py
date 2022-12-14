from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..reportes.TablaSim import *

class Array_type(Expresion):
    def __init__(self, linea, columna, tipado, tipadoel, index):
        super().__init__(linea, columna)
        self.tipado = tipado
        self.tipadoel = tipadoel
        self.index = index

    def Ejecutar(self, environment):
        print("EJECUTANDO TYPE ARRAY")
        
        try:
            var = environment.getStruct(self.tipadoel)
            if var != None:
                if var.tipado == Type.STRUCT:
                    self.tipadoel = Type.STRUCT
            return self
        except:
            auxer = "ERROR SEMANTICO, EL TIPO DEL ARRAY ES INVALIDO"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)
