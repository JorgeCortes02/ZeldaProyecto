import funciones.datos as d
import random
mapaActual = []
#Contea la cantidad de cada tipo de arma.
def conteoInventario():

    for element in d.inventarioArmas:
       
        if d.inventarioArmas[element]["tipo"] == "Wood Shield":
              d.dict_tipos["Wood Shield"]["total"] += 1

            
        elif  d.inventarioArmas[element]["tipo"] == "Shield":

            d.dict_tipos["Shield"]["total"] += 1
        elif d.inventarioArmas[element]["tipo"] == "Wood Sword":

            d.dict_tipos["Wood Sword"]["total"] += 1        

        elif  d.inventarioArmas[element]["tipo"] == "Sword":

            d.dict_tipos["Sword"]["total"] += 1

    
    woodSwort = 10
    woodShield = 6
    swort = 10
    shield = 6

    #Calcula cual es el arma con menos usos.    
    for element1 in d.inventarioArmas:

        if d.inventarioArmas[element1]["tipo"] == "Wood Sword" and d.inventarioArmas[element1]["usos"] < woodSwort:

            d.dict_tipos["Wood Sword"]["minUsos"] = element1
            woodSwort = d.inventarioArmas[element1]["usos"]

        elif d.inventarioArmas[element1]["tipo"] == "Sword" and d.inventarioArmas[element1]["usos"] < swort:

             d.dict_tipos["Sword"]["minUsos"] = element1
             swort = d.inventarioArmas[element1]["usos"]

        elif d.inventarioArmas[element1]["tipo"] == "Wood Shield" and d.inventarioArmas[element1]["usos"] < woodShield:

            d.dict_tipos["Wood Shield"]["minUsos"] = element1
            woodShield = d.inventarioArmas[element1]["usos"]

        elif d.inventarioArmas[element1]["tipo"] == "Shield" and d.inventarioArmas[element1]["usos"] < shield:

           d.dict_tipos["Shield"]["minUsos"] = element1
           shield = d.inventarioArmas[element1]["usos"]




#Funcion mostrar inventario.
def mostrarInventario(Select):
    
    #Le pasamos un select el cual define que ventana del inventario muestra, necesitara que s ele pase por defecto show inventory main para que lo muestre.
    if Select.lower() == "show inventory main": 
        #Sumaremos la candidad de armas y la cantidad total de alimentos que tenemos.
        sumArmas = 0

        sumComida = 0

        for element in d.inventarioArmas:

            sumArmas += 1

        for element in d.inventarioComida:

            sumComida += d.inventarioComida[element]


      #Muestra el main del inventario
        inventario = [" * * * * Inventory * \n",
                            "*\n".rjust(21),
                            " Link".ljust(12) + "  {0}/{1}".format(d.jugador["vidas"],d.jugador["vidas_max"]).rjust(6) + " * \n",
                            " Blod Moon in ".ljust() + "  {0}".format(25 - d.jugador["bloodMoonCoutdown"]).rjust(4) + " * \n",
                            "* \n".rjust(22),
                            " Equipement ".ljust(19) + "* \n",
                            "{0}".format(d.inventarioArmas[d.jugador["escudo_actual"]]["tipo"]).rjust(18) + " * \n",
                            "{0}".format(d.inventarioArmas[d.jugador["arma_actual"]]["tipo"]).rjust(18) + " * \n",
                            
                            "* \n".rjust(22),
                            " Food".ljust(15) + "{0}".format(sumComida).rjust(3) +  " *\n",
                            " Weapons".ljust(15) + "{0}".format(sumArmas).rjust(3) +  " *"
                            ]
                            
        return inventario
    
    #Muestra el inventario de comida
    elif Select.lower() == "show inventory food":

        inventario = [" * * * * * *  Food * \n",
                        "*\n".rjust(21),
                        "*\n".rjust(21),
                        " Vegetables".ljust(16) + "{0}".format(d.inventarioComida["Vegetables"]).rjust(2) + " * \n",
                         " Fish".ljust(16) + "{0}".format(d.inventarioComida["Fish"]).rjust(2) + " * \n",
                         " Meat".ljust(16) + "{0}".format(d.inventarioComida["Meat"]).rjust(2) + " * \n",
                         "* \n".rjust(22),
                         " Salads".ljust(16) + "{0}".format(d.inventarioComida["Salads"]).rjust(2) + " * \n",
                         " Pescatarian".ljust(16) + "{0}".format(d.inventarioComida["Pescatarian"]).rjust(2) + " * \n",
                         " Roasted".ljust(16) + "{0}".format(d.inventarioComida["Roasted"]).rjust(2) + " *"]

        return inventario

    #Muestra el inventario de armas.
    elif Select.lower() == "show inventory weapons":
        #Calculamos cuales son las armas de cada tipo que tienen menos usos para poder imprimir los usos de sa arma.
        conteoInventario()
        inventario = [" * * * * *  Weapons * \n",
                        "*\n".rjust(22),
                        "*\n".rjust(22),
        ]
        
        #Cada if determina como será esa linea en función de si el arma esta equipada o no.   
         
        if d.dict_tipos["Wood Sword"]["total"] == 0:
            inventario += " Wood Sword" + "0/0".rjust(8) + " * \n","* \n".rjust(23),
        else:

            inventario += " Wood Sword" + "{0}/{1}".format(d.inventarioArmas[d.dict_tipos["Wood Sword"]["minUsos"]]["usos"], d.dict_tipos["Wood Sword"]["total"]).rjust(8) + " * \n",
        
            if d.jugador["arma_actual"] in d.inventarioArmas and d.inventarioArmas[d.jugador["arma_actual"]]["tipo"] == "Wood Sword":
                    
                    inventario += "  (equiped)" + "*\n".rjust(11),
            else:
                    inventario += "* \n".rjust(23),
        
        if d.dict_tipos["Sword"]["total"] == 0:
            inventario += " Sword" + "0/0".rjust(13) + " * \n","* \n".rjust(23),
        else:

            inventario +=" Sword" + "{0}/{1}".format(d.inventarioArmas[d.dict_tipos["Sword"]["minUsos"]]["usos"], d.dict_tipos["Sword"]["total"]).rjust(13) + " * \n",
       
            if d.jugador["arma_actual"] in d.inventarioArmas and d.inventarioArmas[d.jugador["arma_actual"]]["tipo"] == "Sword":
                    
                    inventario += "  (equiped)" + "*\n".rjust(11),
            else:
                    inventario += "* \n".rjust(23),
        
        if d.dict_tipos["Wood Shield"]["total"] == 0:
            
            inventario += " Wood shield" + "0/0".rjust(7) + " * \n",  "* \n".rjust(23),            
       
        else:

            inventario += " Wood shield" + "{0}/{1}".format(d.inventarioArmas[d.dict_tipos["Wood Shield"]["minUsos"]]["usos"], d.dict_tipos["Wood Shield"]["total"]).rjust(7) + " * \n",              
        
            if d.jugador["escudo_actual"] in d.inventarioArmas and d.inventarioArmas[d.jugador["escudo_actual"]]["tipo"] == "Swood Shield":
                    
                    inventario += "  (equiped)" + "*\n".rjust(11),
            else:
                    inventario += "* \n".rjust(23),
        if d.dict_tipos["Shield"]["total"] == 0:
            
            inventario += " Shield" + "0/0".rjust(12) + " * \n",  "* \n".rjust(23),         
       
        else:

            inventario += " Shield" + "{0}/{1}".format(d.inventarioArmas[d.dict_tipos["Shield"]["minUsos"]]["usos"], d.dict_tipos["Shield"]["total"]).rjust(12) + " * \n",          
        
                            
            if d.jugador["escudo_actual"] in d.inventarioArmas and d.inventarioArmas[d.jugador["escudo_actual"]]["tipo"] == "Shield":
                    
                    inventario += "  (equiped)" + "*\n".rjust(11),"*".rjust(22)
            else:
                    inventario += "* \n".rjust(23),"*\n".rjust(8),"*".rjust(22)                          
                        
    return inventario                
   
  
#Esta funcion inserta un objeto en el inventario. Solo necesitaremos pasarle el nombre del objeto y el diccionario al cual queremos meterlo (InventarioComida o inventario Arma)
def añadirInventario(objeto, diccionario):

    if objeto == "Wood Sword":
        
        diccionario[objeto] = {"tipo": "Wood Sword", "Usos": 5 }
        
    elif objeto == "Wood Shield":
    
        diccionario[objeto] = {"tipo": "Wood Shield", "Usos": 5 }
    
    elif objeto == "Shield":
        
        diccionario[objeto] = {"tipo": "Shield", "Usos": 9 }
        
    
    elif objeto == "Sword":
        
        diccionario[objeto] = {"tipo": "Sword", "Usos": 9 }

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
def obtenerMapa(playermap):
    
    mapaActual = []
    for element1 in playermap:
            '''Lo hacemos de este modo porque si aplicamos el copy sobre la lista general del mapa, al modificar las listas internas que corresponden
                a cada una de las lineas del mapa, el mapa original si que se ve afectado.'''
            mapaActual.append(element1.copy())
    '''mapaActual = introducirUserInicial(posicionplayer,mapaActual)'''
    imprimirmapa(mapaActual)
    return mapaActual

#Esta funcion simplemente introduce al personaje en la posicon del mapa que le pasemos.
#El mapa que le hemos de pasar será el mapa que ya hayamos copiado y con el que estemos trabajando.
#Hay que pasarle la posicion de inicio del nmapa al que vayamos ya que tambien cambia la posicion actual en el diccionario del Jugador.

def introducirUserInicial(posicionUser, playermap):

    playermap[posicionUser[0]][posicionUser[1]] = "X"
    d.jugador["posicion"][0] = posicionUser[0]
    d.jugador["posicion"][1] = posicionUser[1]
    return playermap


#Esta función imprime tanto el mapa como el inventario lateral.
            
def imprimirmapa(mapaActual):
    mapa = ""
    contadorInventario = 0
    for element in mapaActual:

        for element1 in element:
                mapa += element1
                
        mapa += d.inventario1[contadorInventario]
        
        if contadorInventario < 10:
            contadorInventario += 1
    
    print(mapa)
       
#Gestiona el movimiento del personaje por el mapa.

def moverPersonaje(mapaActual, select, posicionplayer):
    
    select = select.lower()

    if select[0:7] == "go left":
       
        #Comprobamos que la posicion a la que queremos mover al monigote este dentro de los limites del mapa.
        if posicionplayer[1] - int(select[8:]) < 0:
            #En caso de ser incorrecto, devolvemos una tupla con un mensaje de error y la posicion en la que se quedará en personaje.
            return["Invalid action1"], posicionplayer[0], posicionplayer[1]
        else:
            #Cojemos la posicion actual del personaje en el eje que lo vamos a mover y después en otra variable guardamos la posición a la que irá
            int1 = posicionplayer[1]
            int2 = posicionplayer[1] - int(select[8:])
            diferent = True
           
           #Este bucle recorre cada una de las posiciones entre ambos puntos para comprobar que todas son cesped.
            for i in range (int1, int2, -1):
                #Comprobamos que al verificar que el personaje no pase por encima de objetos al moverse, la funcion no cuente la posicion donde estaba el personaje porque sino saltaría error.
                if int(select[8:]) == 1:

                    if mapaActual[posicionplayer[0]][i-1] != " ":
                        
                        return["Invalid action"], posicionplayer[0], posicionplayer[1]
                    
                    else:
                        #Ponemos la posicion donde estaba el personaje como espacio vacio de nuevo.
                        mapaActual[posicionplayer[0]][posicionplayer[1] ] = " "
                        #Colocamos la nueva X
                        mapaActual[posicionplayer[0]][posicionplayer[1] - int(select[8:])] = "X"
                        #Devolvemos el mapa actualizado y las nuevas posiciones.
                        return mapaActual, posicionplayer[0], posicionplayer[1] - int(select[8:])
                else:
                    #Si no solo se ha de mover una posicion y la posicion anterior no es " " marcara un booleano como false, lo que hará que en el siguiente if no intente moverlo.
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


#Es lo mismo que la anterior pero limitando el moviemiento a izquierda y derecha.
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
        map = d.principal1

    elif menu_aleatorio == 2:
        map = d.principal2

    elif menu_aleatorio == 3:
        map = d.principal3

    return map



def menu_principal(menu_inicial):
    menu = True
    while menu == True:
        imprimirmapa_menu(menu_inicial)
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
            break

        else: #Cuando la opcion sea incorrecta se mostrara que la opción es invalida
            print("Invalid Option")


def funcion_new_game():
    back = True
    name = ""
    while back == True:  # Mientras no se de la orden de volver atrás
        imprimirmapa_menu(d.new_game) # Imprimir pantalla de nueva partida
        opc = input()  # Guardar la opcion
        if opc.lower() == "help":  # Si se elige la opcion Help
            help(d.help_new_game)

        elif opc.lower() == "back":  # Si se da la orden de volver atrás se sale del bucle
            back = False

        elif opc.lower() == "":  # Si no se escribe nada se asigna el nombre Link
            name = "Link" # Modificar variable name
            print("Welcome to the game", name)
            before_game(name)

        elif opc.lower().replace(" ", "").isalnum() and len(opc) >= 3 and len(opc) <= 10:  # Cuando el nombre sea correcto se guarda
            name = opc # Modificar variable name
            print("Welcome to the game", name)
            before_game(name)

        else:  # Si es una opcion invalida se imprime escribe que no es valido
            print(opc, "Is not a valid name")


def help(mapa):
    imprimirmapa_menu(mapa)  # Se imprime la pantalla de ayuda
    back_help = True
    while back_help == True:  # Mientras no se de la orden de volver atrás
        opc = input()  # Guardar la opcion
        if opc.lower() == "back":  # Si se elige la opcion de volver atrás se sale del bucle
            back_help = False

        else:  # Si la opcion es incorrecta se imprime invalid option
            print("Invalid Option")

def before_game(name):
    imprimirmapa_menu(d.legend)  # Se imprime la leyenda
    opc = input()  # Se guarda la opcion

    while opc.lower() != "continue":
        print("Invalid action")
        opc = input()

    imprimirmapa_menu(d.plot) # Se imprime la pantalla de plot        
    opc = input()

    while opc.lower() != "continue":
        print("Invalid action")
        opc = input()
    
    print("The adventure begins")
        



def imprimirmapa_menu(mapa):
    for i in mapa:
        print(i[0])
        
        
#--------------- Inventario ----------------------       

#Equipa el arma que le pasemos en el Select.
def equiparArma(Select):
    conteoInventario()
    Select = Select.lower()
    #Comprueba si hay armas en el inventario
    if len(d.inventarioArmas )== 0:

        return "No hay armas en el inventario" 
    #Comprueba el arma que le hemos pedido equipar y guarda el tipo de arma en la misma variable select.
    if Select.find("wood shield") != -1:

        d.jugador["escudo_actual"] = d.dict_tipos["Wood Shield"]["minUsos"]
    
    elif Select.find("shield") != -1 and Select.find("wood") == -1:

        d.jugador["escudo_actual"] = d.dict_tipos["Shield"]["minUsos"]

    elif Select.find("wood sword") != -1:

       d.jugador["arma_actual"] = d.dict_tipos["Wood Sword"]["minUsos"]

     
    elif Select.find("sword") != -1 and Select.find("wood") == -1:

        d.jugador["arma_actual"] = d.dict_tipos["Sword"]["minUsos"]
        
    
  
        
            
def desequiparArma(Select):

    Select= Select.lower()
    if "sword" in Select and (d.jugador["arma_actual"] != "" or d.jugador["arma_actual"] != " "):
        d.jugador["arma_actual"] = " "
        return "Espada desequipado."
    elif "shield" in Select and (d.jugador["escudo_actual"] != "" or d.jugador["escudo_actual"] != " "):
        d.jugador["escudo_actual"] = " "
        return "Escudo desequipado."
    else:
        return "Este elemento no estaba equipado."
    

#---------Encontrar mapa ----------------------

def encontrar_mapa(): #-Hay que buscar de donde sale el mapa
    for i in d.localitzacions:
        if d.localitzacions[i] == d.mapaActual:
            d.jugador["mapa"] = i

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
    objeto_mapa = ""
    for i in d.dades: #busca en objetos en que mapa vamos a interactuar
        if d.jugador["mapa"] in i:
            objeto_mapa = i
    arbol_encontrado = 0
    for j in range(len(d.dades[objeto_mapa]["T"]["lista"])): #Busca en la lista del arbol cual esta cerca y que tenga toda la vida
        if d.jugador["posicion"][0] == d.dades[objeto_mapa]["T"]["lista"][j][0] and d.jugador["posicion"][1]-1 == d.dades[objeto_mapa]["T"]["lista"][j][0]:
            if not d.objetos[objeto_mapa]["T"]["vida"][j] == 0:
                arbol_encontrado = j
        elif d.jugador["posicion"][0]-1 == d.dades[objeto_mapa]["T"]["lista"][j][0] and d.jugador["posicion"][1] == d.dades[objeto_mapa]["T"]["lista"][j][0]:
            if not d.objetos[objeto_mapa]["T"]["vida"][j] == 0:
                arbol_encontrado = j
        elif d.jugador["posicion"][0] == d.dades[objeto_mapa]["T"]["lista"][j][0] and d.jugador["posicion"][1]+1 == d.dades[objeto_mapa]["T"]["lista"][j][0]:
            if not d.objetos[objeto_mapa]["T"]["vida"][j] == 0:
                arbol_encontrado = j
        elif d.jugador["posicion"][0]+1 == d.dades[objeto_mapa]["T"]["lista"][j][0] and d.jugador["posicion"][1] == d.dades[objeto_mapa]["T"]["lista"][j][0]:
            if not d.objetos[objeto_mapa]["T"]["vida"][j] == 0:
                arbol_encontrado = j
    if arbol_encontrado == 0: #si no encuentra nigun arbol con vida no te deja hacer nada
        d.texto_prompt.append("No trees available")
    else:
        porcentaje = random.randint(1,100)
        if d.jugador["arma_actual"] == " " or d.jugador["arma_actual"] == "" : #compruba si cuando has atacado a sido con una espada o no
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
                d.dades[objeto_mapa]["T"]["vida"][arbol_encontrado] -= 1 #Cuando atacas con la espda restas 1 de vida al arbol
            elif porcentaje in range(21,41): #Te da un escudo de madera y tiene que salir un mensaje en el promp
                d.texto_prompt.append("You got a Wood shield")
                añadirInventario("Wood Shield",d.inventarioArmas)
                d.inventarioArmas[d.jugador["arma_actual"]]["Usos"] -= 1 
                d.dades[objeto_mapa]["T"]["vida"][arbol_encontrado] -= 1
            elif porcentaje in range(41,81): #Te da una manzana y tiene que salir un mensaje en el promp
                d.texto_prompt.append("You got an apple")
                d.inventarioArmas[d.jugador["arma_actual"]]["Usos"] -= 1 
                d.dades[objeto_mapa]["T"]["vida"][arbol_encontrado] -= 1
                d.inventarioComida["Vegetables"] += 1
            else: #No te da nada y tiene que salir un mensaje en el promp
                d.texto_prompt.append("The tree didn't give you anything")
                d.inventarioArmas[d.jugador["arma_actual"]]["Usos"] -= 1 
                d.dades[objeto_mapa]["T"]["vida"][arbol_encontrado] -= 1
            if d.dades[objeto_mapa]["T"]["vida"][arbol_encontrado] == 0: #Cuando el arbol llega a 0 se cae y no aparece hasta dentro de 10 movimientos
                d.texto_prompt.append("The tree has fallen") #Este prom lo he añadido yo

def contador_arbol_mapa():
    objeto_mapa = ""
    for i in d.dades:
        if d.jugador["mapa"] in i:
            objeto_mapa = i
    for i in range(len(d.dades[objeto_mapa]["T"]["lista"])):
        if not d.objetos[objeto_mapa]["T"]["vida"][i] == 0:
            d.localitzacions[d.jugador["mapa"]][d.dades[objeto_mapa]["T"]["lista"][i][0]][d.dades[objeto_mapa]["T"]["lista"][i][1]] = d.dades[objeto_mapa]["T"]["contador"][i]


def contador_arbol():
    cont = 0
    for i in d.dades["gerudo"]["T"]["contador"]:
        if i > 0:
            d.dades["gerudo"]["T"]["contador"][cont] = i - 1
        else:
            d.dades["gerudo"]["T"]["vida"][cont] == 4
            d.localitzacions[d.jugador["mapa"]][d.dades[objeto_mapa]["T"]["lista"][i][0]][d.objetos[objeto_mapa]["T"]["lista"][i][1]] = "T" #-Falta terminarlo
        cont = cont + 1

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
    if d.visibilidad_zorro == False:
        d.texto_prompt.append("You don't see any fox")
    else:
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

def cofre_cerrar_sword(): #Comprueba si en tu inventario tienes alguna espada
    if len(d.dict_tipos["Sword"]["total"]) == 0: #-mirar direcciones
       d.objetos_hyrule["M"]["abierto"][0] == False
       d.objetos_gerudo["M"]["abierto"][0] == False
       d.objetos_gerudo["M"]["abierto"][1] == False

def cofre_cerrar_shield(): #Comprueba si en tu inventario tienes algun escudo
    if len(d.dict_tipos["Shield"]["total"]) == 0: #-mirar direcciones
        d.objetos_necluda["M"]["abierto"][0] == False
        d.objetos_necluda["M"]["abierto"][1] == False
        d.objetos_necluda["M"]["abierto"][2] == False
        d.objetos_death["M"]["abierto"][0] == False
        d.objetos_death["M"]["abierto"][1] == False

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
            
def comer(select): #Interaccion de comer #-mirar las direcciones
    if d.vidas == d.vidas_max: #Comprueba si el personaje ya tiene lla vida maxima
        d.texto_prompt.append("You already have your whole life complete")
    else:
        if select == "Eat vegetable": #Comprueba si como un vegetal
            if d.dict_tipos["Vegetables"]["total"] < 0: #Comprueba si la comida que quieres esta en el inventario
                d.texto_prompt.append("You have no vegetables left")
            else: #Si tienes entonces te elimina 1 de comida y te añade la vida que necesites
                d.dict_tipos["Vegetables"]["total"] -= 1
                d.vidas += 1
                d.texto_prompt.append("You have increased 1 health and spent 1 vegetable")
        elif select == "Eat salad": #Comprueba si como un ensalada
            if d.dict_tipos["Salads"]["total"] < 0: #Comprueba si la comida que quieres esta en el inventario
                d.texto_prompt.append("You don't have any salad left")
            else:#Si tienes entonces te elimina 1 de comida y te añade la vida que necesites
                d.dict_tipos["Salads"]["total"] -= 1
                for i in range(2): #Para no pasarse de la vida maxima comprueba si ya esta en su maximo de vida o no
                    if not d.vidas == d.vidas_max:
                        d.vidas += 1
                d.texto_prompt.append("You have increased 2 health and spent 1 salad")
        elif select == "Eat pescatarian": #Comprueba si como un pescado
            if d.dict_tipos["Pescatarian"]["total"] < 0: #Comprueba si la comida que quieres esta en el inventario
                d.texto_prompt.append("You don't have any pescatarian left")
            else:#Si tienes entonces te elimina 1 de comida y te añade la vida que necesites
                d.dict_tipos["Pescatarian"]["total"] -= 1
                for i in range(3): #Para no pasarse de la vida maxima comprueba si ya esta en su maximo de vida o no
                    if not d.vidas == d.vidas_max:
                        d.vidas += 1
                d.texto_prompt.append("You have increased 3 health and spent 1 Pescatarian")
        elif select == "Eat roasted": #Comprueba si como una carne cocinada
            if d.dict_tipos["Roasted"]["total"] < 0: #Comprueba si la comida que quieres esta en el inventario
                d.texto_prompt.append("You don't have anything toasted")
            else:#Si tienes entonces te elimina 1 de comida y te añade la vida que necesites
                d.dict_tipos["Roasted"]["total"] -= 1
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


#Crea el menu inferior en base a lo que haya en el entorno.
def menuInferior():
   
    posicion = d.jugador["posicion"]
    
    menuInferior = "* Exit, Show, Go, Eat"

    if d.jugador["mapa"][posicion[0]+1][posicion[1]] == "T" or d.jugador["mapa"][posicion[0]-1][posicion[1]] == "T" or d.jugador["mapa"][posicion[0]+1][posicion[1]+1]  == "T" or d.jugador["mapa"][posicion[0]+1][posicion[1]-1]  == "T" or d.jugador["mapa"][posicion[0]][posicion[1]+1]  == "T" or d.jugador["mapa"][posicion[0]][posicion[1]-1]  == "T" or d.jugador["mapa"][posicion[0]-1][posicion[1]+1] or d.jugador["mapa"][posicion[0]-1][posicion[1]-1]  == "T":

        menuInferior += ", Attack"

   
    if menuInferior.find("Attack") == -1:
    
        if d.jugador["mapa"][posicion[0]+1][posicion[1]][0] in  ("Z","E") or d.jugador["mapa"][posicion[0]-1][posicion[1]][0] in  ("Z","E") or d.jugador["mapa"][posicion[0]+1][posicion[1]+1][0]  in  ("Z","E") or d.jugador["mapa"][posicion[0]+1][posicion[1]-1][0]  in  ("Z","E") or d.jugador["mapa"][posicion[0]][posicion[1]+1][0]  in  ("Z","E") or d.jugador["mapa"][posicion[0]][posicion[1]-1][0]  in  ("Z","E") or d.jugador["mapa"][posicion[0]-1][posicion[1]+1][0] in  ("Z","E") or d.jugador["mapa"][posicion[0]-1][posicion[1]-1][0]  in  ("Z","E") and d.jugador["arma_actual"] != " ":
            menuInferior += ", Attack"

    if d.jugador["mapa"][posicion[0]+1][posicion[1]][0] == "~" or d.jugador["mapa"][posicion[0]-1][posicion[1]][0]  == "~" or d.jugador["mapa"][posicion[0]+1][posicion[1]+1][0]   == "~" or d.jugador["mapa"][posicion[0]+1][posicion[1]-1][0]   == "~" or d.jugador["mapa"][posicion[0]][posicion[1]+1][0]   == "~" or d.jugador["mapa"][posicion[0]][posicion[1]-1][0]   == "~" or d.jugador["mapa"][posicion[0]-1][posicion[1]+1][0] == "~" or d.jugador["mapa"][posicion[0]-1][posicion[1]-1][0] == "~":
         menuInferior += ", Fish"
    
    if d.jugador["mapa"][posicion[0]+1][posicion[1]][0] in  ("S","M") or d.jugador["mapa"][posicion[0]-1][posicion[1]][0] in  ("S","M") or d.jugador["mapa"][posicion[0]+1][posicion[1]+1][0]  in  ("S","M") or d.jugador["mapa"][posicion[0]+1][posicion[1]-1][0] in  ("S","M") or d.jugador["mapa"][posicion[0]][posicion[1]+1][0] in  ("S","M") or d.jugador["mapa"][posicion[0]][posicion[1]-1][0] in ("S","M") or d.jugador["mapa"][posicion[0]-1][posicion[1]+1][0] in  ("S","M") or d.jugador["mapa"][posicion[0]-1][posicion[1]-1][0]  in ("S","M"):
     
        menuInferior += ", Open"


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

    for linea in range(len(d.mapa_inicio)-1): # Este for va comprueba los santuarios abiertos, si hay santuario abierto, en el mapa se elimina el interrogante que tiene al lado
        for elemento in range(len(d.mapa_inicio[linea])):
            if d.mapa_inicio[linea][elemento] in santuarios_abiertos:
                d.mapa_inicio[linea][elemento] = d.mapa_inicio[linea][elemento][:2] + " "
                


    mapa = "" # Imprimir el mapa de inicio
    for element in d.mapa_inicio:
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
    if d.mapaActual[element[0]-1][element[1]] == " ":

        d.jugador["posicion"][0] = element[0]
        d.jugador["posicion"][1] = element[1] 
        d.mapaActual[element[0]-1][element[1]] = "P"
        print(d.mapaActual)
    elif d.mapaActual[element[0]][element[1]] == " ":

        d.jugador["posicion"][0] = element[0]+1
        d.jugador["posicion"][1] = element[1] 
        d.mapaActual[element[0]+1][element[1]] = "O"
        print(d.mapaActual)
    
    elif d.mapaActual[element[0]][element[1]] == " ":

        d.jugador["posicion"][0] = element[0]
        d.jugador["posicion"][1] = element[1]+1
        d.mapaActual[element[0]][element[1]+1] = "S"
        print(d.mapaActual)

    elif d.mapaActual[element[0]][element[1]-1] == " ":

        d.jugador["posicion"][0] = element[0]
        d.jugador["posicion"][1] = element[1] -1
        d.mapaActual[element[0]][element[1]-1] = "D"
        print(d.mapaActual)
    else:
        print("Invalid Action.") 



#Cheats

#hay que añadir en el menu la comprobacion de que sea mayor a 3 y menor a 10 caracteres y que sea alphanumerico     
def renamePlayer(newName):

   

