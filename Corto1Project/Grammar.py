import ply.lex as lex

tokens =[
    "ID",
    "ENTERO",
    "MAS",
    "MENOS",
    "POR",
    "DIVIDE",
    "PARIZQ",
    "PARDER"
]

t_PARIZQ=r"\("
t_PARDER=r"\)"
t_DIVIDE=r"/"
t_POR=r"\*"
t_MENOS=r"-"
t_MAS=r"\+"

t_ignore=" \t\n"

def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"

def t_ENTERO(t):
    r"[0-9]+"
    try:
        t.value=int(t.value)
    except ValueError:
        t.value=0
    return t

def t_error(t):
    print("error lexico")

Scann =lex.lex()