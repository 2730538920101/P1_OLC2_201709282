import ply.lex as lex
import ply.yacc as yacc


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
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    try:
        t.type = reservadas.get(t.value, 'IDENTIFICADOR')
    except ValueError:
        auxer = "EL VALOR INGRESADO NO PUEDE SER UN IDENTIFICADOR"
        print(auxer)
        t.value='ERROR'
    return t

    
def t_CADENA(t):
    r'[\"][^\"\n]*[\"]'
    try:
        t.value = t.value[1:-1]
    except ValueError:
        auxer = "EL VALOR INGRESADO NO PUEDE SER UNA CADENA"
        print(auxer)
        t.value='ERROR'
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        auxer = "Float muy grande " + str(t.value)
        print(auxer)
        t.value = 0
    return t

def t_NUMERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        auxer = "Integer muy grande " +  str(t.value)
        print(auxer)
        t.value = 0
    return t


def t_CARACTER(t):
    r'[\'][^\'\n]*[\']'
    try:
        t.value = t.value[1:-1]
    except ValueError:
        auxer = "EL VALOR INGRESADO NO PUEDE SER UN CARACTER"
        print(auxer)
        t.value='ERROR'
    return t


def t_error(t):
    auxer = "ERROR LEXICO " + str(t.value[0])
    print(auxer)
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
    

def p_entorno_global(p):
    '''
    entorno_global  : entorno_global global
    '''
    
def p_global_listado(p):
    '''
    entorno_global  : global
    '''
   

def p_global(p):
    '''
    global  : funcion_main
            | instrucciones_modulo
    '''

def p_instrucciones_modulo_1(p):
    '''
    instrucciones_modulo    : declaracion_struct
                            | declaracion_funciones
                            | declaracion_modulo
                            | COMENTARIO
    '''

def p_lista_instrucciones_modulo_1(p):
    '''
    lista_instrucciones_modulo  : lista_instrucciones_modulo instrucciones_modulo
    '''

def p_lista_instrucciones_modulo_2(p):
    '''
    lista_instrucciones_modulo  : instrucciones_modulo
    '''

def p_declaracion_modulo(p):
    '''
    declaracion_modulo  : encapsulamiento MOD IDENTIFICADOR LLAVEAP lista_instrucciones_modulo LLAVECL
    '''
    

def p_funcion_main(p):
    '''
    funcion_main    : FN MAIN PARAP PARCL LLAVEAP lista_instrucciones LLAVECL
    '''

def p_lista_instrucciones_lista(p):
    '''
    lista_instrucciones : lista_instrucciones instruccion
    ''' 
    
def p_lista_instrucciones(p):
    '''
    lista_instrucciones : instruccion
    '''
    
def p_instruccion(p):
    '''
    instruccion : declaracion_variable 
                | expresiones PCOMA
                | asignacion 
                | sentencias 
                | transferencia PCOMA
                | COMENTARIO
    '''
    

def p_transferecia_1(p):
    '''
    transferencia   : BREAK
                    | RETURN 
                    | CONTINUE 
    '''
    
def p_transferecia_2(p):
    '''
    transferencia   : RETURN expresiones 
    '''
    
def p_sentencias(p):
    '''
    sentencias  : generar_if
                | generar_while
                | generar_for
                | generar_loop
                | generar_match
    '''
    

def p_generar_if(p):   
    '''
    generar_if  : IF expresiones LLAVEAP lista_instrucciones LLAVECL generar_else

    '''
    
def p_generar_else_1(p):
    '''
    generar_else    : ELSE LLAVEAP lista_instrucciones LLAVECL  
    ''' 

def p_generar_else_2(p):
    '''
    generar_else    : ELSE generar_if
    '''
    
def p_generar_else_3(p):
    '''
    generar_else    : empty
    ''' 
    
def p_empty(p):
    'empty :'
    

def p_generar_while(p):
    '''
    generar_while : WHILE expresiones LLAVEAP lista_instrucciones LLAVECL
    '''
    
def p_generar_for(p):
    '''
    generar_for : FOR IDENTIFICADOR IN expresiones LLAVEAP lista_instrucciones LLAVECL 
    '''
    
def p_generar_loop(p):
    '''
    generar_loop    : LOOP LLAVEAP lista_instrucciones LLAVECL
    '''
    
def p_generar_match(p):
    '''
    generar_match   : MATCH expresiones LLAVEAP lista_cases LLAVECL
    '''
    

def p_lista_cases_2(p):
    '''
    lista_cases : lista_cases cases 
    '''

def p_lista_cases_3(p):
    '''
    lista_cases : cases
    '''

def p_cases_1(p):
    '''
    cases   : lista_expresiones DOBFLECHA LLAVEAP lista_instrucciones LLAVECL
    '''
    
def p_cases_2(p):
    '''
    cases : lista_expresiones DOBFLECHA instruccion 
    '''
    
def p_cases_3(p):
    '''
    cases : GBAJO DOBFLECHA LLAVEAP lista_instrucciones LLAVECL
    '''
    
def p_cases_4(p):
    '''
    cases : GBAJO DOBFLECHA instruccion 
    '''
    

def p_declaracion_struct_1(p):
    '''
    declaracion_struct  : encapsulamiento STRUCT IDENTIFICADOR LLAVEAP lista_parametros LLAVECL
    '''    
    
##PARAMETROS FUNCION Y ATRIBUTOS STRUCT
def p_lista_parametros_1(p):
    '''
    lista_parametros    : lista_parametros COMA parametros_declaracion
    '''

def p_lista_parametros_2(p):
    '''
    lista_parametros    : parametros_declaracion
    '''

def p_parametros_declaracion_funcion_1(p):
    '''
    parametros_declaracion    :  encapsulamiento IDENTIFICADOR DOSPUNTOS tipo_dato
    '''
    
def p_encapsulamiento_atributo_1(p):
    '''
    encapsulamiento    : PUB
    '''

def p_encapsulamiento_atributo_2(p):
    '''
    encapsulamiento    : empty
    '''


##FUNCION
def p_declaracion_funciones_1(p):
    '''
    declaracion_funciones   : encapsulamiento FN IDENTIFICADOR PARAP lista_parametros PARCL LLAVEAP lista_instrucciones LLAVECL
    '''
    
##FUNCION
def p_declaracion_funciones_2(p):
    '''
    declaracion_funciones   : encapsulamiento FN IDENTIFICADOR PARAP lista_parametros PARCL FLECHA tipo_dato LLAVEAP lista_instrucciones LLAVECL
    '''
    
##FUNCION
def p_declaracion_funciones_3(p):
    '''
    declaracion_funciones   : encapsulamiento FN IDENTIFICADOR PARAP  PARCL LLAVEAP lista_instrucciones LLAVECL
    '''
    
##FUNCION
def p_declaracion_funciones_4(p):
    '''
    declaracion_funciones   : encapsulamiento FN IDENTIFICADOR PARAP  PARCL FLECHA tipo_dato LLAVEAP lista_instrucciones LLAVECL
    '''
    
    
def p_declaracion_mutabilidad_1(p):
    '''
    declaracion_mutabilidad : LET
    '''

def p_declaracion_mutabilidad_2(p):
    '''
    declaracion_mutabilidad : LET MUT
    '''

def p_declaracion_variable(p):
    '''
    declaracion_variable    : declaracion_mutabilidad assig
		                    		     
    '''



def p_assig_2(p):
    '''
    assig   : IDENTIFICADOR DOSPUNTOS tipo_dato IGUAL res_assign PCOMA
    '''

def p_assig_3(p):
    '''
    assig   : IDENTIFICADOR IGUAL res_assign PCOMA 
    '''


    
def p_asignacion_4(p):
    '''
    asignacion  : lista_identificadores IGUAL res_assign PCOMA
    '''

def p_res_assign(p):
    '''
    res_assign  : sentencias
                | expresiones
    '''




    

#EXPRESIONES
def p_expresiones(p):
    '''
    expresiones : expresiones_aritmeticas
                | expresiones_logicas
                | expresiones_relacionales
                | valores
                | casting
                | funciones_vectores
                | print
                | parentesis
                | range
                | arrays_gen
                | vectores_gen
                | structs_gen              
    '''



#EXPRESIONES ENTRE PARENTESIS
def p_expresiones_2(p):
    '''
    parentesis : PARAP expresiones PARCL
    '''
    

def p_lista_identificadores_2(p):
    '''
    lista_identificadores   : IDENTIFICADOR lista_identificadores_modulo
    '''

def p_lista_identificadores_3(p):
    '''
    lista_identificadores   : IDENTIFICADOR lista_indices lista_identificadores_modulo
    '''


def p_lista_modulo_struct_3(p):
    '''
    lista_identificadores_modulo   : DOSPUNTOS DOSPUNTOS lista_identificadores                                   
    '''

def p_lista_modulo_struct_4(p):
    '''
    lista_identificadores_modulo   : PUNTO lista_identificadores                                   
    '''

def p_lista_modulo_struct_5(p):
    '''
    lista_identificadores_modulo   : llamada_funcion
    '''



def p_lista_modulo_struct_7(p):
    '''
    lista_identificadores_modulo   : empty
    '''



    
##ARRAY INSTANCIA CON VALORES ASIGNADOS
def p_expresiones_4(p):
    '''
    arrays_gen : CORCHETEAP expresiones PCOMA expresiones CORCHETECL
    '''
    
##ARRAY INSTANCIA CON ELEMENTOS
def p_expresiones_5(p):
    '''
    arrays_gen : CORCHETEAP lista_expresiones CORCHETECL
    '''
    
##VECTOR INSTANCIA VALORES ASIGNADOS
def p_expresiones_6(p):
    '''
    vectores_gen : VECMIN NOT CORCHETEAP expresiones PCOMA expresiones CORCHETECL
    '''
    
##VECTOR INSTANCIA CON ELEMENTOS
def p_expresiones_7(p):
    '''
    vectores_gen : VECMIN NOT CORCHETEAP lista_expresiones CORCHETECL
    '''
    
##VECTOR INSTANCIA NEW
def p_expresiones_8(p):
    '''
    vectores_gen : VECMAY DOSPUNTOS DOSPUNTOS NEW PARAP PARCL
    '''
    
##VECTOR INSTANCIA WITH CAPACITY
def p_expresiones_9(p):
    '''
    vectores_gen    : VECMAY DOSPUNTOS DOSPUNTOS WITH_CAPACITY PARAP expresiones PARCL
    '''
    
#INSTANCIA STRUCT
def p_expresiones_10(p):
    '''
    structs_gen : IDENTIFICADOR LLAVEAP lista_atributos LLAVECL
    '''
    
#RANGE
def p_expresiones_12(p):
    '''
    range : expresiones PUNTO PUNTO expresiones
    '''
 
 

##ARRAY Y VECTOR LISTA DE INDICES
def p_lista_indices_1(p):
    '''
    lista_indices   :   lista_indices indice
    '''
def p_lista_indices_2(p):
    '''
    lista_indices   : indice
    '''

    
##ARRAY Y VECTOR
def p_indice(p):
    '''
    indice   : CORCHETEAP expresiones CORCHETECL
    '''

#LISTA ATRIBUTOS DE STRUCTS    
def p_lista_atributos_1(p):
    '''
    lista_atributos :   lista_atributos COMA atributo_struct 
    '''

def p_lista_atributos_2(p):
    '''
    lista_atributos : atributo_struct 
    '''

#ATRIBUTO STRUCT    
def p_atributo_struct(p):
    '''
    atributo_struct :   IDENTIFICADOR DOSPUNTOS expresiones
    '''

#LISTA DE EXPRESIONES SEPARADOR (,) Y (|)    
def p_lista_exp_1(p):
    '''
    lista_expresiones   : lista_expresiones COMA expresiones
                        | lista_expresiones BARRA expresiones

    '''
    

def p_lista_exp_2(p):
    '''
    lista_expresiones   : expresiones
    '''
    
#ARITMETICAS BASICAS
def p_expresiones_aritmeticas_1(p):
    '''
    expresiones_aritmeticas : expresiones MAS expresiones
                            | expresiones MENOS expresiones
                            | expresiones POR expresiones
                            | expresiones DIV expresiones
                            | expresiones MODULO expresiones
    '''

#ARITMETICAS UNARIO    
def p_expresiones_aritmeticas_2(p):
    '''
    expresiones_aritmeticas : MENOS expresiones %prec UMENOS
    '''

#ARITMETICAS POTENCIA    
def p_expresiones_aritmeticas_3(p):
    '''
    expresiones_aritmeticas : POW PARAP lista_expresiones PARCL
                            | POWF PARAP lista_expresiones PARCL
    '''

#ARITMETICAS RAIZ    
def p_expresiones_aritmeticas_4(p):
    '''
    expresiones_aritmeticas : expresiones PUNTO SQRT PARAP PARCL 
    '''

#LOGICAS AND Y OR    
def p_expresiones_logicas_1(p):
    '''
    expresiones_logicas : expresiones AND expresiones
                        | expresiones OR expresiones
    '''

#LOGICAS NOT    
def p_expresiones_logicas_2(p):
    '''
    expresiones_logicas : NOT expresiones
    '''

#RELACIONALES    
def p_expresiones_relacionales(p):
    '''
    expresiones_relacionales    : expresiones MAYOR expresiones
                                | expresiones MENOR expresiones
                                | expresiones DOBIGUAL expresiones
                                | expresiones DIF expresiones
                                | expresiones MAYORIG expresiones
                                | expresiones MENORIG expresiones
    ''' 

#CASTEO EXPLICITO    
def p_especiales_1(p):
    '''
    casting  : expresiones AS tipo_dato
    '''

#CASTEO DE STR A STRING    
def p_especiales_2(p):
    '''
    casting : expresiones PUNTO TO_STRING PARAP PARCL
            | expresiones PUNTO TO_OWNED PARAP PARCL
    '''

#CREA UNA COPIA DE UN STRING    
def p_especiales_3(p):
    '''
    casting : expresiones PUNTO CLONE PARAP PARCL
    '''

#CASTEO AL VALOR ABSOLUTO    
def p_especiales_4(p):
    '''
    casting : expresiones PUNTO ABS PARAP PARCL
    '''

#CASTEO DE STRING A ARRAY DE CHARS    
def p_especiales_5(p):
    '''
    casting : expresiones PUNTO CHARS PARAP PARCL
    '''
    
##VECTOR
def p_funciones_vectores_1(p):
    '''
    funciones_vectores  : expresiones PUNTO PUSH PARAP expresiones PARCL
    '''
    
##VECTOR
def p_funciones_vectores_2(p):
    '''
    funciones_vectores  : expresiones PUNTO REMOVE PARAP expresiones PARCL
    '''
    
##VECTOR
def p_funciones_vectores_3(p):
    '''
    funciones_vectores  : expresiones PUNTO INSERT PARAP lista_expresiones PARCL
    '''
    
##VECTOR
def p_funciones_vectores_4(p):
    '''
    funciones_vectores  : expresiones PUNTO LEN PARAP PARCL
    '''
    
##VECTOR
def p_funciones_vectores_5(p):
    '''
    funciones_vectores  : expresiones PUNTO CAPACITY PARAP PARCL
    '''
    
##VECTOR
def p_funciones_vectores_6(p):
    '''
    funciones_vectores  : expresiones PUNTO CONTAINS PARAP CONCAT expresiones PARCL
    '''
    
#CADENA STR
def p_valores_1(p):
    '''
    valores : CADENA
    '''

#CARACTER CHAR   
def p_valores_2(p):
    '''
    valores : CARACTER
    '''
    
#DECIMAL F64
def p_valores_3(p):
    '''
    valores : DECIMAL
    '''

#NUMERO I64    
def p_valores_4(p):
    '''
    valores : NUMERO
            
    '''

#TRUE O FALSE BOOL    
def p_valores_5(p):
    '''
    valores : TRUE
            | FALSE
    '''

def p_valores_6(p):
    '''
    valores : lista_identificadores
    '''

##FUNCION
def p_llamada_funcion(p):
    '''
    llamada_funcion :   PARAP lista_parametros_llamada PARCL
    '''
    
def p_llamada_funcion_2(p):
    '''
    llamada_funcion :   PARAP  PARCL
    '''
    
##FUNCION
def p_lista_parametros_llamada_1(p):
    '''
    lista_parametros_llamada    : lista_parametros_llamada COMA parametro_llamada
    '''
    
##FUNCION
def p_lista_parametros_llamada_2(p):
    '''
    lista_parametros_llamada    : parametro_llamada
    '''
    
##FUNCION
def p_parametro_llamada_1(p):
    '''
    parametro_llamada   : referencia expresiones
    '''
    
##FUNCION
def p_parametro_llamada_2(p):
    '''
    parametro_llamada   : expresiones
    '''

#PRINT    
def p_print(p):
    '''
    print   : PRINTLN NOT PARAP lista_expresiones PARCL
    '''

#TIPADOS    
def p_tipo_dato_1(p):
    '''
    tipo_dato   : I64
                | F64
                | STRING
                | CHAR
                | BOOL
                | STR
                | USIZE
                | lista_identificadores
                | tipo_array
                | tipo_vector
    '''

def p_tipo_dato_ref(p):
    '''
    tipo_dato   : referencia tipo_dato
    '''

def p_tipo_arr(p):
    '''
    tipo_array  : tipo_array_1d
                | tipo_array_md
    '''



def p_referencia(p):
    '''
    referencia  : CONCAT MUT
    '''

def p_referencia_2(p):
    '''
    referencia  : CONCAT
    '''
    
#ARRAY 1D    
def p_tipo_dato_4(p):
    '''
    tipo_array_1d   : CORCHETEAP tipo_dato CORCHETECL
    ''' 
    
##ARRAY 1D
def p_tipo_array(p):
    '''
    tipo_array_md  : CORCHETEAP tipo_dato PCOMA NUMERO CORCHETECL
    '''
    
##ARRAY MD
def p_tipo_array_2(p):
    '''
    tipo_array_md  : CORCHETEAP tipo_array_md PCOMA NUMERO CORCHETECL
    '''

#VECTOR    
def p_tipo_vector_1(p):
    '''
    tipo_vector : VECMAY MENOR tipo_dato MAYOR
    '''



#ERROR SINTACTICO    
def p_error(p):
    auxer = "ERROR SINTACTICO EN EL TOKEN: " + str(p.type) + " VALOR: "+ str(p.value) +" EN LA LINEA: " + str(p.lexer.lineno) + " EN LA COLUMNA: " + str(p.lexpos)
    print(auxer)
    
parser = yacc.yacc()