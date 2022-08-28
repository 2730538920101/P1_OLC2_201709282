from ..expresiones.generar_struct import *
from ..abstract.instrucciones import *
from ..symbol.environment import *
from ..abstract.retorno import *
from ..symbol.struct import *

class Assigment(Instruccion):
    def __init__(self, linea, columna, id, value, tipado):
        super().__init__(linea, columna)
        self.id = id
        self.value = value
        self.tipado = tipado
    
    def Ejecutar(self, environment):
        print("EJECUTANDO ASSIGMENT")
        try:
            exp = self.value.Ejecutar(environment)
            val = environment.getVariable(self.id)
            if val != None:
                #viene en la tabla de simbolos 
                if self.tipado == Type.NULL:
                    #sentencia no tipada
                    if val.valor == None:
                        #valor nulo declaracion
                        environment.guardarVariables(self.id, exp.value, exp.tipado, val.mutabilidad)
                    else:
                        #valor modificable
                        if val.tipado == exp.tipado:
                            #validar tipos
                            if val.mutabilidad == True:
                                environment.guardarVariables(self.id, exp.value, exp.tipado, val.mutabilidad)
                            else:
                                print("ERROR SEMANTICO, LA VARIABLE NO ES MUTABLE")
                        else:
                            print("ERROR SEMANTICO, NO SE PUEDE ASIGNAR UN VALOR DE DIFERENTE TIPO")
                else:
                    #sentencia tipada
                    if val.valor == None:
                        #valor nulo declaracion
                        if self.tipado == exp.tipado:
                            #validar tipos
                            environment.guardarVariables(self.id, exp.value, exp.tipado, val.mutabilidad)
                        else:
                            print("ERROR SEMANTICO, NO SE PUEDE ASIGNAR UN VALOR DE DIFERENTE TIPO")
                    else:
                        #valor modificable
                        if self.tipado == exp.tipado:
                            if val.mutabilidad == True:
                                environment.guardarVariables(self.id, exp.value, exp.tipado, val.mutabilidad)
                            else:
                                print("ERROR SEMANTICO, LA VARIABLE NO ES MUTABLE")
                        else:
                            print("ERROR SEMANTICO, NO SE PUEDE ASIGNAR UN VALOR DE DIFERENTE TIPO")
            else:
                print("ERROR SEMANTICO, LA VARIABLE NO HA SIDO DECLARADA")
        except:
            print("ERROR SEMANTICO EN LA ASIGNACION")

    
    def getId(self):
        return self.id

    


