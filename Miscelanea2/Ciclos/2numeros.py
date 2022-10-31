n = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))
n3 = n
conter=0
if n2>n:
    n=n2
    n2=n3
while n>=n2:
    n-=n2
    conter+=1
print ('El cociente es:' ,conter, 'y el residuo es: ' ,n)