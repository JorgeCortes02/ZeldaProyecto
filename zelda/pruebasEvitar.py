import funciones.datos as d
import funciones.funciones as f

posicionplayer = [8,19]
mapaActual = []
playermap = d.localitzacions["hyrule"]
mapa = ""
retorno = []
print(len(d.inventario1))
print(d.dict_tipos)
mapaActual = f.obtenerMapa(d.localitzacions["hyrule"])
print(f.menuInferior(mapaActual))




while(True):

   
    select = input("Selecciona una opcion:")
    
    retorno = f.moverPersonaje(mapaActual, select, posicionplayer)
    
    f.imprimirmapa(retorno[0])
    posicionplayer = [retorno[1], retorno[2]]


