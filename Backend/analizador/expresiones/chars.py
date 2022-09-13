from ..abstract.expresiones import * 
from ..abstract.retorno import *
from ..symbol.array import *
from ..reportes.TablaSim import *

class Chars(Expresion):
    def __init__(self, linea, columna, exp):
        super().__init__(linea, columna)
        self.exp = exp

    def Ejecutar(self, environment):
        print("EJECUTANDO CHARS")
        try:
            val = self.exp.Ejecutar(environment)
            aux = Retorno()
            arr = Arreglo()
            if val != None:
                if val.tipado == Type.STRING:
                    listaux = list(val.value)
                    for valor in listaux:
                        ret = Retorno()
                        ret.value = valor
                        ret.tipado = Type.CHAR
                        arr.values.append(ret)
                    arr.tipado = Type.CHAR
                    aux.value = arr
                    aux.tipado = Type.ARRAY           
                    return aux
                else:
                    auxer = "ERROR SEMANTICO, SOLO SE PUEDEN CONVERTIR A ARREGLOS LAS EXPRESIONES DE TIPO STRING"
                    print(auxer)
                    TablaErrores.append(auxer)
                    Prints.append(auxer)
            else:
                auxer = "ERROR SEMANTICO, ERROR EN LA EXPRESION"
                print(auxer)
                TablaErrores.append(auxer)
                Prints.append(auxer)
        except:
            auxer = "ERROR SEMANTICO, NO SE PUEDE CONVERTIR LA EXPRESION A UN ARREGLO"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)

            