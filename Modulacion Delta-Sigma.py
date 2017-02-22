# Modulacion Delta - Codificador
# entrada x(t), salida: y[n]
# propuesta:edelros@espol.edu.ec
import numpy as np
import matplotlib.pyplot as plt
import math
# Definir la funcion de Entrada
def entradax(t,fs):
    # función matemática CAMBIAR AQUI
    T=1/fs
    n=t//T
    x=math.exp(t-(n*T))
    # función matemática CAMBIAR AQUI
    return(x)

# PROGRAMA para la modulación
# INGRESO
t0=0
tn=float(input('rango [0,tn]:'))
k=int(input('Secciones en el rango k:'))

# PROCEDIMIENTO
# Analógica Referencia
fs=1
m=500  # puntos en eje t para gráfico analógica
dm=(tn-t0)/m
t=np.arange(0,tn,dm)  # eje tiempo analógica
xanalog=np.zeros(m, dtype=float)
for i in range(0,m):
    xanalog[i]=entradax(t[i],fs)

# Codificar Sigma-Delta
deltaY=0.3    # Tamaño delta en eje Y
deltaT=(tn-t0)/k    # Tamaño delta en eje tiempo
td=np.arange(0,tn,deltaT)    # tiempo muestreo
muestra=np.zeros(k, dtype=float)    # analógica para comparar
xdigital=np.zeros(k, dtype=float)   # digital
ysalida=np.zeros(k, dtype=int)      # Salida de +1|-1

td[0]=t0
muestra[0]=entradax(td[0],fs)
ysalida[0]=0
for i in range(1,k):
    muestra[i]=entradax(td[i],fs) # referencia analógica
    diferencia=muestra[i]-xdigital[i-1]
    if (diferencia>0):
        bit=1
    else:
        bit=-1
    xdigital[i]=xdigital[i-1]+bit*deltaY
    ysalida[i]=bit
parametros=np.array([deltaT,deltaY,k])

# SALIDA
print(ysalida)
print(parametros)
np.savetxt('sigmadelta_datos.txt',ysalida,fmt='%i')
np.savetxt('sigmadelta_parametros.txt',parametros)
# Graficar
plt.figure(1)       # define la grafica
plt.suptitle('Codificador Sigma-Delta')
plt.subplot(211)    # grafica de 2x1 y subgrafica 1
plt.ylabel('x(t), x[n]')
xmax=np.max(xanalog)+0.1*np.max(xanalog) # rango en el eje y
xmin=np.min(xanalog)-0.1*np.max(xanalog)
plt.axis((t0,tn,xmin,xmax)) # Ajusta ejes
plt.plot(t,xanalog, 'g')
plt.axis((t0,tn,xmin,xmax))
plt.plot(td,xdigital,'bo')  # Puntos x[n]
plt.step(td,xdigital, where='post',color='m')
plt.subplot(212)    # grafica de 2x1 y subgrafica 2
plt.ylabel('y[n]')
plt.axis((0,k,-1.1,1.1))
plt.plot(ysalida, 'bo')     # Puntos y[n]
puntos=np.arange(0,k,1)     #posicion eje x para escalon
plt.step(puntos,ysalida, where='post')
plt.show()
