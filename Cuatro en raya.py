

matriz=[[1,1,1,1,0,0,0,0],
        [0,0,0,0,2,0,0,0],
        [0,1,1,0,0,2,0,1],
        [0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,1,0,0,0,0,0]]



def Cuatro(matriz):

#COMPROBAR FICHAS DEL JUGADOR 1
    grupox=[]
    grupoy=[]
    contHor=0
    for i in range (8):
        for j in range (8):
            if matriz[i][j]==1:
                grupox.append(i)
                grupoy.append(j)
                contHor=contHor+1
            if matriz[i][j]!=1:
                if contHor<4:
                    grupox=[]
                    grupoy=[]
                    contHor=0
                if contHor==4:

                    return (True,grupox,grupoy)
                contHor=0
    grupox=[]
    grupoy=[]
    contVer=0
    for i in range (8):
        for j in range (8):
            if matriz[j][i]==1:
                grupox.append(i)
                grupoy.append(j)
                contVer=contVer+1
                print(grupox,grupoy)
            if matriz[j][i]!=1:
                if contVer<4:
                    grupox=[]
                    grupoy=[]
                    contVer=0
                if contVer==4:
                    return (True,grupox,grupoy)

    grupox=[]
    grupoy=[]
    for i in range (8):
        for j in range (8):
            if matriz[j][i]==1:
                if j+1<8 and j+2<8 and j+3<8 and i+1<8 and i+2<8 and i+3<9:
                    if matriz[j+1][i+1]==1:
                        if matriz[j+2][i+2]==1:
                            if matriz[j+3][i+3]==1:
                                grupox.append(j)
                                grupoy.append(i)
                                grupox.append(j+1)
                                grupoy.append(i+1)
                                grupox.append(j+2)
                                grupoy.append(i+2)
                                grupox.append(j+3)
                                grupoy.append(i+3)
                                return (True,grupox,grupoy)
    grupox=[]
    grupoy=[]
    for i in range (7,-1,-1):
        for j in range (7,-1,-1):
            if matriz[j][i]==1:
                if j+1<8 and j+2<8 and j+3<8 and i-1>=0 and i-2>=0 and i-3>=0:
                    if matriz[j+1][i-1]==1:
                        if matriz[j+2][i-2]==1:
                            if matriz[j+3][i-3]==1:
                                grupox.append(j)
                                grupoy.append(i)
                                grupox.append(j+1)
                                grupoy.append(i-1)
                                grupox.append(j+2)
                                grupoy.append(i-2)
                                grupox.append(j+3)
                                grupoy.append(i-3)
                                return (True,grupox,grupoy)
#COMPROBAR FICHAS DEL JUGADOR 2
    grupox=[]
    grupoy=[]
    contHor=0
    for i in range (8):
        for j in range (8):
            if matriz[i][j]==2:
                grupox.append(i)
                grupoy.append(j)
                contHor=contHor+1
            if matriz[i][j]!=2:
                if contHor<4:
                    grupox=[]
                    grupoy=[]
                    contHor=0
                if contHor==4:
                    return (True,grupox,grupoy)
                contHor=0
    grupox=[]
    grupoy=[]
    contVer=0
    for i in range (8):
        for j in range (8):
            if matriz[j][i]==2:
                grupox.append(i)
                grupoy.append(j)
                contVer=contVer+1
            if matriz[j][i]!=2:
                if contVer<4:
                    grupox=[]
                    grupoy=[]
                    contVer=0
                if contVer==4:
                    return (True,grupox,grupoy)
    grupox=[]
    grupoy=[]
    for i in range (8):
        for j in range (8):
            if matriz[j][i]==2:
                if j+1<8 and j+2<8 and j+3<8 and i+1<8 and i+2<8 and i+3<9:
                    if matriz[j+1][i+1]==2:
                        if matriz[j+2][i+2]==2:
                            if matriz[j+3][i+3]==2:
                                grupox.append(j)
                                grupoy.append(i)
                                grupox.append(j+1)
                                grupoy.append(i+1)
                                grupox.append(j+2)
                                grupoy.append(i+2)
                                grupox.append(j+3)
                                grupoy.append(i+3)
                                return (True,grupox,grupoy)
    grupox=[]
    grupoy=[]
    for i in range (7,-1,-1):
        for j in range (7,-1,-1):
            if matriz[j][i]==2:
                if j+1<8 and j+2<8 and j+3<8 and i-1>=0 and i-2>=0 and i-3>=0:
                    if matriz[j+1][i-1]==2:
                        if matriz[j+2][i-2]==2:
                            if matriz[j+3][i-3]==2:
                                grupox.append(j)
                                grupoy.append(i)
                                grupox.append(j+1)
                                grupoy.append(i-1)
                                grupox.append(j+2)
                                grupoy.append(i-2)
                                grupox.append(j+3)
                                grupoy.append(i-3)
                                return (True,grupox,grupoy)

    return(False,grupox,grupoy)





print(Cuatro(matriz))