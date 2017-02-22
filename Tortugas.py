import random
import copy

def distribuye (n,m,q,total):
    campo=[]
    contador=0
    for i in range(n):
        campo.append([])
        for j in range(m):
            campo[i].append(0)
    while contador < total:
        x=random.randrange(0,n)
        y=random.randrange(0,m)
        if (campo[x][y])>=(q):
          continue
        else:
            campo[x][y]=campo[x][y]+1
        contador=contador+1
    return campo

def movimiento(campo):
    campoalterno=copy.copy(campo)
    sintortugas=0
    tortugassalieron=0
    coordenadas=[]
    for i in range (len(campo)):
        for j in range (len(campo[0])):
            decision=random.randrange(0,2) #0 para dejar la tortuga en el mismo lugar y 1 para mover en diagonal
            diagonal=random.randrange(0,4) #0 (diagonal superior izquierda) 1 (diagonal superior derecha) 2 (diagonal inferior derecha) 3 (diagonal inferior izquierda)

            if decision==1:
                if campo[i][j]==0:
                    continue
                else:
                    campo[i][j]=campo[i][j]-1
                    if diagonal==0:
                        if i-1>=0 and i-1<=len(campo)-1 and j-1>=0 and j-1<=len(campo[0])-1:
                            campo[i-1][j-1]=campo[i-1][j-1]+1
                            coordenadas.append([i,j])
                        else:
                            tortugassalieron=tortugassalieron+1
                    if diagonal==1:
                        if i-1>=0 and i-1<=len(campo)-1 and j+1>=0 and j+1<=len(campo[0])-1:
                            campo[i-1][j+1]=campo[i-1][j+1]+1
                            coordenadas.append([i,j])
                        else:
                            tortugassalieron=tortugassalieron+1
                    if diagonal==2:
                        if i+1>=0 and i+1<=len(campo)-1 and j+1>=0 and j+1<=len(campo[0])-1:
                            campo[i+1][j+1]=campo[i+1][j+1]+1
                            coordenadas.append([i,j])
                        else:
                            tortugassalieron=tortugassalieron+1
                    if diagonal==3:
                        if i+1>=0 and i+1<=len(campo)-1 and j-1>=0 and j-1<=len(campo[0])-1:
                            campo[i+1][j-1]=campo[i+1][j-1]+1
                            coordenadas.append([i,j])
                        else:
                            tortugassalieron=tortugassalieron+1
    for i in range (len(campo)):
        for j in range (len(campo[0])):
            if campo[i][j]==0:
                sintortugas=sintortugas+1


    print("CASILLAS SIN TORTUGAS:",sintortugas)
    print("TORTUGAS QUE SALIERON:",tortugassalieron)
    print("AUMENTO POBLACION EN:",coordenadas)
    return (campo)

x=(distribuye(4,4,3,30))
print(x)
print (movimiento(x))
