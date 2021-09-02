import ply.lex as lex

literals = [ '+','-','*','/' ]

tokens = (
    'ID',
    'ENTERO',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDE',
    'PARIZQ',
    'PARDER',
)

t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDE    = r'/'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'

t_ignore    = ' \t\n'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    print('encontre '+str(t))

def t_ENTERO(t):
    r'[0-9]+'
    try:
        t.value=int(t.value)
    except ValueError:
        t.value=0
    print('encontre '+str(t))
    return t

def t_error(t):
    print('error lexico')

def t_eof(t):
    return None

Scann =lex.lex()
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