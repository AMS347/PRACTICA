def IngresarAspirante(aspirantes):
    aspirante=[]
    nombre=input("INGRESE EL NOMBRE DEL ASPIRANTE:")
    ID=input("INGRESE LA CÉDULA DEL ASPIRANTE:")
    fisica=float(input("INGRESE LA NOTA DE LA PRUEBA FISICA DEL ASPIRANTE:"))
    escrita=float(input("INGRESE LA NOTA DE LA PRUEBA ESCRITA DEL ASPIRANTE:"))
    aspirante.append(nombre)
    aspirante.append(ID)
    aspirante.append(fisica)
    aspirante.append(escrita)
    aspirantes.append(aspirante)
    return aspirantes

def VisualizarAspirantes(aspirantes):
    for i in range(len(aspirantes)):
        for j in range (len(aspirantes[i])):
            print (aspirantes[i][j],"     ", end="")
        print("\n")

def ObtenerPromedio(aspirantes):
    promedioFiscia=0
    promedioEscrita=0
    for i in range(len(aspirantes)):
        promedioFiscia=promedioFiscia+aspirantes[i][2]
        promedioEscrita=promedioEscrita+aspirantes[i][3]
    print("EL PROMEDIO DE LA PRUEBA FISICA ES:",(promedioFiscia/len(aspirantes)))
    print("EL PROMEDIO DE LA PRUEBA ESCRITA ES:",(promedioEscrita/len(aspirantes)))

def BuscarDatos(aspirantes):
    nombre=input("INGRESE EL NOMBRE DEL ASPIRANTE A BUSCAR:")
    for i in range (len(aspirantes)):
        if nombre in aspirantes[i][0]:
            print("ASPIRANTE ENCONTRADO:",aspirantes[i][1])

aspirantes=[]
while True:

    print("         MENU            ")
    print("1.INGRESE UN ASPIRANTE")
    print("2.VISUALICE LOS ASPIRANTES")
    print("3,OBTENGA PROMEDIO DE LAS PRUEBAS ESCRITASY FISICAS DE LOS ASPIRANTES")
    print("4,SALIR                         ")

    op=int(input("INGRESE UNA OPCION:"))

    if op==1:
        IngresarAspirante(aspirantes)
    elif op==2:
        VisualizarAspirantes(aspirantes)
    elif op==3:
        ObtenerPromedio(aspirantes)
    elif op==4:
        print("GRACIAS POR UTILIZAR NUESTRO SISTEMA")
        break
