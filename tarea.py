from ply.lex import lex
from ply.yacc import yacc
import sys

# --------------------- Análisis Léxico ---------------------

# Lista de tokens
tokens = (
    'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'ID', 'ASSIGN',
    'EQ', 'NE', 'LT', 'GT', 'LE', 'GE',
    'IF', 'ELSE', 'WHILE',
    'SEMICOLON'
)

# Palabras reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE'
}

# Expresiones regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ASSIGN = r'='
t_EQ = r'=='
t_NE = r'!='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_SEMICOLON = r';'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Token para números (enteros y decimales)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    try:
        t.value = int(t.value)
    except ValueError:
        t.value = float(t.value)
    return t

# Token para identificadores y palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# Contador de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores léxicos
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

# --------------------- Análisis Sintáctico ---------------------

# Precedencia de operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

# Gramática

def p_program(p):
    '''program : statement
               | program statement'''
    if len(p) == 2:
        p[0] = ['program', p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : expression SEMICOLON
                 | assignment SEMICOLON
                 | if_statement
                 | while_statement'''
    p[0] = ('stmt', p[1])

def p_assignment(p):
    'assignment : ID ASSIGN expression'
    p[0] = ('assign', p[1], p[3])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_compare(p):
    '''expression : expression EQ expression
                  | expression NE expression
                  | expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression'''
    p[0] = ('compare', p[2], p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = ('group', p[2])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])

def p_expression_id(p):
    'expression : ID'
    p[0] = ('id', p[1])

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = ('uminus', p[2])

def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN statement
                   | IF LPAREN expression RPAREN statement ELSE statement'''
    if len(p) == 6:
        p[0] = ('if', p[3], p[5], None)
    else:
        p[0] = ('if', p[3], p[5], p[7])

def p_while_statement(p):
    'while_statement : WHILE LPAREN expression RPAREN statement'
    p[0] = ('while', p[3], p[5])

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' en la línea {p.lineno}")
    else:
        print("Error de sintaxis al final de la entrada")

# --------------------- Función Principal ---------------------

def main():
    # Construir el lexer y parser
    lexer = lex()
    parser = yacc()

    print("Intérprete básico. Escribe 'salir' para terminar.")
    
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        if not s:
            continue
        if s.lower() == 'salir':
            break
        
        result = parser.parse(s)
        print(result)

if __name__ == '__main__':
    main()