from abc import ABCMeta, abstractclassmethod
from ..util.tabla_tipos import *

class Instruccion(metaclass=ABCMeta):
    
    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna
    
    @abstractclassmethod
    def Ejecutar(self, environment):
        pass