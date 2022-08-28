from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..symbol.array import *
from ..symbol.vector import *

class Access_index(Expresion):
    def __init__(self, linea, columna, id, indices):
        super().__init__(linea, columna)
        self.id = id
        self.indices = indices

    def Ejecutar(self, environment):
        print("EJECUTANDO ACCESS INDEX")
        try:
            val = environment.getVariable(self.id)
            if val != None:
                if val.tipado == Type.ARRAY or val.tipado == Type.VECTOR:
                    aux = Retorno()
                    auxv = val.valor
                    for x in range(len(self.indices)):
                        if isinstance(auxv, Vector) or isinstance(auxv, Arreglo):
                            auxv = auxv.values
                        if self.indices[x].tipado == Type.I64:
                            auxv = auxv.pop(self.indices[x].valor)
                            if isinstance(auxv, Retorno):
                                tip = auxv.tipado
                                auxv = auxv.value      
                        else:
                            print("ERROR SEMANTICO, LOS INDICES DEBEN SER UN VALOR ENTERO")
                    aux.tipado = tip
                    aux.value = auxv
                    return aux
                else:
                    print("ERROR SEMANTICO, SOLO SE PUEDE ACCEDER A EXPRESONES ITERABLES ARRAY O VECTOR")
            else:
                print("LA VARIABLE NO HA SIDO DECLARADA")
        except:
            print("ERROR SEMANTICO, ELEMENTO ACCEDIDO INVALIDO")
  