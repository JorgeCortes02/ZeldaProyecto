import funciones.datos as d

import funciones.funciones as f

def movimientoCercano(Select):

    lista_arboles = []

    if Select[len(Select)-1] == "T":

        for element in d.dades["death"]["arboles"]:

            suma1 =  d.jugador["posicion"][0] - element[0]
            suma2= d.jugador["posicion"][1] - element[1]
            suma3 = abs(suma1 + suma2)
            lista_arboles.append(suma3)

    for i in range(len(lista_arboles)-1):

        for j in range(len(lista_arboles)-1-i):

            if lista_arboles[j] > lista_arboles[j+1]:

                lista_arboles[j], lista_arboles[j+1] = lista_arboles[j+1],lista_arboles[j]
                d.dades["death"]["arboles"][j], d.dades["death"]["arboles"][j+1] = d.dades["death"]["arboles"][j+1],d.dades["death"]["arboles"][j]
    print(lista_arboles)
    
    element = d.dades["death"]["arboles"][0]
        
    print([element])
    if d.mapaActual[element[0]-1][element[1]] == " ": #Comprueba si esta libre arriba

        d.jugador["posicion"][0] = element[0]
        d.jugador["posicion"][1] = element[1] 
        d.mapaActual[element[0]-1][element[1]] = "X"
        print(d.mapaActual)
    elif d.mapaActual[element[0]+1][element[1]] == " ": #Comprueba si esta libre abajo

        d.jugador["posicion"][0] = element[0]+1
        d.jugador["posicion"][1] = element[1] 
        d.mapaActual[element[0]+1][element[1]] = "X"
        print(d.mapaActual)
    
    elif d.mapaActual[element[0]][element[1]-1] == " ": #Comprueba si esta libre izquierda

        d.jugador["posicion"][0] = element[0]
        d.jugador["posicion"][1] = element[1]+1
        d.mapaActual[element[0]][element[1]-1] = "X"
        print(d.mapaActual)

    elif d.mapaActual[element[0]][element[1]+1] == " ": #Comprueba si esta libre derecha

        d.jugador["posicion"][0] = element[0]
        d.jugador["posicion"][1] = element[1] -1
        d.mapaActual[element[0]][element[1]+1] = "X"
        print(d.mapaActual)
    else:
        print("Invalid Action") 


movimientoCercano("Go to T")
f.obtenerMapa(d.mapaActual,d.jugador["posicion"])