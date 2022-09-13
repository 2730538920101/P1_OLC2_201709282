from ..expresiones.generar_struct import *
from ..abstract.instrucciones import *
from ..symbol.environment import *
from ..abstract.retorno import *
from ..symbol.struct import *
from ..expresiones.tipo_vector import *
from ..expresiones.array_type import *
from ..reportes.TablaSim import *

class Assigment(Instruccion):
    def __init__(self, linea, columna, id, value, tipado):
        super().__init__(linea, columna)
        self.id = id
        self.value = value
        self.tipado = tipado
    
    def Ejecutar(self, environment):
        global TablaErrores
        global Prints
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
                                auxer = "ERROR SEMANTICO, LA VARIABLE NO ES MUTABLE"
                                print(auxer)
                                TablaErrores.append(auxer)
                                Prints.append(auxer)
                        elif val.tipado == Type.USIZE and exp.tipado == Type.I64:
                            if val.mutabilidad == True:
                                environment.guardarVariables(self.id, exp.value, exp.tipado, val.mutabilidad)
                            else:
                                auxer = "ERROR SEMANTICO, LA VARIABLE NO ES MUTABLE"
                                print(auxer)
                                TablaErrores.append(auxer)
                                Prints.append(auxer)
                        else:
                            auxer = "ERROR SEMANTICO, NO SE PUEDE ASIGNAR UN VALOR DE DIFERENTE TIPO"
                            print(auxer)
                            TablaErrores.append(auxer)
                            Prints.append(auxer)
                else:
                    #sentencia tipada
                    if val.valor == None:
                        #valor nulo declaracion
                        if isinstance(self.tipado, Tipo_vector) and exp.tipado == Type.VECTOR:
                            tip = self.tipado.Ejecutar(environment)
                            environment.guardarVariables(self.id, exp.value, exp.tipado, val.mutabilidad)
                        elif isinstance(self.tipado, Array_type) and exp.tipado == Type.ARRAY:
                            environment.guardarVariables(self.id, exp.value, exp.tipado, val.mutabilidad)
                        elif (self.tipado == exp.tipado):
                            #validar tipos
                            environment.guardarVariables(self.id, exp.value, exp.tipado, val.mutabilidad)
                        elif self.tipado == Type.USIZE and exp.tipado == Type.I64:
                            environment.guardarVariables(self.id, exp.value, self.tipado, val.mutabilidad)
                        else:
                            auxer = "ERROR SEMANTICO, NO SE PUEDE ASIGNAR UN VALOR DE DIFERENTE TIPO"
                            print(auxer)
                            TablaErrores.append(auxer)
                            Prints.append(auxer)
                    else:
                        if val.mutabilidad == True:
                        #valor modificable
                            if isinstance(self.tipado, Tipo_vector) and exp.tipado == Type.VECTOR:
                                environment.guardarVariables(self.id, exp.value, exp.tipado, val.mutabilidad)
                            elif isinstance(self.tipado, Array_type) and exp.tipado == Type.ARRAY:
                                environment.guardarVariables(self.id, exp.value, exp.tipado, val.mutabilidad)
                            elif self.tipado == exp.tipado:
                                environment.guardarVariables(self.id, exp.value, exp.tipado, val.mutabilidad)
                            elif self.tipado == Type.USIZE and exp.tipado == Type.I64:
                                environment.guardarVariables(self.id, exp.value, self.tipado, val.mutabilidad)
                            else:
                                auxer = "ERROR SEMANTICO, NO SE PUEDE ASIGNAR UN VALOR DE DIFERENTE TIPO"
                                print(auxer)
                                TablaErrores.append(auxer)
                                Prints.append(auxer)
                        else:
                                auxer = "ERROR SEMANTICO, LA VARIABLE NO ES MUTABLE"
                                print(auxer)
                                TablaErrores.append(auxer)
                                Prints.append(auxer)
            else:
                auxer = "ERROR SEMANTICO, LA VARIABLE NO HA SIDO DECLARADA"
                print(auxer)
                TablaErrores.append(auxer)
                Prints.append(auxer)
        except:
            auxer = "ERROR SEMANTICO EN LA ASIGNACION"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)

    
    def getId(self):
        return self.id

    


