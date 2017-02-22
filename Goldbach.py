#Validar que el numero ingresado sea impar
while True:
    num=int(input("Ingresar numero impar: "))
    if(num%2!=0):
        break

primos=[]
for i in range(2,(num//2)+1):
    #Compruebo cada numero que sea primo
    cont=0
    for j in range(2,i):
        if(i%j==0):
            cont+=1

    if(cont==0):
        primos.append(i)
print(primos)

d1=0
d2=0
d3=0
suma=0
while (d1<(len(primos)-1)) or (d2<(len(primos)-1)) or (d3<(len(primos)-1)) and (d3>=0 and d2>=0 and d1>=0):
    print(primos[d1],primos[d2],primos[d3])
    suma=primos[d1]+primos[d2]+primos[d3]
    if (suma==num):
        print("LOS NUMEROS SON", primos[d1],primos[d2],primos[d3])
        break
    if (d3<(len(primos)-1)):
        d3=d3+1
    if d3==(len(primos)-1):
        if (d2<(len(primos)-1)):
            d2=d2+1
    if d2==(len(primos)-1):
        if d1<(len(primos)-1):
            d1=d1+1
    if d3==(len(primos)-1) and d2==(len(primos)-1) and d3==(len(primos)-1):
        d2=d2-1
        d3=d3-2







