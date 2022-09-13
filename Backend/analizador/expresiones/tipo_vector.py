from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..reportes.TablaSim import *

class Tipo_vector(Expresion):
    def __init__(self, linea, columna, tipadoel, tipado):
        super().__init__(linea, columna)
        self.tipadoel = tipadoel
        self.tipado = tipado

    def Ejecutar(self, environment):
        print("EJECUTANDO TYPE VECTOR")
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