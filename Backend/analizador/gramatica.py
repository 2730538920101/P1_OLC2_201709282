import ply.lex as lex
import ply.yacc as yacc
from .abstract.expresiones import *
from .abstract.instrucciones import *
from .abstract.retorno import *
from .expresiones.arithmetic import *
from .expresiones.literal import *
from .expresiones.logic import *
from .expresiones.relational import *
from .symbol.environment import *

cont = 0
reservadas = {
    'String' : 'STRING',
    'i64' : 'I64',
    'f64' : 'F64',
    'bool' : 'BOOL',
    'char' : 'CHAR',
    'str' : 'STR',
    'usize' : 'USIZE',
    'struct' : 'STRUCT',
    'let' : 'LET',
    'new' : 'NEW',
    'mut' : 'MUT',
    'as' : 'AS',
    'pow' : 'POW',
    'powf' : 'POWF',
    'println' : 'PRINTLN',
    'fn' : 'FN',
    'abs' : 'ABS',
    'sqrt' : 'SQRT',
    'clone' : 'CLONE',
    'len' : 'LEN',
    'push' : 'PUSH',
    'remove' : 'REMOVE',
    'contains' : 'CONTAINS',
    'insert' : 'INSERT',
    'capacity' : 'CAPACITY',
    'with_capacity' : 'WITH_CAPACITY',
    'if' : 'IF',
    'else' : 'ELSE',
    'match' : 'MATCH',
    'loop' : 'LOOP',
    'while' : 'WHILE',
    'for' : 'FOR',
    'in' : 'IN',
    'vec' : 'VECMIN',
    'Vec' : 'VECMAY',
    'chars' : 'CHARS',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',
    'mod' : 'MOD',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'to_owned' : 'TO_OWNED',
    'to_string' : 'TO_STRING',
    'pub' : 'PUB',
    'main' : 'MAIN'
}

tokens = [
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'MAYOR',
    'MENOR',
    'IGUAL',
    'LLAVEAP',
    'LLAVECL',
    'NOT',
    'PCOMA',
    'DOSPUNTOS',
    'CORCHETEAP',
    'CORCHETECL',
    'PARAP',
    'PARCL',
    'PUNTO',
    'COMA',
    'MODULO',
    'BARRA',
    'MENORIG',
    'MAYORIG',
    'CONCAT',
    'OR',
    'AND',
    'DIF',
    'FLECHA',
    'DOBFLECHA',
    'DOBIGUAL',
    'COMENTARIO',
    'GBAJO',
    'IDENTIFICADOR',
    'CADENA',
    'NUMERO',
    'DECIMAL',
    'CARACTER'
]+ list(reservadas.values())

t_MAS = r'\+'
t_MENOS = r'[\-]'
t_POR =	r'[\*]'
t_DIV =	r'[\/]'
t_MAYOR = r'[\<]'
t_MENOR = r'[\>]'
t_IGUAL	= r'[\=]'
t_CORCHETEAP =	r'\['
t_CORCHETECL =	r'\]'
t_LLAVEAP =	r'[\{]'
t_LLAVECL =	r'[\}]'
t_NOT =	r'[\!]'
t_PCOMA = r'[\;]'
t_DOSPUNTOS = r'[\:]'
t_PARAP	= r'\(' 
t_PARCL	= r'\)'
t_PUNTO	= r'[\.]'
t_COMA	= r'[\,]'
t_MODULO =	r'[\%]'
t_BARRA = r'\|'
t_MENORIG = r'[\<][\=]'
t_MAYORIG = r'[\>][\=]'
t_OR = r'[\|][\|]'
t_GBAJO = r'[\_]'
t_CONCAT = r'[\&]'
t_AND =	r'[\&][\&]'
t_DIF =	r'[\!][\=]'
t_DOBFLECHA = r'[\=][\>]'
t_FLECHA =	r'[\-][\>]'
t_DOBIGUAL = r'[\=][\=]'


t_ignore = ' \n\r\t'


def t_COMENTARIO(t):
    r'[\/][\/].*'
    t.lexer.lineno += 1



def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    try:
        t.type = reservadas.get(t.value, 'IDENTIFICADOR')
    except ValueError:
        print("EL VALOR INGRESADO NO PUEDE SER UN IDENTIFICADOR")
        t.value='ERROR'
    return t

    
def t_CADENA(t):
    r'[\"][^\"\n]*[\"]'
    try:
        t.value = t.value[1:-1]
    except ValueError:
        print("EL VALOR INGRESADO NO PUEDE SER UNA CADENA")
        t.value='ERROR'
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float muy grande %d", t.value)
        t.value = 0
    return t

def t_NUMERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer muy grande %d", t.value)
        t.value = 0
    return t


def t_CARACTER(t):
    r'[\'][^\'\n]*[\']'
    try:
        t.value = t.value[1:-1]
    except ValueError:
        print("EL VALOR INGRESADO NO PUEDE SER UN CARACTER")
        t.value='ERROR'
    return t


def t_error(t):
     print("ERROR LEXICO '%s'" % t.value[0])
     t.lexer.skip(1)


def t_newline(t):
    r'\n+'
   
    cont = t.lexer.lexpos
    t.lexer.lineno += t.value.count("\n")
    

def t_eof(t):
    return None


precedence = (
    ('nonassoc', 'AS', 'IN'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'), 
    ('left', 'DIF', 'DOBIGUAL', 'MENORIG', 'MAYORIG', 'MENOR', 'MAYOR'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIV', 'MODULO'),
    ('nonassoc', 'PARAP' , 'PARCL'),
    ('right', 'UMENOS')
)

lexer = lex.lex()


def p_init(p) :
    '''
    init    : entorno_global 
    '''
    p[0] = p[1]


def p_entorno_global(p):
    '''
    entorno_global  : entorno_global global
    '''
    p[1].append(p[2])
    p[0] = p[1]

def p_global_listado(p):
    '''
    entorno_global  : global
    '''
    p[0] = [p[1]]

def p_global(p):
    '''
    global  : expresiones
    '''
    p[0] = p[1]


def p_expresiones(p):
    '''
    expresiones : expresiones_aritmeticas
                | expresiones_logicas
                | expresiones_relacionales
                | valores
               
    '''
    p[0] = p[1]

def p_expresiones_2(p):
    '''
    expresiones : PARAP expresiones PARCL
    '''
    p[0] = p[2]

def p_expresiones_aritmeticas_1(p):
    '''
    expresiones_aritmeticas : expresiones MAS expresiones
                            | expresiones MENOS expresiones
                            | expresiones POR expresiones
                            | expresiones DIV expresiones
                            | expresiones MODULO expresiones
    '''
    if p[2] == "+":
        p[0] = Arithmetic(p.lineno(2), p.lexpos(2), p[1], p[3], ArithmeticOption.SUMA)
    elif p[2] == "-":
        p[0] = Arithmetic(p.lineno(2), p.lexpos(2), p[1], p[3], ArithmeticOption.RESTA)
    elif p[2] == "*":
        p[0] = Arithmetic(p.lineno(2), p.lexpos(2), p[1], p[3], ArithmeticOption.MULTIPLICACION)
    elif p[2] == "/":
        p[0] = Arithmetic(p.lineno(2), p.lexpos(2), p[1], p[3], ArithmeticOption.DIVISION)
    elif p[2] == "%":
        p[0] = Arithmetic(p.lineno(2), p.lexpos(2), p[1], p[3], ArithmeticOption.MODULO)

def p_expresiones_aritmeticas_2(p):
    '''
    expresiones_aritmeticas : MENOS expresiones %prec UMENOS
    '''
    p[0] = Arithmetic(p.lineno(1), p.lexpos(1), 0, p[2], ArithmeticOption.UNARIO)

def p_expresiones_logicas_1(p):
    '''
    expresiones_logicas : expresiones AND expresiones
                        | expresiones OR expresiones
                        | expresiones BARRA expresiones
    '''
    if p[2] == "&&":
        p[0] = Logic(p.lineno(1), p.lexpos(1), p[1], p[3], LogicOption.AND)
    elif p[2] == "|" or p[2] == "||":
        p[0] =  Logic(p.lineno(1), p.lexpos(1), p[1], p[3], LogicOption.OR)

def p_expresiones_logicas_2(p):
    '''
    expresiones_logicas : NOT expresiones
    '''
    p[0] = Logic(p.lineno(1), p.lexpos(1), p[2], None, LogicOption.NOT)

def p_expresiones_relacionales(p):
    '''
    expresiones_relacionales    : expresiones MAYOR expresiones
                                | expresiones MENOR expresiones
                                | expresiones DOBIGUAL expresiones
                                | expresiones DIF expresiones
                                | expresiones MAYORIG expresiones
                                | expresiones MENORIG expresiones
    ''' 
    if p[2] == ">":
        p[0] = Relational(p.lineno(2), p.lexpos(2), p[1], p[3], RelationalOption.MAYOR)
    elif p[2] == ">=":
        p[0] = Relational(p.lineno(2), p.lexpos(2), p[1], p[3], RelationalOption.MAYORIG)    
    elif p[2] == "<":
        p[0] = Relational(p.lineno(2), p.lexpos(2), p[1], p[3], RelationalOption.MENOR)
    elif p[2] == "<=":
        p[0] = Relational(p.lineno(2), p.lexpos(2), p[1], p[3], RelationalOption.MENORIG)
    elif p[2] == "!=":
        p[0] = Relational(p.lineno(2), p.lexpos(2), p[1], p[3], RelationalOption.DIF)
    elif p[2] == "==":
        p[0] = Relational(p.lineno(2), p.lexpos(2), p[1], p[3], RelationalOption.DOBIGUAL)

def p_especiales_1(p):
    '''
    especiales  : expresiones AS tipo_dato
                | expresiones IN expresiones
    '''

def p_especiales_2(p):
    '''
    especiales  :   expresiones PUNTO PUNTO expresiones
                
    '''

def p_valores_1(p):
    '''
    valores : CADENA
    '''
    p[0] = Literal(p.lineno(1), p.lexpos(1), p[1], Type.STRING)

def p_valores_2(p):
    '''
    valores : CARACTER
    '''
    p[0] = Literal(p.lineno(1), p.lexpos(1), p[1], Type.CHAR)


def p_valores_3(p):
    '''
    valores : DECIMAL
    '''
    p[0] = Literal(p.lineno(1), p.lexpos(1), p[1], Type.F64)

def p_valores_4(p):
    '''
    valores : NUMERO
            
    '''
    p[0] = Literal(p.lineno(1), p.lexpos(1), p[1], Type.I64)

def p_valores_5(p):
    '''
    valores : TRUE
            | FALSE
    '''
    if p[1] == "true":
        p[0] = Literal(p.lineno(1), p.lexpos(1), True, Type.BOOL)
    else:
        p[0] = Literal(p.lineno(1), p.lexpos(1), False, Type.BOOL)



def p_tipo_dato(p):
    '''
    tipo_dato   : I64
                | F64
                | STRING
                | CHAR
                | BOOL
                | STR
                | USIZE
                | STRUCT
    '''
    p[0] = p[1]

def p_tipo_dato_2(p):
    '''
    tipo_dato   : CONCAT MUT I64
                | CONCAT MUT F64
                | CONCAT MUT STR
                | CONCAT MUT CHAR
                | CONCAT MUT BOOL
    '''
    p[0] = p[1] + p[2] + p[3]

def p_tipo_dato_3(p):
    '''
    tipo_dato   : CONCAT I64
                | MUT I64
                | CONCAT F64
                | MUT F64
                | CONCAT STR
                | MUT STR
                | MUT STRING
                | CONCAT CHAR
                | MUT CHAR
                | CONCAT BOOL
                | MUT BOOL
    '''
    p[0] = p[1] + p[2] 

def p_error(p):
    linea_actual = p.lexer.lexpos - cont
    print(cont)
    print("ERROR SINTACTICO EN EL TOKEN: ", p.type, "EN LA LINEA: ", p.lexer.lineno, "EN LA COLUMNA: ", linea_actual)
          
parser = yacc.yacc()