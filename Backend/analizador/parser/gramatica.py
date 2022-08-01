reservadas = {
    'string' : 'STRING',
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
    'print' : 'PRINT',
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
    'vec' : 'VEC',
    'chars' : 'CHARS',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',
    'mod' : 'MOD',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'to_owned' : 'TO_OWNED',
    'to_string' : 'TO_STRING'
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
    'OR',
    'AND',
    'DIF',
    'FLECHA',
    'DOBIGUAL',
    'COMENTARIO',
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
t_AND =	r'[\&][\&]'
t_DIF =	r'[\!][\=]'
t_FLECHA =	r'[\-][\>]'
t_DOBIGUAL = r'[\=][\=]'


t_ignore_COMENTARIO = r'[\/][\/].*'

t_ignore = r' '

def t_IDENTIFICADOR(t):
    r'[a-zA-Z0-9\_]+([a-zA-Z0-9\_]*[a-zA-Z0-9]+|[a-zA-Z0-9]+)'
    try:
        t.type = reservadas.get(t.value.lower(), 'IDENTIFICADOR')
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
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_NUMERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
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
    print("ERROR LEXICO ", t.value[0])
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


precedence = (
    ('left', '||'),
    ('left', '&&'),
    ('right', '!'), 
    ('left', '!=', '==', '<=', '>=', '<', '>'),
    ('left', '+', '-'),
    ('left', '*', '/', '%'),
    ('nonassoc', 'ˆ'),
    ('nonassoc', '(' , ')'),
    ('right', 'UMENOS')
)
