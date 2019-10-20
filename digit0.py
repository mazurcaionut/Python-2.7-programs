k=input("Dati numarul")
def are_0(k):
    while k!=0:
        u=k%10
        if u==0:
            return True
        k=k/10
    return False
print are_0(k)
        
