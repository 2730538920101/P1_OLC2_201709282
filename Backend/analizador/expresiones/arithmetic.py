from .literal import Literal
from .access import Access
from ..abstract.expresiones import *
from ..abstract.retorno import *
from enum import Enum, unique


@unique
class ArithmeticOption(Enum):
    SUMA = 0,
    RESTA = 1,
    MULTIPLICACION = 2,
    DIVISION = 3,
    MODULO = 4,
    UNARIO = 5

class Arithmetic(Expresion):
    def __init__(self, linea, columna, valor1, valor2, tipoOp):
        super().__init__(linea, columna)
        self.valor1 = valor1
        self.valor2 = valor2
        self.tipoOp = tipoOp

    def Ejecutar(self, environment):
        resultado = Retorno()
        if self.valor1 != None:
            if isinstance(self.valor1, Access):    
                leftvalue = self.valor1.Ejecutar(environment).value
            else:
                leftvalue = self.valor1.Ejecutar(environment)
        if self.valor2 != None:
            if isinstance(self.valor2, Access):
                rightvalue = self.valor2.Ejecutar(environment).value
            else:
                rightvalue = self.valor2.Ejecutar(environment)
        try:
            if self.tipoOp == ArithmeticOption.SUMA:
                dominanteSuma = self.DominanteSuma(leftvalue.tipado, rightvalue.tipado)
                if dominanteSuma == Type.I64:
                    resultado.value = leftvalue.value + rightvalue.value
                    resultado.tipado = Type.I64
                elif dominanteSuma == Type.F64:
                    resultado.value = leftvalue.value + rightvalue.value
                    resultado.tipado = Type.F64
                elif dominanteSuma == Type.STRING:
                    resultado.value = leftvalue.value + rightvalue.value
                    resultado.tipado = Type.STRING                
                else:
                    print("ERROR SEMANTICO EN LA SUMA")
            elif self.tipoOp == ArithmeticOption.RESTA:
                dominanteResta = self.DominanteResta(leftvalue.tipado, rightvalue.tipado)
                if dominanteResta == Type.I64:
                    resultado.value = leftvalue.value - rightvalue.value
                    resultado.tipado = Type.I64
                elif dominanteResta == Type.F64:
                    resultado.value = leftvalue.value - rightvalue.value
                    resultado.tipado = Type.F64
                else:
                    print("ERROR SEMANTICO EN LA RESTA")
            elif self.tipoOp == ArithmeticOption.MULTIPLICACION:
                dominanteMultiplicacion = self.DominanteMultiplicacion(leftvalue.tipado, rightvalue.tipado)
                if dominanteMultiplicacion == Type.I64:
                    resultado.value = leftvalue.value * rightvalue.value
                    resultado.tipado = Type.I64
                elif dominanteMultiplicacion == Type.F64:
                    resultado.value = leftvalue.value * rightvalue.value
                    resultado.tipado = Type.F64
                else:
                    print("ERROR SEMANTICO EN LA MULTIPLICACION")
            elif self.tipoOp == ArithmeticOption.DIVISION:
                dominanteDivision = self.DominanteDivision(leftvalue.tipado, rightvalue.tipado)
                if rightvalue.value == 0:
                    print("ERROR SEMANTICO EN LA DIVISION")
                else:
                    if dominanteDivision == Type.I64:
                        resultado.value = leftvalue.value / rightvalue.value
                        resultado.tipado = Type.F64
                    elif dominanteDivision == Type.F64:
                        resultado.value = leftvalue.value / rightvalue.value
                        resultado.tipado = Type.F64
                    else:
                        print("ERROR SEMANTICO EN LA DIVISION")
            elif self.tipoOp == ArithmeticOption.MODULO:
                dominanteModulo = self.DominanteModulo(leftvalue.tipado, rightvalue.tipado)
                if dominanteModulo == Type.I64:
                    resultado.value = leftvalue.value % rightvalue.value
                    resultado.tipado = Type.I64
                elif dominanteModulo == Type.F64:
                    resultado.value = leftvalue.value % rightvalue.value
                    resultado.tipado = Type.F64
                else:
                    print("ERROR SEMANTICO EN EL MODULO")
            elif self.tipoOp == ArithmeticOption.UNARIO:
                dominanteUnario = self.DominanteUnario(rightvalue.tipado)
                if dominanteUnario == Type.I64:
                    resultado.value = 0 - rightvalue.value
                    resultado.tipado = Type.I64
                elif dominanteUnario == Type.F64:
                    resultado.value = 0 - rightvalue.value
                    resultado.tipado = Type.F64
                else:
                    print("ERROR SEMANTICO EN OPERACION UNARIA")
            return resultado

        except:
            print("ERROR EN LA OPERACION ARITMETICA")
