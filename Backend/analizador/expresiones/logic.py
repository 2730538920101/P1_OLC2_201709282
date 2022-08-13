from ..abstract.expresiones import *
from ..abstract.retorno import *
from enum import Enum, unique

@unique
class LogicOption(Enum):
    AND = 0,
    OR = 1,
    NOT = 2

class Logic(Expresion):
    def __init__(self, linea, columna, valor1, valor2, tipoOp):
        super().__init__(linea, columna)
        self.valor1 = valor1
        self.valor2 = valor2
        self.tipoOp = tipoOp

    def Ejecutar(self, environment):
        print("EJECUTANDO UNA EXPRESION LOGICA")
        resultado = Retorno()
        if self.tipoOp == LogicOption.AND:
            leftvalue = self.valor1.Ejecutar(environment)
            rightvalue = self.valor2.Ejecutar(environment)
            resultado.value = leftvalue.value and rightvalue.value
            resultado.tipado = Type.BOOL
        elif self.tipoOp == LogicOption.OR:
            leftvalue = self.valor1.Ejecutar(environment)
            rightvalue = self.valor2.Ejecutar(environment)
            resultado.value = leftvalue.value or rightvalue.value
            resultado.tipado = Type.BOOL
        elif self.tipoOp == LogicOption.NOT:
            leftvalue = self.valor1.Ejecutar(environment)
            resultado.value = not(leftvalue.value)
            resultado.tipado = Type.BOOL
        else:
            print("ERROR SEMANTICO EN EXPRESION LOGICA")
        return resultado