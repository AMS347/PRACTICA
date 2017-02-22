tendencias={"08-22-2016":{"#Rio2016","#BSC","#ECU"},"08-25-2016":{"#GYE","#BRA"},"08-27-2016":{"#YoSoyEspol","#GYE","#BSC"}}
listafechas=["08-22-2016","08-27-2016"]

fechas1=["08-22-2016","08-27-2016"]
fechas2=["08-25-2016"]

def CuentaEtiquetas(tendencias,listasfechas):
    diccionario={}
    for i in tendencias:
        temp=tendencias.get(i)
        for k in listafechas:
            if k==i:
                for j in temp:
                    if j not in diccionario:
                        diccionario[j]=0
                    if j in diccionario:
                        diccionario[j] = diccionario.get(j)+1
    return (diccionario)

def ReportaTendencias (tendencias,listafechas):
    todas=[]
    una=[]
    diccionario={}
    for i in listafechas:
        for j in tendencias:
            if i==j:
                for k in tendencias.get(j):
                    una.append(k)
                    if k not in diccionario:
                        diccionario[k]=0
                    if k in diccionario:
                        diccionario[k]= diccionario.get(k)+1
    for i in diccionario:
        if diccionario[i]==len(listafechas):
            todas.append(i)
    una=set(una)
    return (una,todas)

def TendenciasExcluyentes(tendencias,fechas1,fechas2):
    one=[]
    two=[]
    for i in fechas1:
        for j in tendencias:
            if i==j:
                for k in tendencias.get(j):
                    one.append(k)
    for i in fechas2:
        for j in tendencias:
            if i==j:
                for k in tendencias.get(j):
                    if k in one:
                        two.append(k)
    for i in one:
        if i in two:
            one.remove(i)
            two.remove(i)
    one=set(one)
    two=set(two)
    return (one,two)

#CuentaEtiquetas(tendencias,listafechas)

#ReportaTendencias(tendencias,listafechas)

#TendenciasExcluyentes(tendencias,fechas1,fechas2)


