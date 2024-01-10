import funciones.datos as d
import random
mapaActual = []

def mostrarInventario():
    '''
    if Select.lower() == "show inventory main":
    '''  
    inventario = [" * * * * Inventory * \n",
                        "*\n".rjust(21),
                        " Link".ljust(12) + "  {0}/{1}".format(d.vidas,d.vidas_max).rjust(6) + " * \n",
                        " Blod Moon in ".ljust(10) + "  {0}".format(25).rjust(4) + " * \n",
                        "* \n".rjust(22),
                        " Equipement ".ljust(19) + "* \n",
                         "{0}".format(d.escudo_actual).rjust(18) + " * \n",
                         "{0}".format(d.arma_actual).rjust(18) + " * \n",
                         
                         "* \n".rjust(22),
                         " Food".ljust(15) + "{0}".format(5).rjust(3) +  " *\n",
                         " Weapons".ljust(15) + "{0}".format(5).rjust(3) +  " *\n",
                         "* \n".rjust(22),
                        " * * * * * * * * * *"]
    return inventario
    '''
    elif Select.lower() == "Show inventory Food":

        inventario = [" * * * * * *  Food * \n",
                        "*\n".rjust(21),
                        "*\n".rjust(21),
                        " Vegetables".ljust(16) + "10".rjust(2) + " * \n",
                         " Fish".ljust(16) + "10".rjust(2) + " * \n",
                         " Meat".ljust(16) + "10".rjust(2) + " * \n",
                         "* \n".rjust(22),
                         " Salads".ljust(16) + "10".rjust(2) + " * \n",
                         " Pescatarian".ljust(16) + "10".rjust(2) + " * \n",
                         " Roasted".ljust(16) + "10".rjust(2) + " * \n",
                         "*\n".rjust(21),
                        " * * * * * * * * * *"]

        return inventario

    elif Select.lower() == "Show inventory Weapons":
    '''
    inventario = [" * * * * *  Weapons * \n",
                    "*\n".rjust(22),
                    "*\n".rjust(22),
                    " Wood Sword" + "{0}".format(5/2).rjust(8) + " * \n"]
                    
    if d.arma_actual == "Wood Sword":
            
            inventario += "  (equiped)" + "*\n".rjust(11)," Sword" + "{0}".format("5/2").rjust(13) + " * \n",
    else:
            inventario += "* \n".rjust(23)," Sword" + "{0}".format("5/2").rjust(13) + " * \n",

    if d.arma_actual == "Sword":
            
            inventario += "  (equiped)" + "*\n".rjust(11)," Wood shield" + "{0}".format("5/2").rjust(7) + " * \n",
    else:
            inventario += "* \n".rjust(23)," Wood shield" + "{0}".format("5/2").rjust(7) + " * \n",              

    if d.escudo_actual == "Swood Shield":
            
            inventario += "  (equiped)" + "*\n".rjust(11)," Shield" + "{0}".format("5/2").rjust(12) + " * \n",
    else:
            inventario += "* \n".rjust(23)," Shield" + "{0}".format("5/2").rjust(12) + " * \n",          
                        
    if d.escudo_actual == "Shield":
            
            inventario += "  (equiped)" + "*\n".rjust(11),"* \n".rjust(22)," * * * * * * * * * *"
    else:
            inventario += "* \n".rjust(23),"*\n".rjust(8),"* \n".rjust(22)," * * * * * * * * * *"                          
                    
    return inventario                
    '''
  

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
        
        diccionario[objeto] = {"nombre": "Vegetable" }

    elif  objeto == "salad":
        
        diccionario[objeto] = {"nombre": "salad" }
    
    elif  objeto == "pescatarian":
        
        diccionario[objeto] = {"nombre": "pescatarian" }
    
    elif objeto == "roasted":
        
        diccionario[objeto] = {"nombre": "roasted" }


A esta función le pasamos los datos del mapa en cuestion y los copia en otra variable para poder editar este segundo mapa sin que el original se vea afectado.'''
def obtenerMapa(playermap,posicionplayer):
    mapa = ""
    mapaActual = []
    for element1 in playermap:
            '''Lo hacemos de este modo porque si aplicamos el copy sobre la lista general del mapa, al modificar las listas internas que corresponden
                a cada una de las lineas del mapa, el mapa original si que se ve afectado.'''
            mapaActual.append(element1.copy())
    mapaActual = introducirUserInicial(posicionplayer,mapaActual)
    imprimirmapa(mapaActual)
    return mapaActual

def introducirUserInicial(posicionUser, playermap):

    playermap[posicionUser[0]][posicionUser[1]] = "X"
    return playermap



            
def imprimirmapa(mapaActual):
    mapa = ""
    contadorInventario = 0
    for element in mapaActual:

        for element1 in element:
                mapa += element1
                
        

        mapa += d.inventario1[contadorInventario]
        
        if contadorInventario < 11:
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
        
        if posicionplayer[0] + int(select[8:]) > len(mapaActual)-2:

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

                       
      
#Menu aleatorio
def menu_random():
    menu_aleatorio = random.randint(1, 3)
    if menu_aleatorio == 1:
        map = d.principal1

    elif menu_aleatorio == 2:
        map = d.principal2

    elif menu_aleatorio == 3:
        map = d.principal3

    return map





def menu_principal():
    game = True
    while game == True:
        for i in playmap: #Imprimir menu
            print(i[0])
        opc = input() #Guardar la opcion
        if opc.lower() == "continue": #Si se elige continuar partida
            print("Continue")

        elif opc.lower() == "new game": #Si se elige nueva partida
            funcion_new_game()

        elif opc.lower() == "help": #Si se elige la opcion help se ira a la pantalla de help, main menu
            help(d.help_main)

        elif opc.lower() == "about": #Si se elige la opción about se ira a la pantalla about
            help(d.about_main)

        elif opc.lower() == "exit": #Si la opción es exit se sale del juego.
            game = False

        else: #Cuando la opcion sea incorrecta se mostrara que la opción es invalida
            print("Invalid Option")


def funcion_new_game():
    back = True
    name = ""
    while back == True:  # Mientras no se de la orden de volver atrás
        for i in d.new_game:  # Imprimir pantalla de nueva partida
            print(i[0])
        opc = input()  # Guardar la opcion
        if opc.lower() == "help":  # Si se elige la opcion Help
            help(d.help_new_game)

        elif opc.lower() == "back":  # Si se da la orden de volver atrás se sale del bucle
            back = False


        elif opc.lower() == "":  # Si no se escribe nada se asigna el nombre Link
            name = "Link"
            print("Welcome to the game", name)

        elif opc.lower().replace(" ", "").isalnum() and len(opc) >= 3 and len(opc) <= 10:  # Cuando el nombre sea correcto se guarda
            name = opc
            print("Welcome to the game", name)

        else:  # Si es una opcion invalida se imprime escribe que no es valido
            print(opc, "Is not a valid name")

        if name != "":  # Si el nombre ha sido cambiado se ira a la pestaña de legend
            for i in d.legend:  # Se imprime la leyenda
                print(i[0])
            opc = input()  # Se guarda la opcion

            while opc.lower() != "continue":
                print("Invalid Option")
                opc = input()

            if opc.lower() == "continue":  # Si se elige continue pasamos a la pantalla de plot
                for i in d.plot:  # Se imprime la pantalla de plot
                    print(i[0])
                opc = input()


def help(mapa):
    for i in mapa:  # Se imprime la pantalla de ayuda
        print(i[0])
    back_help = True
    while back_help == True:  # Mientras no se de la orden de volver atrás
        opc = input()  # Guardar la opcion
        if opc.lower() == "back":  # Si se elige la opcion de volver atrás se sale del bucle
            back_help = False

        else:  # Si la opcion es incorrecta se imprime invalid option
            print("Invalid Option")

       
       
       
       
def añadirInventario(objeto, diccionario):

        numeroRandom = "" 

        for i in range(3):

            numeroRandom += str(random.randint(0,20))

        if objeto == "Wood Sword":
            
            diccionario[objeto + numeroRandom] = {"nombre": "Wood Sword", "Usos": 5 }
            
        elif objeto == "Wood Shield":
        
            diccionario[objeto + numeroRandom] = {"nombre": "Wood Shield", "Usos": 5 }
        
        elif objeto == "Shield":
            
            diccionario[objeto + numeroRandom] = {"nombre": "Shield", "Usos": 9 }
            
        
        elif objeto == "Sword":
            
            diccionario[objeto + numeroRandom] = {"nombre": "Sword", "Usos": 9 }

        elif objeto == "Vegetable":
            
            diccionario[objeto + numeroRandom] = {"nombre": "Vegetable" }

        elif  objeto == "salad":
            
            diccionario[objeto + numeroRandom] = {"nombre": "salad" }
        
        elif  objeto == "pescatarian":
            
            diccionario[objeto + numeroRandom] = {"nombre": "pescatarian" }
        
        elif objeto == "roasted":
            
            diccionario[objeto + numeroRandom] = {"nombre": "roasted" }

        
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

             Select = Select[Select.find("Shield"): ]
    
    lista_dict = list(d.inventarioArmas.keys())
    

    if len(lista_dict)== 0:

        print ("No dispones de este arma en tu inventario.")

    for i in range(len(lista_dict)):
        for j in range(0, len(lista_dict)-i-1):
            if lista_dict[j]["usos"] > lista_dict[j+1]["usos"]:
                lista_dict[j]["usos"], lista_dict[j+1]["usos"] = lista_dict[j+1]["usos"], lista_dict[j]["usos"]

    if "Shield" in lista_dict[0]:

        d.jugador["escudo_actual"] = lista_dict[0]
    
    elif "Sword" in lista_dict[0]:

        d.jugador["arma_actual"] = lista_dict[0]