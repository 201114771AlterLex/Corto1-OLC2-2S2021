import ply.lex as Tlex

tokens = (
    'MAS',
    'MENOS',
    'POR',
    'DIVIDE',
    'PARIZQ',
    'PARDER',
    'ID',
    'ENTERO',
    'IGUAL',
    'MAYOR',
    'MENOR',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IGUALQUE',
    'DIFERENTE',
    'AND',
    'OR',
    'NOT',
    'VTRUE',
    'VFALSE',
)

#tokens

t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDE    = r'/'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_IGUAL     = r'='
t_MAYOR     = r'>'
t_MENOR     = r'<'
t_MAYORIGUAL= r'>='
t_MENORIGUAL= r'<='
t_IGUALQUE  = r'=='
t_DIFERENTE = r'!='
t_AND       = r'AND'
t_OR        = r'OR'
t_NOT       = r'NOT'
t_VTRUE     = r'TRUE'
t_VFALSE    = r'FALSE'
t_ignore    = ' \t\n'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t
    #print('encontre '+str(t))

def t_ENTERO(t):
    r'[0-9]+'
    try:
        t.value=int(t.value)
    except ValueError:
        t.value=0
    #print('encontre '+str(t))
    return t

def t_error(t):
    print('error lexico')
    t.lexer.skip(1)

def t_eof(t):
    return None

Scann =Tlex.lex()
"""f=open("/home/alterlex/Documentos/Corto1-OLC2-2S2021/Corto1Project/Test.t","r")
finput=f.read()
print(finput)
Scann.input(finput)
while True:
    t=Scann.token()
    if t==None:
          break
    print(t)
pass
"""