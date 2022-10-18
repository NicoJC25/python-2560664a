numero = int(input('Ponga un numero:' ))

if numero >=0 and numero <=9:
    print ("El numero tiene 1 cifra")
elif numero >=10 and numero <=99:
    print ("El numero tiene 2 cifras")
elif numero >=100 and numero <=999:
    print ('El numero tiene 3 cifras')
elif numero >=1000 and numero <=9999:
    print ('El numero tiene 4 cifras')
else:
    print ('El numero no es valido')
