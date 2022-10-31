#Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el valor del medio es 11. No use operadores lógicos
#Pedir los 3 numeros
numero1 = int(input('Ingrese el primer numero:' ))
numero2 = int(input('Ingrese el segundo numero:' ))
numero3 = int(input('Ingrese el tercer numero:' ))
#Organizarlos 
menor = min(numero1, numero2, numero3)
mayor = max(numero1, numero2, numero3)
medio = (numero1 + numero2 + numero3) - menor - mayor
#Imprimir el orden
print (menor, medio, mayor)

