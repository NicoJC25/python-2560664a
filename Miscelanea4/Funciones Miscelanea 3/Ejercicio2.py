import random
def llenar_lista(lista):
    lista=[round(random.randrange(100))for i in range(random.randint(10,25))]
    return lista

lista=llenar_lista(list)
lista.sort()
print(lista)
rango=len(lista)

def par_impar(numero):
    if numero%2==0 and numero>=2:
        return 'Par'
    elif numero==0:
        return 'El numero es 0'
    else:
        return 'Impar'