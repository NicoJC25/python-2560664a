N = int(input('Digite un numero: '))

A = 0
B = 1
C = 1

for i in range (1, N, 1):
    C = A+B
    A = B
    B = C

print (C)
    