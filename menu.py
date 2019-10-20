def citire(x):
    n = input("Cate elemente are vectorul?")
    for i in range(0,n):
        r=input("Dati o valoare.")
        x.append(r)

def afisare(x):
    s=""
    for i in range(0,len(x)):
        s+=str(x[i])+""
    print "Vectorul citit este:"+s

def suma_elemente(x):
    s = 0
    for i in range(0,len(x)):
        s+=x[i]
    return s

def elemente_pozitive(x):
    s=""
    for i in range(0,len(x)):
        if x[i]>0:
            s+=str(x[i])+""
        if len(s)!=0:
            print "Elementele pozitive sunt."+s
        else:
            print "Vectorul dat nu are elemente pozitive."


def cate_impare(x):
    c=0
    for i in range(0,len(x)):
        if x[i]%2==1:
            c+=1
    return c

def produs_scalar(x,y):
    if len(x)!=len(y):
        return 0
    p=0
    for i in range(0,len(x)):
        p+=x[i]*y[i]
    return p

v1=list()
v2=list()

citire(v1)
afisare(v1)
""

print "Suma elementelor este."+str(suma_elemente(v1))
elemente_pozitive(v1)
print"NUmarul de elemente impare."+str(cate_impare(v1))

citire(v2)
print produs_scalar(v1,v2)
