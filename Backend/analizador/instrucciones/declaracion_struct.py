from ..abstract.instrucciones import *
from ..symbol.struct import *
from ..reportes.TablaSim import *

class Declaracion_struct(Instruccion):
    def __init__(self, linea, columna, id, code, tipado, mutabilidad):
        super().__init__(linea, columna)
        self.id = id
        self.code = code
        self.tipado = tipado
        self.mutabilidad = mutabilidad

    def Ejecutar(self, environment):
        print("EJECUTANDO DECLARACION STRUCT")
        var = environment.getStruct(self.id)
        if var == None:
            aux = Struct(self.id)
            for inst in self.code:
                aux.atributos.append(inst.id)
                aux.tipados.append(inst.tipado)
            environment.guardarStructs(self.id, aux, self.tipado, self.mutabilidad)
        else:
            auxer = "ERROR SEMANTICO, YA SE HA DECLARADO UN STRUCT CON EL MISMO NOMBRE"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)