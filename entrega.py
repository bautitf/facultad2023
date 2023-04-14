#10. Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, escriba un
#programa que manipule dichas estructuras de datos para poder resolver los siguientes puntos:
#A. Generar una estructura con todas las notas relacionando el nombre del estudiante con las
#notas. Utilizar esta estructura para la resolución de los siguientes items.
#B. Calcular el promedio de notas de cada estudiante.
#C. Calcular el promedio general del curso.
#D. Identificar al estudiante con la nota promedio más alta.
#E. Identificar al estudiante con la nota más baja.
#Nota:
#• Las 3 estructuras están ordenadas de forma que los elementos en la misma posición corresponden
#a un mismo alumno.
#• Realizar funciones con cada item


nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


nombre_lista = nombres.split(",")

   # si hago zip de 3 listas que contienen (Agustin,Alan,Andrés);(81,60,72);(30,95,28) obtengo (Agustin,81,30),(Alan,60,95),(Andrés,72,28)


# A. Generar una estructura con todas las notas relacionando el nombre del estudiante con las notas.
def generar_diccionario_notas(nombre_lista, notas_1, notas_2):
    notas = {}  #el diccionario de notas a retornar
    for nombre, nota_1, nota_2 in zip(nombre_lista, notas_1, notas_2):   #pude entender iterar con multiples indices gracias a esta pregunta https://stackoverflow.com/questions/63440644/for-loop-with-two-indexes
        notas[nombre] = [nota_1, nota_2]            #agregamos al dic. de notas
    return notas            

# B. Calcular el promedio de notas de cada estudiante.
def calcular_promedio(dic_notas):
    promedios = {} #el diccionario de promedios a retornar
    for nombre, notas in dic_notas.items():   #items devuelve el diccionario en una tupla que separa en llave-valores,y yo voy a usar esta tupla para iterar con notas,el segundo valor indice
        #print(nombre,notas)                
        promedio = sum(notas) / len(notas) #sum devuelve la suma de todo lo contenido en notas,y len es la longitud de notas
        promedios[nombre]  = promedio     #agregamos al dic. de promedios
    return promedios


# C. Calcular el promedio general del curso
def promedio_del_curso (dic_promedios):
    contador = [] #la lista que voy a usar para juntar todos los promedios
    for estudiante in dic_promedios: 
        contador.append(dic_promedios[estudiante]) #quiero usar append porque se me hace más familiar resolver este problema agregando en una lista,y contando lo que tiene la lista
    promedio = sum(contador) / len(contador)  #el mismo promedio que use antes
    return promedio



# D. Identificar al estudiante con la nota promedio más alta.
def mejor_promedio(dic_promedios):
    max = 0.00
    elmejor = ""
    for estudiante, promedio in dic_promedios.items(): #obtenemos el diccionario en una tupla devuelta,para recorrer
        if promedio > max:       # si el promedio del estudiante supera el max
            max = promedio
            elmejor = estudiante       # entonces actualizamos ambos maximos
    return elmejor



# E. Identificar al estudiante con la nota más baja.
def peor_promedio(dic_promedios):
    min = 100.00
    elpeor = ""
    for estudiante, promedio in dic_promedios.items(): #obtenemos el diccionario en una tupla devuelta,para recorrer
        if promedio < min:       # si el promedio del estudiante es peor que el min
            min = promedio
            elpeor = estudiante       # entonces actualizamos ambos minimos
    return elpeor




#print(nombre_lista)
dic_notas = generar_diccionario_notas(nombre_lista, notas_1, notas_2)
print(dic_notas)
dic_promedios = calcular_promedio(dic_notas)
print(dic_promedios)
promedio_total = promedio_del_curso(dic_promedios)
print (int(promedio_total))
mejorestudiante = mejor_promedio(dic_promedios)
print(mejorestudiante)
peorestudiante = peor_promedio(dic_promedios)
print(peorestudiante)