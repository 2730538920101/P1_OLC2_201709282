from ..abstract.expresiones import *
from ..abstract.retorno import *

class Literal(Expresion):
    def __init__(self, linea, columna, valor, tipado):
        super().__init__(linea, columna)
        self.valor = valor
        self.tipado = tipado
    
    def Ejecutar(self, environment):
        aux = Retorno()
        if self.tipado.value[0] == 0:
            aux.setReturnValue(self.valor, Type.I64)
        elif self.tipado.value[0] == 1:
            aux.setReturnValue(self.valor, Type.F64)
        elif self.tipado.value[0] == 2:
            aux.setReturnValue(self.valor, Type.CHAR)
        elif self.tipado.value[0] == 3:
            aux.setReturnValue(self.valor, Type.STRING)
        elif self.tipado.value[0] == 4:
            aux.setReturnValue(self.valor, Type.STR)
        elif self.tipado.value[0] == 5:
            aux.setReturnValue(self.valor, Type.BOOL) 
        elif self.tipado.value[0] == 6:
            aux.setReturnValue(self.valor, Type.USIZE)
        elif self.tipado.value[0] == 7:
            aux.setReturnValue(self.valor, Type.STRUCT)
        else:
            aux.setReturnValue(self.valor, Type.NULL)        
        return aux
