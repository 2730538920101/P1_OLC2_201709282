from abc import ABCMeta, abstractclassmethod
from .retorno import Retorno
from ..util.tabla_tipos import *

class Expresion(metaclass=ABCMeta):
    
    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna
    
    @abstractclassmethod
    def Ejecutar(self, environment):
        pass

    def DominanteSuma(self, tipo1, tipo2):
        tipado = TablaSuma[tipo1.value[0]][tipo2.value[0]]
        return tipado

    def DominanteResta(self, tipo1, tipo2):
        tipado = TablaResta[tipo1.value[0]][tipo2.value[0]]
        return tipado

    def DominanteMultiplicacion(self, tipo1, tipo2):
        tipado = TablaMultiplicacion[tipo1.value[0]][tipo2.value[0]]
        return tipado

    def DominanteDivision(self, tipo1, tipo2):
        tipado = TablaDivision[tipo1.value[0]][tipo2.value[0]]
        return tipado

    def DominantePotencia(self, tipo1, tipo2):
        tipado = TablaPotencia[tipo1.value[0]][tipo2.value[0]]
        return tipado

    def DominanteModulo(self, tipo1, tipo2):
        tipado = TablaModulo[tipo1.value[0]][tipo2.value[0]]
        return tipado

    def DominanteUnario(self, tipo1):
        tipado = TablaUnario[tipo1.value[0]][0]
        return tipado

    