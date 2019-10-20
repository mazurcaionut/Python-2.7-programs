x=input("Dati numarul")
def numar_divizori(x):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c=c+1
    return c
print numar_divizori(x)


