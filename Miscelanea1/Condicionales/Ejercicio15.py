'''La fecha de Pascua corresponde al primer domingo después de la primera luna
llena que sigue al equinoccio de primavera, y se calcula con las siguientes
expresiones:
A= año MOD 19
B= año MOD 4
C= año MOD 7
D= (19*A+24) MOD 30
E= (2*B+4*C+6*D+5) MOD 7
N= (22+D+E)
En el que N indica el número de día del mes de marzo (o abril si N es superior a
31) correspondiente al domingo de Pascua. Realizar un programa que
determine esta fecha para un año ingresado por teclado.'''
#Pedir el año
año= int(input("Ingrese un año: "))
#Copiar y pegar las ecuaciones del ejercicio
A= año % 19
B= año % 4
C= año % 7
D= (19*A+24) % 30
E= (2*B+4*C+6*D+5) % 7
N= (22+D+E)
#Condicion cuando el mes sea abril que es cuando N sea mayor a 31
if N>31:
    N-=31
    print('La pascua fue el',N,'de Abril')
elif N<=31:
    print('La pascua fue el',N,'de Marzo') #Marzo es menor igual a 31

