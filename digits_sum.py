a=input("Dati numarul")
def suma_cifre(a):
    s=0
    while a!=0:
        u=a%10
        s+=u
        a=a/10
    return s
print suma_cifre(a)
