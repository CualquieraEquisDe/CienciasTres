import ply.lex as lex

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS','SPACE' ]

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r':='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_SPACE = r'\n'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer
def lectura (entrada):
    linea=entrada.readlines()

    for a in range(0,len(linea)):
        lex.input(linea[a])
        while True:
            tok = lex.token()
            if not tok: break
            print str(tok.value) + " - " + str(tok.type)
        print("----------------------------")
    

#lex.input("x = 3 - 4 + 5 * 6")
entrada=open("expresion.in.txt")
lectura(entrada)
        

