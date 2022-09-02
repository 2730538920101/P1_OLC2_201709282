from ..abstract.instrucciones import *
from ..abstract.retorno import *


class Struct_assigment(Instruccion):
    def __init__(self, linea, columna, id, atributo, exp):
        super().__init__(linea, columna)
        self.id = id
        self.atributo = atributo
        self.exp = exp 

    def Ejecutar(self, environment):
        print("EJECUTANDO STRUCT ASSIGMENT")
        try:
            var = environment.getVariable(self.id)
            if var != None:
                if var.tipado == Type.STRUCT:
                    if var.mutabilidad == True:
                        id_index = var.valor.atributos.index(self.atributo)
                        tip = var.valor.tipados[id_index]
                        if self.exp.Ejecutar(environment).tipado == tip:
                            var.valor.valores[id_index] = self.exp.Ejecutar(environment).value
                        else:
                            print("ERROR SEMANTICO, LA EXPRESION DEBE SER DEL MISMO TIPO DEL ATRIBUTO")
                    else:
                        print("ERROR SEMANTICO, EL STRUCT NO ES MUTABLE")
                else:
                    print("ERROR SEMANTICO, LA VARIABLE NO ES DE TIPO STRUCT")
            else:
                print("ERROR SEMANTICO, LA VARIABLE NO HA SIDO DECLARADA")
        except:
            print("ERROR SEMANTICO, EL STRUCT O ALGUNO DE LOS ATRIBUTOS NO ES VALIDO")