matriz=[[1,3,5,4,6,2,9,8,7],
        [7,6,2,1,9,8,5,4,3],
        [8,9,4,5,3,7,6,2,1],
        [9,7,8,6,1,3,2,5,4],
        [4,1,6,9,2,5,3,7,8],
        [2,5,3,7,8,4,1,6,9],
        [5,2,7,3,4,1,8,9,6],
        [3,8,9,2,7,6,4,1,5],
        [6,4,1,8,5,9,7,3,2]]
def ValidarSudoku(matriz):
    for i in matriz:
        i=set(i)
        if len(i)<9:
            return ("NO ES MATRIZ SUDOKU!!!")
    for i in range(len(matriz)):
        temp=[]
        for j in range(len(matriz)):
            temp.append(matriz[j][i])
        temp=set(temp)
        if len(temp)<9:
            return("NO ES MATRIZ SUDOKU!!!")
    return ("ES MATRIZ SUDOKU")
    suma=0
    for i in range (0,7,3):
        for j in range (0,7,3):
            suma=0
            for k in range(i,i+3):
                for l in range(j,j+3):
                    suma=suma+matriz[k][l]
            if suma!=45:
                return ("NO ES MATRIZ SUDOKU")

print(ValidarSudoku(matriz))