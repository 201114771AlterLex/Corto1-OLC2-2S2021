import ply.yacc as yacc
from Grammar import tokens,Scann

precedence = (
     ('left', 'MAS', 'MENOS'),
     ('left', 'POR', 'DIVIDE'),
 )
class TC3D:
    def __init__(self):
        self.TMP=None
        self.C3D=None
        

def p_S(p):
    'S : E'
    #p[0]=p[1]
    #print(p[1].C3D)
    print("S")

def p_E(p):
    '''E : E MAS T
         | E MENOS T 
         | T'''
    if(len(p)==4):
        if(p[2]=='+'):
            #p[0]= TC3Dprintln
            #p[0].TMP=TC3D
            #p[0].C3D=p[1].C3D+p[3].C3D+p[0].TMP+"="+p[1].TMP+"+"+p[3].TMP
            print("E1")
        elif(p[2]=='-'):
            #p[0]= TC3D
            #p[0].TMP=TC3D
            #p[0].C3D=p[1].C3D+p[3].C3D+p[0].TMP+"="+p[1].TMP+"-"+p[3].TMP
            print("E2")
    elif(len(p)==2):
        #p[0]=TC3D
        #p[0].TMP=p[1].TMP
        #p[0].C3D=p[1].C3D
        print("E3")

def p_T(p):
    '''T : T POR F
         | T DIVIDE F 
         | F'''
    if(len(p)==4):
        if(p[2]=='*'):
            #p[0]= TC3D
            #p[0].TMP=TC3D
            #p[0].C3D=p[1].C3D+p[3].C3D+p[0].TMP+"="+p[1].TMP+"*"+p[3].TMP
            print("T1")
        elif(p[2]=='/'):
            #p[0]= TC3D
            #p[0].TMP=TC3D
            #p[0].C3D=p[1].C3D+p[3].C3D+p[0].TMP+"="+p[1].TMP+"/"+p[3].TMP
            print("T2")
    elif(len(p)==2):
        #p[0]=TC3D
        #p[0].TMP=p[1].TMP
        #p[0].C3D=p[1].C3D
        print("T3")


def p_F(p):
    '''F : PARIZQ E PARDER
         | ID
         | ENTERO'''
    if(len(p)==4):
        #p[0]=TC3D
        #p[0].TMP=p[2].TMP
        #p[0].C3D=p[2].C3D
        print("F1")
    elif(len(p)==2):
        #p[0]=TC3D
        #p[0].TMP=p[1]
        #p[0].C3D=""
        print("F23")

def p_error(p):
    if p==None:
          return
    print("Error sintactico"+str(p))

parser = yacc.yacc()

f=open("/home/alterlex/Documentos/Corto1-OLC2-2S2021/Corto1Project/Test.t","r")
finput=f.read()
print(finput)
parser.parse(input=finput)