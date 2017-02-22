def IdentificarSimetria(matriz):
    asimetrica=antisimetrica=False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]!=matriz[j][i]:
                asimetrica=True
            if i!=j and (matriz[i][j]==0 or matriz[j][i]==0):
                antisimetrica=True
    if asimetrica==True:
        print("LA MATRIZ ES ASIMETRICA")
    else:
        print("ES SIMETRICA")
    if antisimetrica==True:
        print("LA MATRIZ ES ANTISIMETRICA")

matriz=[[5,3,2],
        [5,1,1],
        [4,6,0]]
IdentificarSimetria(matriz)