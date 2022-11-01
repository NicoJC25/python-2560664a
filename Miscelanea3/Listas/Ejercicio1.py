import random
'''1. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. 
De cada elemento de la lista diga si el elemento está por encima del promedio, 
debajo del promedio o es igual al promedio de todos los números de la lista.  '''
vector=[]
suma=0
promedio=0
cont=0
rango=random.randint(10,25)
for i in range(rango):
    vector.append(round(random.random()*100))
    suma+=vector[i]
    promedio=suma//rango
print(rango)
print(vector)
print(promedio)

for n in vector:
    if n<promedio:
        print('El numero',n,'es menor al promedio')
    elif n>promedio:
        print('El numero',n,'es mayor al promedio')
    elif n==promedio:
        print('El numero',n,'es igual al promedio')