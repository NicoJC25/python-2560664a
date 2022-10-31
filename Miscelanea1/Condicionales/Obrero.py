horas = int(input('Ingrese la cantidad de horas: '))

h2 = horas - 40

if horas < 40:
    horas *= 2600
    print ('El salario semanal es:' ,horas)
elif horas > 40:
    horas = 40
    horas *= 2600
    h2 *= 5000
    print ('El salario semanal es:' ,horas + h2)