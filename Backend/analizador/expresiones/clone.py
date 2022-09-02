from ..abstract.expresiones import *
from ..abstract.retorno import *
from .access import *
 
class Clone(Expresion):
    def __init__(self, linea, columna, exp):
        super().__init__(linea, columna)
        self.exp = exp

    def Ejecutar(self, environment):
        print("EJECUTANDO CASTING STRING TO STR")
        try:
            aux = Retorno()
            val = self.exp.Ejecutar(environment)
            if val.tipado == Type.STRING:
                aux.tipado = Type.STRING
                aux.value = val.value
            else:
                print("ERROR SEMANTICO, NO SE PUEDE HACER UNA COPIA DE LA EXPRESION, DEBE SER DE TIPO STRING")   
            return aux
        except:
            print("ERROR SEMANTICO, NO SE PUEDE COPIAR EL VALOR DE LA EXPRESION")
