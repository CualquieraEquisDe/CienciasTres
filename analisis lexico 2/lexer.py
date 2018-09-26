
import ply.lex as lex

tokens = [ 'NAME','NUMBER','PLUS','MINUS','MULTIPLICA','DIVIDE', 'EQUALS', 'SPACE' ]

t_ignore = ' \t'
t_PLUS = r'SUM'
t_MINUS = r'RES'
t_MULTIPLICA = r'MULTI'
t_DIVIDE = r'DIV'
t_EQUALS = r'='
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

entrada = open("Expresions.in","r")
exp = entrada.readlines()

for i in range(0, len(exp)):    
    pp = exp[i]
    str1 = str(pp)
    print ("------####-------")
    print (str1)
    print ("P")
    lex.input(str1)
    while True:
        tok = lex.token()
        if not tok: break
        print (str(tok.value) + " - " + str(tok.type))
