from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..symbol.vector import *
from ..reportes.TablaSim import *

class Vector_complete(Expresion):
    def __init__(self, linea, columna, exp_list, tipado, capacidad):
        super().__init__(linea, columna)
        self.exp_list = exp_list
        self.tipado = tipado
        self.capacidad = capacidad

    def Ejecutar(self, environment):
        print("EJECUTANDO VECTOR COMPLETE")
        arr = Vector()
        aux = Retorno()
        if self.exp_list != None:
            if self.exp_list[0].Ejecutar(environment).tipado == Type.VECTOR:
                tipadoaux = self.exp_list[0].Ejecutar(environment).value.values[0].tipado
            elif self.exp_list[0].Ejecutar(environment).tipado == Type.ARRAY:
                auxer = "ERROR SEANTICO, NO SE PUEDE AGREGAR UN ARRAY DENTRO DE UN VECTOR"
                print(auxer)
                TablaErrores.append(auxer)
                Prints.append(auxer)
                return
            else:
                tipadoaux =  self.exp_list[0].Ejecutar(environment).tipado 
            for exp in self.exp_list:
                aux_exp = exp.Ejecutar(environment)
                if aux_exp.tipado != Type.VECTOR:
                    if aux_exp.tipado == tipadoaux:
                        arr.values.append(aux_exp)
                    else:
                        auxer = "ERROR SEMANTICO, LOS ELEMENTOS DEL VECTOR DEBEN SER DEL MISMO TIPO"
                        print(auxer)
                        TablaErrores.append(auxer)
                        Prints.append(auxer)
                        return
                else:
                    if aux_exp.value.values[0].tipado == tipadoaux:
                        arr.values.append(aux_exp)
                    else:
                        auxer = "ERROR SEMANTICO, LOS ELEMENTOS DEL VECTOR DEBEN SER DEL MISMO TIPO"
                        print(auxer)
                        TablaErrores.append(auxer)
                        Prints.append(auxer)
                        return    
            arr.capacidad = len(arr.values)
            arr.tipado = tipadoaux
            aux.value = arr
            aux.tipado = Type.VECTOR
            return aux
        else:
            if self.capacidad != None:
                arr.capacidad = self.capacidad.Ejecutar(environment).value 
            arr.tipado = Type.NULL
            arr.values = []
            aux.value = arr
            aux.tipado = Type.VECTOR
            return aux
