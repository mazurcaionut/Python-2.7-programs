n=input("Dati numarul")
def factorial(n):
    p=1
    for i in range(1,n+1):
        p=p*i
    return p
print factorial(n)
