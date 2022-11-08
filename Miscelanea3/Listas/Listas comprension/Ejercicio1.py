import random
'''1. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. 
De cada elemento de la lista diga si el elemento está por encima del promedio, 
debajo del promedio o es igual al promedio de todos los números de la lista.  '''
#Crear una lista vacia y crear variables
promedio=0
cont=0

rango=random.randint(10,25)#Crear la cantidad de numeros en la lista de forma aleatoria entre 10 y 25

vector=[round(random.random()*100)for i in range(rango)]#Lista comprendida donde los numeros de la lista seran de 1 a 100 en el rango de rango
suma=[0+vector[i] for i in vector]
print (suma)
promedio=suma//rango
print('El rango de la lista es:',rango)
print('Los valores de la lista son:',vector)
print('El promedio de los valores es:',promedio)
#Para n en el vector, n tomara cada valor de la lista y los comparara con el promedio lanzando el respectivo mensaje por cada situacion
for n in vector:
    if n<promedio:
        print('El numero',n,'es menor al promedio')
    elif n>promedio:
        print('El numero',n,'es mayor al promedio')
    elif n==promedio:
        print('El numero',n,'es igual al promedio')


matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

print('Mostrar todos los elementos de la matriz fila por fila')
for row in matrix:
    print(row)

print('Mostrar todos los elementos de la matriz elemento a elemento en columna')
for row in matrix:
    for element in row:
        print(element)

print('Mostrar todos los elementos de una matriz en formato de matriz')
for row in matrix:
    for wlwment in row:
        print(element, end=' ')
    print()