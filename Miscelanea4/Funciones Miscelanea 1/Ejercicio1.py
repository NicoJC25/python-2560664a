def cifras(numero):#Definimos la funcion "cifras"
    if numero >=0 and numero <=9:#Intervalos con if
        return 'El numero tiene 1 cifra'
    elif numero >=10 and numero <=99:
        return 'El numero tiene 2 cifras'
    elif numero >=100 and numero <=999:
         return 'El numero tiene 3 cifras'
    elif numero >=1000 and numero <=9999:
        return 'El numero tiene 4 cifras'
    else:
        return 'El numero no es valido'
    
print (cifras(1000))#Imprimimos la funcion y dentro el numero que queramos comprobar