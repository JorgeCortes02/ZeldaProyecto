import funciones.datos as d
import funciones.funciones as f

posicionplayer = [3,9]
mapaActual = []
playermap = d.gerudo
mapa = ""
retorno = []


mapaActual = f.obtenerMapa(d.death, posicionplayer)





while(True):

    
    select = input("Selecciona una opcion:")
    
    retorno = f.moverPersonaje(mapaActual, select, posicionplayer)
    
    f.imprimirmapa(retorno[0])
    posicionplayer = [retorno[1], retorno[2]]


