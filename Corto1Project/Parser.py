import ply.yacc as Tyacc
from Grammar import tokens,Scann

precedence = (
    ('left', 'AND', 'OR'),
    ('left', 'MAYOR', 'MENOR','MAYORIGUAL','MENORIGUAL','IGUALQUE','DIFERENTE'),
     ('left', 'MAS', 'MENOS'),
     ('left', 'POR', 'DIVIDE'),
 )
class TC3D:
    def __init__(self):
        self.LT= []
        self.LF= []
        self.LO= []
        self.TMP=None
        self.C3D=None

Titerator=0
Llabel=0

def p_Incio(p):
    'INICIO : PROR'
    print(p[1].C3D)

def p_PROR(p):
    ''' PROR : PROR OR PRAND
            | PRAND'''
    if len(p)==4:
        p[0]=TC3D()
        p[0].C3D=p[1].C3D
        for label in p[1].LF:
            p[0].C3D+=label
            if label!=p[1].LF[-1] :
                p[0].C3D+=', '
            else:
                p[0].C3D+=':\n'

        for label in p[1].LT:
            p[0].LT.append(label)

        p[0].C3D+=p[3].C3D
        global Llabel
        Llabel+=1
        p[0].LO.append('L'+str(Llabel))
        for label in p[3].LF:
            p[0].C3D+=label
            if label!=p[3].LF[-1] :
                p[0].C3D+=', '
            else:
                p[0].C3D+=':\n'
        p[0].C3D+='[FALSE] \ngoto '+p[0].LO[-1]+'\n'
        for label in p[3].LT:
            p[0].LT.append(label)
        for label in p[0].LT:
            p[0].C3D+=label
            if label!=p[0].LT[-1] :
                p[0].C3D+=', '
            else:
                p[0].C3D+=':\n'
        p[0].LT.clear()
        p[0].C3D+='[TRUE] \n'+p[0].LO[-1]+':\n'

    else:
        p[0]=TC3D()
        p[0].LT=p[1].LT
        p[0].LF=p[1].LF
        p[0].LO=p[1].LO
        p[0].TMP=p[1].TMP
        p[0].C3D=p[1].C3D

def p_PRAND(p):
    ''' PRAND : PRAND AND LOGICUNIT
            | LOGICUNIT'''
    if len(p)==4:
        p[0]=TC3D()
        p[0].C3D=p[1].C3D
        for label in p[1].LT:
            p[0].C3D+=label
            if label!=p[1].LT[-1] :
                p[0].C3D+=', '
            else:
                p[0].C3D+=':\n'

        for label in p[1].LF:
            p[0].LF.append(label)

        p[0].C3D+=p[3].C3D
        global Llabel
        Llabel+=1
        p[0].LO.append('L'+str(Llabel))
        for label in p[3].LT:
            p[0].C3D+=label
            if label!=p[3].LT[-1] :
                p[0].C3D+=', '
            else:
                p[0].C3D+=':\n'
        p[0].C3D+='[True] \ngoto '+p[0].LO[-1]+'\n'
        for label in p[3].LF:
            p[0].LF.append(label)
        for label in p[0].LF:
            p[0].C3D+=label
            if label!=p[0].LF[-1] :
                p[0].C3D+=', '
            else:
                p[0].C3D+=':\n'
        p[0].LF.clear()
        p[0].C3D+='[False] \n'+p[0].LO[-1]+':\n'


        #print(p[0].C3D)
    else:
        p[0]=TC3D()
        p[0].LT=p[1].LT
        p[0].LF=p[1].LF
        p[0].LO=p[1].LO
        p[0].TMP=p[1].TMP
        p[0].C3D=p[1].C3D


def p_LOGICUNIT(p):
    '''LOGICUNIT : NOT LOGICUNIT
            | PARIZQ PROR PARDER
            | REL
            | VTRUE
            | VFALSE'''
    if len(p)==4:
        p[0]=TC3D()
        p[0].LT=p[2].LT
        p[0].LF=p[2].LF
        p[0].LO=p[2].LO
        p[0].TMP=p[2].TMP
        p[0].C3D=p[2].C3D
    elif len(p)==3:
        p[0]=TC3D()
        p[0].LT=p[2].LF
        p[0].LF=p[2].LT
        p[0].LO=p[2].LO
        p[0].TMP=p[2].TMP
        p[0].C3D=p[2].C3D
    else:
        global Titerator
        global Llabel
        if p[1]=='TRUE':
            p[0]=TC3D()
            Titerator+=1
            p[0].TMP='T'+str(Titerator)
            Llabel+=2
            p[0].LT.append('L'+str(Llabel-1))
            p[0].LF.append('L'+str(Llabel))
            p[0].C3D=p[0].TMP+'=TRUE\n'+'IF '+p[0].TMP+' goto L'+str(Llabel-1)+'\n'+'goto L'+str(Llabel)+'\n'
        elif p[1]=='FALSE':
            p[0]=TC3D()
            Titerator+=1
            p[0].TMP='T'+str(Titerator)
            p[0].TMP='T'+str(Titerator)
            Llabel+=2
            p[0].LT.append('L'+str(Llabel-1))
            p[0].LF.append('L'+str(Llabel))
            p[0].C3D=p[0].TMP+'=FALSE\n'+'IF '+p[0].TMP+' goto L'+str(Llabel-1)+'\n'+'goto L'+str(Llabel)+'\n'
        else:
            p[0]=TC3D()
            p[0].LT=p[1].LT
            p[0].LF=p[1].LF
            p[0].LO=p[1].LO
            p[0].TMP=p[1].TMP
            p[0].C3D=p[1].C3D
            
    '''for label in p[0].LT:
        p[0].C3D+=label
        if label!=p[0].LT[-1] :
            p[0].C3D+=', '
        else:
            p[0].C3D+=': '
    print(p[0].C3D)'''
    
def p_REL(p):
    '''REL : S MAYOR S
            | S MENOR S 
            | S MAYORIGUAL S
            | S MENORIGUAL S
            | S IGUALQUE S
            | S DIFERENTE S
            | PARIZQ REL PARDER
            | S'''
    global Titerator
    global Llabel
    if len(p)==4:
        Titerator+=1
        p[0]=TC3D()
        p[0].TMP='T'+str(Titerator)
        if p[2]=='>':
            p[0].C3D=p[1].C3D+'\n'+p[3].C3D+'\n'
            Llabel+=2
            p[0].LT.append('L'+str(Llabel-1))
            p[0].LF.append('L'+str(Llabel))
            p[0].C3D+='IF '+p[1].TMP+'>'+p[3].TMP+' goto L'+str(Llabel-1)+'\n'+'goto L'+str(Llabel)+'\n'
        elif p[2]=='<':
            p[0].C3D=p[1].C3D+'\n'+p[3].C3D+'\n'
            Llabel+=2
            p[0].LT.append('L'+str(Llabel-1))
            p[0].LF.append('L'+str(Llabel))
            p[0].C3D+='IF '+p[1].TMP+'<'+p[3].TMP+' goto L'+str(Llabel-1)+'\n'+'goto L'+str(Llabel)+'\n'
        elif p[2]=='>=':
            p[0].C3D=p[1].C3D+'\n'+p[3].C3D+'\n'
            Llabel+=2
            p[0].LT.append('L'+str(Llabel-1))
            p[0].LF.append('L'+str(Llabel))
            p[0].C3D+='IF '+p[1].TMP+'>='+p[3].TMP+' goto L'+str(Llabel-1)+'\n'+'goto L'+str(Llabel)+'\n'
        elif p[2]=='<=':
            p[0].C3D=p[1].C3D+'\n'+p[3].C3D+'\n'
            Llabel+=2
            p[0].LT.append('L'+str(Llabel-1))
            p[0].LF.append('L'+str(Llabel))
            p[0].C3D+='IF '+p[1].TMP+'<='+p[3].TMP+' goto L'+str(Llabel-1)+'\n'+'goto L'+str(Llabel)+'\n'
        elif p[2]=='==':
            p[0].C3D=p[1].C3D+'\n'+p[3].C3D+'\n'
            Llabel+=2
            p[0].LT.append('L'+str(Llabel-1))
            p[0].LF.append('L'+str(Llabel))
            p[0].C3D+='IF '+p[1].TMP+'=='+p[3].TMP+' goto L'+str(Llabel-1)+'\n'+'goto L'+str(Llabel)+'\n'
        elif p[2]=='!=':
            p[0].C3D=p[1].C3D+'\n'+p[3].C3D+'\n'
            Llabel+=2
            p[0].LT.append('L'+str(Llabel-1))
            p[0].LF.append('L'+str(Llabel))
            p[0].C3D+='IF '+p[1].TMP+'!='+p[3].TMP+' goto L'+str(Llabel-1)+'\n'+'goto L'+str(Llabel)+'\n'
        else:
            p[0]=p[2]
            return
        #print(p[0].C3D)
    else:
        p[0]=TC3D()
        p[0]=p[1]
        #print(p[0].C3D)


def p_S(p):
    'S : E'
    p[0]=TC3D()
    global Titerator
    Titerator+=1
    p[0].TMP='T'+str(Titerator)
    p[0].C3D=p[1].C3D+p[0].TMP+'='+p[1].TMP
    #print(p[0].C3D)
    #print("S")

def p_E(p):
    '''E : E MAS T
         | E MENOS T 
         | T'''
    global Titerator
    if(len(p)==4):
        if(p[2]=='+'):
            p[0]= TC3D()
            Titerator+=1
            p[0].TMP='T'+str(Titerator)
            p[0].C3D=p[1].C3D+p[3].C3D+p[0].TMP+"="+p[1].TMP+"+"+p[3].TMP+'\n'
            #print("E1")
        elif(p[2]=='-'):
            p[0]= TC3D()
            Titerator+=1
            p[0].TMP='T'+str(Titerator)
            p[0].C3D=p[1].C3D+p[3].C3D+p[0].TMP+"="+p[1].TMP+"-"+p[3].TMP+'\n'
            #print("E2")
    elif(len(p)==2):
        p[0]=TC3D()
        p[0].TMP=p[1].TMP
        p[0].C3D=p[1].C3D
        #print("E3")

def p_T(p):
    '''T : T POR F
         | T DIVIDE F 
         | F'''
    global Titerator
    if(len(p)==4):
        if(p[2]=='*'):
            p[0]= TC3D()
            Titerator+=1
            p[0].TMP='T'+str(Titerator)
            p[0].C3D=p[1].C3D+p[3].C3D+p[0].TMP+"="+p[1].TMP+"*"+p[3].TMP+'\n'
            #print("T1")
        elif(p[2]=='/'):
            p[0]= TC3D()
            Titerator+=1
            p[0].TMP='T'+str(Titerator)
            p[0].C3D=p[1].C3D+p[3].C3D+p[0].TMP+"="+p[1].TMP+"/"+p[3].TMP+'\n'
            #print("T2")
    elif(len(p)==2):
        p[0]=TC3D()
        p[0].TMP=p[1].TMP
        p[0].C3D=p[1].C3D
        #print("T3")


def p_F(p):
    '''F : PARIZQ E PARDER
         | ID
         | ENTERO'''
    if(len(p)==4):
        p[0]=TC3D()
        p[0].TMP=p[2].TMP
        p[0].C3D=p[2].C3D
        #print("F1")
    elif(len(p)==2):
        p[0]=TC3D()
        p[0].TMP=str(p[1])
        p[0].C3D=""
        #print("F23")

def p_error(p):
    if p==None:
          return
    print("Error sintactico"+str(p))


parser = Tyacc.yacc(start='INICIO')

f=open("/home/alterlex/Documentos/Corto1-OLC2-2S2021/Corto1Project/Test.t","r")
finput=f.read()
print('Cadena de entrada -> '+finput)
print('Codgio de 3 direcciones:')
parser.parse(input=finput,lexer=Scann)