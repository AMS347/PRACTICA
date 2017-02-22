def lipovocal(frase):
    a=False
    e=False
    i=False
    o=False
    u=False
    frase=frase.upper()
    retorno=[]
    for x in range(len(frase)):
        if frase[x]=="A":
            a=True
        if frase[x]=="E":
            e=True
        if frase[x]=="I":
            i=True
        if frase[x]=="O":
            o=True
        if frase[x]=="U":
            u=True
    if a==False:
        retorno.append("a")
    if e==False:
        retorno.append("e")
    if i==False:
        retorno.append("i")
    if o==False:
        retorno.append("o")
    if u==False:
        retorno.append("u")
    if len(retorno)==0:
        return ("NO CUMPLE")
    else:
        return (retorno)
