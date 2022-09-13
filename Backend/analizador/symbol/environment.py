from enum import Enum, unique
from ..reportes.TablaSim import TablaSimbolos
from .symbol import Symbol

@unique
class ClaseSym(Enum):
    VARIABLE = 0,
    FUNCION = 1,
    STRUCT = 2



class Entorno():
    def __init__(self,  entorno_anterior = None):
        self.variables = {}
        self.funciones = {}
        self.structs = {}
        self.entorno_anterior = entorno_anterior

    def guardarVariables(self, id, valor, tipado, mutabilidad = False, tipotoken = ClaseSym.VARIABLE):
        env = self
        while(env != None):
            if id in env.variables:
                sim = Symbol(id, valor, tipado, mutabilidad, tipotoken)
                TablaSimbolos.append(sim)
                env.variables[id] = sim
                return
            env = env.entorno_anterior
        sim2 = Symbol(id, valor, tipado, mutabilidad, tipotoken)
        self.variables[id] = sim2
        TablaSimbolos.append(sim2)

    def guardarStructs(self, id, valor, tipado, mutabilidad = True, tipotoken = ClaseSym.STRUCT):
        env = self
        while(env != None):
            if id in env.structs:
                sim = Symbol(id, valor, tipado, mutabilidad, tipotoken)
                TablaSimbolos.append(sim)
                env.structs[id] =  sim
                return
            env = env.entorno_anterior
        sim2 = Symbol(id, valor, tipado, mutabilidad, tipotoken = ClaseSym.STRUCT)
        self.structs[id]= sim2
        TablaSimbolos.append(sim2)

    def guardarFunciones(self, id, funcion, mutabilidad = False, tipotoken = ClaseSym.FUNCION):
        env = self
        while(env != None):
            if id in env.funciones:
                sim = Symbol(id, funcion, funcion.tipado, mutabilidad, tipotoken = ClaseSym.FUNCION)
                TablaSimbolos.append(sim)
                env.funciones[id] = funcion
                return
            env = env.entorno_anterior
        sim2 = Symbol(id, funcion, funcion.tipado, mutabilidad, tipotoken = ClaseSym.FUNCION)
        TablaSimbolos.append(sim2)
        self.funciones[id] = funcion


    def getVariable(self, id):
        env = self
        while(env != None):
            if id in env.variables:
                return env.variables.get(id)
            env = env.entorno_anterior
        return None        

    def getStruct(self, id):
        env = self
        while(env != None):
            if id in env.structs:
                return env.structs.get(id)
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
        

