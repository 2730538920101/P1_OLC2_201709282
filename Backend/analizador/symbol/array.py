from .symbol import *

class Arreglo():
    def __init__(self):
        self.values = []

    def getArray(self, index):
        return self.values[index]

    def setArray(self, index, value):
        self.values[index] = value

        