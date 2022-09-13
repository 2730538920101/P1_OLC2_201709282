import math
from .literal import Literal
from .access import Access
from ..abstract.expresiones import *
from ..abstract.retorno import *
from enum import Enum, unique
from ..reportes.TablaSim import *


@unique
class ArithmeticOption(Enum):
    SUMA = 0,
    RESTA = 1,
    MULTIPLICACION = 2,
    DIVISION = 3,
    MODULO = 4,
    UNARIO = 5,
    POTENCIA = 6
    RAIZ = 7

class Arithmetic(Expresion):
    def __init__(self, linea, columna, valor1, valor2, tipoOp):
        super().__init__(linea, columna)
        self.valor1 = valor1
        self.valor2 = valor2
        self.tipoOp = tipoOp

    def Ejecutar(self, environment):
        print("EJECUTANDO ARITHMETIC")
        
        resultado = Retorno()
        if self.valor1 != None:
            leftvalue = self.valor1.Ejecutar(environment)
        if self.valor2 != None:
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
                    resultado.value = str(leftvalue.value) + str(rightvalue.value)
                    resultado.tipado = Type.STRING 
                elif dominanteSuma == Type.USIZE:
                    resultado.value = leftvalue.value + rightvalue.value
                    resultado.tipado = Type.USIZE                
                else:
                    auxer = "ERROR SEMANTICO EN LA SUMA"
                    print(auxer)
                    TablaErrores.append(auxer)
                    Prints.append(auxer)
            elif self.tipoOp == ArithmeticOption.RESTA:
                dominanteResta = self.DominanteResta(leftvalue.tipado, rightvalue.tipado)
                if dominanteResta == Type.I64:
                    resultado.value = leftvalue.value - rightvalue.value
                    resultado.tipado = Type.I64
                elif dominanteResta == Type.F64:
                    resultado.value = leftvalue.value - rightvalue.value
                    resultado.tipado = Type.F64
                elif dominanteResta == Type.USIZE:
                    resultado.value = leftvalue.value - rightvalue.value
                    resultado.tipado = Type.USIZE
                else:
                    auxer = "ERROR SEMANTICO EN LA RESTA"
                    print(auxer)
                    TablaErrores.append(auxer)
                    Prints.append(auxer)

            elif self.tipoOp == ArithmeticOption.MULTIPLICACION:
                dominanteMultiplicacion = self.DominanteMultiplicacion(leftvalue.tipado, rightvalue.tipado)
                if dominanteMultiplicacion == Type.I64:
                    resultado.value = leftvalue.value * rightvalue.value
                    resultado.tipado = Type.I64
                elif dominanteMultiplicacion == Type.F64:
                    resultado.value = leftvalue.value * rightvalue.value
                    resultado.tipado = Type.F64
                else:
                    auxer = "ERROR SEMANTICO EN LA MULTIPLICACION"
                    print(auxer)
                    TablaErrores.append(auxer)
                    Prints.append(auxer)
            elif self.tipoOp == ArithmeticOption.DIVISION:
                dominanteDivision = self.DominanteDivision(leftvalue.tipado, rightvalue.tipado)
                if rightvalue.value == 0:
                    auxer = "ERROR SEMANTICO EN LA DIVISION"
                    print(auxer)
                    TablaErrores.append(auxer)
                    Prints.append(auxer)
                else:
                    if dominanteDivision == Type.F64:
                        resultado.value = leftvalue.value / rightvalue.value
                        resultado.tipado = Type.F64
                    else:
                        auxer = "ERROR SEMANTICO EN LA DIVISION"
                        print(auxer)
                        TablaErrores.append(auxer)
                        Prints.append(auxer)
            elif self.tipoOp == ArithmeticOption.MODULO:
                dominanteModulo = self.DominanteModulo(leftvalue.tipado, rightvalue.tipado)
                if dominanteModulo == Type.I64:
                    resultado.value = leftvalue.value % rightvalue.value
                    resultado.tipado = Type.I64
                elif dominanteModulo == Type.F64:
                    resultado.value = leftvalue.value % rightvalue.value
                    resultado.tipado = Type.F64
                else:
                    auxer = "ERROR SEMANTICO EN EL MODULO"
                    print(auxer)
                    TablaErrores.append(auxer)
                    Prints.append(auxer)
            elif self.tipoOp == ArithmeticOption.UNARIO:
                dominanteUnario = self.DominanteUnario(rightvalue.tipado)
                if dominanteUnario == Type.I64:
                    resultado.value = 0 - rightvalue.value
                    resultado.tipado = Type.I64
                elif dominanteUnario == Type.F64:
                    resultado.value = 0 - rightvalue.value
                    resultado.tipado = Type.F64
                else:
                    auxer = "ERROR SEMANTICO EN OPERACION UNARIA"
                    print(auxer)
                    TablaErrores.append(auxer)
                    Prints.append(auxer)
            elif self.tipoOp == ArithmeticOption.POTENCIA:
                dominantePotencia = self.DominantePotencia(leftvalue.tipado, rightvalue.tipado)
                if dominantePotencia == Type.I64:
                    resultado.value = pow(leftvalue.value, rightvalue.value)
                    resultado.tipado = Type.I64
                elif dominantePotencia == Type.F64:
                    resultado.value = round(math.pow(leftvalue.value, rightvalue.value),2)
                    resultado.tipado == Type.F64
                else:
                    auxer = "ERROR SEMANTICO EN OPERACION POTENCIA"
                    print(auxer)
                    TablaErrores.append(auxer)
                    Prints.append(auxer)
            elif self.tipoOp == ArithmeticOption.RAIZ:
                dominanteRaiz = self.DominanteRaiz(rightvalue.tipado)
                if dominanteRaiz == Type.I64 or dominanteRaiz == Type.F64:
                    resultado.value = round(math.sqrt(rightvalue.value),2)
                    resultado.tipado = Type.F64
            return resultado
        except:
            auxer = "ERROR EN LA OPERACION ARITMETICA"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)
