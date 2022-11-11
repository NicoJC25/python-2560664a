def maximo_numeros(numero_maximo):
    numero=0
    contador=0
    suma=0
    while(suma<=numero_maximo): #Mientras que la suma sea menor o igual al numero insetado, numero sumara 1, suma sera re asignada
        numero+=1
        suma=0
        for i in range(0,numero+1): #Para i en el rango de 0 hasta el numero mas 1, suma sumara su valor con i
            suma+=i
    
    return numero


print(maximo_numeros(6))