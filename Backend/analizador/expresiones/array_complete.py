from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..symbol.array import *
from ..reportes.TablaSim import *

class Array_complete(Expresion):
    def __init__(self, linea, columna, exp_list, tipado):
        super().__init__(linea, columna)
        self.exp_list = exp_list
        self.tipado = tipado

    def Ejecutar(self, environment):
        print("EJECUTANDO ARRAY COMPLETE")
        
        arr = Arreglo()
        aux = Retorno()
        if self.exp_list[0].Ejecutar(environment).tipado == Type.ARRAY:
            tipadoaux = self.exp_list[0].Ejecutar(environment).value.values[0].tipado
        elif self.exp_list[0].Ejecutar(environment).tipado == Type.VECTOR:
            auxer = "ERROR SEANTICO, NO SE PUEDE AGREGAR UN VECTOR DENTRO DE UN ARRAY"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)
            return
        else:
            tipadoaux =  self.exp_list[0].Ejecutar(environment).tipado 
        for exp in self.exp_list:
            aux_exp = exp.Ejecutar(environment)
            if aux_exp.tipado != Type.ARRAY:
                if aux_exp.tipado == tipadoaux:
                    arr.values.append(aux_exp)
                else:
                    auxer = "ERROR SEMANTICO, LOS ELEMENTOS DEL ARRAY DEBEN SER DEL MISMO TIPO"
                    print(auxer)
                    TablaErrores.append(auxer)
                    Prints.append(auxer)
                    return
            else:
                if aux_exp.value.values[0].tipado == tipadoaux:
                    arr.values.append(aux_exp)
                else:
                    auxer = "ERROR SEMANTICO, LOS ELEMENTOS DEL ARRAY DEBEN SER DEL MISMO TIPO"
                    print(auxer)
                    TablaErrores.append(auxer)
                    Prints.append(auxer)
                    return 
        arr.tipado = tipadoaux   
        aux.value = arr
        aux.tipado = Type.ARRAY
        return aux

