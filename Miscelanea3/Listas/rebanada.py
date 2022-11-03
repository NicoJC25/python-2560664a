'''Ejercicio donde hay que eliminar los valores repetidos de una lista'''
#Valores constantes de la lista y crear una lista vacia
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
temporal=[]

for i in my_list:#Para i en la lista principal
    if i not in temporal:#Si i no esta en la segunda lista, 
        temporal.append(i)#Se agregara ese numero
    
print("La lista con elementos únicos:")
print(temporal)
