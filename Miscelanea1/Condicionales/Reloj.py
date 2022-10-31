Horas=int(input('Ingrese la hora "Formato militar": '))
Minutos=int(input('Ingrese los minutos "Formato militar": '))
Segundos=int(input('Ingrese los segundos "Formato militar": '))

if Segundos>58:
    Segundos=00
    Minutos+=1
    if Minutos>58:
        Minutos=00
        Horas+=1
        if Horas>23:
            Horas=00
            print('La hora un segundo despues es:',Horas,':',Minutos,':',Segundos)
        else:
            print('La hora un segundo despues es:',Horas,':',Minutos,':',Segundos)
    else:
        print('La hora un segundo despues es:',Horas,':',Minutos,':',Segundos)
else:
    Segundos+=1
    print('La hora un segundo despues es:',Horas,':',Minutos,':',Segundos)


