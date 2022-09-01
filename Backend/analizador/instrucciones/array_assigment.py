from ..expresiones.array_type import Array_type
from ..abstract.instrucciones import *
from ..abstract.retorno import *
from ..symbol.array import *
from ..symbol.environment import *

class Array_assigment(Instruccion):
    def __init__(self, linea, columna, id, value, tipado):
        super().__init__(linea, columna)
        self.id = id
        self.value = value
        self.tipado = tipado

    def Ejecutar(self, environment):
        print("EJECUTAR ARRAY ASSIGMENT")
        try:
            index = self.tipado.index
            tam = len(index)
            arr = self.value.Ejecutar(environment).value.values
            if isinstance(self.tipado, Array_type):
                tip = self.tipado.tipado
            var = environment.getVariable(self.id)
            if arr[0].tipado == Type.ARRAY:      
                tipoexp = arr[0].value.values[0].tipado
            else:
                tipoexp = arr[0].tipado
            if var != None:
                if tip == tipoexp:
                    for x in range(tam):
                        auxind = index.pop()
                        bandera = self.validar_indices(auxind, arr)
                        if bandera == False:
                            break
                        if x+1 < tam:
                            auxarr = arr.pop()
                            arr = auxarr.value.values
                    if bandera == False:
                        print("ERROR SEMANTICO, EL ARREGLO ASIGNADO NO TIENE LOS INDICES ESPECIFICADOS EN LA ASIGNACION")
                    else:
                        if var.mutabilidad == True:
                            environment.guardarVariables(self.id, self.value.Ejecutar(environment).value.values, Type.ARRAY, True)
                        else:
                            environment.guardarVariables(self.id, self.value.Ejecutar(environment).value.values, Type.ARRAY, False)
                else:
                    print("ERROR SEMANTICO, EL TIPO DE DATO DEL ARREGLO NO COINCIDE CON EL TIPO DE DATO DE LA DECLARACION")
            else:
                print("ERROR SEMANTICO, LA VARIABLE NO HA SIDO DECLARADA")
        except:
            print("ERROR SEMANTICO, LA EXPRESION ASIGNADA NO ES UN ARREGLO VALIDO")

    def validar_indices(self, index, arr):
        if index == len(arr):
            return True
        else:
            return False            

    def getTipado(self, environment):
        return self.tipado

    def getId(self):
        return self.id

    def getValue(self):
        return self.value