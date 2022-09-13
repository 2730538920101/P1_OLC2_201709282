from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..expresiones.tipo_vector import *
from ..expresiones.array_type import *
from ..reportes.TablaSim import *

class Parametros_declaracion(Expresion):
    def __init__(self, linea, columna, id, tipado, isref):
        super().__init__(linea, columna)
        self.id = id
        self.tipado = tipado
        self.isref = isref

    def Ejecutar(self, environment):
        print("EJECUTANDO PARAMETROS DE FUNCION")
        if (isinstance(self.tipado, Tipo_vector) or isinstance(self.tipado, Array_type) or self.tipado == Type.STRUCT) and self.isref == True:
            return self
        elif ((self.tipado == Type.I64) or (self.tipado == Type.F64) or (self.tipado == Type.STRING) or (self.tipado == Type.STR) or (self.tipado == Type.CHAR) or (self.tipado == Type.BOOL) or (self.tipado == Type.USIZE)) and (self.isref == False):
            return self
        else:
            auxer = "ERROR SEMANTICO, LOS PARAMETROS DE TIPO ARRAY, VECTOR O STRUCT DEBEN SER PASADOS POR REFERENCIA Y LOS DEMAS TIPOS POR VALOR"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)
            return None