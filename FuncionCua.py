from ast import Num


A = int(input('Ingrese el valor de A: '))
X = int(input('Ingrese el valor de X: '))

if A == Num:
    P = input('¿Desea poner el valor de B?: ')
    if P == 'si':
        B = int(input('Ingrese el valor de B'))
        if B == Num:
            P = input('¿Desea poner el valor de C?: ')
            if P == 'si':
                C = int(input('Ingrese el valor de C: '))
                F = (A*(X**2)) + (B*X) + C
                print ('La funcion cuadratica es: ',F)
