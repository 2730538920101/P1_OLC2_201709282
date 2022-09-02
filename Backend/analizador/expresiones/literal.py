from mimetypes import init
from ..abstract.expresiones import *
from ..abstract.retorno import *

class Literal(Expresion):
    def __init__(self, linea, columna, valor, tipado):
        super().__init__(linea, columna)
        self.valor = valor
        self.tipado = tipado
    
    def Ejecutar(self, environment):
        print("EJECUTANDO LITERAL")
        aux = Retorno()
        if self.tipado.value[0] == 0:
            aux.__init__(int(self.valor), Type.I64)
        elif self.tipado.value[0] == 1:
            aux.__init__(float(self.valor), Type.F64)
        elif self.tipado.value[0] == 2:
            aux.__init__(str(self.valor), Type.CHAR)
        elif self.tipado.value[0] == 4:
            aux.__init__(str(self.valor), Type.STR)
        elif self.tipado.value[0] == 5:
            aux.__init__(self.valor, Type.BOOL) 
        elif self.tipado.value[0] == 6:
            aux.__init__(self.valor, Type.USIZE)
        elif self.tipado.value[0] == 7:
            aux.__init__(self.valor, Type.STRUCT)
        else:
            aux.__init__(self.valor, Type.NULL)        
        return aux
