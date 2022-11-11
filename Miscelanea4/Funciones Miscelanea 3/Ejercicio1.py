import random
def llenar_lista(lista):
    lista=[round(random.randrange(100))for i in range(random.randint(10,25))]
    return lista

lista=llenar_lista(list)
lista.sort()
print(lista)
rango=len(lista)

def mediana(lista):
    mitad=int(rango//2)
    if rango%2==0:
        mediana=(lista[mitad-1]+lista[mitad])//2
    else:#Si no, solo tomar el valor central
        mediana=lista[mitad]
    return mediana

print('La longitud de la lista es:',rango)
print(mediana(lista))