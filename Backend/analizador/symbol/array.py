from ..abstract.retorno import *
class Arreglo():
    def __init__(self):
        self.values = []
        self.tipado = Type.NULL

    def getArray(self, index):
        return self.values[index]

    def setArray(self, index, value):
        self.values[index] = value

        