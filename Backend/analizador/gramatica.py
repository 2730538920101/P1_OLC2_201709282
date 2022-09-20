import ply.lex as lex
import ply.yacc as yacc

from .abstract.expresiones import *
from .abstract.instrucciones import *
from .abstract.retorno import *
from .expresiones.arithmetic import *
from .expresiones.literal import *
from .expresiones.logic import *
from .expresiones.relational import *
from .expresiones.access import *
from .expresiones.casting import *
from .expresiones.array_index import *
from .expresiones.array_complete import *
from .expresiones.array_type import *
from .expresiones.vector_index import *
from .expresiones.vector_complete import *
from .expresiones.atributo_struct import *
from .expresiones.generar_struct import *
from .expresiones.access_index import *
from .expresiones.struct_access import *
from .expresiones.clone import *
from .expresiones.abs import *
from .expresiones.chars import *
from .expresiones.len import *
from .expresiones.capacity import *
from .expresiones.contains import *
from .expresiones.casting_str_string import *
from .expresiones.range import *
from .expresiones.parametros_declaracion import *
from .expresiones.tipo_vector import *
from .expresiones.parametro_llamada import *
from .symbol.environment import *
from .instrucciones.statement import *
from .instrucciones.assigment import *
from .instrucciones.declaration import *
from .instrucciones.funcion import *
from .instrucciones.if_inst import *
from .instrucciones.while_inst import *
from .instrucciones.break_inst import *
from .instrucciones.continue_inst import *
from .instrucciones.return_inst import *
from .instrucciones.loop import *
from .instrucciones.match import *
from .instrucciones.case import *
from .instrucciones.for_inst import *
from .instrucciones.declaracion_struct import *
from .instrucciones.declaracion_atributo import *
from .instrucciones.access_assigment import *
from .instrucciones.struct_assigment import *
from .instrucciones.push import *
from .instrucciones.insert import *
from .instrucciones.remove import *
from .instrucciones.funcion import *
from .instrucciones.llamada_funcion import *
from .instrucciones.print import *
from .instrucciones.funcion_main import *
from .reportes.TablaSim import *

Contadormain = 0

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
t_MAYOR = r'[\>]'
t_MENOR = r'[\<]'
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
t_CONCAT = r'[\&]'
t_AND =	r'[\&][\&]'
t_DIF =	r'[\!][\=]'
t_DOBFLECHA = r'[\=][\>]'
t_FLECHA =	r'[\-][\>]'
t_DOBIGUAL = r'[\=][\=]'
t_GBAJO = r'[_]'


t_ignore = ' \n\r\t'


def t_COMENTARIO(t):
    r'[\/][\/].*'
    t.lexer.lineno += 1



def t_IDENTIFICADOR(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    try:
        t.type = reservadas.get(t.value, 'IDENTIFICADOR')
    except ValueError:
        auxer = "EL VALOR INGRESADO NO PUEDE SER UN IDENTIFICADOR"
        print(auxer)
        TablaErrores.append(auxer)
        Prints.append(auxer)
        t.value='ERROR'
    return t

    
def t_CADENA(t):
    r'[\"][^\"\n]*[\"]'
    try:
        t.value = t.value[1:-1]
    except ValueError:
        auxer = "EL VALOR INGRESADO NO PUEDE SER UNA CADENA"
        print(auxer)
        TablaErrores.append(auxer)
        Prints.append(auxer)
        t.value='ERROR'
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        auxer = "Float muy grande " + str(t.value)
        print(auxer)
        TablaErrores.append(auxer)
        Prints.append(auxer)
        t.value = 0
    return t

def t_NUMERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        auxer = "Integer muy grande " +  str(t.value)
        print(auxer)
        TablaErrores.append(auxer)
        Prints.append(auxer)
        t.value = 0
    return t


def t_CARACTER(t):
    r'[\'][^\'\n]*[\']'
    try:
        t.value = t.value[1:-1]
    except ValueError:
        auxer = "EL VALOR INGRESADO NO PUEDE SER UN CARACTER"
        print(auxer)
        TablaErrores.append(auxer)
        Prints.append(auxer)
        t.value='ERROR'
    return t


def t_error(t):
    auxer = "ERROR LEXICO " + str(t.value[0])
    print(auxer)
    TablaErrores.append(auxer)
    Prints.append(auxer)
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
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
    global  : funcion_main
            | declaracion_struct
            | declaracion_funciones
            | COMENTARIO
    '''
    p[0] = p[1]

def p_funcion_main(p):
    '''
    funcion_main    : FN MAIN PARAP PARCL entorno
    '''
    p[0] = Funcion_main(p.lineno(1), p.lexpos(1), p[5])
    
def p_instruccion(p):
    '''
    instruccion : declaracion_variable
		        | asignacion
                | expresiones
                | asignacion_arr
                | COMENTARIO
    '''
    p[0] = p[1]


def p_transferecia_1(p):
    '''
    transferencia   : BREAK
                    | RETURN 
                    | CONTINUE 
    '''
    if p[1] == "break":
        p[0] = Break(p.lineno(1), p.lexpos(1), None, Type.BREAK)
    elif p[1] == "return":
        p[0] = Return(p.lineno(1), p.lexpos(1), None, Type.RETURN)
    elif [1] == "continue":
        p[0] = Continue(p.lineno(1), p.lexpos(1), None, Type.CONTINUE)
    else:
        print("ERROR EN LA INSTRUCCION DE TRANSFERENCIA")

def p_transferecia_2(p):
    '''
    transferencia   : BREAK expresiones
                    | RETURN expresiones 
    '''
    if p[1] == "break":
        p[0] = Break(p.lineno(1), p.lexpos(1), p[2], Type.BREAK)
    elif p[1] == "return":
        p[0] = Return(p.lineno(1), p.lexpos(1), p[2], Type.RETURN)

def p_sentencias(p):
    '''
    sentencias  : generar_if
                | generar_while
                | generar_for
                | generar_loop
                | generar_match
    '''
    p[0] = p[1]


def p_generar_if(p):   
    '''
    generar_if  : IF expresiones entorno generar_else

    '''
    p[0] = If(p.lineno(1), p.lexpos(1), p[2], p[3], p[4])

def p_generar_else_1(p):
    '''
    generar_else    : ELSE entorno  
    generar_else    : ELSE generar_if
    ''' 
    p[0] = p[2]

def p_generar_else_2(p):
    '''
    generar_else    : empty
    ''' 
    p[0] = p[1]

def p_empty(p):
    'empty :'
    p[0] = Type.NULL


def p_generar_while(p):
    '''
    generar_while : WHILE expresiones entorno
    '''
    p[0] = While(p.lineno(1), p.lexpos(1), p[2], p[3])

def p_generar_for(p):
    '''
    generar_for : FOR IDENTIFICADOR IN expresiones entorno 
    '''
    p[0] = For(p.lineno(1), p.lexpos(1), p[2], p[4], p[5])

def p_generar_loop(p):
    '''
    generar_loop    : LOOP entorno
    '''
    p[0] = Loop(p.lineno(1), p.lexpos(1), p[2])

def p_entorno_match (p):
    '''
    entorno_match   : LLAVEAP lista_cases LLAVECL
    '''
    p[0] = p[2]

def p_generar_match(p):
    '''
    generar_match   : MATCH expresiones entorno_match
    '''
    p[0] = Match(p.lineno(1), p.lexpos(1), p[2], p[3])

def p_lista_cases(p):
    '''
    lista_cases : lista_cases lista_expresiones DOBFLECHA entorno
    '''
    c1 = Case(p.lineno(1), p.lexpos(1), p[2], p[4])
    p[1].append(c1)
    p[0] = p[1]

def p_lista_cases_2(p):
    '''
    lista_cases : lista_cases lista_expresiones DOBFLECHA instruccion
    '''
    c2 = Case(p.lineno(1), p.lexpos(1), p[2], p[4])
    p[1].append(c2)
    p[0] = p[1]

def p_lista_cases_3(p):
    '''
    lista_cases : lista_cases GBAJO DOBFLECHA entorno
    '''
    c3 = Case(p.lineno(1), p.lexpos(1), p[2], p[4])
    p[1].append(c3)
    p[0] = p[1]

def p_lista_cases_4(p):
    '''
    lista_cases : lista_cases GBAJO DOBFLECHA instruccion 
    '''
    c1 = Case(p.lineno(1), p.lexpos(1), p[2], p[4])
    p[1].append(c1)
    p[0] = p[1]

def p_lista_cases_5(p):
    '''
    lista_cases : lista_expresiones DOBFLECHA entorno
    '''
    p[0] = [Case(p.lineno(1), p.lexpos(1), p[1], p[3])]

def p_lista_cases_6(p):
    '''
    lista_cases : lista_expresiones DOBFLECHA instruccion 
    '''
    p[0] = [Case(p.lineno(1), p.lexpos(1), p[1], p[3])]

def p_lista_cases_7(p):
    '''
    lista_cases : GBAJO DOBFLECHA entorno
    '''
    p[0] = [Case(p.lineno(1), p.lexpos(1), p[1], p[3])]

def p_lista_cases_8(p):
    '''
    lista_cases : GBAJO DOBFLECHA instruccion 
    '''
    p[0] = [Case(p.lineno(1), p.lexpos(1), p[1], p[3])]

def p_entorno_1(p):
    '''
    entorno : LLAVEAP lista_instrucciones LLAVECL
    '''
    p[0] = Statement(p.lineno(1), p.lexpos(1), p[2])

def p_entorno_2(p):
    '''
    entorno : LLAVEAP LLAVECL
    '''
    pass

def p_lista_instrucciones_lista(p):
    '''
    lista_instrucciones : lista_instrucciones instruccion
    ''' 
    p[0] = p[1].append(p[2])
    p[0] = p[1]

def p_lista_instrucciones(p):
    '''
    lista_instrucciones : instruccion
    '''
    p[0] = [p[1]]


def p_declaracion_struct_1(p):
    '''
    declaracion_struct  : STRUCT IDENTIFICADOR LLAVEAP lista_atributos_declaracion LLAVECL
    '''
    p[0] = Declaracion_struct(p.lineno(1), p.lexpos(1), p[2], p[4], Type.STRUCT, False)


def p_declaracion_struct_2(p):
    '''
    declaracion_struct  : PUB STRUCT IDENTIFICADOR LLAVEAP lista_atributos_declaracion LLAVECL
    '''
    p[0] = Declaracion_struct(p.lineno(1), p.lexpos(1), p[3], p[5], Type.STRUCT, True)


def p_lista_atributos_struct_1(p):
    '''
    lista_atributos_declaracion :   lista_atributos_declaracion COMA IDENTIFICADOR DOSPUNTOS tipo_dato
    '''
    atr = Declaracion_atributo(p.lineno(3), p.lexpos(3), p[3], p[5])
    p[1].append(atr)
    p[0] = p[1] 

def p_lista_atributos_struct_2(p):
    '''
    lista_atributos_declaracion :   IDENTIFICADOR DOSPUNTOS tipo_dato
    '''
    p[0] = [Declaracion_atributo(p.lineno(1), p.lexpos(1), p[1], p[3])]

##FUNCION
def p_lista_parametros_1(p):
    '''
    lista_parametros    : lista_parametros COMA IDENTIFICADOR DOSPUNTOS tipo_dato
    '''
    atr = Parametros_declaracion(p.lineno(1), p.lexpos(1), p[3], p[5], False)
    p[1].append(atr)
    p[0] = p[1]

##FUNCION
def p_lista_parametros_2(p):
    '''
    lista_parametros    :   IDENTIFICADOR DOSPUNTOS tipo_dato
    '''
    p[0] = [Parametros_declaracion(p.lineno(1), p.lexpos(1), p[1], p[3], False)]

##FUNCION
def p_lista_parametros_3(p):
    '''
    lista_parametros    : lista_parametros COMA IDENTIFICADOR DOSPUNTOS CONCAT MUT tipo_dato
    '''
    atr = Parametros_declaracion(p.lineno(1), p.lexpos(1), p[3], p[7], True)
    p[1].append(atr)
    p[0] = p[1]

##FUNCION
def p_lista_parametros_4(p):
    '''
    lista_parametros    :   IDENTIFICADOR DOSPUNTOS CONCAT MUT tipo_dato
    '''
    p[0] = [Parametros_declaracion(p.lineno(1), p.lexpos(1), p[1], p[5], True)]


##FUNCION
def p_declaracion_funciones_1(p):
    '''
    declaracion_funciones   : FN IDENTIFICADOR PARAP lista_parametros PARCL entorno
    '''
    p[0] = Funcion(p.lineno(1), p.lexpos(1), p[2], Type.NULL, p[6], p[4], False)

##FUNCION
def p_declaracion_funciones_2(p):
    '''
    declaracion_funciones   : FN IDENTIFICADOR PARAP lista_parametros PARCL FLECHA tipo_dato entorno
    '''
    p[0] = Funcion(p.lineno(1), p.lexpos(1), p[2], p[7], p[8], p[4], False)


##FUNCION
def p_declaracion_funciones_3(p):
    '''
    declaracion_funciones   : PUB FN IDENTIFICADOR PARAP lista_parametros PARCL entorno
    '''
    p[0] = Funcion(p.lineno(1), p.lexpos(1), p[3], Type.NULL, p[7], p[5], True)

##FUNCION
def p_declaracion_funciones_4(p):
    '''
    declaracion_funciones   : PUB FN IDENTIFICADOR PARAP lista_parametros PARCL FLECHA tipo_dato entorno
    '''
    p[0] = Funcion(p.lineno(1), p.lexpos(1), p[3], p[8], p[9], p[5], True)



def p_declaracion_variable(p):
    '''
    declaracion_variable    : LET asignacion
		                    		     
    '''
    p[0] = Declaration(p.lineno(1), p.lexpos(1), p[2], False)

def p_declaracion_variable_2(p):
    '''
    declaracion_variable    : LET MUT asignacion
    '''
    p[0] = Declaration(p.lineno(1), p.lexpos(1), p[3], True)

def p_asignacion_1(p):
    '''
    asignacion  : IDENTIFICADOR DOSPUNTOS tipo_dato IGUAL expresiones
    '''
    if p[3] == Type.I64:
        p[0] = Assigment(p.lineno(1), p.lexpos(1), p[1], p[5], Type.I64)
    elif p[3] == Type.F64:
        p[0] = Assigment(p.lineno(1), p.lexpos(1), p[1], p[5], Type.F64)
    elif p[3] == Type.CHAR:
        p[0] = Assigment(p.lineno(1), p.lexpos(1), p[1], p[5], Type.CHAR)
    elif p[3] == Type.BOOL:
        p[0] = Assigment(p.lineno(1), p.lexpos(1), p[1], p[5], Type.BOOL)
    elif p[3] == Type.STRING:
        p[0] = Assigment(p.lineno(1), p.lexpos(1), p[1], p[5], Type.STRING)
    elif p[3] == Type.STR:
        p[0] = Assigment(p.lineno(1), p.lexpos(1), p[1], p[5], Type.STR)
    elif p[3] == Type.STRUCT:
        p[0] = Assigment(p.lineno(1), p.lexpos(1), p[1], p[5], Type.STRUCT)
    elif p[3] == Type.USIZE:
        p[0] = Assigment(p.lineno(1), p.lexpos(1), p[1], p[5], Type.USIZE)
    elif isinstance(p[3], Array_type):
        p[0] = Assigment(p.lineno(1), p.lexpos(1), p[1], p[5], p[3])
    elif isinstance(p[3], Tipo_vector):
        p[0] = Assigment(p.lineno(1), p.lexpos(1), p[1], p[5], p[3])

    

def p_asignacion_2(p):
    '''
    asignacion  : IDENTIFICADOR IGUAL expresiones
    '''
    p[0] = Assigment(p.lineno(1), p.lexpos(1), p[1], p[3], Type.NULL)



##ARRAY
def p_asignacion_arr(p):
    '''
    asignacion_arr  : IDENTIFICADOR lista_indices IGUAL expresiones
    '''
    p[0] = Access_assigment(p.lineno(1), p.lexpos(1), p[1], p[2],p[4])



def p_expresiones(p):
    '''
    expresiones : expresiones_aritmeticas
                | expresiones_logicas
                | expresiones_relacionales
                | valores
                | sentencias
                | transferencia
                | casting
                | expresiones PCOMA
                | funciones_vectores
                | llamada_funcion
                | print               
    '''
    p[0] = p[1]


def p_expresiones_2(p):
    '''
    expresiones : PARAP expresiones PARCL
    '''
    p[0] = p[2]



def p_identificadores_1(p):
    '''
    expresiones :   lista_identificadores
                    
    '''
    if len(p[1]) > 1:
        p[0] = Struct_access(p.lineno(1), p.lexpos(1), p[1])
    else:
        p[0] = Access(p.lineno(1), p.lexpos(1), p[1].pop(0)) 

def p_lista_identificadores_1(p):
    '''
    lista_identificadores   : lista_identificadores PUNTO IDENTIFICADOR
    '''
    p[1].append(p[3])
    p[0] = p[1]


def p_lista_identificadores_3(p):
    '''
    lista_identificadores   : IDENTIFICADOR 
    '''
    p[0] = [p[1]]

##ARRAY
def p_expresiones_4(p):
    '''
    expresiones : CORCHETEAP expresiones PCOMA expresiones CORCHETECL
    '''
    p[0] = Array_index(p.lineno(1), p.lexpos(1), p[2], p[4])

##ARRAY
def p_expresiones_5(p):
    '''
    expresiones : CORCHETEAP lista_expresiones CORCHETECL
    '''
    p[0] = Array_complete(p.lineno(1), p.lexpos(1), p[2], Type.ARRAY)

##VECTOR
def p_expresiones_6(p):
    '''
    expresiones : VECMIN NOT CORCHETEAP expresiones PCOMA expresiones CORCHETECL
    '''
    p[0] = Vector_index(p.lineno(1), p.lexpos(1), p[4], p[6])

##VECTOR
def p_expresiones_7(p):
    '''
    expresiones : VECMIN NOT CORCHETEAP lista_expresiones CORCHETECL
    '''
    p[0] = Vector_complete(p.lineno(1), p.lexpos(1), p[4], Type.VECTOR, None)

##VECTOR
def p_expresiones_8(p):
    '''
    expresiones : VECMAY DOSPUNTOS DOSPUNTOS NEW PARAP PARCL
    '''
    p[0] = Vector_complete(p.lineno(1), p.lexpos(1), None, Type.VECTOR, None)

##VECTOR
def p_expresiones_9(p):
    '''
    expresiones : VECMAY DOSPUNTOS DOSPUNTOS WITH_CAPACITY PARAP expresiones PARCL
    '''
    p[0] = Vector_complete(p.lineno(1), p.lexpos(1), None, Type.VECTOR, p[6])


def p_expresiones_10(p):
    '''
    expresiones : IDENTIFICADOR LLAVEAP lista_atributos LLAVECL
    '''
    p[0] = Generar_struct(p.lineno(1), p.lexpos(1), p[1], p[3], Type.STRUCT)

##ARRAY Y VECTOR
def p_expresiones_11(p):
    '''
    expresiones : IDENTIFICADOR lista_indices
    '''
    p[0] = Access_index(p.lineno(1), p.lexpos(1), p[1], p[2])



def p_expresiones_12(p):
    '''
    expresiones : expresiones PUNTO PUNTO expresiones
    '''
    p[0] = Range(p.lineno(1), p.lexpos(1), p[1], p[4])


##ARRAY Y VECTOR
def p_lista_indices_1(p):
    '''
    lista_indices   :   lista_indices CORCHETEAP expresiones CORCHETECL
    '''
    p[1].append(p[3])
    p[0] = p[1]

##ARRAY Y VECTOR
def p_lista_indices_2(p):
    '''
    lista_indices   : CORCHETEAP expresiones CORCHETECL
    '''
    p[0] = [p[2]]

def p_lista_atributos_1(p):
    '''
    lista_atributos :   lista_atributos COMA IDENTIFICADOR DOSPUNTOS expresiones 
    '''
    atr1 = Atributo_struct(p.lineno(3), p.lexpos(3),p[3], p[5])
    p[1].append(atr1)
    p[0] = p[1]

def p_lista_atributos_2(p):
    '''
    lista_atributos :   IDENTIFICADOR DOSPUNTOS expresiones
    '''
    p[0] = [Atributo_struct(p.lineno(1), p.lexpos(1), p[1], p[3])]

def p_lista_exp_1(p):
    '''
    lista_expresiones   : lista_expresiones COMA expresiones
                        | lista_expresiones BARRA expresiones

    '''
    p[1].append(p[3])
    p[0] = p[1]

def p_lista_exp_2(p):
    '''
    lista_expresiones   : expresiones
    '''
    p[0] = [p[1]]



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
    p[0] = Arithmetic(p.lineno(1), p.lexpos(1), None, p[2], ArithmeticOption.UNARIO)

def p_expresiones_aritmeticas_3(p):
    '''
    expresiones_aritmeticas : POW PARAP expresiones COMA expresiones PARCL
                            | POWF PARAP expresiones COMA expresiones PARCL
    '''
    p[0] = Arithmetic(p.lineno(1), p.lexpos(1), p[3], p[5], ArithmeticOption.POTENCIA)

def p_expresiones_aritmeticas_4(p):
    '''
    expresiones_aritmeticas : expresiones PUNTO SQRT PARAP PARCL 
    '''
    p[0] = Arithmetic(p.lineno(1), p.lexpos(1), None, p[1], ArithmeticOption.RAIZ)  

def p_expresiones_logicas_1(p):
    '''
    expresiones_logicas : expresiones AND expresiones
                        | expresiones OR expresiones
    '''
    if p[2] == "&&":
        p[0] = Logic(p.lineno(1), p.lexpos(1), p[1], p[3], LogicOption.AND)
    elif p[2] == "||":
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
    casting  : expresiones AS tipo_dato
    '''
    p[0] = Casting(p.lineno(1), p.lexpos(1), p[1], p[3])

def p_especiales_2(p):
    '''
    casting : expresiones PUNTO TO_STRING PARAP PARCL
            | expresiones PUNTO TO_OWNED PARAP PARCL
    '''
    p[0] = Casting_str_string(p.lineno(1), p.lexpos(1), p[1])

def p_especiales_3(p):
    '''
    casting : expresiones PUNTO CLONE PARAP PARCL
    '''
    p[0] = Clone(p.lineno(1), p.lexpos(1), p[1])

def p_especiales_4(p):
    '''
    casting : expresiones PUNTO ABS PARAP PARCL
    '''
    p[0] = Abs(p.lineno(1), p.lexpos(1), p[1])

def p_especiales_5(p):
    '''
    casting : expresiones PUNTO CHARS PARAP PARCL
    '''
    p[0] = Chars(p.lineno(1), p.lexpos(1), p[1])

##VECTOR
def p_funciones_vectores_1(p):
    '''
    funciones_vectores  : expresiones PUNTO PUSH PARAP expresiones PARCL
    '''
    p[0] = Push(p.lineno(1), p.lexpos(1), p[1], p[5])

##VECTOR
def p_funciones_vectores_2(p):
    '''
    funciones_vectores  : expresiones PUNTO REMOVE PARAP expresiones PARCL
    '''
    p[0] = Remove(p.lineno(1), p.lexpos(1), p[1], p[5])

##VECTOR
def p_funciones_vectores_3(p):
    '''
    funciones_vectores  : expresiones PUNTO INSERT PARAP expresiones COMA expresiones PARCL
    '''
    p[0] = Insert(p.lineno(1), p.lexpos(1), p[1], p[7], p[5])

##VECTOR
def p_funciones_vectores_4(p):
    '''
    funciones_vectores  : expresiones PUNTO LEN PARAP PARCL
    '''
    p[0] = Len(p.lineno(1), p.lexpos(1), p[1])

##VECTOR
def p_funciones_vectores_5(p):
    '''
    funciones_vectores  : expresiones PUNTO CAPACITY PARAP PARCL
    '''
    p[0] = Capacity(p.lineno(1), p.lexpos(1), p[1])

##VECTOR
def p_funciones_vectores_6(p):
    '''
    funciones_vectores  : expresiones PUNTO CONTAINS PARAP CONCAT expresiones PARCL
    '''
    p[0] = Contains(p.lineno(1), p.lexpos(1), p[1], p[6])


def p_valores_1(p):
    '''
    valores : CADENA
    '''
    p[0] = Literal(p.lineno(1), p.lexpos(1), p[1], Type.STR)

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


##FUNCION
def p_llamada_funcion(p):
    '''
    llamada_funcion :   IDENTIFICADOR PARAP lista_parametros_llamada PARCL
    '''
    p[0] = Llamada_funcion(p.lineno(1), p.lexpos(1), p[1], p[3])

def p_llamada_funcion_2(p):
    '''
    llamada_funcion :   IDENTIFICADOR PARAP  PARCL
    '''
    p[0] = Llamada_funcion(p.lineno(1), p.lexpos(1), p[1], None)

##FUNCION
def p_lista_parametros_llamada_1(p):
    '''
    lista_parametros_llamada    : lista_parametros_llamada COMA parametro_llamada
    '''
    p[1].append(p[3])
    p[0] = p[1]

##FUNCION
def p_lista_parametros_llamada_2(p):
    '''
    lista_parametros_llamada    : parametro_llamada
    '''
    p[0] = [p[1]]

##FUNCION
def p_parametro_llamada_1(p):
    '''
    parametro_llamada   : CONCAT MUT expresiones
    '''
    p[0] = Parametro_llamada(p.lineno(1), p.lexpos(1), p[3], True)

##FUNCION
def p_parametro_llamada_2(p):
    '''
    parametro_llamada   : expresiones
    '''
    p[0] = Parametro_llamada(p.lineno(1), p.lexpos(1), p[1], False)

def p_print(p):
    '''
    print   : PRINTLN NOT PARAP lista_expresiones PARCL
    '''
    p[0] = Println(p.lineno(1), p.lexpos(1), p[4])

def p_tipo_dato_1(p):
    '''
    tipo_dato   : I64
                | F64
                | STRING
                | CHAR
                | BOOL
                | CONCAT STR
                | USIZE
                | STRUCT
                | IDENTIFICADOR
    '''
    if p[1] == "i64":
        p[0] = Type.I64
    elif p[1] == "f64":
        p[0] = Type.F64
    elif p[1] == "String":
        p[0] = Type.STRING
    elif p[1] == "char":
        p[0] = Type.CHAR
    elif p[1] == "bool":
        p[0] = Type.BOOL
    elif p[1] == "&":
        p[0] = Type.STR
    elif p[1] == "usize":
        p[0] = Type.USIZE
    elif p[1] == "struct":
        p[0] = Type.STRUCT
    else:
        p[0] = Type.STRUCT

def p_tipo_dato_2(p):
    '''
    tipo_dato   : tipo_array
    '''
    p[0] = p[1]

def p_tipo_dato_3(p):
    '''
    tipo_dato   : tipo_vector
    '''
    p[0] = p[1]

def p_tipo_dato_4(p):
    '''
    tipo_dato   : CORCHETEAP tipo_dato CORCHETECL
    ''' 
    cero = Literal(p.lineno(1), p.lexpos(1), 0, Type.I64)
    p[0] = Array_type(p.lineno(1), p.lexpos(1), Type.ARRAY, p[2], [cero])

##ARRAY
def p_tipo_array(p):
    '''
    tipo_array  : CORCHETEAP tipo_dato PCOMA NUMERO CORCHETECL
    '''
    p[0] = Array_type(p.lineno(1), p.lexpos(1), Type.ARRAY, p[2], [p[4]])

##ARRAY
def p_tipo_array_2(p):
    '''
    tipo_array  : CORCHETEAP tipo_array PCOMA NUMERO CORCHETECL
    '''
    p[2].index.append(p[4])
    p[0] = p[2]

def p_tipo_vector_1(p):
    '''
    tipo_vector : VECMAY MENOR tipo_dato MAYOR
    '''
    p[0] = Tipo_vector(p.lineno(1), p.lexpos(1), p[3], Type.VECTOR)
    
def p_error(p):
    auxer = "ERROR SINTACTICO EN EL TOKEN: " + str(p.type) + "EN LA LINEA: " + str(p.lexer.lineno) + "EN LA COLUMNA: " + str(p.lexpos)
    print(auxer)
    TablaErrores.append(auxer)
    Prints.append(auxer)      
parser = yacc.yacc()