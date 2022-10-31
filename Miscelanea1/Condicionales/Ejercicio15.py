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

