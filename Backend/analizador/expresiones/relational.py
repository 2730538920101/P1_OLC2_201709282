from .access import Access
from ..abstract.expresiones import *
from ..abstract.retorno import *
from enum import Enum, unique

@unique
class RelationalOption(Enum):
    DOBIGUAL = 0,
    DIF = 1,
    MENOR = 2,
    MENORIG = 3,
    MAYOR = 4,
    MAYORIG = 5

class Relational(Expresion):
    def __init__(self, linea, columna, valor1, valor2, tipoOp):
        super().__init__(linea, columna)
        self.valor1 = valor1
        self.valor2 = valor2
        self.tipoOp = tipoOp

    def Ejecutar(self, environment):
        print("EJECUTANDO RELATIONAL")
        if self.valor1 != None:
            leftvalue = self.valor1.Ejecutar(environment)
        if self.valor2 != None:
            rightvalue = self.valor2.Ejecutar(environment)
        resultado = Retorno()
        if self.tipoOp == RelationalOption.DOBIGUAL:
            resultado.value = leftvalue.value == rightvalue.value
            resultado.tipado = Type.BOOL
        elif self.tipoOp == RelationalOption.DIF:
            resultado.value = leftvalue.value != rightvalue.value
            resultado.tipado = Type.BOOL
        elif self.tipoOp == RelationalOption.MAYOR:
            resultado.value = leftvalue.value > rightvalue.value
            resultado.tipado = Type.BOOL
        elif self.tipoOp == RelationalOption.MAYORIG:
            resultado.value = leftvalue.value >= rightvalue.value
            resultado.tipado = Type.BOOL
        elif self.tipoOp == RelationalOption.MENOR:
            resultado.value = leftvalue.value < rightvalue.value
            resultado.tipado = Type.BOOL
        elif self.tipoOp == RelationalOption.MAYORIG:
            resultado.value = leftvalue.value <= rightvalue.value
            resultado.tipado = Type.BOOL
        else:
            print("ERROR SEMANTICO EN EXPRESION RELACIONAL")
        return resultado
