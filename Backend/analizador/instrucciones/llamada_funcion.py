from ..abstract.instrucciones import *
from ..abstract.retorno import *
from ..instrucciones.funcion import *
from ..expresiones.tipo_vector import *
from ..expresiones.array_type import *
from ..reportes.TablaSim import *

class Llamada_funcion(Instruccion):
    def __init__(self, linea, columna, id, params):
        super().__init__(linea, columna)
        self.id = id
        self.params = params

    def Ejecutar(self, environment):
        print("EJECUTANDO LLAMADA A FUNCION")
        fun = environment.getFuncion(self.id)
        if isinstance(fun, Funcion):
            tipret = fun.tipado
            if self.params != None:
                for p in self.params:
                    p = p.Ejecutar(environment)
                bandera = self.ValidarParams(fun.parametros, self.params, environment)
                if bandera == True:
                    element = fun.statement.Ejecutar(environment)
                    if element != None:
                        if element.tipado == tipret:
                            return element
                        elif tipret == Type.NULL:
                            auxer = "ERROR, SEMANTICO, LA FUNCION NO DEBE RETORNAR NINGUN VALOR"
                            print(auxer)
                            TablaErrores.append(auxer)
                            Prints.append(auxer)
                            return None     
                        else:
                            auxer = "ERROR SEMANTICO, LA FUNCION DEBE RETORNAR UN VALOR DEL TIPO ESPECIFICADO EN EL RETORNO DE LA FUNCION"
                            print(auxer)
                            TablaErrores.append(auxer)
                            Prints.append(auxer)
                            return None
                    else:
                        if tipret != Type.NULL:
                            auxer = "ERROR SEMANTICO, LA FUNCION DEBE RETORNAR UN VALOR DEL TIPO ESPECIFICADO EN EL RETORNO DE LA FUNCION"
                            print(auxer)
                            TablaErrores.append(auxer)
                            Prints.append(auxer)
                else:
                    auxer = "ERROR SEMANTICO, LOS TIPOS DE LOS PARAMETROS NO SON VALIDOS"
                    print(auxer)
                    TablaErrores.append(auxer)
                    Prints.append(auxer)
            else:
                element = fun.statement.Ejecutar(environment)
                if element != None:
                    if element.tipado == tipret:
                        return element
                    elif tipret == Type.NULL:
                        auxer = "ERROR, SEMANTICO, LA FUNCION NO DEBE RETORNAR NINGUN VALOR"
                        print(auxer)
                        TablaErrores.append(auxer)
                        Prints.append(auxer)
                        return None     
                    else:
                        auxer = "ERROR SEMANTICO, LA FUNCION DEBE RETORNAR UN VALOR DEL TIPO ESPECIFICADO EN EL RETORNO DE LA FUNCION"
                        print(auxer)
                        TablaErrores.append(auxer)
                        Prints.append(auxer)
                        return None
                else:
                    if tipret != Type.NULL:
                        auxer = "ERROR SEMANTICO, LA FUNCION DEBE RETORNAR UN VALOR DEL TIPO ESPECIFICADO EN EL RETORNO DE LA FUNCION"
                        print(auxer)
                        TablaErrores.append(auxer)
                        Prints.append(auxer)
        else:
            auxer = "ERROR SEMANTICO, LA FUNCION NO HA SIDO DECLARADA"
            print(auxer)
            TablaErrores.append(auxer)
            Prints.append(auxer)


    def ValidarParams(self, parametrosfuncion, parametrosllamada, environment):
        flag = False
        if len(parametrosfuncion) == len(parametrosllamada):
            for x in range(len(parametrosfuncion)):
                val = parametrosllamada[x].exp.Ejecutar(environment)
                iden = parametrosfuncion[x].id
                tip = parametrosfuncion[x].tipado
                if isinstance(tip, Tipo_vector) or isinstance(tip, Array_type):
                    tip = tip.tipado
                if tip == val.tipado:
                    environment.guardarVariables(iden, val.value, val.tipado, True)
                    flag = True
                else:
                    flag = False
                    break
        else:
            flag = False
        return flag
    

