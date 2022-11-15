def obrero_horas(horas):#Definimos la funcion "obrero_horas"
    h2=horas-40
    if horas<=40:#Intervalos con if
        horas*= 2600
        return horas
    elif horas>40:
        horas=40
        horas*=2600
        h2*=5000
        return (horas+h2)
    
print(obrero_horas(80))#Imprimimos la funcion y dentro el numero que queramos comprobar