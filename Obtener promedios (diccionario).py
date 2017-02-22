def obtenerInfoestudiantes():
    op=''
    dic={}
    while (op!='no'):
        print('ingrese los datos del estudiante')
        mat=int(input('Matriculas:'))
        dic2={}
        dic2['nombres']=input('nombres:')
        dic2['apellidos']=input('apellidos:')
        dic2['carrera']=input('carrera')
        op2=''
        materias=[]
        promedios=[]
        while (op2!='no'):
            print('ingrese los datos de una asignatura')
            materias.append(input('\tmateria:'))
            promedios.append(float(input('\tpromedio:')))
            op2=input('\tquiere ingresar mas asignaturas, si o no?:')
            print('')
        dic2['asignaturas']=tuple(materias)
        dic2['calificaciones']=tuple(promedios)
        op=input('quiere ingresar mas estudiantes, si o no:?')
        dic[mat]=dic2
    return dic

def calcularPromediosEstudiantes(diccionario):
    promedios={}
    for i in diccionario:
        temp=diccionario.get(i)
        calificaciones=temp.get("calificaciones")
        promedio=0
        for j in range(len(calificaciones)):
            promedio+=calificaciones[j]
        promedio=promedio/(len(calificaciones))
        promedios[i]=promedio
    return promedios

def obtenerMejoresPromedios(diccionario,inicial,final):
    mejores=[]
    for i in diccionario:
        if diccionario.get(i)>=inicial and diccionario.get(i)<=final :
            mejores.append(i)
    return mejores


informacion=obtenerInfoestudiantes()
promedios=calcularPromediosEstudiantes(informacion)
inicio=int(input("Ingrese el valor minimo de la nota para la beca:"))
final=int(input("Ingrese el valor maximo de la nota para la beca:"))
mejores=obtenerMejoresPromedios(promedios,inicio,final)
print("********MEJORES PROMEDIOS********")
for i in range(len(mejores)):
    temp=informacion.get(mejores[i])
    print(str(temp.get("nombres")) +" "+ str(temp.get("apellidos")) +"   "+ str(temp.get("carrera")) +"  "+ str(mejores[i]))


