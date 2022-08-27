from ..abstract.retorno import *
from ..abstract.instrucciones import *
from ..symbol.vector import *
from ..symbol.environment import *

class Vector_assigment_new(Instruccion):
    def __init__(self, linea, columna, id, tipado, capacidad):
        super().__init__(linea, columna)
        self.id = id
        self.tipado = tipado
        self.value = Vector()
        self.capacidad = capacidad

    def Ejecutar(self, environment):
        print("EJECUTANDO NEW VECTOR")
        try:
            self.value.tipado = self.tipado
            var = environment.getVariable(self.id)
            if self.capacidad != None:
                self.value.capacidad = self.capacidad
            if var != None:
                    if var.mutabilidad == True:
                        environment.guardarVariables(self.id, self.value, Type.VECTOR, True)
                    else:
                        environment.guardarVariables(self.id, self.value, Type.VECTOR, False)
            else:
                print("ERROR SEMANTICO, LA VARIABLE NO HA SIDO DECLARADA")
        except:
            print("ERROR SEMANTICO, LA EXPRESION ASIGNADA NO ES UN VECTOR VALIDO")

    def getTipado(self, environment):
        return Type.VECTOR

    def getId(self):
        return self.id

    def getValue(self):
        return self.value