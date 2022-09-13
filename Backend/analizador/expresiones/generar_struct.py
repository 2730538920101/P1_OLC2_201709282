from ..expresiones.tipo_vector import *
from ..expresiones.array_type import *
from ..abstract.expresiones import *
from ..symbol.environment import *
from ..abstract.retorno import *
from ..reportes.TablaSim import *

class Generar_struct(Expresion):
    def __init__(self, linea, columna, id, code, tipado):
        super().__init__(linea, columna)
        self.id = id
        self.code = code
        self.tipado = tipado

    def Ejecutar(self, environment):
        print("EJECUTANDO STRUCT INSTANCE")
        aux = Retorno()
        varaux = environment.getStruct(self.id)
        if varaux == None:
            auxer = "ERROR SEMANTICO, EL STRUCT NO HA SIDO DECLARADO"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)
        else:
            try:
                if varaux.id == self.id:
                    for x in range(len(self.code)):
                        valoraux = self.code[x].exp.Ejecutar(environment)
                        idaux = self.code[x].id
                        if varaux.valor.atributos[x]== idaux:
                            if isinstance(varaux.valor.tipados[x], Array_type) and (valoraux.tipado == Type.ARRAY):
                                varaux.valor.valores.append(valoraux.value)
                            elif isinstance(varaux.valor.tipados[x], Tipo_vector) and (valoraux.tipado == Type.VECTOR):
                                varaux.valor.valores.append(valoraux.value)
                            elif valoraux.tipado == varaux.valor.tipados[x]:
                                varaux.valor.valores.append(valoraux.value)
                            else:
                                auxer = "ERROR SEMANTICO, EL ATRIBUTO NO ES DEL TIPO DE LA DECLARACION"
                                print(auxer)
                                TablaErrores.append(auxer)
                                Prints.append(auxer)
                        else:
                            auxer = "ERROR SEMANTICO, EL ATRIBUTO INGRESADO NO ES CORRECTO"
                            print(auxer)
                            TablaErrores.append(auxer)
                            Prints.append(auxer)
                    aux.value = varaux.valor
                    aux.tipado = Type.STRUCT
                    return aux
                else:
                    auxer = "ERROR SEMANTICO, EL STRUCT NO HA SIDO DECLARADO"
                    print(auxer)
                    TablaErrores.append(auxer)
                    Prints.append(auxer)
            except:
                auxer = "ERROR SEMANTICO, NO SE HA PODIDO INSTANCIAR EL STRUCT"
                print(auxer)
                TablaErrores.append(auxer)
                Prints.append(auxer)
            




    