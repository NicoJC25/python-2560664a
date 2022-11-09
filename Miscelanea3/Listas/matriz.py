import random
rango=random.randint(2,5)
vector=[[round(random.random()*100)for filas in range (rango)]
        for columnas in range (rango)]
print(vector)
print(vector[0][0])