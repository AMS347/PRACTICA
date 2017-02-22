def potencia (a,b):
    if b==0:
        return 1
    else:
        if b>0 and b%2==0:
            pot=potencia(a,b/2)
            return pot * pot
        if b>0 and b%2==1:
            pot=potencia(a,b-1)
            return a * pot

print(potencia(3,4))
