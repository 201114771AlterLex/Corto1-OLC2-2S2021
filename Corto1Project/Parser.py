import ply.yacc as yacc
from Grammar import tokens,Scann

class TC3D:
    def __init__(self):
        self.TMP=None
        self.C3P=None
        

def p_S(t):
    'S : E'
    t[0]=t[1]
    print(t[1].C3D)

def p_E(t):


def p_F(t):
    'F : (E)'
    t[0]=TC3D
    t[0].TMP=t[2].TMP
    t[0].C3P=t[2].C3P

def p_F(t):
    'F : ID'
    t[0]=TC3D
    t[0].TMP=t[1]
    t[0].C3P=""
    

def p_error(t):
    print("Error sintactico")

parser = yacc.yacc()

f=open("./Test.t","r")
input=f.read()
print(input)
parser.parse(input)