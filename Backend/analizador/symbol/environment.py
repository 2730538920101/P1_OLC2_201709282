from enum import Enum, unique
from ..reportes.TablaSim import TablaSimbolos
from .symbol import Symbol

@unique
class ClaseSym(Enum):
    VARIABLE = 0,
    FUNCION = 1



class Entorno():
    def __init__(self,  entorno_anterior = None):
        self.variables = {}
        self.funciones = {}
        self.entorno_anterior = entorno_anterior

    def guardarVariables(self, id, valor, tipado, mutabilidad = False, tipotoken = ClaseSym.VARIABLE):
        env = self
        while(env != None):
            if id in env.variables:
                sim = Symbol(id, valor, tipado, mutabilidad, tipotoken)
                TablaSimbolos.append(sim)
                env.variables.setdefault(id, sim)
                return
            env = env.entorno_anterior
        sim2 = Symbol(id, valor, tipado, mutabilidad, tipotoken)
        self.variables.setdefault(id, sim2)
        TablaSimbolos.append(sim2)

    def guardarFunciones(self, id, funcion):
        env = self
        while(env != None):
            if id in env.funciones:
                sim = Symbol(id, "FUNCION", funcion.tipado, mutabilidad = False, tipotoken = ClaseSym.FUNCION)
                TablaSimbolos.append(sim)
                env.funciones.setdefault(id, funcion)
                return
            env = env.entorno_anterior
        sim2 = Symbol(id, "FUNCION", funcion.tipado, mutabilidad=False, tipotoken = ClaseSym.FUNCION)
        TablaSimbolos.append(sim2)
        self.funciones.setdefault(id, funcion)


    def getVariable(self, id):
        env = self
        while(env != None):
            if id in env.variables:
                return env.variables.get(id)
            env = env.entorno_anterior
        return None        


    def getFuncion(self, id):
        env = self
        while(env != None):
            if id in env.funciones:
                return env.funciones.get(id)
            env = env.entorno_anterior
        return None     


    def getGlobal(self):
        env = self
        while(env.entorno_anterior != None):
            env = env.entorno_anterior
        return env
        

