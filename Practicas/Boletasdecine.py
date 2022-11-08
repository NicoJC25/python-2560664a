""" Boletas de Cine
    Parámetros:
      cantidad_boletas (int): La cantidad de boletas que se van a comprar
      tipo_sala (str): El tipo de sala en que se proyecta la película. Puede ser '2D', '3D' o 'Dinamix'
      hora_pico (bool): Indica si el horario en que se proyecta la película es una hora pico o no
      pago_tarjeta_cinema (bool): Indica si el pago de las boletas se hará con la tarjeta del cinema
      reserva (bool): Indica si se van a reservar las boletas antes de comprarlas
    Retorno:
      int: El costo total de las boletas, redondeado al número entero más cercano.
    """
#Definir variables
precio_boleta=0
descuento1=0
descuento2=0
descuento3=0
adicional=0
adicional2=0
total_a_pagar=0
#Pedir todos los datos al usuario
cantidad_boletas=int(input('¿Cuantas boletas desea comprar?: '))
tipo_sala=str(input('¿Que tipo de sala va a elegir?(elija entre 2D, 3D y Dinamix): '))
hora_pico=str(input('¿El horario pedido es una hora pico?(responda con Si o No): '))
pago_tarjeta_cinema=str(input('¿Realizara el pago con tarjeta del cine?(responda Si o No): '))
reserva=str(input('¿Se reservaran las boletas antes de comprarse?(responda Si o No): '))
#Si el tipo de sala es 2D, 3D o Dinamix, poner sus valores correspondientes
if tipo_sala=='2D':
    precio_boleta=11300
if tipo_sala=='3D':
    precio_boleta=15500
if tipo_sala=='Dinamix':
    precio_boleta=18800
#El precio de las boletas será el establecido de acuerdo al tipo de sala por la cantidad de boletas
precio_boleta*=cantidad_boletas
#Si no es hora pico, 10% de descuento y adicional si son mas de 3 boletas, 500 pesos menos por cada boleta
if hora_pico=='No':
    descuento1=precio_boleta*10//100
    if cantidad_boletas>=3:
        descuento2=cantidad_boletas*500
#Si el pago se hace con tarjeta cinema, 5% de descuento
if pago_tarjeta_cinema=='Si':
    descuento3=precio_boleta*5//100
#Si se hace reserva, 2000 pesos adicionales por cada boleta
if reserva=='Si':
    adicional=cantidad_boletas*2000
#Si la hora es pico, sacar el adicional de las boletas de acuerdo al enunciado
if hora_pico=='Si':
    if tipo_sala=='2D':
        adicional2=precio_boleta*0.25
    elif tipo_sala=='3D':
        adicional2=precio_boleta*0.25
    elif tipo_sala=='Dinamix':
        adicional2=precio_boleta*0.50
#El total sera la resta de todos los descuentos al costo mas el aumento si hay reserva y si es hora pico
total_a_pagar=round(precio_boleta-descuento1-descuento2-descuento3+adicional+adicional2)
#Print el total
print('El total a pagar es:',total_a_pagar)