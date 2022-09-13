from ..abstract.instrucciones import *
from ..abstract.retorno import *
from ..expresiones.access import *
from ..reportes.TablaSim import *

class Insert(Instruccion):
    def __init__(self, linea, columna, id, exp, indice):
        super().__init__(linea, columna)
        self.id = id
        self.exp = exp
        self.indice = indice

    def Ejecutar(self, environment):
        print("EJECUTANDO INSERT AL VECTOR")
        try:
            if isinstance(self.id, Access):
                self.id = self.id.id
            var = environment.getVariable(self.id)
            if var != None:
                if var.tipado == Type.VECTOR:
                    if var.mutabilidad == True:
                        val = self.exp.Ejecutar(environment)
                        ind = self.indice.Ejecutar(environment)
                        if ind.tipado == Type.I64:
                            if var.valor.capacidad > len(var.valor.values):
                                var.valor.values.insert(ind.value,val)
                            elif var.valor.capacidad == len(var.valor.values):
                                var.valor.capacidad = var.valor.capacidad * 2
                                var.valor.values.insert(ind.value,val)
                        else:
                            auxer = "ERROR SEMANTICO, EL INDICE DEBE SER DE VALOR ENTERO"
                            print(auxer)
                            TablaErrores.append(auxer)
                            Prints.append(auxer)
                    else:
                        auxer = "ERROR SEMANTICO, LA VARIABLE NO ES MUTABLE"
                        print(auxer)
                        TablaErrores.append(auxer)
                        Prints.append(auxer)
                else:
                    auxer = "ERROR SEMANTICO, LA VARIABLE NO ES UN VECTOR"
                    print(auxer)
                    TablaErrores.append(auxer)
                    Prints.append(auxer)
            else:
                auxer = "ERROR SEMANTICO, LA VARIABLE NO HA SIDO DECLARADA"
                print(auxer)
                TablaErrores.append(auxer)
                Prints.append(auxer)
        except:
            auxer = "ERROR SEMANTICO, VECTOR INVALIDO"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)