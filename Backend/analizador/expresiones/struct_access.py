from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..reportes.TablaSim import *
from ..symbol.struct import *

class Struct_access(Expresion):
    def __init__(self, linea, columna, expl):
        super().__init__(linea, columna)
        self.expl = expl

    def Ejecutar(self,environment):
        print("EJECUTANDO STRUCT ACCESS")
        
         

       
            

    
        