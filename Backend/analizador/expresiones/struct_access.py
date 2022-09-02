from ..abstract.expresiones import *
from ..abstract.retorno import *

class Struct_access(Expresion):
    def __init__(self, linea, columna, id, atributo):
        super().__init__(linea, columna)
        self.id = id
        self.atributo = atributo

    def Ejecutar(self,environment):
        print("EJECUTANDO STRUCT ACCESS")
        var = environment.getVariable(self.id)
        if var != None:
            if var.tipado == Type.STRUCT:
                aux = Retorno()
                id_index = var.valor.atributos.index(self.atributo)
                aux.tipado = var.valor.tipados[id_index]
                aux.value = var.valor.valores[id_index]
                return aux
            else: 
                print("ERROR SEMANTICO, EL STRUCT NO ES VALIDO")
        else:
            print("ERROR SEMANTICO, LA VARIABLE NO HA SIDO DECLARADA")
        