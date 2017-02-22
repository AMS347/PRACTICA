
telegrama = input ("INGRESE UNA FRASE:")

lista = telegrama.split(" ")
telegramaProcesado = ""

for i in range (len(lista)):
    if len(lista[i])>5:
        if lista[i][-1]==".":
            telegramaProcesado = telegramaProcesado + lista[i][:5] + "@" + "STOP"
        else:
            telegramaProcesado=telegramaProcesado+lista[i][:5]+"@"+" "
    else:
        telegramaProcesado = telegramaProcesado + lista[i]+" "
print (telegramaProcesado)
