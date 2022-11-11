def costo_minutos(Minutos):
    if Minutos<=3 and Minutos>0:
        return 'La llamada costó 200 pesos'
    elif Minutos>3:
        Minutos=((Minutos-3)*50)+200 #Ecuacion para determinar el resto de los minutos
        return Minutos
    else:
        return 'El numero ingresado no es valido'
    
print(costo_minutos(5))