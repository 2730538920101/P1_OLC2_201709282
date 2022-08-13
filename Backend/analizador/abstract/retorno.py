from enum import Enum, unique

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
    

class Retorno:
    def setReturnValue(self, value, tipado):
        self.value = value
        self.tipado = tipado

