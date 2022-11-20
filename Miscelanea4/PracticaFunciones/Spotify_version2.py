spotify={}
def cancion(spotify):
    cancion=input('Ingrese el nombre de la cancion: ')
    spotify.update({cancion:{}})
    return spotify

def agregar_info_cancion(spotify):
    cancion=input('Ingrese el nombre de la cancion: ')
    artista=input('Ingrese el nombre del artista: ')
    genero=input('Ingrese el genero: ')
    duracion=input('Ingrese la duracion en formato xx(mm):xx(ss): ')
    if cancion in spotify:
        spotify.update({cancion:{'artista':artista,'genero':genero,'duracion':duracion}})
    else:
        print('La cancion no se encuentra, agreguela primero')
    return spotify
    
def buscar_artista(spotify):
    buscar=input('¿Que artista desea buscar?: ')
    for a in (spotify.values()):
        if buscar==a['artista']:
            print('El artista',buscar,'se encuentra en spotify y su genero es:',a['genero'])
            return None
    print('El artista no se encuentra, ingrese la cancion con el artista')
    
def buscar_cancion(spotify):
    buscar=input('¿Que cancion desea buscar?: ')
    for i in sorted(spotify.keys()):    
        if buscar==i:
            print('La cancion',buscar,'se encuentra en spotify y su duracion es:',spotify[i]['duracion'])
            return None
    print('La cancion no se encuentra, ingrese el nombre primero')

def eliminar_cancion(spotify):
    buscar=input('¿Que cancion desde elminiar?: ')
    for i in sorted(spotify.keys()):
        if buscar==i:
            del spotify[i]
            print('La cancion',buscar,'fue eliminada correctamente')

def mayor(spotify):
    menor=dict
    menor_valor=0
    for a in (spotify.keys()):
        minutos=spotify[a]['duracion'][0]
        minutos+=spotify[a]['duracion'][1]
        segundos=spotify[a]['duracion'][3]
        segundos+=spotify[a]['duracion'][4]
        segundos= int(segundos)+int(minutos)*60
        if menor_valor<=segundos:
            menor_valor=segundos
            menor=a
    print('La cancion mas larga es',menor)
        
def menor(spotify):
    menor=dict
    menor_valor=9e99999
    for a in (spotify.keys()):
        minutos=spotify[a]['duracion'][0]
        minutos+=spotify[a]['duracion'][1]
        segundos=spotify[a]['duracion'][3]
        segundos+=spotify[a]['duracion'][4]
        segundos= int(segundos)+int(minutos)*60
        if menor_valor>=segundos:
            menor_valor=segundos
            menor=a
    print('La cancion mas corta es',menor)

while True:
    import os
    os.system ("cls")
    pedir=int(input('Bienvenido al menu, presione 1 para agregar una cancion, 2 para agregar informacion detallada\n a una cancion ya agregada 3 para buscar un artista, 4 para buscar una cancion, 5 para eliminar una cancion \n 6 para mostrar todo el diccionario, 7 para mostrar la cancion mas larga, 8 para mostrar la cancion mas corta \n y 9 para finalizar el programa: '))
    if pedir==1:
        (cancion(spotify))
    elif pedir==2:
        (agregar_info_cancion(spotify))
    elif pedir==3:
        (buscar_artista(spotify))
    elif pedir==4:
        (buscar_cancion(spotify))
    elif pedir==5:
        (eliminar_cancion(spotify))
    elif pedir==6:
        print(spotify)
    elif pedir==7:
        mayor(spotify)
    elif pedir==8:
        menor(spotify)
    elif pedir==9:
        break
    else:
        print('El numero no es valido')
    os.system('pause')