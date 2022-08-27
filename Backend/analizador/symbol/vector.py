from ..abstract.retorno import *
class Vector():
    def __init__(self):
        self.values = []
        self.tipado = Type.NULL
        self.capacidad = 1

    def getVector(self, index):
        return self.values[index]

    def setVector(self, index, value):
        self.values[index] = value

    def getCapacidad(self):
        return self.capacidad
    