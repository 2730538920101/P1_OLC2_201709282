from ..expresiones.tipo_param import *
from ..abstract.instrucciones import *
from ..expresiones.tipo_retorno import *

class Funcion(Instruccion):
    def __init__(self, linea, columna, id, tipado, statement, parametros, mutabilidad):
        super().__init__(linea,columna)
        self.id = id
        self.tipado = tipado
        self.statement = statement
        self.parametros = parametros
        self.mutabilidad = mutabilidad
        

    def Ejecutar(self, environment):
        print("EJECUTANDO FUNCION")
        if isinstance(self.tipado, Tipo_retorno):
            self.tipado.Ejecutar(environment)
        else:
            var = environment.getVariable(self.tipado)
            if var != None:
                if var.tipado == Type.STRUCT:
                    self.tipado = Type.STRUCT
            for par in self.parametros:
                par.Ejecutar(environment)
        environment.guardarFunciones(self.id, self, self.mutabilidad)
