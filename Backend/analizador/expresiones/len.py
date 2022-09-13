from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..symbol.array import *
from ..symbol.vector import *
from ..expresiones.access import *
from ..expresiones.access_index import *
from ..reportes.TablaSim import *

class Len(Expresion):
    def __init__(self, linea, columna, id):
        super().__init__(linea, columna)
        self.id = id

    def Ejecutar(self, environment):
        print("EJECUTANDO LEN AL VECTOR")
        try:
            if isinstance(self.id, Access_index):
                arr = self.id.Ejecutar(environment)
                if arr != None:
                    if arr.tipado == Type.VECTOR or arr.tipado == Type.ARRAY:
                        aux = Retorno()
                        if isinstance(arr.value, Arreglo) or isinstance(arr.value, Vector):
                            aux.value = len(arr.value.values)
                        aux.tipado = Type.I64
                        return aux
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
            if isinstance(self.id, Access):
                self.id = self.id.id
            var = environment.getVariable(self.id)
            if var != None:
                if var.tipado == Type.VECTOR or var.tipado == Type.ARRAY:
                    aux = Retorno()
                    if isinstance(var.valor, Arreglo) or isinstance(var.valor, Vector):
                        aux.value = len(var.valor.values)
                    else:
                        aux.value = len(var.valor)
                    aux.tipado = Type.I64
                    return aux
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