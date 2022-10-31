n = int(input("introduzca un numero para determinar sus divisores = "))
i = 1

print("Los divisores son: ")
while(n >= i):
 if n%i == 0:
  print(i)
 i+=1