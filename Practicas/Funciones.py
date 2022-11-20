def llenar_lista(lista):
    import random
    lista=[round(random.random()*100)for i in range(random.randint(10,25))]
    return lista

lista=llenar_lista(list)
lista.sort()

def par (lista):
    par=[x for x in lista if x%2==0]
    return par

def impar (lista):
    impar=[x for x in lista if x%2!=0]
    return impar

def suma_par(lista):
    suma=0
    par=[x for x in lista if x%2==0]
    for i in range(len(par)):
        suma+=par[i]
    return suma

def promedio_impar(lista):
    impar=[x for x in lista if x%2!=0]
    suma=0
    rango=len(impar)
    for i in range(len(impar)):
        suma+=impar[i]
    promedio=suma//rango
    return promedio

def mediana(lista):
    rango=len(lista)
    mitad=int(rango//2)
    if rango%2==0:
        mediana=(lista[mitad-1]+lista[mitad])//2
    else:
        mediana=lista[mitad]
    return mediana

def primo(lista):
    for n in lista:
        i=1
        contador=0
        while n>=i:
            if n%i==0:
                contador+=1
            i+=1
        if not contador>2 or n<=1:
            print('El numero',n,'es un primo de la lista')

def perfecto(lista):
    for n in lista:
        i=1
        contador=0
        suma=0
        while n>i:
            if n%i==0:
                contador=i
            i+=1
        for i in range(contador+1):
            suma+=i
        if n==suma:
            print('El numero',n,'es perfecto')

print('La lista principal es:',lista)
print('La lista con solo numeros pares es:',par(lista))
print('La lista con solo numeros impares es:',impar(lista))
print('La suma de los numeros pares es:',suma_par(lista))
print('El promedio de los impares es:',promedio_impar(lista))
print('La mediana de la lista es:',mediana(lista))
primo(lista)
perfecto(lista)
