class Struct():
    def __init__(self, id):
        self.id = id
        self.atributos = []
        self.tipados = []
        self.valores = []

    def getAtributos(self, index):
        return self.atributos[index]

    def setAtributos(self, index, value):
        self.atributos[index] = value

    def getTipados(self, index):
        return self.tipados[index]

    def setTipados(self, index, value):
        self.tipados[index] = value

    def getValores(self, index):
        return self.valores[index]

    def setValores(self, index, value):
        self.valores[index] = value
