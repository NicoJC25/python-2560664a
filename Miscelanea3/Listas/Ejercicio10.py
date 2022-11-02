import random
'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. Encuentre la desviación estandar'''
#Crear una lista vacia y la cantidad de valores entre 10 y 25
vector=[]
suma=0
promedio=0
desviacion=0
rango=random.randint(10,25)
#Para i en rango de la ecuacion anterior, hacer que los valores de la lista sean aleatorios entre 1 y 100
for i in range(rango):
    vector.append(round(random.random()*100))
    suma+=vector[i]
    promedio=suma//rango
    vector.sort()
    tamaño=len(vector)
    tamaño_division=tamaño-1
desviacion=(suma-promedio)**2
division=desviacion//tamaño_division
resultado=division**0.5
print('La lista es:',vector)
print('El tamaño de la lista es:',rango)
print('La desviacion estandar es:',resultado)