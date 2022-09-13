from ..abstract.instrucciones import *
from ..expresiones.access import *
from ..expresiones.tipo_vector import *
from ..expresiones.array_type import *
from ..reportes.TablaSim import *

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
        if isinstance(self.tipado, Access):
            tip = self.tipado.Ejecutar(environment)
            if tip != None:
                self.tipado == Type.STRUCT
            else:
                auxer = "ERROR SEMANTICO, EL STRUCT DEL TIPO DE RETORNO DE LA FUNCION NO HA SIDO DECLARADO"
                print(auxer)
                TablaErrores.append(auxer)
                Prints.append(auxer)
        elif isinstance(self.tipado, Tipo_vector) or isinstance(self.tipado, Array_type):
            tip = self.tipado.Ejecutar(environment)
            self.tipado == tip.tipado
        auxpar = []
        for p in self.parametros:
            p = p.Ejecutar(environment)
            if p != None:
                auxpar.append(p)
            else:
                auxpar = None
                break
        self.parametros = auxpar
        environment.guardarFunciones(self.id, self, self.mutabilidad)
