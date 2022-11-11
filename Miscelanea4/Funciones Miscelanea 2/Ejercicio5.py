def division_resta (numero1,numero2):
    numero3=numero1
    contador=0
    if numero2>numero1: #Si el segundo numero es mayor, intercambiaran valores
        numero1=numero2
        numero2=numero3
    while numero1>=numero2: #Mientras el primero es el mayor, el menor le ira restando al mayor mientras que el contador aumentara
        numero1-=numero2
        contador+=1
    return 'El cociente es:' ,contador, 'y el residuo es: ' ,numero2


print(division_resta(6,2))