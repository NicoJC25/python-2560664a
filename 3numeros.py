numero1 = int(input('Ingrese el primer numero:' ))
numero2 = int(input('Ingrese el segundo numero:' ))
numero3 = int(input('Ingrese el tercer numero:' ))

mitad = numero1 

if numero2 < mitad:
    mitad = numero2
elif numero3 < mitad:
    mitad = numero3


print ('El numero del medio es:' ,mitad)