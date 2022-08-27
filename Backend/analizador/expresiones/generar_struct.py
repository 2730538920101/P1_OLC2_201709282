from ..abstract.expresiones import *
from ..symbol.environment import *
from ..abstract.retorno import *

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
            print("ERROR SEMANTICO, EL STRUCT NO HA SIDO DECLARADO")
        else:
            try:
                if varaux.id == self.id:
                    for x in range(len(self.code)):
                        valoraux = self.code[x].exp.Ejecutar(environment)
                        idaux = self.code[x].id
                        if varaux.valor.atributos[x]== idaux:
                            if valoraux.tipado == varaux.valor.tipados[x]:
                                varaux.valor.valores.append(valoraux.value)
                            else:
                                print("ERROR SEMANTICO, EL ATRIBUTO NO ES DEL TIPO DE LA DECLARACION")
                        else:
                            print("ERROR SEMANTICO, EL ATRIBUTO INGRESADO NO ES CORRECTO")
                    aux.value = varaux.valor
                    aux.tipado = Type.STRUCT
                    return aux
                else:
                    print("ERROR SEMANTICO, EL STRUCT NO HA SIDO DECLARADO")
            except:
                print("ERROR SEMANTICO, NO SE HA PODIDO INSTANCIAR EL STRUCT")
            




    