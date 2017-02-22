import random

#Definimos tres listas aparte de la que contiene el nombe de los jugadores para de esta manera poder almacenar los puntajes de cada jugador.
#Siempre manteniendo el orden de los mismos.

jugadores =  ["jorge","raul","jose","santiago","lucia","elena","solange"]
PDN = [0,0,0,0,0,0,0]
PDE = [0,0,0,0,0,0,0]
PF = [0,0,0,0,0,0,0]

#En estos enlaces de FOR realizamos el lanzamiento de las 50 veces de los dados de cada jugador

for i in range (len(jugadores)):
    for j in range (49):
        dadoNormal = random.randint(1, 6)
        dadoEspecial = random.randint(1, 6)
        PDN[i] = PDN[i] + dadoNormal
        PDE[i] = PDE[i] + dadoEspecial
    puntajeFinal = (float(PDN[i]) + float(PDE[i]) * 1.5)
    PF[i] = PF[i] + puntajeFinal

#Procedemos a sacar la media de los puntajes

sumaPDN = 0
sumaPF = 0

for i in range (len(PDN)):
    sumaPDN = sumaPDN + PDN[i]
    sumaPF = sumaPF + PF[i]

mediaPDN = sumaPDN/(len(PDN))
mediaPF = sumaPF/(len(PF))

#En este bloque encontramos al juador con mayor y menor puntaje de la lista

mayorPuntaje = 0
nombreMayor = ""
menorPuntaje = mediaPF
nombreMenor = ""
for i in range (len(jugadores)):
    if PF[i]>mayorPuntaje:
        mayorPuntaje = PF[i]
        nombreMayor = jugadores[i]
    if PF[i]<menorPuntaje:
        menorPuntaje = PF[i]
        nombreMenor = jugadores[i]

#En esta seccion utilizamos lazos FOR para comparar y poder encontrar los jugadores con PF y PDN mayor a la media

mediaSuperior = []
for i in range (len(jugadores)):
    if PF[i]>mediaPF and PDN[i]>mediaPDN:
        mediaSuperior.append(jugadores[i])

#mostramos los valores obtenidos por cada jugador y datos adicionales

for i in range (len(jugadores)):
    print (jugadores[i].upper().center(50,"="))
    print ("Puntaje normal: " + str(PDN[i]).ljust(100," "))
    print ("Puntaje especial: "+ str(PDE[i]).ljust(50, " "))
    print ("Puntaje final: "+ str(PF[i]).ljust(50, " "))
print ("".center(50," "))
print ("DATOS ADICIONALES".center(50,"="))
print ("".center(50," "))
print ("MAYOR PUNTAJE: " + nombreMayor.capitalize() + " con" + str(mayorPuntaje).center(50," "))
print ("MENOR PUNTAJE: " + nombreMenor.capitalize() + " con" + str(menorPuntaje).center(50, " "))
print ("Media de puntaje final: " + ('{:.2f}'.format(mediaPF)))
print ("".center(50," "))
print("JUGADORES CON PUNTAJE FINAL Y NORMAL MAYOR A LA MEDIA".center(50," "))
for i in range (len(mediaSuperior)):
    print(mediaSuperior[i].capitalize())



