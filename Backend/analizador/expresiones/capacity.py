from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..expresiones.access import *
from ..reportes.TablaSim import *

class Capacity(Expresion):
    def __init__(self, linea, columna, id):
        super().__init__(linea, columna)
        self.id = id

    def Ejecutar(self, environment):
        print("EJECUTANDO CAPACITY AL VECTOR")
        
        try:
            if isinstance(self.id, Access):
                self.id = self.id.id
            var = environment.getVariable(self.id)
            if var != None:
                if var.tipado == Type.VECTOR:
                    aux = Retorno()
                    aux.value = var.valor.capacidad
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