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
                        if self.indices[x].tipado == Type.I64:
                            if x == 0:
                                auxv = auxv[self.indices[x].valor]
                            else:
                                auxv = auxv.value.values[self.indices[x].valor]
                        else:
                            print("ERROR SEMANTICO, LOS INDICES DEBEN SER UN VALOR ENTERO")
                    aux.tipado = auxv.tipado
                    aux.value = auxv.value
                    return aux
                else:
                    print("ERROR SEMANTICO, SOLO SE PUEDE ACCEDER A EXPRESONES ITERABLES ARRAY O VECTOR")
            else:
                print("ERROR SEMANTICO, LA VARIABLE NO HA SIDO DECLARADA")
        except:
            print("ERROR SEMANTICO, ELEMENTO ACCEDIDO INVALIDO")
  