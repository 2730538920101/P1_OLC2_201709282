from ..abstract.instrucciones import *
from ..abstract.retorno import *
from ..symbol.environment import *
from ..symbol.vector import *

class Declaration(Instruccion):
    def __init__(self, linea, columna, asignacion, mutabilidad):
        super().__init__(linea, columna)
        self.asignacion = asignacion
        self.mutabilidad = mutabilidad
    
    def Ejecutar(self, environment):
        print("EJECUTANDO DECLARATION")
        iden = self.asignacion.getId()
        environment.guardarVariables(iden, None, Type.NULL, self.mutabilidad)
        self.asignacion.Ejecutar(environment)
            
        
        