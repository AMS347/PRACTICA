import math

def CalcularCostos(x,y,z):
    x=abs(distancia=x-y)
    costo=0
    if z<10:
        costo+=500+x*100
    elif z>=10 and z<=30:
        costo+=1000+x*100
    else:
        costo+=3000+x*100

def TablaDePuntos():
    tabla=[]
    distancia=0
    distancias=[]

    while True:
        subtabla=[]
        x=float(input("INGRESE LA COORDENADA X:"))
        y=float(input("INGRESE LA COORDENADA Y:"))
        z=float(input("INGRESE LA COORDENADA Z:"))
        subtabla.append(x)
        subtabla.append(y)
        subtabla.append(z)
        tabla.append(subtabla)
        op=input("DESEA SEGUIR INGRESANDO(0 PARA SALIR Ó ENTER PARA SEGUIR)")
        if op==0:
            break
    for i in range(len(tabla)):
        for j in range(len(tabla[i])):
            if i+1<len(tabla):
                distancia+=(tabla[i+1][j]-tabla[i][j])**2
        if i+1<len(tabla):
            distancias.append(math.sqrt(distancia))
    distancias.sort()
    mayor=distancias[len(distancias)-1]
    return mayor