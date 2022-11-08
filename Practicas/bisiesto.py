'''Pedir un año e indicar si el año es o no bisiesto'''
#Pedimos el año
año=int(input('Ingrese el año: '))
#Condicion
if año %4!=0:#Si el año no es divisible entre 4, no es bisiesto
    print('El año no es bisiesto')
elif año%4==0 and año%100!=0:#Si el año es divisible entre 4 pero no entre 100, es bisiesto
    print('El año es bisiesto')
elif año%4==0 and año%100==0 and año%400!=0:#Si el año es divisible entre 4 y 100 pero no entre 400, no es bisiesto
    print('El año no es bisiesto')
elif año%4==0 and año%100==0 and año%400==0:#Si el año es divisible entre 4, 100 y 400, es bisiesto
    print('El año es bisiesto')