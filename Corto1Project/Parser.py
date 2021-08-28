import ply.yacc as yacc
from Grammar import tokens,Scann

class TC3D:
    def __init__(self):
        self.TMP=None
        self.C3D=None
        

def p_S(t):
    'S : E'
    t[0]=t[1]
    print(t[1].C3D)

def p_E(t):
    '''E : E MAS T
        | E MENOS T 
        | T'''
    if(len(t)==4):
        if(t[2]=='+'):
            t[0]= TC3D
            t[0].TMP=TC3D
            t[0].C3D=t[1].C3D+t[3].C3D+t[0].TMP+"="+t[1].TMP+"+"+t[3].TMP
        elif(t[2]=='-'):
            t[0]= TC3D
            t[0].TMP=TC3D
            t[0].C3D=t[1].C3D+t[3].C3D+t[0].TMP+"="+t[1].TMP+"-"+t[3].TMP
    elif(len(t)==2):
        t[0]=TC3D
        t[0].TMP=t[1].TMP
        t[0].C3D=t[1].C3D

def p_T(t):
    '''T : T POR F
    | T DIVIDE F 
    | F'''
    if(len(t)==4):
        if(t[2]=='*'):
            t[0]= TC3D
            t[0].TMP=TC3D
            t[0].C3D=t[1].C3D+t[3].C3D+t[0].TMP+"="+t[1].TMP+"*"+t[3].TMP
        elif(t[2]=='/'):
            t[0]= TC3D
            t[0].TMP=TC3D
            t[0].C3D=t[1].C3D+t[3].C3D+t[0].TMP+"="+t[1].TMP+"/"+t[3].TMP
    elif(len(t)==2):
        t[0]=TC3D
        t[0].TMP=t[1].TMP
        t[0].C3D=t[1].C3D


def p_F(t):
    '''F : PARIZQ E PARDER
        | ID'''
    if(len(t)==4):
        t[0]=TC3D
        t[0].TMP=t[2].TMP
        t[0].C3D=t[2].C3D
    elif(len(t)==2):
        t[0]=TC3D
        t[0].TMP=t[1]
        t[0].C3D=""

def p_error(t):
    print("Error sintactico"+t.value)

parser = yacc.yacc()

f=open("/home/alterlex/Documentos/Corto1-OLC2-2S2021/Corto1Project/Test.t","r")
input=f.read()
print(input)
parser.parse(input)