import funciones.datos as d
import random
mapaActual = []

def mostrarInventario(select):
    
    if select.lower() == "show inventory main":
    
        inventario = [" * * * * Inventory * \n",
                        "*\n".rjust(21),
                        " Link".ljust(12) + "  {0}/{1}".format(d.jugador["vidas"],d.jugador["vidas_max"]).rjust(6) + " * \n",
                        " Blod Moon in ".ljust(10) + "  {0}".format(25).rjust(4) + " * \n",
                        "* \n".rjust(22),
                        " Equipement ".ljust(19) + "* \n",
                         "{0}".format(d.jugador["escudo_actual"]).rjust(18) + " * \n",
                         "{0}".format(d.jugador["arma_actual"]).rjust(18) + " * \n",
                         
                         "* \n".rjust(22),
                         " Food".ljust(15) + "{0}".format(5).rjust(3) +  " *\n",
                         " Weapons".ljust(15) + "{0}".format(5).rjust(3) +  " *"
                         ]
                        
        return inventario
    
    elif select.lower() == "show inventory food":

        inventario = [" * * * * * *  Food * \n",
                        "*\n".rjust(21),
                        "*\n".rjust(21),
                        " Vegetables".ljust(16) + "10".rjust(2) + " * \n",
                         " Fish".ljust(16) + "10".rjust(2) + " * \n",
                         " Meat".ljust(16) + "10".rjust(2) + " * \n",
                         "* \n".rjust(22),
                         " Salads".ljust(16) + "10".rjust(2) + " * \n",
                         " Pescatarian".ljust(16) + "10".rjust(2) + " * \n",
                         " Roasted".ljust(16) + "10".rjust(2) + " *"]

        return inventario

    elif select.lower() == "show inventory weapons":
    
        inventario = [" * * * * *  Weapons * \n",
                    "*\n".rjust(22),
                    "*\n".rjust(22),
                    " Wood Sword" + "{0}".format("5/2").rjust(8) + " * \n"]
                    
        if d.jugador["arma_actual"] == "Wood Sword":
            
            inventario += "  (equiped)" + "*\n".rjust(11)," Sword" + "{0}".format("5/2").rjust(13) + " * \n",
        else:
            inventario += "* \n".rjust(23)," Sword" + "{0}".format("5/2").rjust(13) + " * \n",

        if d.jugador["arma_actual"] == "Sword":
            
            inventario += "  (equiped)" + "*\n".rjust(11)," Wood shield" + "{0}".format("5/2").rjust(7) + " * \n",
        else:
            inventario += "* \n".rjust(23)," Wood shield" + "{0}".format("5/2").rjust(7) + " * \n",              

        if d.jugador["escudo_actual"] == "Swood Shield":
            
            inventario += "  (equiped)" + "*\n".rjust(11)," Shield" + "{0}".format("5/2").rjust(12) + " * \n",
        else:
            inventario += "* \n".rjust(23)," Shield" + "{0}".format("5/2").rjust(12) + " * \n",          
                        
        if d.jugador["escudo_actual"] == "Shield":
            
            inventario += "  (equiped)" + "*\n".rjust(11),"*".rjust(22)
        else:
            inventario += "* \n".rjust(23),"*\n".rjust(8),"*".rjust(22)                          
                    
        return inventario                
   
  

def añadirInventario(objeto, diccionario):

    if objeto == "Wood Sword":
        
        diccionario[objeto] = {"nombre": "Wood Sword", "Usos": 5 }
        
    elif objeto == "Wood Shield":
    
        diccionario[objeto] = {"nombre": "Wood Shield", "Usos": 5 }
    
    elif objeto == "Shield":
        
        diccionario[objeto] = {"nombre": "Shield", "Usos": 9 }
        
    
    elif objeto == "Sword":
        
        diccionario[objeto] = {"nombre": "Sword", "Usos": 9 }

    elif objeto == "Vegetable":
        
        diccionario[objeto] += 1 
    elif objeto == "Fish":
        
        diccionario[objeto] += 1 
    elif objeto == "Meat":
        
        diccionario[objeto] += 1 
    elif  objeto == "Salad":
        
        diccionario[objeto] += 1 
    
    elif  objeto == "Pescatarian":
        
        diccionario[objeto] += 1 
    
    elif objeto == "Roasted":
        
        diccionario[objeto] += 1 

'''
A esta función le pasamos los datos del mapa en cuestion y los copia en otra variable para poder editar este segundo mapa sin que el original se vea afectado.'''
def obtenerMapa(playermap,posicionplayer):
    mapa = ""
    mapaActual = []
    for element1 in playermap:
            '''Lo hacemos de este modo porque si aplicamos el copy sobre la lista general del mapa, al modificar las listas internas que corresponden
                a cada una de las lineas del mapa, el mapa original si que se ve afectado.'''
            mapaActual.append(element1.copy())
    '''mapaActual = introducirUserInicial(posicionplayer,mapaActual)'''
    imprimirmapa(mapaActual)
    return mapaActual

def introducirUserInicial(posicionUser, playermap):

    playermap[posicionUser[0]][posicionUser[1]] = "X"
    return playermap

#inventario1 = mostrarInventario(d.select)
            
def imprimirmapa(mapaActual):
    mapa = ""
    contadorInventario = 0
    for element in mapaActual:

        for element1 in element:
                mapa += str(element1)
                
        

        mapa += mostrarInventario(d.select)[contadorInventario]
        
        if contadorInventario < 10:
            contadorInventario += 1
    
    print(mapa)
       

def moverPersonaje(mapaActual, select, posicionplayer):
    
    
    if select[0:7] == "go left":
        print(posicionplayer[1], posicionplayer[1] - int(select[8:]) )
        if posicionplayer[1] - int(select[8:]) < 0:
            
            return["Invalid action1"], posicionplayer[0], posicionplayer[1]
        else:
            int1 = posicionplayer[1]
            int2 = posicionplayer[1] - int(select[8:])
            diferent = True
           
            for i in range (int1, int2, -1):
                
                if int(select[8:]) == 1:

                    if mapaActual[posicionplayer[0]][i-1] != " ":
                        
                        return["Invalid action"], posicionplayer[0], posicionplayer[1]
                    
                    else:

                        mapaActual[posicionplayer[0]][posicionplayer[1] ] = " "
                        mapaActual[posicionplayer[0]][posicionplayer[1] - int(select[8:])] = "X"
                        return mapaActual, posicionplayer[0], posicionplayer[1] - int(select[8:])
                else:

                    if mapaActual[posicionplayer[0]][i-1] != " ":
                        
                        diferent = False
            if diferent == True:

                mapaActual[posicionplayer[0]][posicionplayer[1] ] = " "
                mapaActual[posicionplayer[0]][posicionplayer[1] - int(select[8:])] = "X"
                return mapaActual, posicionplayer[0], posicionplayer[1] - int(select[8:])        
            else:
                return["Invalid action"], posicionplayer[0], posicionplayer[1]
                       
                        

    elif select[0:8] == "go right":
       
        if posicionplayer[1] + int(select[8:]) > 57:
            

            return["Invalid action1"], posicionplayer[0], posicionplayer[1]
        else:
            int1 = posicionplayer[1]
            int2 = posicionplayer[1] + int(select[9:])
            diferent = True
            for i in range (int2, int1, -1):
                
                if int(select[9:]) == 1:

                    if mapaActual[posicionplayer[0]][i+1] != " ":
                        
                        return["Invalid action2"], posicionplayer[0], posicionplayer[1]
                    
                    
                else:

                    if mapaActual[posicionplayer[0]][i+1] != " ":
                        diferent = False
            
            if diferent == True:
       
                mapaActual[posicionplayer[0]][posicionplayer[1] ] = " "
                mapaActual[posicionplayer[0]][posicionplayer[1] + int(select[9:])] = "X"
                return mapaActual, posicionplayer[0], posicionplayer[1] + int(select[9:])
            else:
                return["Invalid action"], posicionplayer[0], posicionplayer[1]


    elif select[0:5] == "go up":

        if posicionplayer[0] - int(select[6:]) < 1:

            return["Invalid action1"], posicionplayer[0], posicionplayer[1]
        else:
            int1 = posicionplayer[0]
            int2 = posicionplayer[0] - int(select[6:])
            diferent = True
            for i in range (int1, int2, -1):
                
                if int(select [6:]) == 1:

                    if mapaActual[i-1][posicionplayer[1]] != " ":
                        
                        return["Invalid action2"], posicionplayer[0], posicionplayer[1]
                    
                    else:

                        mapaActual[posicionplayer[0]][posicionplayer[1] ] = " "
                        mapaActual[posicionplayer[0]- int(select[6:])][posicionplayer[1] ] = "X"
                        return mapaActual, posicionplayer[0]- int(select[6:]), posicionplayer[1]
                else:

                    if mapaActual[i-1][posicionplayer[1]] != " ":
                        
                        diferent=False
                    
            if diferent == True:
       
                mapaActual[posicionplayer[0]][posicionplayer[1] ] = " "
                mapaActual[posicionplayer[0]- int(select[6:])][posicionplayer[1] ] = "X"
                return mapaActual, posicionplayer[0]- int(select[6:]), posicionplayer[1]
            else:
                return["Invalid action"], posicionplayer[0], posicionplayer[1]

                   
    elif select[0:7] == "go down":
        
        if posicionplayer[0] + int(select[8:]) > len(mapaActual)-1:

            return["Invalid action1"], posicionplayer[0], posicionplayer[1]
        else:
            int1 = posicionplayer[0]
            int2 = posicionplayer[0] + int(select[8:])
            diferent = True
            for i in range (int1, int2):
                print(mapaActual[i+1][posicionplayer[1]])
                if int(select [8:]) == 1:

                    if mapaActual[i+1][posicionplayer[1]] != " ":
                        
                        return["Invalid action2"], posicionplayer[0], posicionplayer[1]
                    
                    else:

                        mapaActual[posicionplayer[0]][posicionplayer[1] ] = " "
                        mapaActual[posicionplayer[0]+ int(select[8:])][posicionplayer[1] ] = "X"
                        return mapaActual, posicionplayer[0]+ int(select[8:]), posicionplayer[1]
                else:

                    if mapaActual[i+1][posicionplayer[1]] != " ":
                        
                      if mapaActual[i-1][posicionplayer[1]] != " ":
                        
                        diferent=False
                    
            if diferent == True:
       
                mapaActual[posicionplayer[0]][posicionplayer[1] ] = " "
                mapaActual[posicionplayer[0]+ int(select[8:])][posicionplayer[1] ] = "X"
                return mapaActual, posicionplayer[0]+ int(select[8:]), posicionplayer[1]
            else:
                return["Invalid action"], posicionplayer[0], posicionplayer[1]

def movimientoCercano(Select):
    
    if Select[len(Select)-1].upper() == "T":

        lista_arboles = []

        for element in d.dades[d.jugador["mapa"]]["T"]["lista"]:

            suma1 =  d.jugador["posicion"][0] - element[0]
            suma2= d.jugador["posicion"][1] - element[1]
            suma3 = abs(suma1 + suma2)
            lista_arboles.append(suma3)

        for i in range(len(lista_arboles)-1):

            for j in range(len(lista_arboles)-1-i):

                if lista_arboles[j] > lista_arboles[j+1]:

                    lista_arboles[j], lista_arboles[j+1] = lista_arboles[j+1],lista_arboles[j]
                    d.dades[d.jugador["mapa"]]["T"]["lista"][j], d.dades[d.jugador["mapa"]]["T"]["lista"][j+1] = d.dades[d.jugador["mapa"]]["T"]["lista"][j+1],d.dades[d.jugador["mapa"]]["T"]["lista"][j]
        
        element = d.dades[d.jugador["mapa"]]["T"]["lista"][0]
            
        if d.localitzacions[d.jugador["mapa"]][element[0]][element[1]-1] == " ": #Comprueba si esta libre izquierda

            d.jugador["posicion"][0] = element[0]
            d.jugador["posicion"][1] = element[1]+1
            d.localitzacions[d.jugador["mapa"]][element[0]][element[1]-1] = "X"

        elif d.localitzacions[d.jugador["mapa"]][element[0]][element[1]+1] == " ": #Comprueba si esta libre derecha

            d.jugador["posicion"][0] = element[0]
            d.jugador["posicion"][1] = element[1]-1
            d.localitzacions[d.jugador["mapa"]][element[0]][element[1]+1] = "X"

        elif d.localitzacions[d.jugador["mapa"]][element[0]-1][element[1]] == " ": #Comprueba si esta libre arriba

            d.jugador["posicion"][0] = element[0]-1
            d.jugador["posicion"][1] = element[1] 
            d.localitzacions[d.jugador["mapa"]][element[0]-1][element[1]] = "X"

        elif d.localitzacions[d.jugador["mapa"]][element[0]+1][element[1]] == " ": #Comprueba si esta libre abajo

            d.jugador["posicion"][0] = element[0]+1
            d.jugador["posicion"][1] = element[1] 
            d.localitzacions[d.jugador["mapa"]][element[0]+1][element[1]] = "X"

    if Select[len(Select)-1].upper() == "F":

        if d.visibilidad_zorro == False:
            d.texto_prompt.append("Invalid option")

        else:

            element = d.dades[d.jugador["mapa"]]["F"]["posicion"]
                
            if d.localitzacions[d.jugador["mapa"]][element[0]][element[1]-1] == " ": #Comprueba si esta libre izquierda
                d.jugador["posicion"][0] = element[0]
                d.jugador["posicion"][1] = element[1]+1
                d.localitzacions[d.jugador["mapa"]][element[0]][element[1]-1] = "X"

            elif d.localitzacions[d.jugador["mapa"]][element[0]][element[1]+1] == " ": #Comprueba si esta libre derecha

                d.jugador["posicion"][0] = element[0]
                d.jugador["posicion"][1] = element[1]-1
                d.localitzacions[d.jugador["mapa"]][element[0]][element[1]+1] = "X"

            elif d.localitzacions[d.jugador["mapa"]][element[0]-1][element[1]] == " ": #Comprueba si esta libre arriba

                d.jugador["posicion"][0] = element[0]
                d.jugador["posicion"][1] = element[1]-1
                d.localitzacions[d.jugador["mapa"]][element[0]-1][element[1]] = "X"

            elif d.localitzacions[d.jugador["mapa"]][element[0]+1][element[1]] == " ": #Comprueba si esta libre abajo

                d.jugador["posicion"][0] = element[0]+1
                d.jugador["posicion"][1] = element[1] 
                d.localitzacions[d.jugador["mapa"]][element[0]+1][element[1]] = "X"
    
    if Select[len(Select)-2].upper() == "S":

        for i in range(len(d.dades[d.jugador["mapa"]]["Santuarios"]["posicion"])):

            if d.dades[d.jugador["mapa"]]["Santuarios"]["posicion"][i][2] == Select[len(Select)-2:]:
                
                element = d.dades[d.jugador["mapa"]]["Santuarios"]["posicion"][i]
                    
                if d.localitzacions[d.jugador["mapa"]][element[0]][element[1]-1] == " ": #Comprueba si esta libre izquierda

                    d.jugador["posicion"][0] = element[0]
                    d.jugador["posicion"][1] = element[1]+1
                    d.localitzacions[d.jugador["mapa"]][element[0]][element[1]-1] = "X"

                elif d.localitzacions[d.jugador["mapa"]][element[0]][element[1]+1] == " ": #Comprueba si esta libre derecha

                    d.jugador["posicion"][0] = element[0]
                    d.jugador["posicion"][1] = element[1] -1
                    d.localitzacions[d.jugador["mapa"]][element[0]][element[1]+1] = "X"

                elif d.localitzacions[d.jugador["mapa"]][element[0]-1][element[1]] == " ": #Comprueba si esta libre arriba

                    d.jugador["posicion"][0] = element[0]
                    d.jugador["posicion"][1] = element[1]-1
                    d.localitzacions[d.jugador["mapa"]][element[0]-1][element[1]] = "X"

                elif d.localitzacions[d.jugador["mapa"]][element[0]+1][element[1]] == " ": #Comprueba si esta libre abajo

                    d.jugador["posicion"][0] = element[0]+1
                    d.jugador["posicion"][1] = element[1] 
                    d.localitzacions[d.jugador["mapa"]][element[0]+1][element[1]] = "X"


    if Select[len(Select)-5:].lower() == "water":

        lista_agua = []

        for element in d.dades[d.jugador["mapa"]]["~"]["posicion"]:

            suma1 =  d.jugador["posicion"][0] - element[0]
            suma2= d.jugador["posicion"][1] - element[1]
            suma3 = abs(suma1 + suma2)
            lista_agua.append(suma3)

        for i in range(len(lista_agua)-1):

            for j in range(len(lista_agua)-1-i):

                if lista_agua[j] > lista_agua[j+1]:

                    lista_agua[j], lista_agua[j+1] = lista_agua[j+1],lista_agua[j]
                    d.dades[d.jugador["mapa"]]["~"]["posicion"][j], d.dades[d.jugador["mapa"]]["~"]["posicion"][j+1] = d.dades[d.jugador["mapa"]]["~"]["posicion"][j+1],d.dades[d.jugador["mapa"]]["~"]["posicion"][j]
        
        element = d.dades[d.jugador["mapa"]]["~"]["posicion"][0]
            
        if d.localitzacions[d.jugador["mapa"]][element[0]][element[1]-1] == " ": #Comprueba si esta libre izquierda

            d.jugador["posicion"][0] = element[0]
            d.jugador["posicion"][1] = element[1]+1
            d.localitzacions[d.jugador["mapa"]][element[0]][element[1]-1] = "X"

        elif d.localitzacions[d.jugador["mapa"]][element[0]][element[1]+1] == " ": #Comprueba si esta libre derecha

            d.jugador["posicion"][0] = element[0]
            d.jugador["posicion"][1] = element[1] -1
            d.localitzacions[d.jugador["mapa"]][element[0]][element[1]+1] = "X"

        elif d.localitzacions[d.jugador["mapa"]][element[0]-1][element[1]] == " ": #Comprueba si esta libre arriba

            d.jugador["posicion"][0] = element[0]
            d.jugador["posicion"][1] = element[1]-1
            d.localitzacions[d.jugador["mapa"]][element[0]-1][element[1]] = "X"

        elif d.localitzacions[d.jugador["mapa"]][element[0]+1][element[1]] == " ": #Comprueba si esta libre abajo

            d.jugador["posicion"][0] = element[0]+1
            d.jugador["posicion"][1] = element[1] 
            d.localitzacions[d.jugador["mapa"]][element[0]+1][element[1]] = "X"


def moverPersonajeGanon(mapaActual, select, posicionplayer):
    
    
    if select[0:7] == "go left":
        print(posicionplayer[1], posicionplayer[1] - int(select[8:]) )
        if posicionplayer[1] - int(select[8:]) < 0:
            
            return["Invalid action1"], posicionplayer[0], posicionplayer[1]
        else:
            int1 = posicionplayer[1]
            int2 = posicionplayer[1] - int(select[8:])
            diferent = True
           
            for i in range (int1, int2, -1):
                
                if int(select[8:]) == 1:

                    if mapaActual[posicionplayer[0]][i-1] != " ":
                        
                        return["Invalid action"], posicionplayer[0], posicionplayer[1]
                    
                    else:

                        mapaActual[posicionplayer[0]][posicionplayer[1] ] = " "
                        mapaActual[posicionplayer[0]][posicionplayer[1] - int(select[8:])] = "X"
                        return mapaActual, posicionplayer[0], posicionplayer[1] - int(select[8:])
                else:

                    if mapaActual[posicionplayer[0]][i-1] != " ":
                        
                        diferent = False
            if diferent == True:

                mapaActual[posicionplayer[0]][posicionplayer[1] ] = " "
                mapaActual[posicionplayer[0]][posicionplayer[1] - int(select[8:])] = "X"
                return mapaActual, posicionplayer[0], posicionplayer[1] - int(select[8:])        
            else:
                return["Invalid action"], posicionplayer[0], posicionplayer[1]
                       

    elif select[0:8] == "go right":
       
        if posicionplayer[1] + int(select[8:]) > 57:
            

            return["Invalid action1"], posicionplayer[0], posicionplayer[1]
        else:
            int1 = posicionplayer[1]
            int2 = posicionplayer[1] + int(select[9:])
            diferent = True
            for i in range (int2, int1, -1):
                
                if int(select[9:]) == 1:

                    if mapaActual[posicionplayer[0]][i+1] != " ":
                        
                        return["Invalid action2"], posicionplayer[0], posicionplayer[1]
                    
                    
                else:

                    if mapaActual[posicionplayer[0]][i+1] != " ":
                        diferent = False
            
            if diferent == True:
       
                mapaActual[posicionplayer[0]][posicionplayer[1] ] = " "
                mapaActual[posicionplayer[0]][posicionplayer[1] + int(select[9:])] = "X"
                return mapaActual, posicionplayer[0], posicionplayer[1] + int(select[9:])
            else:
                return["Invalid action"], posicionplayer[0], posicionplayer[1]


#Menu aleatorio
def menu_random():
    menu_aleatorio = random.randint(1, 3)
    map = []
    if menu_aleatorio == 1:
        map = d.diccionarioMenuPrincipal["principal1"]

    elif menu_aleatorio == 2:
        map = d.diccionarioMenuPrincipal["principal2"]

    elif menu_aleatorio == 3:
        map = d.diccionarioMenuPrincipal["principal3"]

    return map



def menu_principal():
    menu_inicial = menu_random()
    menu = True
    salir = False
    while salir == False:
        while menu == True:
            limpiar_pantalla()
            imprimirmapa_menu(menu_inicial)
            prompt()
            opc = input("What to do now? ") #Guardar la opcion
            if opc.lower() == "continue": #Si se elige continuar partida
                back = False
                while back == False:
                    limpiar_pantalla()
                    imprimir_partidas_guardadas()
                    prompt()
                    opc = input("What to do now? ")
                    
                    if opc.lower() == "help":
                        limpiar_pantalla()
                        help(d.diccionarioMenuPrincipal["help_saved_games"])
                    
                    elif opc.lower() == "back":
                        back = True

                    elif opc[:4].lower() == "play":
                        if opc[5].isdigit():
                            guardado = False
                            for i in d.datosPartidas:
                                if i[0] == int(opc[5]):
                                    # cargar los datos guardados
                                    #selectAndChargePartida(opc[5])
                                    # Funcion para guardar que tiene jorge en su rama
                                    guardado = True
                            
                            if guardado == False:
                                d.texto_prompt.append("Invalid option")  
                        
                        else:
                            d.texto_prompt.append("Invalid option")
                    
                    elif opc[:5].lower() == "erase": 
                        if opc[6].isdigit():
                            eliminado = False
                            for i in d.datosPartidas:
                                if i[0] == int(opc[6]):
                                    # eliminar los datos guardados
                                    d.datosPartidas.remove(i) 
                                    eliminado = True
                                    if len(d.datosPartidas) == 0:
                                        d.datosPartidas.append("No hay partidas guardadas, inicia una nueva.")
                            
                            if eliminado == False:
                                d.texto_prompt.append("Invalid option")  
                        
                        else:
                            d.texto_prompt.append("Invalid option") 
                    
                    else:
                        d.texto_prompt.append("Invalid option")      
                

            elif opc.lower() == "new game": #Si se elige nueva partida
                salir = funcion_new_game()
                if salir == True:
                    return True

            elif opc.lower() == "help": #Si se elige la opcion help se ira a la pantalla de help, main menu
                help(d.diccionarioMenuPrincipal["help_main"])

            elif opc.lower() == "about": #Si se elige la opción about se ira a la pantalla about
                help(d.diccionarioMenuPrincipal["about_main"])

            elif opc.lower() == "exit": #Si la opción es exit se sale del juego.
                salir = True
                return False

            else: #Cuando la opcion sea incorrecta se mostrara que la opción es invalida
                d.texto_prompt.append("Invalid Option")


def funcion_new_game():
    back = True
    salir = False
    while salir == False:
        while back == True:  # Mientras no se de la orden de volver atrás
            limpiar_pantalla()
            imprimirmapa_menu(d.diccionarioMenuPrincipal["new_game"]) # Imprimir pantalla de nueva partida
            prompt()
            opc = input("What to do now? ")  # Guardar la opcion
            if opc.lower() == "help":  # Si se elige la opcion Help
                help(d.diccionarioMenuPrincipal["help_new_game"])

            elif opc.lower() == "back":  # Si se da la orden de volver atrás se sale del bucle
                back = False
                salir = True
                return False

            elif opc.lower() == "":  # Si no se escribe nada se asigna el nombre Link
                d.jugador["nombre"] = "Link" # Modificar variable name
                d.texto_prompt.append("Welcome to the game Link")
                salir = before_game()
                return True

            elif opc.lower().replace(" ", "").isalnum() and len(opc) >= 3 and len(opc) <= 10:  # Cuando el nombre sea correcto se guarda
                d.jugador["nombre"] = opc # Modificar variable name
                d.texto_prompt.append("Welcome to the game " + d.jugador['nombre'])
                salir = before_game()
                return True

            else:  # Si es una opcion invalida se imprime escribe que no es valido
                d.texto_prompt.append(opc + " Is not a valid name")


def help(mapa):
    back_help = True
    while back_help == True:  # Mientras no se de la orden de volver atrás
        limpiar_pantalla()
        imprimirmapa_menu(mapa)  # Se imprime la pantalla de ayuda
        prompt()
        opc = input("What to do now? ")  # Guardar la opcion
        if opc.lower() == "back":  # Si se elige la opcion de volver atrás se sale del bucle
            back_help = False

        else:  # Si la opcion es incorrecta se imprime invalid option
            d.texto_prompt.append("Invalid Option")

def before_game():
    limpiar_pantalla()
    imprimirmapa_menu(d.diccionarioMenuPrincipal["legend"])  # Se imprime la leyenda
    prompt()
    opc = input("What to do now? ")  # Se guarda la opcion

    while opc.lower() != "continue":
        d.texto_prompt.append("Invalid action")
        limpiar_pantalla()
        imprimirmapa_menu(d.diccionarioMenuPrincipal["legend"])
        prompt()
        opc = input("What to do now? ")
        d.texto_prompt.append("Invalid action")

    limpiar_pantalla()
    imprimirmapa_menu(d.diccionarioMenuPrincipal["plot"]) # Se imprime la pantalla de plot        
    prompt()
    opc = input("What to do now? ")

    while opc.lower() != "continue":
        d.texto_prompt.append("Invalid action")
        limpiar_pantalla()
        imprimirmapa_menu(d.diccionarioMenuPrincipal["plot"])
        prompt()
        opc = input("What to do now? ")
    
    d.texto_prompt.append("The adventure begins")
    return True




def imprimirmapa_menu(mapa):
    if mapa == d.diccionarioMenuPrincipal["plot"]:
        mapa = [["* Plot  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"],
        ["*                                                                             *"],
        ["*                                                                             *"],
        ["*  Now history is repeating itself, and Princess Zelda has been captured by   *"],
        ["*  Ganon. He has taken over the Guardians and filled Hyrule with monsters.    *"],
        ["*                                                                             *"],
        ["*                                                                             *"],
        ["*  But a young man named {} has just awakened and".format(d.jugador["nombre"]).ljust(78)+"*"],
        ["*  must reclaim the Guardians to defeat Ganon and save Hyrule.                *"],
        ["*                                                                             *"],
        ["*                                                                             *"],
        ["* Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]]

    
    for i in mapa:
        print(i[0])
        
        
#--------------- Inventario ----------------------       

def añadirInventario(objeto, diccionario):

        numeroRandom = "" 

        for i in range(3):

            numeroRandom += str(random.randint(0,9))

        if objeto == "Wood Sword":
            
            diccionario[objeto + numeroRandom] = {"tipo": "Wood Sword", "Usos": 5 }
            
        elif objeto == "Wood Shield":
        
            diccionario[objeto + numeroRandom] = {"tipo": "Wood Shield", "Usos": 5 }
        
        elif objeto == "Shield":
            
            diccionario[objeto + numeroRandom] = {"tipo": "Shield", "Usos": 9 }
            
        
        elif objeto == "Sword":
            
            diccionario[objeto + numeroRandom] = {"tipo": "Sword", "Usos": 9 }

def equiparArma(Select):

    if len(d.inventarioArmas )== 0:

        print("No hay armas en el inventario")

    if Select.find("Wood Shield") != -1:

        if Select[Select.find("Wood Shield"): ]:

            Select = Select[Select.find("Wood Shield"): ]
    
    elif Select.find("Shield") != -1 and Select.find("Wood") == -1:

        if Select[Select.find("Shield"): ] :

             Select = Select[Select.find("Shield"): ]

    elif Select.find("Wood Sword") != -1:

        if Select[Select.find("Wood Sword"): ]:

            Select = Select[Select.find("Wood Shield"): ]

     
    elif Select.find("Sword") != -1 and Select.find("Wood") == -1:

        if Select[Select.find("Sword"): ] :

             Select = Select[Select.find("Sword"): ]
    
    lista_dict = list(d.inventarioArmas.keys())
    

    if len(lista_dict)== 0:

        print ("No dispones de este arma en tu inventario.")

    for i in range(len(lista_dict)):
        for j in range(0, len(lista_dict)-i-1):
            if lista_dict[j]["Usos"] > lista_dict[j+1]["Usos"]:
                lista_dict[j]["Usos"], lista_dict[j+1]["Usos"] = lista_dict[j+1]["Usos"], lista_dict[j]["Usos"]

    if "Shield" in lista_dict[0]:
        if d.jugador["escudo_actual"] == lista_dict[0]:
            return "You already have {lista_dict[0]} equiped"
        else:
            d.jugador["escudo_actual"] = lista_dict[0]
    
    elif "Sword" in lista_dict[0]:

        if d.jugador["arma_actual"] == lista_dict[0]:
            return "You already have {lista_dict[0]} equiped"
        else:
            d.jugador["escudo_actual"] = lista_dict[0]
            return "You already have {lista_dict[0]} equiped"
        
            
def desequiparArma(Select):

    if "Sword" in Select and (d.jugador["arma_actual"] != "" or d.jugador["arma_actual"] != " "):
        d.jugador["arma_actual"] = " "
        return "Espada desequipado."
    elif "Shield" in Select and (d.jugador["escudo_actual"] != "" or d.jugador["escudo_actual"] != " "):
        d.jugador["escudo_actual"] = " "
        return "Escudo desequipado."
    else:
        return "Este elemento no estaba equipado."
    

def conteoInventario():

    for element in d.inventarioArmas:

        if "Wood Shield" in element:
              d.dict_tipos["Wood Shield"]["total"] += 1
            
        elif  "Shield" in element and not "Wood" in element:

            d.dict_tipos["Shield"]["total"] += 1
        elif "Wood Sword" in element:

            d.dict_tipos["Wood Sword"]["total"] += 1        

        elif  "Sword" in element and not "Wood" in element:

            d.dict_tipos["Sword"]["total"] += 1

    for element1 in d.inventarioComida:

            if "vegetal" in d.inventarioComida[element1]["tipo"]:
                d.dict_tipos["Vegetables"]["total"] += 1
                
            elif  "Fish" in d.inventarioComida[element1]["tipo"]:
                d.dict_tipos["Fish"]["total"] += 1
                
            elif "Meat" in d.inventarioComida[element1]["tipo"]:

                d.dict_tipos["Meat"]["total"] += 1        

            elif  "Salads" in d.inventarioComida[element1]["tipo"]:

                d.dict_tipos["Salads"]["total"] += 1

            elif "Pescatarian" in d.inventarioComida[element1]["tipo"]:

                d.dict_tipos["Pescatarian"]["total"] += 1        

            elif  "Roasted" in d.inventarioComida[element1]["tipo"]:

                d.dict_tipos["Roasted"]["total"] += 1

#--------------- prompt ----------------------

def prompt(): #PROMPT
    while len(d.texto_prompt) > 8:
        d.texto_prompt.remove(d.texto_prompt[0]) #Remueve el primer mensaje
    for i in d.texto_prompt: #Imprime el promp
        print(i)

#--------------- Interaciones con los objetos del mapa ----------------------

def cesped(): #Interacion con el cesped
   porcentaje = random.randint(1,100)
   if porcentaje in range(1,10):#Si consigues una lagartija tine que salir esto en el promp y sumar uno de Meat
       d.texto_prompt.append("You got a lizard") 
       d.inventarioComida["Meat"] += 1
   else:
       d.texto_prompt.append("The grass didn't give you anything")

def arbol(): #Interacion con el arbol
    arbol_encontrado = 10
    for j in range(len(d.dades[d.jugador["mapa"]]["T"]["lista"])): #Busca en la lista del arbol cual esta cerca y que tenga toda la vida
        if d.jugador["posicion"][0] == d.dades[d.jugador["mapa"]]["T"]["lista"][j][0] and d.jugador["posicion"][1]-1 == d.dades[d.jugador["mapa"]]["T"]["lista"][j][1]:
            if not d.dades[d.jugador["mapa"]]["T"]["vida"][j] == 0:
                arbol_encontrado = j
        elif d.jugador["posicion"][0]-1 == d.dades[d.jugador["mapa"]]["T"]["lista"][j][0] and d.jugador["posicion"][1] == d.dades[d.jugador["mapa"]]["T"]["lista"][j][1]:
            if not d.dades[d.jugador["mapa"]]["T"]["vida"][j] == 0:
                arbol_encontrado = j
        elif d.jugador["posicion"][0] == d.dades[d.jugador["mapa"]]["T"]["lista"][j][0] and d.jugador["posicion"][1]+1 == d.dades[d.jugador["mapa"]]["T"]["lista"][j][1]:
            if not d.dades[d.jugador["mapa"]]["T"]["vida"][j] == 0:
                arbol_encontrado = j
        elif d.jugador["posicion"][0]+1 == d.dades[d.jugador["mapa"]]["T"]["lista"][j][0] and d.jugador["posicion"][1] == d.dades[d.jugador["mapa"]]["T"]["lista"][j][1]:
            if not d.dades[d.jugador["mapa"]]["T"]["vida"][j] == 0:
                arbol_encontrado = j
    if arbol_encontrado == 10: #si no encuentra nigun arbol con vida no te deja hacer nada
        d.texto_prompt.append("No trees available")
    else:
        porcentaje = random.randint(1,100)
        if d.jugador["arma_actual"] == " " or d.jugador["arma_actual"] == "" or not d.inventarioArmas[d.jugador["arma_actual"]]["tipo"] == "Sword": #compruba si cuando has atacado a sido con una espada o no
            if porcentaje in range(1,6): #Te da una espada de madera y tiene que salir un mensaje en el promp
                d.texto_prompt.append("You got a Wood sword")
                añadirInventario("Wood Sword",d.inventarioArmas)
            elif porcentaje in range(6,11): #Te da un escudo de madera y tiene que salir un mensaje en el promp
                d.texto_prompt.append("You got a Wood shield")
                añadirInventario("Wood Shield",d.inventarioArmas)
            elif porcentaje in range(11,51): #Te da una manzana y tiene que salir un mensaje en el promp
                d.texto_prompt.append("You got an apple")
                d.inventarioComida["Vegetables"] += 1
            else: #No te da nada y tiene que salir un mensaje en el promp
                d.texto_prompt.append("The tree didn't give you anything")
        else:
            if porcentaje in range(1,21): #Te da una espada de madera y tiene que salir un mensaje en el promp
                d.texto_prompt.append("You got a Wood sword")
                añadirInventario("Wood Sword",d.inventarioArmas)
                d.inventarioArmas[d.jugador["arma_actual"]]["Usos"] -= 1 #cuando atacas con la espda restas 1 de vida a la espada
                d.dades[d.jugador["mapa"]]["T"]["vida"][arbol_encontrado] -= 1 #Cuando atacas con la espda restas 1 de vida al arbol
            elif porcentaje in range(21,41): #Te da un escudo de madera y tiene que salir un mensaje en el promp
                d.texto_prompt.append("You got a Wood shield")
                añadirInventario("Wood Shield",d.inventarioArmas)
                d.inventarioArmas[d.jugador["arma_actual"]]["Usos"] -= 1 
                d.dades[d.jugador["mapa"]]["T"]["vida"][arbol_encontrado] -= 1
            elif porcentaje in range(41,81): #Te da una manzana y tiene que salir un mensaje en el promp
                d.texto_prompt.append("You got an apple")
                d.inventarioArmas[d.jugador["arma_actual"]]["Usos"] -= 1 
                d.dades[d.jugador["mapa"]]["T"]["vida"][arbol_encontrado] -= 1
                d.inventarioComida["Vegetables"] += 1
            else: #No te da nada y tiene que salir un mensaje en el promp
                d.texto_prompt.append("The tree didn't give you anything")
                d.inventarioArmas[d.jugador["arma_actual"]]["Usos"] -= 1 
                d.dades[d.jugador["mapa"]]["T"]["vida"][arbol_encontrado] -= 1
            if d.dades[d.jugador["mapa"]]["T"]["vida"][arbol_encontrado] == 0: #Cuando el arbol llega a 0 se cae y no aparece hasta dentro de 10 movimientos
                d.texto_prompt.append("The tree has fallen") #Este prom lo he añadido yo
                d.dades[d.jugador["mapa"]]["T"]["contador"][arbol_encontrado] == 10

def contador_arbol_mapa(mapaActual): #Cambia los arboles por su numero del contador 
    if d.jugador["mapa"] != "castle":
        for i in range(len(d.dades[d.jugador["mapa"]]["T"]["lista"])): #Busca que arbol tiene la vida al 0 y lo cambia por el numero del contador que tenga en ese momento
            if not d.dades[d.jugador["mapa"]]["T"]["vida"][i] == 0:
                mapaActual[d.dades[d.jugador["mapa"]]["T"]["lista"][i][0]][d.dades[d.jugador["mapa"]]["T"]["lista"][i][1]] = str(d.dades[d.jugador["mapa"]]["T"]["contador"][i])
    
    return mapaActual

def contador_arbol(mapaActual): #Baja el contador de todos los arboles
    if d.jugador["mapa"] != "castle":
        cont = 0
        for i in d.dades[d.jugador["mapa"]]["T"]["contador"]: #Mira si x arbol tiene más de 0 de contador 
            if i != 0: #Si es superior a 0 pues le resta uno
                d.dades[d.jugador["mapa"]]["T"]["contador"][cont] = i - 1
            else: #Sino le pone la vida al 4 y cambia el mapa para que tenga el arbol
                d.dades[d.jugador["mapa"]]["T"]["vida"][cont] == 4
                mapaActual[d.dades[d.jugador["mapa"]]["T"]["lista"][cont][0]][d.dades[d.jugador["mapa"]]["T"]["lista"][cont][1]] = "T"
            cont = cont + 1
    
    return mapaActual

def agua(): #Interacion con el agua #-Falata que reinicie lo del pez
    if d.pesca == True: #Comprueba si ya has conseguido un pez
        d.texto_prompt.append("There are no more fish") #-Este prom lo he añadido yo
    else:
        porcentaje = random.randint(1,100)
        if porcentaje in range(1,21): #Te da un pez, confirma que ya has conseguido un pez y te da un mensaje en el promp
            d.texto_prompt.append("You got a fish")
            d.dades 
            d.inventarioComida["Fish"] += 1
        else: #No te da nada y te escribe en el promp
            d.texto_prompt.append("You didn't get a fish")

def reiniciar_pesca():
    d.pesca = False

def zorro_visivilidad(): #Dice si el zorro sera visible o no
    porcentaje = random.randint(1,100)
    if porcentaje in range(1,51):
        d.visibilidad_zorro = True
        d.texto_prompt.append("You see a Fox")
    else:
        d.visibilidad_zorro = False
        d.texto_prompt.append("You don't see a Fox")
    
def zorro(): #Interacion con el zorro
    if d.visibilidad_zorro == False:
        d.texto_prompt.append("You don't see any fox")
    else:
        d.inventarioArmas[d.jugador["arma_actual"]]["Usos"] -= 1
        d.texto_prompt.append("You got meat")
        d.inventarioComida["Meat"] += 1


def cofre_cerrar_sword(): #Comprueba si en tu inventario tienes alguna espada
    if d.dades["hyrule"]["M"]["posicion"][0][2] == True and d.dades["gerudo"]["M"]["posicion"][0][2] == True and d.dades["gerudo"]["M"]["posicion"][1][2] == True:
        if d.dict_tipos["Sword"]["total"] == 0: #-mirar direcciones
            d.dades["hyrule"]["M"]["posicion"][0][2] = False
            d.localitzacions["hyrule"][d.dades["hyrule"]["M"]["posicion"][0][0]][d.dades["hyrule"]["M"]["posicion"][0][1]] = "M"
            d.dades["gerudo"]["M"]["posicion"][0][2] = False
            d.localitzacions["gerudo"][d.dades["gerudo"]["M"]["posicion"][0][0]][d.dades["gerudo"]["M"]["posicion"][0][1]] = "M"
            d.dades["gerudo"]["M"]["posicion"][1][2] = False
            d.localitzacions["gerudo"][d.dades["gerudo"]["M"]["posicion"][1][0]][d.dades["gerudo"]["M"]["posicion"][1][1]] = "M"

def cofre_cerrar_shield(): #Comprueba si en tu inventario tienes algun escudo
    if d.dades["necluda"]["M"]["posicion"][0][2] == True and d.dades["necluda"]["M"]["posicion"][1][2] == True and d.dades["necluda"]["M"]["posicion"][2][2] == True and d.dades["death"]["M"]["posicion"][0][2] == True and d.dades["death"]["M"]["posicion"][1][2] == True:
        if d.dict_tipos["Shield"]["total"] == 0: #-mirar direcciones
            d.dades["necluda"]["M"]["posicion"][0][2] = False
            d.localitzacions["necluda"][d.dades["necluda"]["M"]["posicion"][0][0]][d.dades["necluda"]["M"]["posicion"][0][1]] = "M"
            d.dades["necluda"]["M"]["posicion"][1][2] = False
            d.localitzacions["necluda"][d.dades["necluda"]["M"]["posicion"][1][0]][d.dades["necluda"]["M"]["posicion"][1][1]] = "M"
            d.dades["necluda"]["M"]["posicion"][2][2] = False
            d.localitzacions["necluda"][d.dades["necluda"]["M"]["posicion"][2][0]][d.dades["necluda"]["M"]["posicion"][2][1]] = "M"
            d.dades["death"]["M"]["posicion"][0][2] = False
            d.localitzacions["death"][d.dades["death"]["M"]["posicion"][0][0]][d.dades["death"]["M"]["posicion"][0][1]] = "M"
            d.dades["death"]["M"]["posicion"][1][2] = False
            d.localitzacions["death"][d.dades["death"]["M"]["posicion"][1][0]][d.dades["death"]["M"]["posicion"][1][1]] = "M"
                
                
def abrir_santuario(posicionplayer, mapaActual): #Interacion con el santuario
    posicion_igual = False
    for i in d.dades[d.jugador["mapa"]]["Santuarios"]["posicion"]:
        santuario = [i[0], i[1]]
        
        
        if [posicionplayer[0]+1, posicionplayer[1]] == santuario:
            posicion_igual = True
            if i[3] == True: #Comprueba si esta abierto
                d.texto_prompt.append("You already opened this sanctuary")
        
            else: #Lo abre y añade 1 de vida maxima y escribe en el prompt
                i[3] = True
                d.jugador["vidas_max"] = d.jugador["vidas_max"] + 1
                d.texto_prompt.append("You opened the sanctuary, your maximum health has increased by 1")
                mapaActual[i[0]][i[1]+2] = " "
        
        elif [posicionplayer[0]-1, posicionplayer[1]] == santuario:
            posicion_igual = True
            if i[3] == True: #Comprueba si esta abierto
                d.texto_prompt.append("You already opened this sanctuary")
                
            else: #Lo abre y añade 1 de vida maxima y escribe en el prompt
                i[3] = True
                d.jugador["vidas_max"] = d.jugador["vidas_max"] + 1
                d.texto_prompt.append("You opened the sanctuary, your maximum health has increased by 1")
                mapaActual[i[0]][i[1]+2] = " "
        
        elif [posicionplayer[0], posicionplayer[1]+1] == santuario:
            posicion_igual = True
            if i[3] == True: #Comprueba si esta abierto
                d.texto_prompt.append("You already opened this sanctuary")

            else: #Lo abre y añade 1 de vida maxima y escribe en el prompt
                i[3] = True
                d.jugador["vidas_max"] = d.jugador["vidas_max"] + 1
                d.texto_prompt.append("You opened the sanctuary, your maximum health has increased by 1")
                mapaActual[i[0]][i[1]+2] = " "
        
        elif [posicionplayer[0], posicionplayer[1]-1] == santuario:
            posicion_igual = True
            if i[3] == True: #Comprueba si esta abierto
                d.texto_prompt.append("You already opened this sanctuary")

            else: #Lo abre y añade 1 de vida maxima y escribe en el prompt
                i[3] = True
                d.jugador["vidas_max"] = d.jugador["vidas_max"] + 1
                d.texto_prompt.append("You opened the sanctuary, your maximum health has increased by 1")
                mapaActual[i[0]][i[1]+2] = " "
    
    if posicion_igual == False:
        d.texto_prompt.append("Invalid Option")
    

def cofre(): #Interacion con el cofre
    for j in range(len(d.dades[d.jugador["mapa"]]["M"]["posicion"])):
        if d.jugador["posicion"][0] == d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0] and d.jugador["posicion"][1]+1 == d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]:
            if d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] == True: #comprueba si el cofre ya esta abierto
                d.texto_prompt.append("The chest is now open") #Este prompt lo he puesto yo
            else:
                if d.jugador["mapa"] == ("hyrule" or "gerudo"): #Dependiendo del mapa te dara una espada o un escudo
                    d.texto_prompt.append("You got a sword")
                    d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] = True
                    d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]] = "W"
                    añadirInventario("Sword",d.inventarioArmas)
                else:
                    d.texto_prompt.append("You got a shield")
                    d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] = True
                    d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]] = "W"
                    añadirInventario("Shield",d.inventarioArmas)
        elif d.jugador["posicion"][0] == d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0] and d.jugador["posicion"][1]-1 == d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]:
            if d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] == True: #comprueba si el cofre ya esta abierto
                d.texto_prompt.append("The chest is now open") #Este prompt lo he puesto yo
            else:
                if d.jugador["mapa"] == ("hyrule" or "gerudo"): #Dependiendo del mapa te dara una espada o un escudo
                    d.texto_prompt.append("You got a sword")
                    d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] = True
                    d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]] = "W"
                    añadirInventario("Sword",d.inventarioArmas)
                else:
                    d.texto_prompt.append("You got a shield")
                    d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] = True
                    d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]] = "W"
                    añadirInventario("Shield",d.inventarioArmas)
        elif d.jugador["posicion"][0]+1 == d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0] and d.jugador["posicion"][1] == d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]:
            if d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] == True: #comprueba si el cofre ya esta abierto
                d.texto_prompt.append("The chest is now open") #Este prompt lo he puesto yo
            else:
                if d.jugador["mapa"] == ("hyrule" or "gerudo"): #Dependiendo del mapa te dara una espada o un escudo
                    d.texto_prompt.append("You got a sword")
                    d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] = True
                    d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]] = "W"
                    añadirInventario("Sword",d.inventarioArmas)
                else:
                    d.texto_prompt.append("You got a shield")
                    d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] = True
                    d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]] = "W"
                    añadirInventario("Shield",d.inventarioArmas)
        elif d.jugador["posicion"][0]-1 == d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0] and d.jugador["posicion"][1] == d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]:
            if d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] == True: #comprueba si el cofre ya esta abierto
                d.texto_prompt.append("The chest is now open") #Este prompt lo he puesto yo
            else:
                if d.jugador["mapa"] == ("hyrule" or "gerudo"): #Dependiendo del mapa te dara una espada o un escudo
                    d.texto_prompt.append("You got a sword")
                    d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] = True
                    d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]] = "W"
                    añadirInventario("Sword",d.inventarioArmas)
                else:
                    d.texto_prompt.append("You got a shield")
                    d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] = True
                    d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]] = "W"
                    añadirInventario("Shield",d.inventarioArmas)

def enemigos(): #Interacion con el enemigo
    if not (d.jugador["arma_actual"] == " " or d.jugador["arma_actual"] == ""): #compruba si tienes una espada
        d.texto_prompt.append("I can't attack if you don't have a sword")
    else:
        name = d.jugador["nombre"] 
        vidas = d.jugador["vidas"]
        d.jugador["vidas"]-= 1 #Te resta 1 de vida
        if d.jugador["vidas"] == 0:
            d.texto_prompt.append(f"{name} is dead")
        else:
            d.inventarioArmas[d.jugador["arma_actual"]]["Usos"] -= 1 #Le quita un uso a la espada
            d.texto_prompt.append(f"Brave, keep fighting {name}")
            d.texto_prompt.append(f"Be careful Link, you only have {vidas} hearts")
            for i in range(d.dades[d.jugador["mapa"]]["E"]["posicion"]):
                if d.jugador["posicion"][0] == d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0] and d.jugador["posicion"][1]+1 == d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]:
                    d.dades[d.jugador["mapa"]]["E"]["posicion"][i][3] -= 1 #Le resta 1 de vida al enemigo
                    if d.dades[d.jugador["mapa"]]["E"]["posicion"][i][3] == 0: #Comprueba si al enemigo a un le queda vida
                        d.texto_prompt.append("You defeated an enemy, this is a dangerous zone")
                    else:
                        salir = False
                        while not salir:
                            direccion1 = random.randint(1,2)
                            if direccion1 == 1: #Mira si modificara X o Y
                                direccion2= random.randint(1,2)
                                if direccion2 == 1: #Luego si es para izquierda o derecha o delante o atras
                                    if d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]+1] == " ":
                                        d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] = " "
                                        d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1] -= 1
                                        d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] = "E"
                                        salir = True
                                else:
                                    if d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]-1] == " ":
                                        d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] = " "
                                        d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1] += 1
                                        d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] = "E"
                                        salir = True
                            else:
                                direccion2= random.randint(1,2)
                                if direccion2 == 1:
                                    if d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]+1][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] == " ":
                                        d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] = " "
                                        d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0] -= 1
                                        d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] = "E"
                                        salir = True
                                else:
                                    if d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]-1][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] == " ":
                                        d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] = " "
                                        d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0] += 1
                                        d.localitzacions[d.jugador["mapa"]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] = "E"
                                        salir = True
                
def comer(select): #Interaccion de comer #-mirar las direcciones
    if d.jugador["vidas"] == d.jugador["vidas_max"]: #Comprueba si el personaje ya tiene lla vida maxima
        d.texto_prompt.append("You already have your whole life complete")
    else:
        if select == "Eat vegetable": #Comprueba si como un vegetal
            if d.dict_tipos["Vegetables"]["total"] < 0: #Comprueba si la comida que quieres esta en el inventario
                d.texto_prompt.append("You have no vegetables left")
            else: #Si tienes entonces te elimina 1 de comida y te añade la vida que necesites
                d.dict_tipos["Vegetables"]["total"] -= 1
                d.jugador["vidas"] += 1
                d.texto_prompt.append("You have increased 1 health and spent 1 vegetable")
        elif select == "Eat salad": #Comprueba si como un ensalada
            if d.dict_tipos["Salads"]["total"] < 0: #Comprueba si la comida que quieres esta en el inventario
                d.texto_prompt.append("You don't have any salad left")
            else:#Si tienes entonces te elimina 1 de comida y te añade la vida que necesites
                d.dict_tipos["Salads"]["total"] -= 1
                for i in range(2): #Para no pasarse de la vida maxima comprueba si ya esta en su maximo de vida o no
                    if not d.jugador["vidas"] == d.jugador["vidas_max"]:
                        d.jugador["vidas"] += 1
                d.texto_prompt.append("You have increased 2 health and spent 1 salad")
        elif select == "Eat pescatarian": #Comprueba si como un pescado
            if d.dict_tipos["Pescatarian"]["total"] < 0: #Comprueba si la comida que quieres esta en el inventario
                d.texto_prompt.append("You don't have any pescatarian left")
            else:#Si tienes entonces te elimina 1 de comida y te añade la vida que necesites
                d.dict_tipos["Pescatarian"]["total"] -= 1
                for i in range(3): #Para no pasarse de la vida maxima comprueba si ya esta en su maximo de vida o no
                    if not d.jugador["vidas"] == d.jugador["vidas_max"]:
                        d.jugador["vidas"] += 1
                d.texto_prompt.append("You have increased 3 health and spent 1 Pescatarian")
        elif select == "Eat roasted": #Comprueba si como una carne cocinada
            if d.dict_tipos["Roasted"]["total"] < 0: #Comprueba si la comida que quieres esta en el inventario
                d.texto_prompt.append("You don't have anything toasted")
            else:#Si tienes entonces te elimina 1 de comida y te añade la vida que necesites
                d.dict_tipos["Roasted"]["total"] -= 1
                for i in range(4): #Para no pasarse de la vida maxima comprueba si ya esta en su maximo de vida o no
                    if not d.jugador["vidas"] == d.jugador["vidas_max"]:
                        d.jugador["vidas"] += 1
                d.texto_prompt.append("You have increased 4 health and spent 1 roast")
        else: #Si no existe la comida que ha puesto sale este promp
            d.texto_prompt.append("This food does not exist") #Este promp lo he añadido yo    

#--------------- Cocinar ----------------------
     
def cocinar(receta, inventario): # Funcion para cocinar comida 
    if receta[5:].lower() == "salad": # Si se quiere cocinar una salad   

        if d.inventarioComida["Vegetables"] >= 2: # Si hay 2 o mas vegetables se puede hacer la salad
            aux = d.inventarioComida["Vegetables"]
            aux = aux - 1
            d.inventarioComida["Vegetables"] = aux # Eliminamos los dos vegetables del inventario
                
            d.texto_prompt.append("You cooked a salad successfully")
            añadirInventario("salad", inventario) # Añadimos salad al inventario
        
        else:
            d.texto_prompt.append("Not enough vegetable") # Si no hay mas 1 vegetable se imprime que no se puede cocinar la salad

    elif receta[5:].lower() == "pescatarian": # Si se elige cocinar el pescatarian
                
        if d.inventarioComida["Vegetables"] >= 1 and d.inventarioComida["Fish"] >= 1: # Si hay 1 fish y 1 vegetable se puede cocinar el pescatarian
            aux = d.inventarioComida["Vegetables"]
            aux = aux - 1
            d.inventarioComida["Vegetables"] = aux # Eliminamos los dos objetos del inventario
            aux2 = d.inventarioComida["Fish"]
            aux2 = aux2 - 1
            d.inventarioComida["Fish"] = aux2
            
            d.texto_prompt.append("You cooked a pescatarian successfully")
            añadirInventario("pescatarian", inventario) # Añadimos el pescatarian al inventario 
        
        elif d.inventarioComida["Vegetables"] < 1 and d.inventarioComida["Fish"] < 1: # Si no hay suficientes fish y vegetables se informa
            d.texto_prompt.append("Not enough vegetable and fish")
        
        elif d.inventarioComida["Vegetables"] < 1: # Si no hay suficientes vegetables se informa
            d.texto_prompt.append("Not enough vegetable")
        
        else: # Si no hay suficientes fish se informa
            d.texto_prompt.append("Not enough fish")

    elif receta[5:].lower() == "roasted": # Si se elige cocinar el roasted
                
        if d.inventarioComida["Vegetables"] >= 1 and d.inventarioComida["Meat"] >= 1:
            aux = d.inventarioComida["Vegetables"]
            aux = aux - 1
            d.inventarioComida["Vegetables"] = aux # Eliminamos los dos objetos del inventario
            aux2 = d.inventarioComida["Meat"]
            aux2 = aux2 - 1
            d.inventarioComida["Meat"] = aux2
            
            d.texto_prompt.append("You cooked a roasted successfully")
            añadirInventario("roasted", inventario) # Se añade el roasted al inventario
        
        elif d.inventarioComida["Vegetables"] < 1 and d.inventarioComida["Meat"] < 1: # Si no hay ni vegetable ni meat suficientes se informa
            d.texto_prompt.append("Not enough vegetable and meat")
        
        elif d.inventarioComida["Meat"] < 1: # Si no hay suficientes vegetables se informa
            d.texto_prompt.append("Not enough vegetable")
        
        else: # Si no hay suficientes meat se informa
            d.texto_prompt.append("Not enough meat")

    else: # Si lo que se quiere cocinar no existe, se muestra un mensaje de error
        d.texto_prompt.append("You can't cook", receta[5:])


def menuInferior(mapa):
    #Queda crear el diccionario donde ira el mapa actual
    posicion = d.jugador["posicion"]
    
    menuInferior = "* Exit, Show, Go, Eat"

    if posicion[0] == 10:
        if mapa[posicion[0]+1][posicion[1]] == "T" or mapa[posicion[0]+1][posicion[1]+1]  == "T" or mapa[posicion[0]+1][posicion[1]-1]  == "T" or mapa[posicion[0]][posicion[1]+1]  == "T" or mapa[posicion[0]][posicion[1]-1]  == "T":

            menuInferior += ", Attack"
    
    else:
        if mapa[posicion[0]+1][posicion[1]] == "T" or mapa[posicion[0]-1][posicion[1]] == "T" or mapa[posicion[0]+1][posicion[1]+1]  == "T" or mapa[posicion[0]+1][posicion[1]-1]  == "T" or mapa[posicion[0]][posicion[1]+1]  == "T" or mapa[posicion[0]][posicion[1]-1]  == "T" or mapa[posicion[0]-1][posicion[1]+1] or mapa[posicion[0]-1][posicion[1]-1]  == "T":

            menuInferior += ", Attack"

    '''
    if menuInferior.find("Attack") == -1:
    
        if d.jugador["mapaActual"][posicion[0]+1][posicion[1]][0] in  ("Z","E") or d.jugador["mapaActual"][posicion[0]-1][posicion[1]][0] in  ("Z","E") or d.jugador["mapaActual"][posicion[0]+1][posicion[1]+1][0]  in  ("Z","E") or d.jugador["mapaActual"][posicion[0]+1][posicion[1]-1][0]  in  ("Z","E") or d.jugador["mapaActual"][posicion[0]][posicion[1]+1][0]  in  ("Z","E") or d.jugador["mapaActual"][posicion[0]][posicion[1]-1][0]  in  ("Z","E") or d.jugador["mapaActual"][posicion[0]-1][posicion[1]+1][0]in  ("Z","E") or d.jugador["mapaActual"][posicion[0]-1][posicion[1]-1][0]  in  ("Z","E") and d.jugador["arma actual"] != " ":
            menuInferior += ", Attack"

    if d.jugador["mapaActual"][posicion[0]+1][posicion[1]][0] == "~" or d.jugador["mapaActual"][posicion[0]-1][posicion[1]][0]  == "~" or d.jugador["mapaActual"][posicion[0]+1][posicion[1]+1][0]   == "~" or d.jugador["mapaActual"][posicion[0]+1][posicion[1]-1][0]   == "~" or d.jugador["mapaActual"][posicion[0]][posicion[1]+1][0]   == "~" or d.jugador["mapaActual"][posicion[0]][posicion[1]-1][0]   == "~" or d.jugador["mapaActual"][posicion[0]-1][posicion[1]+1][0] == "~" or d.jugador["mapaActual"][posicion[0]-1][posicion[1]-1][0] == "~":
         menuInferior += ", Fish"
    
     if d.jugador["mapaActual"][posicion[0]+1][posicion[1]][0] == "S" or d.jugador["mapaActual"][posicion[0]-1][posicion[1]][0]  == "S" or d.jugador["mapaActual"][posicion[0]+1][posicion[1]+1][0]   == "S" or d.jugador["mapaActual"][posicion[0]+1][posicion[1]-1][0]   == "S" or d.jugador["mapaActual"][posicion[0]][posicion[1]+1][0]   == "S" or d.jugador["mapaActual"][posicion[0]][posicion[1]-1][0]   == "S" or d.jugador["mapaActual"][posicion[0]-1][posicion[1]+1][0] == "S" or d.jugador["mapaActual"][posicion[0]-1][posicion[1]-1][0] == "S":
     
        menuInferior += ", Open"
'''

    while  len(menuInferior) < 79:
        if len(menuInferior) %2 == 0:

            menuInferior += "*"
            menuInferior += " "
        else:
            menuInferior += " "
            menuInferior += "*"
    print (menuInferior)

#----------------- Mapa -------------------

def mostrar_mapa(): # Faltaria ver como implementar los santuarios, si es un diccionario o una lista
    santuarios_abiertos = []
    for i in d.dades:
        if i != "castle":
            matriz = d.dades[i]["Santuarios"]["posicion"]
            for j in matriz:
                if j[3] == True:
                    santuarios_abiertos.append(j[2] + "?")
            

    for linea in range(len(d.localitzacions["mapa_inicio"])-1): # Este for va comprueba los santuarios abiertos, si hay santuario abierto, en el mapa se elimina el interrogante que tiene al lado
        for elemento in range(len(d.localitzacions["mapa_inicio"][linea])):
            if d.localitzacions["mapa_inicio"][linea][elemento] in santuarios_abiertos:
                d.localitzacions["mapa_inicio"][linea][elemento] = d.localitzacions["mapa_inicio"][linea][elemento][:2] + " "
                


    mapa = "" # Imprimir el mapa de inicio
    for element in d.localitzacions["mapa_inicio"]:
        for element1 in element:
            mapa += element1
        mapa += "\n"

    limpiar_pantalla()
    print(mapa)
    prompt()

    back = True
    while back == True: # Hasta que no se de la orden de "back" no se sale del mapa
        opc = input("What to do now? ")
        while opc.lower() != "back":
            print("Invalid action")
            opc = input("What to do now? ")
        
        back = False


#----------------------- Frases Ganon ----------------

def frase_ganon():
    frase_rand = random.randint(1,10)

    print(d.frases_ganon[frase_rand-1])


#------------------------ Limpiar Pantalla ----------------

import os

def limpiar_pantalla():
    # Verifica el sistema operativo y ejecuta el comando correspondiente para limpiar la pantalla
    sistema_operativo = os.name
    if sistema_operativo == 'posix':  # Unix/Linux/Mac
        os.system('clear')
    elif sistema_operativo == 'nt':   # Windows
        os.system('cls')


#----------------------- Cambiar Mapa -------------------


def cambiar_mapa(select, mapaActual, posicionfallo): # Funcion para cambiar de mapa
    if select[6:].lower() == "hyrule":
        if mapaActual == d.localitzacions["death"] or mapaActual == d.localitzacions["gerudo"]:
            mapaActual = d.localitzacions["hyrule"]
            d.texto_prompt.append("You are now in" + select[6:])
            d.jugador["mapa"] = "hyrule"
            zorro_visivilidad() 
            reiniciar_pesca()
            posicion_player = d.dades["hyrule"]["position"]
            return mapaActual, posicion_player
        
        elif mapaActual == d.localitzacions["hyrule"]:
            d.texto_prompt.append("You already are in " + select[6:])
            return mapaActual
        
        else:
            d.texto_prompt.append("You can't go to" + select[6:] + " from here")
            return mapaActual

        
    elif select[6:].lower() == "gerudo":
        if mapaActual == d.localitzacions["hyrule"] or mapaActual == d.localitzacions["necluda"]:
            mapaActual = d.localitzacions["gerudo"]
            d.texto_prompt.append("You are now in " + select[6:])
            d.jugador["mapa"] = "gerudo"
            zorro_visivilidad() 
            reiniciar_pesca()
            posicion_player = d.dades["gerudo"]["position"]
            return mapaActual, posicion_player

        elif mapaActual == d.localitzacions["gerudo"]:
            d.texto_prompt.append("You already are in " + select[6:])
            return mapaActual
        
        else:
            d.texto_prompt.append("You can't go to " + select[6:] + " from here")
            return mapaActual
            
    elif select[6:].lower() == "death mountain":
        if mapaActual == d.localitzacions["hyrule"] or mapaActual == d.localitzacions["necluda"]:
            mapaActual = d.localitzacions["death"]
            d.texto_prompt.append("You are now in " + select[6:])
            d.jugador["mapa"] = "death"
            zorro_visivilidad()
            reiniciar_pesca() 
            posicion_player = d.dades["death"]["position"]
            return mapaActual, posicion_player
        
        elif mapaActual == d.localitzacions["death"]:
            d.texto_prompt.append("You already are in " + select[6:])
            return mapaActual
        
        else:
            d.texto_prompt.append("You can't go to " + select[6:] + " from here")
            return mapaActual
        
    elif select[6:].lower() == "necluda":
        if mapaActual == d.localitzacions["death"] or mapaActual == d.localitzacions["gerudo"]:
            mapaActual = d.localitzacions["necluda"]
            d.texto_prompt.append("You are now in " + select[6:])
            d.jugador["mapa"] = "necluda"
            zorro_visivilidad() 
            reiniciar_pesca()
            posicion_player = d.dades["necluda"]["position"]
            return mapaActual, posicion_player
        
        elif mapaActual == d.localitzacions["necluda"]:
            d.texto_prompt.append("You already are in " + select[6:])
            return mapaActual
        
        else:
            d.texto_prompt.append("You can't go to " + select[6:] + " from here")
            return mapaActual
        
    elif select[6:].lower() == "castle":
        if mapaActual == d.localitzacions["hyrule"]:
            d.mapa_anterior = "hyrule"

        elif mapaActual == d.localitzacions["gerudo"]:
            d.mapa_anterior = "gerudo"

        elif mapaActual == d.localitzacions["death"]:
            d.mapa_anterior = "death"
        
        elif mapaActual == d.localitzacions["necluda"]:
            d.mapa_anterior = "necluda"

        if d.win == False:
            d.jugador["mapa"] = "castle"
            mapaActual = d.localitzacions["castle"]
            d.texto_prompt.append("You are now in " + select[6:])
            posicion_player = d.dades["castle"]["position"]
            return mapaActual, posicion_player

        else:
            d.jugador["mapa"] = "castle_win"
            mapaActual = d.localitzacions["castle_win"]
            d.texto_prompt.append("You are now in " + select[6:])
            posicion_player = d.dades["castle"]["position"]
            return mapaActual, posicion_player
    
    else:
        d.texto_prompt.append("Invalid option")
        return mapaActual, posicionfallo
        
        
# Lo dejo comentado por si no da tiempo, no esta perfecto, hay que modificar algunas cosas     
'''def trucos(select):
    if select[0:22].lower() == "cheat rename player to":
        if select[23:].lower().replace(" ", "").isalnum() and len(select[23:]) >= 3 and len(select[23:]) <= 10:
            d.jugador["nombre"] = select[23:]
            d.texto_prompt.append("Name changed to " + d.jugador["nombre"])
        
        else:
            d.texto_prompt.append("Incorrect name")
    
    elif select.lower() == "cheat add vegetable":
        añadirInventario("Vegetable", d.inventarioComida)
    
    elif select.lower() == "cheat add fish":
        añadirInventario("Fish", d.inventarioComida)
    
    elif select.lower() == "cheat add meat":
        añadirInventario("Meat", d.inventarioComida)
        
    elif select.lower() == "cheat cook salad":
        cocinar("cook salad", d.inventarioComida)
        
    elif select.lower() == "cheat cook pescatarian":
        cocinar("cook pescatarian", d.inventarioComida)
        
    elif select.lower() == "cheat cook roasted":
        cocinar("cook roasted", d.inventarioComida)
        
    elif select.lower() == "cheat add wood sword":
        añadirInventario("Wood Sword", d.inventarioArmas)
    
    elif select.lower() == "cheat add sword":
        añadirInventario("Sword", d.inventarioArmas)
        
    elif select.lower() == "cheat add wood shield":
        añadirInventario("Wood Shield", d.inventarioArmas)
    
    elif select.lower() == "cheat add shield":
        añadirInventario("Shield", d.inventarioArmas)
    
    elif select.lower() == "cheat open sanctuaries":
        print("a") # Falta hacerlo
    
    elif select.lower() == "cheat game over":
        d.jugador["vidas"] = 0
        
    elif select.lower() == "cheat win game":
        d.ganon["vida"] = 0
    
    else:
        d.texto_prompt.append("Invalid option")'''
        
        

def imprimir_partidas_guardadas():
    saved_games = [["* Saved games * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]]
    
    if len(d.datosPartidas) > 1:
        for i in d.datosPartidas:
            saved_games.append(["* {}: {} {} - {}, {}".format(i[0], i[4], "18:37:15", i[1], i[9]).ljust(72) + "♥ {}/{} *".format(i[5], i[6])])
        
        while len(saved_games) != 11:
            saved_games.append(["* ".ljust(78) + "*"]) 
    
    elif len(d.datosPartidas) == 1 and type(d.datosPartidas[0]) == list:
        for i in d.datosPartidas:
            saved_games.append(["* {}: {} {} - {}, {}".format(i[0], i[4], "18:37:15", i[1], i[9]).ljust(72) + "♥ {}/{} *".format(i[5], i[6])])
        
        while len(saved_games) != 11:
            saved_games.append(["* ".ljust(78) + "*"])
    
    else:
        saved_games.append(["* {}".format(d.datosPartidas[0]).ljust(78) + "*"])
        
        while len(saved_games) != 11:
            saved_games.append(["* ".ljust(78) + "*"]) 
        
    saved_games.append(["* Play X, Erase X, Help, Back * * * * * * * * * * * * * * * * * * * * * * * * *"])
    
    imprimirmapa_menu(saved_games)




def atacar(posicionplayer, mapaActual, objeto):
    if mapaActual[posicionplayer[0]+1][posicionplayer[1]] == objeto:
        if objeto == "E":
            enemigos()
            return True
        
        elif objeto == "F":
            zorro()
            return True
        
        elif objeto == "T":
            arbol()
            return True
        
        elif objeto == " ":
            cesped()
            return True
        
            
    elif mapaActual[posicionplayer[0]-1][posicionplayer[1]] == objeto:
        if objeto == "E":
            enemigos()
            return True
        
        elif objeto == "F":
            zorro()
            return True
        
        elif objeto == "T":
            arbol()
            return True
        
        elif objeto == " ":
            cesped()
            return True
        
    elif mapaActual[posicionplayer[0]][posicionplayer[1]+1] == objeto:
        if objeto == "E":
            enemigos()
            return True
        
        elif objeto == "F":
            zorro()
            return True
        
        elif objeto == "T":
            arbol()
            return True
        
        elif objeto == " ":
            cesped()
            return True
        
    elif mapaActual[posicionplayer[0]][posicionplayer[1]-1] == objeto:
        if objeto == "E":
            enemigos()
            return True
        
        elif objeto == "F":
            zorro()
            return True
        
        elif objeto == "T":
            arbol()
            return True
        
        elif objeto == " ":
            cesped()
            return True

    else:
        return False