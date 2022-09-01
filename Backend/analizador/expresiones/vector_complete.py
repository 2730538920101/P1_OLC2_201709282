from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..symbol.vector import *

class Vector_complete(Expresion):
    def __init__(self, linea, columna, exp_list, tipado):
        super().__init__(linea, columna)
        self.exp_list = exp_list
        self.tipado = tipado

    def Ejecutar(self, environment):
        print("EJECUTANDO VECTOR COMPLETE")
        arr = Vector()
        aux = Retorno()
        if self.exp_list[0].Ejecutar(environment).tipado == Type.VECTOR:
            tipadoaux = self.exp_list[0].Ejecutar(environment).value.values[0].tipado
        elif self.exp_list[0].Ejecutar(environment).tipado == Type.ARRAY:
            print("ERROR SEANTICO, NO SE PUEDE AGREGAR UN ARRAY DENTRO DE UN VECTOR")
            return
        else:
            tipadoaux =  self.exp_list[0].Ejecutar(environment).tipado 
        for exp in self.exp_list:
            aux_exp = exp.Ejecutar(environment)
            if aux_exp.tipado != Type.VECTOR:
                if aux_exp.tipado == tipadoaux:
                    arr.values.append(aux_exp)
                else:
                    print("ERROR SEMANTICO, LOS ELEMENTOS DEL VECTOR DEBEN SER DEL MISMO TIPO")
                    return
            else:
                if aux_exp.value.values[0].tipado == tipadoaux:
                    arr.values.append(aux_exp)
                else:
                    print("ERROR SEMANTICO, LOS ELEMENTOS DEL VECTOR DEBEN SER DEL MISMO TIPO")
                    return    
        arr.capacidad = len(arr.values)
        arr.tipado = tipadoaux
        aux.value = arr
        aux.tipado = Type.VECTOR
        return aux

