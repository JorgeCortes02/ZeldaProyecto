import funciones.datos as d
import funciones.funciones as f

posicionplayer = [8,19]
mapaActual = []
playermap = d.localitzacions["hyrule"]
mapa = ""
retorno = []


mapaActual = f.obtenerMapa(d.localitzacions["hyrule"], posicionplayer)
print(f.menuInferior(mapaActual))




while(True):

   
    select = input("Selecciona una opcion:")
    
    retorno = f.moverPersonaje(mapaActual, select, posicionplayer)
    
    f.imprimirmapa(retorno[0])
    posicionplayer = [retorno[1], retorno[2]]


