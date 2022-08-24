from enum import Enum, unique
from http.client import CONTINUE

@unique
class Type(Enum):
    I64 = 0,
    F64 = 1,
    CHAR = 2,
    STRING = 3,
    STR = 4,
    NULL = 5,
    BOOL = 6,
    USIZE = 7,
    STRUCT = 8,
    BREAK = 9,
    CONTINUE = 10,
    RETURN = 11,
    ARRAY = 12
    

class Retorno:
    def __init__(self, value = None, tipado = Type.NULL):
        self.value = value
        self.tipado = tipado

