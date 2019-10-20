y=input("Dati numarul")
def cate_impare(y):
    c=0
    while y!=0:
        u=y%10
        if u%2!=0:
            c=c+1
        y=y/10
    return c
print cate_impare(y)
    
