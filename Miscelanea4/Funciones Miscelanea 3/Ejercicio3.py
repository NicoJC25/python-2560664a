import random
def llenar_lista(lista):
    lista=[round(random.randrange(100))for i in range(random.randint(10,25))]
    return lista

lista=llenar_lista(list)
lista.sort()
rango=len(lista)

def promedio(lista):
    suma=0
    for i in range(rango):
        suma+=lista[i]
    promedio=suma//rango
    return promedio

print('El rango de la lista es:',rango)
print('Los valores de la lista son:',lista)
print('El promedio de los valores es:',promedio(lista))

for n in lista:
    if n<promedio(lista):
        print('El numero',n,'es menor al promedio')
    elif n>promedio(lista):
        print('El numero',n,'es mayor al promedio')
    elif n==promedio(lista):
        print('El numero',n,'es igual al promedio')
