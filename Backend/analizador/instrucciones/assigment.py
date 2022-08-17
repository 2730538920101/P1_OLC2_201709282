from ..abstract.instrucciones import *
from ..symbol.environment import *
from ..abstract.retorno import *

class Assigment(Instruccion):
    def __init__(self, linea, columna, id, value, tipado):
        super().__init__(linea, columna)
        self.id = id
        self.value = value
        self.tipado = tipado
    
    def Ejecutar(self, environment):
        print("EJECUTANDO ASSIGMENT")
        val = self.value.Ejecutar(environment)
        iden = environment.getVariable(self.id)
        if iden != None:
            if self.tipado == Type.NULL:
                self.tipado = val.tipado        
                if iden.mutabilidad == True:
                    environment.guardarVariables(self.id, val.value, self.tipado, True)
                else:
                    print("ERROR SEMANTICO, LA VARIABLE NO ES MUTABLE")
            else:
                if iden.tipado ==  self.tipado:
                    if iden.mutabilidad == True:
                        environment.guardarVariables(self.id, val.value, val.tipado, True)
                    else:
                        print("ERROR SEMANTICO, LA VARIABLE NO ES MUTABLE")
                else:
                    print("ERROR SEMANTICO, NO PUEDE ASIGNAR UNA EXPRESION DE DIFERENTE TIPO AL QUE LA VARIABLE FUE DECLARADA")
        else:
            print("ERROR SEMANTICO, LA VARIABLE NO HA SIDO DECLARADA")

    def getTipado(self, environment):
        return self.value.Ejecutar(environment).tipado

    def getId(self):
        return self.id

    def getValue(self):
        return self.value
    


