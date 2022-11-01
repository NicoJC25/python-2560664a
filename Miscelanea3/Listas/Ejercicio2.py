import random

vector=[]
rango=random.randint(10,25)
for n in range(rango):
    vector.append(round(random.random()*100))
print('Lista:',vector)
for n in vector:
    i=1
    cont=0
    while(n>=i):
        if n%i==0:
            cont+=1
        i+=1
    if not cont>2 or n <=1: #Si el numero no cumple ninguna de estas condiciones, es primo
        print('El numero',n,'es primo')