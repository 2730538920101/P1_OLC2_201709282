from ..abstract.instrucciones import *
from ..abstract.retorno import *
from ..symbol.environment import *

class Declaration(Instruccion):
    def __init__(self, linea, columna, asignacion, tipado = Type.NULL, mutabilidad = False):
        super().__init__(linea, columna)
        self.asignacion = asignacion
        self.tipado = tipado
        self.mutabilidad = mutabilidad
    
    def Ejecutar(self, environment):
        print("EJECUTANDO DECLARATION")
        iden = self.asignacion.getId()
        tipo = self.asignacion.getTipado(environment)
        if self.tipado == Type.NULL:
            self.tipado = tipo
            environment.guardarVariables(iden, None, self.tipado, self.mutabilidad)
            self.asignacion.Ejecutar(environment)
        else:
            if tipo == self.tipado:
                environment.guardarVariables(iden, None, self.tipado, self.mutabilidad)
                self.asignacion.Ejecutar(environment)
            else:
                print("ERROR SEMANTICO, EL TIPO DE DATO DE LA DECLARACION NO COINCIDE CON EL TIPO DE DATO DE LA EXPRESION ASIGNADA")
        
        