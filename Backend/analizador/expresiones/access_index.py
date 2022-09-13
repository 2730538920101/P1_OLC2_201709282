from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..symbol.array import *
from ..symbol.vector import *
from ..expresiones.access import *
from ..expresiones.literal import *
from ..expresiones.arithmetic import *
from ..reportes.TablaSim import TablaErrores
from ..reportes.TablaSim import Prints

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
                        if isinstance(self.indices[x], Access) or isinstance(self.indices[x], Arithmetic):
                            ind = self.indices[x].Ejecutar(environment)
                        else:
                            ind = self.indices[x]
                        if ind.tipado == Type.I64 or ind.tipado == Type.USIZE:
                            if x == 0:
                                if isinstance(ind, Literal):
                                    if isinstance(auxv, Arreglo) or isinstance(auxv, Vector):
                                        auxv = auxv.values[ind.valor]
                                    else:
                                        auxv = auxv[ind.valor]
                                else:
                                    if isinstance(auxv, Arreglo) or isinstance(auxv, Vector):
                                        auxv = auxv.values[ind.value]
                                    else:
                                        auxv = auxv[ind.value]
                                    
                            else:
                                if isinstance(ind, Literal):
                                    if isinstance(auxv, Arreglo) or isinstance(auxv, Vector):
                                        auxv = auxv.values[ind.valor]
                                    else:
                                        auxv = auxv.value.values[ind.valor]
                                else:
                                    if isinstance(auxv, Arreglo) or isinstance(auxv, Vector):
                                        auxv = auxv.values[ind.value]
                                    else:
                                        auxv = auxv.value.values[ind.value]
                        else:
                            auxer = "ERROR SEMANTICO, LOS INDICES DEBEN SER UN VALOR ENTERO"
                            print(auxer)
                            TablaErrores.append(auxer)
                            Prints.append(auxer)
                    aux.tipado = auxv.tipado
                    aux.value = auxv.value
                    return aux
                else:
                    auxer = "ERROR SEMANTICO, SOLO SE PUEDE ACCEDER A EXPRESONES ITERABLES ARRAY O VECTOR"
                    print(auxer)
                    TablaErrores.append(auxer)
                    Prints.append(auxer)
            else:
                auxer = "ERROR SEMANTICO, LA VARIABLE NO HA SIDO DECLARADA"
                print(auxer)
                TablaErrores.append(auxer)
                Prints.append(auxer)
        except:
            auxer = "ERROR SEMANTICO, ELEMENTO ACCEDIDO INVALIDO"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)

            