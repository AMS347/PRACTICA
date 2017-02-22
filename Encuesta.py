import openpyxl
import os


while (True):
    print("""
        *****************************************
        *  ***********************************  *
        *  *            ENCUESTAS            *  *
        *  *                                 *  *
        *  *   1. Conteo total de personas   *  *
        *  *   2. Conteo por categoria       *  *
        *  *   3. Listado por categoria      *  *
        *  *   4. Busquedad por persona      *  *
        *  *   5. Agregar Personas           *  *
        *  *   6. Cargar DataSet             *  *
        *  *   7. Salir                      *  *
        *  *                                 *  *
        *  ***********************************  *
        *****************************************
    """)
    while True:  # Validar el ingreso
        try:
            op = int(input("Ingrese una opción: "))
            if op >= 1 and op <= 7:
                break
            else:
                print("Número de opción fuera de rango")
        except:
            print("INGRESO NO VÁLIDO")
            print("\n")

    if op == 1:
        print("EL NUMERO DE ENCUESTADOS ES: " + str(len(baseDatos)))
        tiempo = input("Presione cualquier tecla para continuar".center(50, " "))
        os.system("cls")

    elif op == 2:
        drama1 = 0
        lirico = 0
        epico = 0
        otros1 = 0
        ciencia = 0
        romance = 0
        accion = 0
        drama2 = 0
        comedia = 0
        otros2 = 0
        baladas = 0
        pop = 0
        salsa = 0
        disco = 0
        rock = 0
        bachata = 0
        clasica = 0
        vallenato = 0
        reggue = 0
        electronica = 0
        otros3 = 0

        for i in range(len(baseDatos)):
            for j in range (len(baseDatos[i])):
                if baseDatos[i][j]=="DRAMA" and j==4:
                    drama1+=1
                elif baseDatos[i][j]=="LÍRICO" and j==4:
                    lirico+=1
                elif baseDatos[i][j]=="ÉPICO" and j==4:
                    epico+=1
                elif baseDatos[i][j] == "OTROS" and j == 4:
                    otros1+=1

                if baseDatos[i][j]=="CIENCIA FICCIÓN" and j==5:
                    ciencia+=1
                elif baseDatos[i][j]=="ROMANCE" and j==5:
                    romance+=1
                elif baseDatos[i][j] == "ACCIÓN" and j == 5:
                    accion+=1
                elif baseDatos[i][j] == "DRAMA" and j == 5:
                    drama2+=1
                elif baseDatos[i][j] == "COMEDIA" and j == 5:
                    comedia+=1
                elif baseDatos[i][j] == "OTROS" and j == 5:
                    otros2+=1

                if baseDatos[i][j]=="BALADAS" and j==6:
                   baladas+=1
                elif baseDatos[i][j] == "POP" and j == 6:
                    pop+=1
                elif baseDatos[i][j] == "SALSA" and j == 6:
                    salsa+=1
                elif baseDatos[i][j] == "DISCO" and j == 6:
                    disco+=1
                elif baseDatos[i][j] == "ROCK" and j == 6:
                    rock+=1
                elif baseDatos[i][j] == "BACHATA" and j == 6:
                    bachata+=1
                elif baseDatos[i][j] == "CLÁSICA" and j == 6:
                    clasica+=1
                elif baseDatos[i][j] == "VALLENATO" and j == 6:
                    vallenato+=1
                elif baseDatos[i][j] == "REGGAETON" and j == 6:
                    reggue+=1
                elif baseDatos[i][j] == "ELECTRÓNICA" and j == 6:
                    electronica+=1
                elif baseDatos[i][j] == "OTROS" and j == 6:
                    otros3+=1

        print("GÉNERO LITERARIO".center(50,"="))
        print("Drama " + str(drama1))
        print("Lírico " + str(lirico))
        print("Épico " + str(epico))
        print("Otros " + str(otros1))

        print("GÉNERO CINE".center(50, "="))
        print("Ciencia Ficción " + str(ciencia))
        print("Romance " + str(romance))
        print("Acción " +str(accion))
        print("Drama " + str(drama2))
        print("Comedia " + str(comedia))
        print("Otros " + str(otros2))

        print("GÉNERO MUSICAL".center(50, "="))
        print("Baladas " + str(baladas))
        print("Pop " + str(pop))
        print("Salsa " + str(salsa))
        print("Disco " + str(disco))
        print("Rock " + str(rock))
        print("Bachata " + str(bachata))
        print("Clásica " + str(clasica))
        print("Vallenato " + str(vallenato))
        print("Reggaeton " + str(reggue))
        print("Electrónica " + str(electronica))
        print("Otros " + str(otros3))
        tiempo = input("Presione cualquier tecla para continuar".center(50, " "))
        os.system('cls')


    elif op==3:
        print("""
        ELIGA UNA OPCION:
        1.Género liteario
        2.Género cine
        3.Género musical
        """)
        while True:
            try:
                op1 = int(input("Ingrese una opción: "))
                if op1 >= 1 and op1 <= 3:
                    break
                else:
                    print("Número de opción fuera de rango")
            except:
                print("INGRESO NO VÁLIDO")
                print("\n")

        if op1==1:
            print("GÉNERO LITERARIO".center(50, "="))
            print("""
            1.Drama
            2.Lírico
            3.Épico
            4.Otros
            """)

            while True:
                try:
                    op2 = int(input("Ingrese una opción: "))
                    if op2 >= 1 and op2 <= 4:
                        break
                    else:
                        print("Número de opción fuera de rango")
                except:
                    print("INGRESO NO VÁLIDO")
                    print("\n")

            if op2==1:
                for i in range(len(baseDatos)):
                    if baseDatos[i][4] == "DRAMA":
                        for j in range(len(baseDatos[i])):
                            print(str(baseDatos[i][j]).upper() + "\t")
                tiempo = input("Presione cualquier tecla para continuar".center(50, " "))
            elif op2==2:
                for i in range(len(baseDatos)):
                    if baseDatos[i][4] == "LÍRICO":
                        for j in range(len(baseDatos[i])):
                            print(str(baseDatos[i][j]).upper() + "\t")
                tiempo = input("Presione cualquier tecla para continuar".center(50, " "))
            elif op2 == 3:
                for i in range(len(baseDatos)):
                    if baseDatos[i][4] == "ÉPICO":
                        for j in range(len(baseDatos[i])):
                            print(str(baseDatos[i][j]).upper() + "\t")
                tiempo = input("Presione cualquier tecla para continuar".center(50, " "))
            elif op2 == 4:
                for i in range(len(baseDatos)):
                    if baseDatos[i][4] == "OTROS":
                        for j in range(len(baseDatos[i])):
                            print(str(baseDatos[i][j]).upper() + "\t")
                tiempo = input("Presione cualquier tecla para continuar".center(50, " "))

        elif op1==2:
            print("GÉNERO CINE".center(50, "="))
            print("""
            1.Ciencia Ficción
            2.Romance
            3.Acción
            4.Drama
            5.Comedia
            6.Otros
            """)

            while True:
                try:
                    op2 = int(input("Ingrese una opción: "))
                    if op2 >= 1 and op2 <= 6:
                        break
                    else:
                        print("Número de opción fuera de rango")
                except:
                    print("INGRESO NO VÁLIDO")
                    print("\n")

            if op2 == 1:
                for i in range(len(baseDatos)):
                    if baseDatos[i][5] == "DRAMA":
                        for j in range(len(baseDatos[i])):
                            print(str(baseDatos[i][j]).upper() + "\t")
                tiempo = input("Presione cualquier tecla para continuar".center(50, " "))
            elif op2 == 2:
                for i in range(len(baseDatos)):
                    if baseDatos[i][4] == "LÍRICO":
                        for j in range(len(baseDatos[i])):
                            print(str(baseDatos[i][j]).upper() + "\t")
                tiempo = input("Presione cualquier tecla para continuar".center(50, " "))
            elif op2 == 3:
                for i in range(len(baseDatos)):
                    if baseDatos[i][4] == "ÉPICO":
                        for j in range(len(baseDatos[i])):
                            print(str(baseDatos[i][j]).upper() + "\t")
                tiempo = input("Presione cualquier tecla para continuar".center(50, " "))
            elif op2 == 4:
                for i in range(len(baseDatos)):
                    if baseDatos[i][4] == "OTROS":
                        for j in range(len(baseDatos[i])):
                            print(str(baseDatos[i][j]).upper() + "\t")
                tiempo = input("Presione cualquier tecla para continuar".center(50, " "))

        elif op1==3:
            print("GÉNERO MUSICAL".center(50, "="))
            print("""
            1.Baladas
            2.Pop
            3.Salsa
            4.Disco
            5.Rock
            6.Bachata
            7.Clásica
            8.Vallenato
            9.Reggaeton
            10.Electrónica
            11.Otros
            """)
            while True:
                try:
                    op2 = int(input("Ingrese una opción: "))
                    if op2 >= 1 and op2 <= 11:
                        break
                    else:
                        print("Número de opción fuera de rango")
                except:
                    print("INGRESO NO VÁLIDO")
                    print("\n")


        tiempo = input("Presione cualquier tecla para continuar".center(50, " "))
        os.system('cls')

    elif op == 4:
        nombre = str(input("Ingrese el nombre que desea buscar:"))
        for i in range(len(baseDatos)):
            if nombre.upper() in  baseDatos[i][0].upper():
                print("".center(50,"="))
                for j in range(len(baseDatos[i])):
                    print(str(baseDatos[i][j]).upper() + "\t")
        tiempo = input("Presione cualquier tecla para continuar".center(50," "))
        os.system("cls")

    elif op == 5:
        print("En proceso")
        tiempo = input("Presione cualquier tecla para continuar".center(50, " "))
        os.system('cls')

    elif op == 6:
        doc = openpyxl.load_workbook('DATA SET.xlsx')
        nombreHoja = doc.get_sheet_names()[0]
        hoja = doc.get_sheet_by_name(nombreHoja)
        baseDatos = []
        for filas in hoja.rows:
            usuario = []
            for columnas in filas:
                usuario.append(columnas.value)
            baseDatos.append(usuario)
        baseDatos.remove(baseDatos[0])

        tiempo = input("Presione cualquier tecla para continuar".center(50, " "))
        os.system('cls')

    elif op == 7:
        os.system('cls')
        print("GOOD BYE!!!".center(50,"="))
        break