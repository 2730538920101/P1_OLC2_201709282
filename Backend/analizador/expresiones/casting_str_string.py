from ..abstract.expresiones import *
from ..abstract.retorno import *
from ..expresiones.access import *

class Casting_str_string(Expresion):
    def __init__(self, linea, columna, exp):
        super().__init__(linea, columna)
        self.exp = exp

    def Ejecutar(self, environment):
        print("EJECUTANDO CASTING STR TO STRING")
        try:
            aux = Retorno()
            val = self.exp.Ejecutar(environment)
            if val.tipado == Type.STR:
                aux.tipado = Type.STRING
                aux.value = val.value   
            else:
                print("ERROR SEMANTICO, EL TIPO DE DATO NO SE PUEDE CONVERTIR A STRING")
            return aux
        except:
            print("ERROR SEMANTICO, AL CONVERTIR DE STR A STRING")