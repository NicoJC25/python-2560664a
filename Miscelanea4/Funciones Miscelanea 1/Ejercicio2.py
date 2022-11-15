def notas(nota):#Definimos la funcion "notas"
    if nota >=0 and nota <=3:#Intervalos con if
        return 'RECUPERACION'
    elif nota >=4 and nota <=6:
        return 'INSUFICIENTE'
    elif nota >=7 and nota <=7.9:
        return 'NOTABLE'
    elif nota >=8 and nota <=8.9:
        return 'BIEN'
    elif nota >=9 and nota <=10:
        return 'SOBRESALIENTE'
    else:
        return 'El numero no es valido'
    
print(notas(10))#Imprimimos la funcion y dentro el numero que queramos comprobar