from ..abstract.instrucciones import *
from ..symbol.environment import *
from ..abstract.retorno import *

class Assigment(Instruccion):
    def __init__(self, linea, columna, id, value, tipado = Type.NULL):
        super().__init__(linea, columna)
        self.id = id
        self.value = value
        self.tipado = tipado
    
    def Ejecutar(self, environment):
        print("EJECUTANDO ASSIGMENT")
        val = self.value.Ejecutar(environment)
        iden = environment.getVariable(self.id)
        tip = environment.getVariable(self.id)
        if iden == None or tip == None:
            print("ERROR SEMANTICO, LA VARIABLE NO HA SIDO DECLARADA")
        else:
            if self.tipado == Type.NULL:
                self.tipado = val.tipado
                environment.guardarVariables(self.id, val.value, self.tipado)
            else:
                if tip.tipado ==  self.tipado:
                    environment.guardarVariables(self.id, val.value, val.tipado)
                else:
                    print("ERROR SEMANTICO, NO PUEDE ASIGNAR UNA EXPRESION DE DIFERENTE TIPO AL QUE LA VARIABLE FUE DECLARADA")

    def getTipado(self, environment):
        return self.value.Ejecutar(environment).tipado

    def getId(self):
        return self.id
    


