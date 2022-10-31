data_max=int(input('Introduzca el numero del dato maximo: '))
n=0
contador=0
suma=0
while(suma<=data_max):
    n+=1
    suma=0
    for i in range(0,n+1):
        suma+=i
 
print(n,"es el numero natural minimo requerido para superar el dato maximo")