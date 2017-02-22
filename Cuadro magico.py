def CuadroMagico(matriz):
    repetidos=[]
    suma=sumaD1=sumaD2=0
    for i in range(len(matriz)):
        suma=suma+matriz[i][0]
        for j in range (len(matriz[i])):
            if matriz[i][j] not in repetidos:
                repetidos.append(matriz[i][j])
            else:
                return False
    for i in range(len(matriz)):
        sumaH=sumaV=0
        for j in range(len(matriz)):
            sumaH=sumaH+matriz[i][j]
            sumaV=sumaV+matriz[j][i]
        sumaD1=sumaD1+matriz[i][i]
        sumaD2=sumaD2+matriz[i][len(matriz)-i-1]
        if suma!=sumaH or suma!=sumaV:
            return False
    if suma!=sumaD2 or suma!=sumaD1:
        return False
    return True

matriz=[[4,9,2],
        [3,5,7],
        [8,1,6]]
print(CuadroMagico(matriz))

