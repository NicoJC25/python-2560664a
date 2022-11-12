import random
def llenar_lista(lista):
    lista=[round(random.randrange(100))for i in range(random.randint(10,25))]
    return lista

lista=llenar_lista(list)
lista.sort()
rango=len(lista)

def primo(lista):
    for n in lista: #Para n en vector, n tomara el valor de cada cifra en la lista y se crearan 2 variables llamadas i y cont
        i=1
        cont=0
        while(n>=i):#Mientras n sea mayor o igual a i, si el residuo del valor de la lista dividido en i es 0, entonces el contador aumentara 1
            if n%i==0:
                cont+=1
            i+=1#E i siempre aumentara por cada vuelta
        if not cont>2 or n <=1:
            print('El numero',n,'es primo') #Si el numero no cumple ninguna de estas condiciones, es primo

print('Lista:',lista)
primo(lista)