dia = int(input('Ingrese el dia del año'))

if dia >=0 and dia <=31:
    print ("El mes es Enero")
elif dia >=32 and dia <=60:
    print ("El mes es Febrero")
elif dia >=61 and dia <=92:
    print ("El mes es Marzo")
elif dia >=93 and dia <=123:
    print ("El mes es Abril")
elif dia >=124 and dia <=155:
    print ("El mes es Mayo")
elif dia >=156 and dia <=186:
    print ("El mes es Junio")
elif dia >=187 and dia <=218:
    print ("El mes es Julio")
else:
    print ('El numero no es valido')