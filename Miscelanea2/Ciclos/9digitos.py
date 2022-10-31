'''num= input("ingrese maximo 9 digitos: ")
for i in range(len(num)-1,-1,-1):
    print((num[i]),end=(""))'''

jiji= int(input('Ingrese 9 digitos: '))
jiji= str(jiji)
conter= len(jiji)
for i in range (1, 10):
    if i>0:
        jaja= jiji[-1]
    if i>1:
        jaja+= jiji[-2]
    if i>2:
        jaja+= jiji[-3]
    if i>3:
        jaja+= jiji[-4]
    if i>4:
        jaja+= jiji[-5]
    if i>5:
        jaja+= jiji[-6]
    if i>6:
        jaja+= jiji[-7]
    if i>7:
        jaja+= jiji[-8]
    if i>8:
        jaja+= jiji[-9]
    print(jaja)
