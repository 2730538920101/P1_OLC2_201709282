from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..reportes.TablaSim import *

class Abs(Expresion):
    def __init__(self, linea, columna, exp):
        super().__init__(linea, columna)
        self.exp = exp

    def Ejecutar(self, environment):
        print("EJECUTANDO ABS")
        try:
            val = self.exp.Ejecutar(environment)
            aux = Retorno()
            if val != None:
                if val.tipado == Type.F64 or val.tipado == Type.I64:
                    aux.tipado = Type.I64
                    aux.value = abs(int(val.value))
                    return aux                    
                else:
                    auxer = "ERROR SEMANTICO, SOLO PUEDE OBTENER EL VALOR ABSOLUTO DE EXPRESIONES DE TIPO F64 O I64"
                    print(auxer)
                    TablaErrores.append(auxer)
                    Prints.append(auxer)
            else:
                auxer = "ERROR SEMANTICO, LA EXPRESION NO ES VALIDA"
                print(auxer)
                TablaErrores.append(auxer)
                Prints.append(auxer)
        except:
            auxer = "ERROR SEMANTICO, NO SE PUEDE OBTENER EL VALOR ABSOLUTO DE LA EXPRESION"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)