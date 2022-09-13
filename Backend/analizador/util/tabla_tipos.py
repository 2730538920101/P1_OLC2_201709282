from ..abstract.retorno import *

TablaSuma = [
    #i64       #f64       #char      #string     #str      #null       #usize
    [Type.I64, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.USIZE],
    [Type.NULL, Type.F64, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.STRING, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.STRING, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.USIZE, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.USIZE]    
]

TablaResta = [
    [Type.I64, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.USIZE],
    [Type.NULL, Type.F64, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.USIZE, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.USIZE] 
]

TablaMultiplicacion = [
    [Type.I64, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.F64, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL]
]

TablaDivision = [
    [Type.F64, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.F64, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL]
]

TablaPotencia = [
    [Type.I64, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.F64, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL]
]

TablaModulo = [
    [Type.I64, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.F64, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL],
    [Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL, Type.NULL]
]

TablaUnario = [
    [Type.I64],
    [Type.F64],
    [Type.NULL],
    [Type.NULL],
    [Type.NULL],
    [Type.NULL]
]

TablaRaiz = [
    [Type.F64],
    [Type.F64],
    [Type.NULL],
    [Type.NULL],
    [Type.NULL],
    [Type.NULL]
]
