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

inventario1 = mostrarInventario(d.select)
            
def imprimirmapa(mapaActual):
    mapa = ""
    contadorInventario = 0
    for element in mapaActual:

        for element1 in element:
                mapa += element1
                
        

        mapa += inventario1[contadorInventario]
        
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
            d.texto_prompt.append("What to do now? " + opc)
            if opc.lower() == "continue": #Si se elige continuar partida
                print("Continue")

            elif opc.lower() == "new game": #Si se elige nueva partida
                salir = funcion_new_game()
                if salir == True:
                    return True

            elif opc.lower() == "help": #Si se elige la opcion help se ira a la pantalla de help, main menu
                help(d.diccionarioMenuPrincipal["help_main"])

            elif opc.lower() == "about": #Si se elige la opción about se ira a la pantalla about
                help(d.diccionarioMenuPrincipal["about_main"])

            elif opc.lower() == "exit": #Si la opción es exit se sale del juego.
                return False

            else: #Cuando la opcion sea incorrecta se mostrara que la opción es invalida
                d.texto_prompt.append("Invalid Option")


def funcion_new_game():
    back = True
    name = ""
    salir = False
    while salir == False:
        while back == True:  # Mientras no se de la orden de volver atrás
            limpiar_pantalla()
            imprimirmapa_menu(d.diccionarioMenuPrincipal["new_game"]) # Imprimir pantalla de nueva partida
            prompt()
            opc = input("What to do now? ")  # Guardar la opcion
            d.texto_prompt.append("What to do now? " + opc)
            if opc.lower() == "help":  # Si se elige la opcion Help
                help(d.diccionarioMenuPrincipal["help_new_game"])

            elif opc.lower() == "back":  # Si se da la orden de volver atrás se sale del bucle
                back = False
                salir = True
                return False

            elif opc.lower() == "":  # Si no se escribe nada se asigna el nombre Link
                d.name = "Link" # Modificar variable name
                d.texto_prompt.append("Welcome to the game " + d.name)
                salir = before_game()
                return True

            elif opc.lower().replace(" ", "").isalnum() and len(opc) >= 3 and len(opc) <= 10:  # Cuando el nombre sea correcto se guarda
                d.name = opc # Modificar variable name
                d.texto_prompt.append("Welcome to the game " + d.name)
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
        d.texto_prompt.append("What to do now? " + opc)
        if opc.lower() == "back":  # Si se elige la opcion de volver atrás se sale del bucle
            back_help = False

        else:  # Si la opcion es incorrecta se imprime invalid option
            d.texto_prompt.append("Invalid Option")

def before_game():
    limpiar_pantalla()
    imprimirmapa_menu(d.diccionarioMenuPrincipal["legend"])  # Se imprime la leyenda
    prompt()
    opc = input("What to do now? ")  # Se guarda la opcion
    d.texto_prompt.append("What to do now? " + opc)

    while opc.lower() != "continue":
        d.texto_prompt.append("Invalid Action")
        limpiar_pantalla()
        imprimirmapa_menu(d.diccionarioMenuPrincipal["plot"])
        prompt()
        opc = input("What to do now? ")
        d.texto_prompt.append("Invalid Action")

    limpiar_pantalla()
    imprimirmapa_menu(d.diccionarioMenuPrincipal["plot"]) # Se imprime la pantalla de plot        
    prompt()
    opc = input("What to do now? ")
    d.texto_prompt.append("What to do now? " + opc)

    while opc.lower() != "continue":
        d.texto_prompt.append("Invalid Action")
        limpiar_pantalla()
        imprimirmapa_menu(d.diccionarioMenuPrincipal["plot"])
        prompt()
        opc = input("What to do now? ")
        d.texto_prompt.append("What to do now? " + opc)
    
    d.texto_prompt.append("The adventure begins")
    return True




def imprimirmapa_menu(mapa):
    for i in mapa:
        print(i[0])
        
        
#--------------- Inventario ----------------------       

       
       

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

    if "Sword" in Select:
        d.jugador["arma_actual"] = " "
        return "Escudo desequipado."
    elif "Shield" in Select:
        d.jugador["arma_actual"] = " "
        return "Espada desequipado."
    else:
        return "Incorrect Option"
    

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
   if porcentaje in range(1,10):
       d.texto_prompt.append("You got a lizard") #Si consigues una lagartija tine que salir esto en el promp
       #-Falta hacer que se añada 1 de carne al inventario
   else:
       d.texto_prompt.append("The grass didn't give you anything")

def arbol(espada): #Interacion con el arbol
    #-Queda hacer lo de que aparezca despues de 10 movimientos
    #-Tambien hay que hacer en el mapa que cuando un arbol caiga un contador que ponga cuantos turnos falta para que se vulva a regenerar
    porcentaje = random.randint(1,100)
    if d.vida_arbol == 0: #
        d.texto_prompt.append("The tree is not ready yet")
    else:
        if d.espada == False: #compruba si cuando has atacado a sido con una espada o no
            if porcentaje in range(1,6): #Te da una espada de madera y tiene que salir un mensaje en el promp
                d.texto_prompt.append("You got a Wood sword")
                #-Falta hacer que se añada al inventario
            elif porcentaje in range(6,11): #Te da un escudo de madera y tiene que salir un mensaje en el promp
                d.texto_prompt.append("You got a Wood shield")
                #-Falta hacer que se añada al inventario
            elif porcentaje in range(11,51): #Te da una manzana y tiene que salir un mensaje en el promp
                d.texto_prompt.append("You got an apple")
                #-Falta hacer que se añada al inventario
            else: #No te da nada y tiene que salir un mensaje en el promp
                d.texto_prompt.append("The tree didn't give you anything")
        else:
            if porcentaje in range(1,21): #Te da una espada de madera y tiene que salir un mensaje en el promp
                d.texto_prompt.append("You got a Wood sword")
                #-Falta hacer que se añada al inventario
                d.vida_espada_madera -= 1 #cuando atacas con la espda restas 1 de vida a la espada
                d.vida_arbol -= 1 #Cuando atacas con la espda restas 1 de vida al arbol
            elif porcentaje in range(21,41): #Te da un escudo de madera y tiene que salir un mensaje en el promp
                d.texto_prompt.append("You got a Wood shield")
                #-Falta hacer que se añada al inventario
                d.vida_espada_madera -= 1 
                d.vida_arbol -= 1
            elif porcentaje in range(41,81): #Te da una manzana y tiene que salir un mensaje en el promp
                d.texto_prompt.append("You got an apple")
                #-Falta hacer que se añada al inventario
                d.vida_espada_madera -= 1 
                d.vida_arbol -= 1
            else: #No te da nada y tiene que salir un mensaje en el promp
                d.texto_prompt.append("The tree didn't give you anything")
                d.vida_espada_madera -= 1 
                d.vida_arbol -= 1
            if d.vida_arbol == 0: #Cuando el arbol llega a 0 se cae y no aparece hasta dentro de 10 movimientos
                d.texto_prompt.append("The tree has fallen") #Este prom lo he añadido yo

def agua(): #Interacion con el agua
    porcentaje = random.randint(1,100)
    if d.pesca == True: #Comprueba si ya has conseguido un pez
        d.texto_prompt.append("There are no more fish") #-Este prom lo he añadido yo
    else:
        if porcentaje in range(1,21): #Te da un pez, confirma que ya has conseguido un pez y te da un mensaje en el promp
            d.texto_prompt.append("You got a fish")
            d.pesca = True
            #-Falta hacer que se añada al inventario
        else: #No te da nada y te escribe en el promp
            d.texto_prompt.append("You didn't get a fish")

def zorro_visivilidad(): #Dice si el zorro sera visible o no
    porcentaje = random.randint(1,100)
    if porcentaje in range(1,51):
        d.visibilidad_zorro = True
        d.texto_prompt.append("You see a Fox")
    else:
        d.visibilidad_zorro = False
        d.texto_prompt.append("You don't see a Fox")
    
def zorro(): #Interacion con el zorro
    d.vida_espada_madera -= 1
    d.texto_prompt.append("You got meat")
    #-Falta hacer que se añada 1 de carne al inventario

def abrir_santuario(): #Interacion con el santuario
    if d.puerta_santuario == True: #Comprueba si esta abierto
        d.texto_prompt.append("You already opened this sanctuary")
    else: #Lo abre y añade 1 de vida maxima y escribe en el prompt
        d.puerta_santuario = True
        d.vidas_max += 1
        d.texto_prompt.append("You opened the sanctuary, your maximum health has increased by 1")

def cofre_cerrar(): #Comprueba si en tu inventario tienes alguna espada
    if len(d.inventarioArmas) == 0:
        d.cofre_abierto = False
        #-No esta perfecto queda especificar más como lo tiene que buscar
        #-Tambien no se si solo tiene que ser con espada o tambien escudo o si tambien cuentan las espadas de madera

def cofre(): #Interacion con el cofre
    if d.cofre_abierto == True: #comprueba si el cofre ya esta abierto
        d.texto_prompt.append("The chest is now open") #Este prompt lo he puesto yo
    else:
        if d.mapa == (d.hyrule or d.gerudo): #Dependiendo del mapa te dara una espada o un escudo
            d.texto_prompt.append(f"You got a sword")
            d.cofre_abierto = True
            #-Falta hacer que se añada una espada al inventario 
        else:
            d.texto_prompt.append(f"You got a shield")
            d.cofre_abierto = True
            #-Falta hacer que se añada un escudo al inventario

def enemigos(): #Interacion con el enemigo
    #-Queda que el enemigo se mueva bien y que no se ponga en un sitio donde no se puede
    d.vida_espada_madera -= 1 #Le quita un uso a la espada
    d.texto_prompt.append(f"Brave, keep fighting {d.name}")
    d.vidas -= 1 #Te resta 1 de vida
    d.texto_prompt.append(f"Be careful Link, you only have {d.vidas} hearts")
    d.vida_enemigo -= 1 #Le resta 1 de vida al enemigo
    if d.vidas == 0: #Comprueba si a un te queda vida
        d.texto_prompt.append(f"{d.name} is dead")
    else:
        if d.vida_enemigo == 0: #Comprueba si al enemigo a un le queda vida
            d.texto_prompt.append("You defeated an enemy, this is a dangerous zone")
        else:
            direccion1 = random.randint(1,2)
            if direccion1 == 1: #Mira si modificara X o Y
                direccion2= random.randint(1,2)
                if direccion2 == 1: #Luego si es para delante o atras o izquierda o derecha
                    d.posicion_enemigo[0] += 1
                else:
                    d.posicion_enemigo[0] -= 1
            else:
                direccion2= random.randint(1,2)
                if direccion2 == 1:
                    d.posicion_enemigo[1] += 1
                else:
                    d.posicion_enemigo[1] -= 1
            
def comer(select): #Interaccion de comer
    #-Habra que modificar el como se dirije a la comida
    if d.vidas == d.vidas_max: #Comprueba si el personaje ya tiene lla vida maxima
        d.texto_prompt.append("You already have your whole life complete")
    else:
        if select == "Eat vegetable": #Comprueba si como un vegetal
            if d.inventarioComida[0] < 0: #Comprueba si la comida que quieres esta en el inventario
                d.texto_prompt.append("You have no vegetables left")
            else: #Si tienes entonces te elimina 1 de comida y te añade la vida que necesites
                d.inventarioComida[0] -= 1
                d.vidas += 1
                d.texto_prompt.append("You have increased 1 health and spent 1 vegetable")
        elif select == "Eat salad": #Comprueba si como un ensalada
            if d.inventarioComida[0] < 0: #Comprueba si la comida que quieres esta en el inventario
                d.texto_prompt.append("You don't have any salad left")
            else:#Si tienes entonces te elimina 1 de comida y te añade la vida que necesites
                d.inventarioComida[0] -= 1
                for i in range(2): #Para no pasarse de la vida maxima comprueba si ya esta en su maximo de vida o no
                    if not d.vidas == d.vidas_max:
                        d.vidas += 1
                d.texto_prompt.append("You have increased 2 health and spent 1 salad")
        elif select == "Eat pescatarian": #Comprueba si como un pescado
            if d.inventarioComida[0] < 0: #Comprueba si la comida que quieres esta en el inventario
                d.texto_prompt.append("You don't have any pescatarian left")
            else:#Si tienes entonces te elimina 1 de comida y te añade la vida que necesites
                d.inventarioComida[0] -= 1
                for i in range(3): #Para no pasarse de la vida maxima comprueba si ya esta en su maximo de vida o no
                    if not d.vidas == d.vidas_max:
                        d.vidas += 1
                d.texto_prompt.append("You have increased 3 health and spent 1 Pescatarian")
        elif select == "Eat roasted": #Comprueba si como una carne cocinada
            if d.inventarioComida[0] < 0: #Comprueba si la comida que quieres esta en el inventario
                d.texto_prompt.append("You don't have anything toasted")
            else:#Si tienes entonces te elimina 1 de comida y te añade la vida que necesites
                d.inventarioComida[0] -= 1
                for i in range(4): #Para no pasarse de la vida maxima comprueba si ya esta en su maximo de vida o no
                    if not d.vidas == d.vidas_max:
                        d.vidas += 1
                d.texto_prompt.append("You have increased 4 health and spent 1 roast")
        else: #Si no existe la comida que ha puesto sale este promp
            d.texto_prompt.append("This food does not exist") #Este promp lo he añadido yo    

#--------------- Cocinar ----------------------
     
def cocinar(receta, inventario): # Funcion para cocinar comida 
    if receta[5:].lower() == "salad": # Si se quiere cocinar una salad
        cont = 0
        claves_eliminar = []

        for i in inventario: # Por cada elemento del diccionario miramos si es el objeto vegetable
            if inventario[i]["nombre"].lower() == "vegetable":
                cont += 1
                if cont <= 2:
                    claves_eliminar.append(i)  # Los dos vegetables los añadimos en una lista para luego eliminarlas del diccionario     

        if cont >= 2: # Si hay 2 o mas vegetables se puede hacer la salad
            for claves in claves_eliminar: # Eliminamos los dos vegetables del inventario
                del inventario[claves]
                
            print("You cooked a salad successfully")
            añadirInventario("salad", inventario) # Añadimos salad al inventario
        
        else:
            print("Not enough vegetable") # Si no hay mas 1 vegetable se imprime que no se puede cocinar la salad

    elif receta[5:].lower() == "pescatarian": # Si se elige cocinar el pescatarian
        cont_vege = 0
        cont_fish = 0
        claves_eliminar = []

        for i in inventario: #Por cada elemento del inventario contamos cuantos vegetables y fish hay
            if inventario[i]["nombre"].lower() == "vegetable":
                cont_vege += 1
                if cont_vege <= 1:
                    claves_eliminar.append(i) # El vegetable que usamos lo añadimos a la lista para eliminarlo
            
            elif inventario[i]["nombre"].lower() == "fish":
                cont_fish += 1
                if cont_fish <= 1:
                    claves_eliminar.append(i)  # El fish que usamos también lo eliminamos después

        if cont_vege >= 1 and cont_fish >= 1: # Si hay 1 fish y 1 vegetable se puede cocinar el pescatarian
            for claves in claves_eliminar: # Eliminamos los dos objetos del inventario
                del inventario[claves]
            
            print("You cooked a pescatarian successfully")
            añadirInventario("pescatarian", inventario) # Añadimos el pescatarian al inventario 
        
        elif cont_vege < 1 and cont_fish < 1: # Si no hay suficientes fish y vegetables se informa
            print("Not enough vegetable and fish")
        
        elif cont_vege < 1: # Si no hay suficientes vegetables se informa
            print("Not enough vegetable")
        
        else: # Si no hay suficientes fish se informa
            print("Not enough fish")

    elif receta[5:].lower() == "roasted": # Si se elige cocinar el roasted
        cont_vege = 0
        cont_meat = 0
        claves_eliminar = []

        for i in inventario: # Por cada elemento del inventario se comprueba si es un vegetable o un meat
            if inventario[i]["nombre"].lower() == "vegetable":
                cont_vege += 1
                if cont_vege <= 1:
                    claves_eliminar.append(i) # Añadimos al vegetable en la lista para eliminar 
            
            elif inventario[i]["nombre"].lower() == "meat":
                cont_meat += 1
                if cont_meat <= 1:
                    claves_eliminar.append(i)  # Añadimos al met en la lista para eliminar

        if cont_vege >= 1 and cont_meat >= 1:
            for claves in claves_eliminar:
                del inventario[claves] # Si hay suficientes objetos se eliminan los 2 que se usan del inventario
            
            print("You cooked a roasted successfully")
            añadirInventario("roasted", inventario) # Se añade el roasted al inventario
        
        elif cont_vege < 1 and cont_meat < 1: # Si no hay ni vegetable ni meat suficientes se informa
            print("Not enough vegetable and meat")
        
        elif cont_vege < 1: # Si no hay suficientes vegetables se informa
            print("Not enough vegetable")
        
        else: # Si no hay suficientes meat se informa
            print("Not enough meat")

    else: # Si lo que se quiere cocinar no existe, se muestra un mensaje de error
        print("You can't cook", receta[5:])



def menuInferior(mapa):
    #Queda crear el diccionario donde ira el mapa actual
    posicion = d.jugador["posicion"]
    
    menuInferior = "* Exit, Show, Go, Eat"

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

def mostrar_mapa(santuarios_abiertos): # Faltaria ver como implementar los santuarios, si es un diccionario o una lista
    #santuarios_abiertos = ["S0?", "S2?"]

    for linea in range(len(d.localitzacions["mapa_inicio"])-1): # Este for va comprueba los santuarios abiertos, si hay santuario abierto, en el mapa se elimina el interrogante que tiene al lado
        for elemento in range(len(d.localitzacions["mapa_inicio"][linea])):
            if d.localitzacions["mapa_inicio"][linea][elemento] in santuarios_abiertos:
                d.localitzacions["mapa_inicio"][linea][elemento] = d.localitzacions["mapa_inicio"][linea][elemento][:2] + " "
                


    mapa = "" # Imprimir el mapa de inicio
    for element in d.localitzacions["mapa_inicio"]:
        for element1 in element:
            mapa += element1
        mapa += "\n"

    print(mapa)

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


def cambiar_mapa(select, mapaActual): # Funcion para cambiar de mapa
    if select[6:].lower() == "hyrule":
        if mapaActual == d.localitzacions["death"] or mapaActual == d.localitzacions["gerudo"]:
            mapaActual = d.localitzacions["hyrule"]
            d.texto_prompt.append("You are now in" + select[6:])
            zorro_visivilidad() 
            return mapaActual
        
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
            zorro_visivilidad() 
            return mapaActual

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
            zorro_visivilidad() 
            return mapaActual
        
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
            zorro_visivilidad() 
            return mapaActual
        
        elif mapaActual == d.localitzacions["necluda"]:
            d.texto_prompt.append("You already are in " + select[6:])
            return mapaActual
        
        else:
            d.texto_prompt.append("You can't go to " + select[6:] + " from here")
            return mapaActual
        
    elif select[6:].lower() == "castle":
        if d.win == False:
            mapaActual = d.localitzacions["castle"]
            d.texto_prompt.append("You are now in " + select[6:])
            return mapaActual

        else:
            mapaActual = d.localitzacions["castle_win"]
            d.texto_prompt.append("You are now in " + select[6:])
            return mapaActual