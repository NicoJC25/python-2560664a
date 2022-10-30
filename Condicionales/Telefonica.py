Minutos=int(input('Ingrese la cantidad de minutos que dura la llamada: '))
Tres_minutos=200
if Minutos<=3 and Minutos>0:
    print ('La llamada costó 200 pesos')
elif Minutos>3:
    Minutos=((Minutos-3)*50)+200
    print ('La llamada costó',Minutos)
else:
    print ('El numero ingresado no es valido')
