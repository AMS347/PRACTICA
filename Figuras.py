import turtle
import numpy as np
import random


def boxRelleno (pen, intDim):
    pen.begin_fill()
    pen.forward(intDim)
    pen.left(90)
    pen.forward(intDim)
    pen.left(90)
    pen.forward(intDim)
    pen.left(90)
    pen.forward(intDim)
    pen.end_fill()
    pen.setheading(0)

def boxVacio (pen, intDim):
    pen.begin_fill()
    pen.forward(intDim)
    pen.left(90)
    pen.forward(intDim)
    pen.left(90)
    pen.forward(intDim)
    pen.left(90)
    pen.forward(intDim)
    pen.setheading(0)

def transformar(pixel):
    x,y = pixel.shape
    arreglo = []
    for i in range(x):
        if (x/3)+1 == i or (x/3)+(x/3)+2==i :
            for j in range(3):
                vacio = []
                for k in range(y):
                    vacio.append(0)
                arreglo.append(vacio)
        arreglo.append(pixel[i])
    modificada = np.array(arreglo)
    return modificada


def drawPixelArtEnPartes(pixel):
    turtle.setup(800, 600)
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    wn.title("Project")
    pixels = transformar(pixel)
    myPen = turtle.Turtle()
    myPen.speed(100)
    myPen.color("#000000")

    boxSize = 10
    myPen.penup()
    myPen.forward(-100)
    myPen.setheading(90)
    myPen.forward(100)
    myPen.setheading(0)
    (n,m) = pixels.shape
    for i in range (n):
        for j in range(m):
            if pixels[i][j]==1:
                boxRelleno(myPen,boxSize)
            myPen.penup()
            myPen.forward(boxSize)
            myPen.pendown()
        myPen.setheading(270)
        myPen.penup()
        myPen.forward(boxSize)
        myPen.setheading(180)
        myPen.forward(boxSize*m)
        myPen.setheading(0)
        myPen.pendown()
    myPen.getscreen().update()

    wn.clear()
    wn.reset()

def drawPixelArt(pixels):
    turtle.setup(800, 600)
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    wn.title("Project")
    myPen = turtle.Turtle()
    myPen.speed(100)
    myPen.color("#000000")


    boxSize = 10
    myPen.penup()
    myPen.forward(-100)
    myPen.setheading(90)
    myPen.forward(100)
    myPen.setheading(0)
    (n,m) = pixels.shape
    for i in range (n):
        for j in range(m):
            if pixels[i][j]==1:
                boxRelleno(myPen,boxSize)
            myPen.penup()
            myPen.forward(boxSize)
            myPen.pendown()
        myPen.setheading(270)
        myPen.penup()
        myPen.forward(boxSize)
        myPen.setheading(180)
        myPen.forward(boxSize*m)
        myPen.setheading(0)
        myPen.pendown()

    myPen.getscreen().update()
    wn.clear()
    wn.reset()


pixel1 = np.array([
[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0],
[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
[0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0],
[0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[0,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0],
[0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0],
[0,0,0,1,0,0,1,1,1,0,0,0,1,0,0,0],
[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0],
[0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

pixel2 = np.array([
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0],
[1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
[0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
[0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0],
[0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0],
[0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0],
[0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0],
[0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0]])

pixel3 = np.array([
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
[0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
[0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
[0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

while True:
    print("           ************MENU************            ")
    print("1.Juego de dados")
    print("2.Figuras")
    print("3.Salir")
    op = int((input("INGRESE LA OPCION QUE DESEA EJECUTAR:")))
    if op == 1:
        jugadores = ["jorge", "raul", "jose", "santiago", "lucia", "elena", "solange"]
        PDN = [0, 0, 0, 0, 0, 0, 0]
        PDE = [0, 0, 0, 0, 0, 0, 0]
        PF = [0, 0, 0, 0, 0, 0, 0]

        # En estos enlaces de FOR realizamos el lanzamiento de las 50 veces de los dados de cada jugador

        for i in range(len(jugadores)):
            for j in range(49):
                dadoNormal = random.randint(1, 6)
                dadoEspecial = random.randint(1, 6)
                PDN[i] = PDN[i] + dadoNormal
                PDE[i] = PDE[i] + dadoEspecial
            puntajeFinal = (float(PDN[i]) + float(PDE[i]) * 1.5)
            PF[i] = PF[i] + puntajeFinal

        # Procedemos a sacar la media de los puntajes

        sumaPDN = 0
        sumaPF = 0

        for i in range(len(PDN)):
            sumaPDN = sumaPDN + PDN[i]
            sumaPF = sumaPF + PF[i]

        mediaPDN = sumaPDN / (len(PDN))
        mediaPF = sumaPF / (len(PF))

        # En este bloque encontramos al juador con mayor y menor puntaje de la lista

        mayorPuntaje = 0
        nombreMayor = ""
        menorPuntaje = mediaPF
        nombreMenor = ""
        for i in range(len(jugadores)):
            if PF[i] > mayorPuntaje:
                mayorPuntaje = PF[i]
                nombreMayor = jugadores[i]
            if PF[i] < menorPuntaje:
                menorPuntaje = PF[i]
                nombreMenor = jugadores[i]

        # En esta seccion utilizamos lazos FOR para comparar y poder encontrar los jugadores con PF y PDN mayor a la media

        mediaSuperior = []
        for i in range(len(jugadores)):
            if PF[i] > mediaPF and PDN[i] > mediaPDN:
                mediaSuperior.append(jugadores[i])

        # mostramos los valores obtenidos por cada jugador y datos adicionales

        for i in range(len(jugadores)):
            print (jugadores[i].upper().center(50, "="))
            print ("Puntaje normal: " + str(PDN[i]).ljust(100, " "))
            print ("Puntaje especial: " + str(PDE[i]).ljust(50, " "))
            print ("Puntaje final: " + str(PF[i]).ljust(50, " "))
        print ("".center(50, " "))
        print ("DATOS ADICIONALES".center(50, "="))
        print ("".center(50, " "))
        print ("MAYOR PUNTAJE: " + nombreMayor.capitalize() + " con" + str(mayorPuntaje).center(50, " "))
        print ("MENOR PUNTAJE: " + nombreMenor.capitalize() + " con" + str(menorPuntaje).center(50, " "))
        print ("Media de puntaje final: " + ('{:.2f}'.format(mediaPF)))
        print ("".center(50, " "))
        print("JUGADORES CON PUNTAJE FINAL Y NORMAL MAYOR A LA MEDIA".center(50, " "))
        for i in range(len(mediaSuperior)):
            print(mediaSuperior[i].capitalize())

    elif op==2:
        while True:

            print("           ************MENU************            ")
            print("1.Pixel 1")
            print("2.Pixel 2")
            print("3.Pixel 3")
            print("4.Salir")

            op = int((input("INGRESE LA OPCION QUE DESEA EJECUTAR:")))
            if op == 1:
                print("1.Completa")
                print("2.En partes")
                op1 = int(input("Ingrese la opcion que desea: "))
                if op1 == 1:
                    drawPixelArt(pixel1)
                    break
                else:
                    drawPixelArtEnPartes(pixel1)
                    break
            elif op == 2:
                print("1.Completa")
                print("2.En partes")
                op1 = int(input("Ingrese la opcion que desea: "))
                if op1 == 1:
                    drawPixelArt(pixel2)
                    break
                else:
                    drawPixelArtEnPartes(pixel2)
                    break
            elif op == 3:
                print("1.Completa")
                print("2.En partes")
                op1 = int(input("Ingrese la opcion que desea: "))
                if op1 == 1:
                    drawPixelArt(pixel3)
                    break
                else:
                    drawPixelArtEnPartes(pixel3)
                    break
            else:
                break
    else:
        exit()









