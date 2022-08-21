from .case import *
from ..abstract.instrucciones import *
from ..abstract.retorno import *
from ..symbol.environment import *

class Match(Instruccion):
    def __init__(self, linea, columna, cambio, casos):
        super().__init__(linea, columna)
        self.cambio = cambio
        self.casos = casos

    def Ejecutar(self, environment):
        actual = self.cambio.Ejecutar(environment)
        for caso in self.casos:
            casoexp = caso.getExp()
            if casoexp != None:
                casoactual = casoexp.Ejecutar(environment)
                if actual.tipado == casoactual.tipado:
                    if actual.value == casoactual.value:
                        element = caso.Ejecutar(environment)
                        if element != None:
                            if element.tipado == Type.BREAK:
                                break
                            elif element.tipado == Type.CONTINUE:
                                continue
                            else:
                                return element
                else:
                    print("ERROR SEMANTICO, EL VALOR DE LA OPERACION A REALIZAR NO ES DEL MISMO TIPO QUE EL VALOR ASIGNADO POR LA SENTENCIA MATCH")                
            else:
                elemento = caso.Ejecutar(environment)
                if elemento != None:
                        if elemento.tipado == Type.BREAK:
                            break
                        elif elemento.tipado == Type.CONTINUE:
                            continue
                        else:
                            return elemento   

            