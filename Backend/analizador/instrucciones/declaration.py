from ..abstract.instrucciones import *
from ..abstract.retorno import *
from ..symbol.environment import *
from ..symbol.vector import *

class Declaration(Instruccion):
    def __init__(self, linea, columna, asignacion, tipado, mutabilidad):
        super().__init__(linea, columna)
        self.asignacion = asignacion
        self.tipado = tipado
        self.mutabilidad = mutabilidad
    
    def Ejecutar(self, environment):
        print("EJECUTANDO DECLARATION")
        iden = self.asignacion.getId()
        tipo = self.asignacion.getTipado(environment)
        if not isinstance(self.asignacion.getValue(), Vector):
            val = self.asignacion.getValue().Ejecutar(environment)
            environment.guardarVariables(iden, val, tipo, self.mutabilidad)
            self.asignacion.Ejecutar(environment)
        else:
            environment.guardarVariables(iden, self.asignacion.getValue(), tipo, self.mutabilidad)
            self.asignacion.Ejecutar(environment)
            
        
        