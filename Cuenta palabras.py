def imprimir_palabras(mensaje):
    palabras=mensaje.split(" ")
    palabras1=palabras.copy()
    finalPalabras=[]
    finalContadores=[]
    for i in range(len(palabras)):
        flag = False
        temp=palabras.pop()
        if len(finalPalabras)==0:
            finalPalabras.append(temp)
            finalContadores.append(1)
        else:
            for j in range (len(finalPalabras)):
                if temp==finalPalabras[j]:
                    finalContadores[j]+=1
                    flag=True
            if flag==False:
                finalPalabras.append(temp)
                finalContadores.append(1)
    for i in range(len(finalPalabras)):
        print(finalPalabras[i] + "--->" + str(finalContadores[i]) + "\n")
    mensajeImprimir=""
    for i in range(len(palabras1)):
        mensajeImprimir+=palabras1[i].lower()+" "
    print(mensajeImprimir)
    return ()

def imprimir_pals_top(mensaje):
    palabras = mensaje.split(" ")
    finalPalabras = []
    finalContadores = []
    contador=0
    for i in range(len(palabras)):
        flag = False
        temp=palabras.pop()
        if len(finalPalabras)==0:
            finalPalabras.append(temp)
            finalContadores.append(1)
        else:
            for j in range (len(finalPalabras)):
                if temp==finalPalabras[j]:
                    finalContadores[j]+=1
                    flag=True
            if flag==False:
                finalPalabras.append(temp)
                finalContadores.append(1)

    topPalabras=[0,0,0,0,0]
    topContadores=[0,0,0,0,0]

    for j in range(2):
        for i in range(len(finalPalabras)):
            while True:
                if (finalContadores[i])>(topContadores[0]):
                    topPalabras[0]=finalPalabras[i]
                    topContadores[0]=finalContadores[i]
                    break
                if (finalContadores[i])>(topContadores[1]):
                    topPalabras[1]=finalPalabras[i]
                    topContadores[1]=finalContadores[i]
                    break
                if (finalContadores[i])>(topContadores[2]):
                    topPalabras[2]=finalPalabras[i]
                    topContadores[2]=finalContadores[i]
                    break
                if (finalContadores[i])>(topContadores[3]):
                    topPalabras[3]=finalPalabras[i]
                    topContadores[3]=finalContadores[i]
                    break
                if (finalContadores[i])>(topContadores[4]):
                    topPalabras[4]=finalPalabras[i]
                    topContadores[4]=finalContadores[i]
                    break
                else:
                    break
    for i in range(len(topContadores)):
        print(str(topPalabras[i]) + "--->" + str( topContadores[i] ) + "\n")
    return()

while True:
    print("           ************MENU************            ")
    print("1.Cuenta palabras")
    print("2.Palabras más frecuentes")
    print("3.Salir")
    print("")

    op= int(input("Ingrese una opcion: "))
    if op==1:
        mensaje=str(input("Ingrese un mensaje: "))
        imprimir_palabras(mensaje)
    elif op==2:
        mensaje = str(input("Ingrese un mensaje: "))
        imprimir_pals_top(mensaje)
    else:
        break

mensaje="la salud y la properidad en la vida"
