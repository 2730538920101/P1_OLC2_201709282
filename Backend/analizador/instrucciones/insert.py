from ..abstract.instrucciones import *
from ..abstract.retorno import *

class Insert(Instruccion):
    def __init__(self, linea, columna, id, exp, indice):
        super().__init__(linea, columna)
        self.id = id
        self.exp = exp
        self.indice = indice

    def Ejecutar(self, environment):
        print("EJECUTANDO INSERT AL VECTOR")
        try:
            var = environment.getVariable(self.id)
            if var != None:
                if var.tipado == Type.VECTOR:
                    if var.mutabilidad == True:
                        val = self.exp.Ejecutar(environment)
                        if val.tipado == var.valor.tipado:
                            ind = self.indice.Ejecutar(environment)
                            if ind.tipado == Type.I64:
                                if var.valor.capacidad > len(var.valor.values):
                                    var.valor.values.insert(ind.value,val)
                                elif var.valor.capacidad == len(var.valor.values):
                                    var.valor.capacidad = var.valor.capacidad * 2
                                    var.valor.values.insert(ind.value,val)
                            else:
                                print("ERROR SEMANTICO, EL INDICE DEBE SER DE VALOR ENTERO")
                        else:
                            print("ERROR SEMANTICO, LA EXPRESION DEBE SER DEL MISMO TIPO DE LA VARIABLE")
                    else:
                        print("ERROR SEMANTICO, LA VARIABLE NO ES MUTABLE")
                else:
                    print("ERROR SEMANTICO, LA VARIABLE NO ES UN VECTOR")
            else:
                print("ERROR SEMANTICO, LA VARIABLE NO HA SIDO DECLARADA")
        except:
            print("ERROR SEMANTICO, VECTOR INVALIDO")