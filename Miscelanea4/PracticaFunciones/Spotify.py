spotify={}
def artista(spotify):
    artista=input('Ingrese el nombre del artista: ')
    spotify.update({artista:{}})
    return spotify

def agregar_cancion(spotify):
    artist=input('Ingrese el nombre del artista: ')
    genero=input('Ingrese el genero: ')
    can=input('Ingrese una cancion del artista: ')
    duracion=input('Ingrese la duracion en formato xx(mm):xx(ss)')
    if artist in spotify:
        spotify.update({artist:{'Genero':genero,['Canciones']:{[can]:duracion}}})
        spotify[artist]['Canciones'].append(can)
        print (spotify)
    else:
        print('El artista no se encuentra, agreguelo primero')
    while True:
            try:
                pedir=int(input('Si desea agregar otra cancion al mismo artista, presione 1, de lo contrario, presione 0: '))
            except:
                print('Ingrese un numero valido')
            if pedir==1:
                    can=(input('Ingrese otra cancion del artista: '))
                    duracion=input('Ingrese la duracion en formato xx(mm):xx(ss)')
                    spotify[artist]['Canciones']['Cancion'].append(can)
            elif pedir==0:
                break
    return spotify
    
def buscar_artista(spotify):
    buscar=input('¿Que artista desea buscar?: ')
    for i in sorted(spotify.keys()):
        if buscar==i:
            print('El artista',buscar,'se encuentra en spotify y su genero es:',spotify[i]['Genero'])
        else:
            print('El artista',buscar,'no se encuentra en spotify')
    
def buscar_cancion(spotify):
    buscar=input('¿Que cancion desea buscar?: ')
    for a in sorted(spotify.keys()):    
        for i in sorted(spotify.values()):
            if buscar==i:
                print('La cancion',buscar,'se encuentra en spotify y su duracion es:',spotify[a]['Duracion'])
            else:
                print('La cancion',buscar,'no se encuentra en spotify')

def eliminar_artista(spotify):
    buscar=input('¿Que artista desde elminiar?: ')
    for i in sorted(spotify.keys()):
        if buscar==i:
            del spotify[i]
            print('El artista',buscar,'fue eliminado correctamente')



while True:
    import os
    os.system ("cls")
    pedir=int(input('Bienvenido al menu, presione 1 para agregar un artista, 2 para agregar una cancion a un artista ya agregado \n 3 para buscar un artista, 4 para buscar una cancion, 5 para eliminar el artista \n 6 para mostrar todo el diccionario, 7 para mostrar la cancion mas larga, 8 para mostrar la cancion mas corta \n y 9 para finalizar el programa: '))
    if pedir==1:
        (artista(spotify))
    elif pedir==2:
        (agregar_cancion(spotify))
    elif pedir==3:
        (buscar_artista(spotify))
    elif pedir==4:
        (buscar_cancion(spotify))
    elif pedir==5:
        (eliminar_artista(spotify))
    elif pedir==6:
        print(spotify)
    elif pedir==9:
        break
    else:
        print('El numero no es valido')
    os.system('pause')
            
        
