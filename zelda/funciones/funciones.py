import funciones.datos as d

import random
import mysql.connector
mapaActual = []
db = mysql.connector.connect(
    host="172.187.226.29",  # Cambia a tu dirección IP
    user="root2",
    passwd="EsteveTerradas2023.", 
    database="ZeldaBBDD"

)
cursor = db.cursor()


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
                            " Blod Moon in ".ljust(2) + "  {0}".format(d.jugador["bloodMoonCoutdown"]).rjust(4) + " * \n",
                            "* \n".rjust(22),
                            " Equipement ".ljust(19) + "* \n",]
        
        if len(d.inventarioArmas) == 0 or d.jugador["escudo_actual"] not in d.inventarioArmas or d.jugador["escudo_actual"] == " " or d.jugador["escudo_actual"] == "":

                inventario += "* \n".rjust(22),
        else:
                inventario += "{0}".format(d.inventarioArmas[d.jugador["escudo_actual"]]["tipo"]).rjust(18) + " * \n",

        if len(d.inventarioArmas) == 0 or d.jugador["arma_actual"] not in d.inventarioArmas or d.jugador["arma_actual"] == " " or d.jugador["arma_actual"] == "":

                inventario += "* \n".rjust(22),
        else:
                inventario += "{0}".format(d.inventarioArmas[d.jugador["arma_actual"]]["tipo"]).rjust(18) + " * \n",


        inventario += "* \n".rjust(22), " Food".ljust(15) + "{0}".format(sumComida).rjust(3) +  " *\n"," Weapons".ljust(15) + "{0}".format(sumArmas).rjust(3) +  " *"
                            
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
                         " Roasted".ljust(16) + "{0}".format(d.inventarioComida["Roasted"]).rjust(2) + " *\n",
                         "*".rjust(20)]

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
        
        diccionario[objeto] = {"tipo": "Wood Sword", "usos": 5 }
        
    elif objeto == "Wood Shield":
    
        diccionario[objeto] = {"tipo": "Wood Shield", "usos": 5 }
    
    elif objeto == "Shield":
        
        diccionario[objeto] = {"tipo": "Shield", "usos": 9 }
        
    
    elif objeto == "Sword":
        
        diccionario[objeto] = {"tipo": "Sword", "usos": 9 }

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

    saveGame()
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
                mapa += str(element1)
               
        mapa += mostrarInventario(d.select)[contadorInventario]
        
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
       
        if posicionplayer[1] + int(select[9:]) > 57:
            

            return["Invalid action1"], posicionplayer[0], posicionplayer[1]
        else:
            int1 = posicionplayer[1]
            int2 = posicionplayer[1] + int(select[9:])
            diferent = True
            for i in range (int1, int2):
                
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

def movimientoCercano(Select, mapaActual):
    
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

            mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = " "
            d.jugador["posicion"][0] = element[0]
            d.jugador["posicion"][1] = element[1]-1
            mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = "X"

        elif d.localitzacions[d.jugador["mapa"]][element[0]][element[1]+1] == " ": #Comprueba si esta libre derecha

            mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = " "
            d.jugador["posicion"][0] = element[0]
            d.jugador["posicion"][1] = element[1]+1
            mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = "X"

        elif d.localitzacions[d.jugador["mapa"]][element[0]-1][element[1]] == " ": #Comprueba si esta libre arriba

            mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = " "
            d.jugador["posicion"][0] = element[0]-1
            d.jugador["posicion"][1] = element[1] 
            mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = "X"

        elif d.localitzacions[d.jugador["mapa"]][element[0]+1][element[1]] == " ": #Comprueba si esta libre abajo

            mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = " "
            d.jugador["posicion"][0] = element[0]+1
            d.jugador["posicion"][1] = element[1] 
            mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = "X"

    if Select[len(Select)-1].upper() == "F":

        if d.visibilidad_zorro == False:
            d.texto_prompt.append("Invalid option")

        else:

            element = d.dades[d.jugador["mapa"]]["F"]["posicion"]
                
            if d.localitzacions[d.jugador["mapa"]][element[0]][element[1]-1] == " ": #Comprueba si esta libre izquierda
                mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = " "
                d.jugador["posicion"][0] = element[0]
                d.jugador["posicion"][1] = element[1]-1
                mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = "X"

            elif d.localitzacions[d.jugador["mapa"]][element[0]][element[1]+1] == " ": #Comprueba si esta libre derecha
                mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = " "
                d.jugador["posicion"][0] = element[0]
                d.jugador["posicion"][1] = element[1]+1
                mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = "X"

            elif d.localitzacions[d.jugador["mapa"]][element[0]-1][element[1]] == " ": #Comprueba si esta libre arriba
                mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = " "
                d.jugador["posicion"][0] = element[0]-1
                d.jugador["posicion"][1] = element[1]
                mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = "X"

            elif d.localitzacions[d.jugador["mapa"]][element[0]+1][element[1]] == " ": #Comprueba si esta libre abajo
                mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = " "
                d.jugador["posicion"][0] = element[0]+1
                d.jugador["posicion"][1] = element[1] 
                mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = "X"
    
    if Select[len(Select)-2].upper() == "S":

        for i in range(len(d.dades[d.jugador["mapa"]]["Santuarios"]["posicion"])):

            if d.dades[d.jugador["mapa"]]["Santuarios"]["posicion"][i][2] == Select[len(Select)-2:].upper():
                
                element = d.dades[d.jugador["mapa"]]["Santuarios"]["posicion"][i]
                    
                if d.localitzacions[d.jugador["mapa"]][element[0]][element[1]-1] == " ": #Comprueba si esta libre izquierda
                    mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = " "
                    d.jugador["posicion"][0] = element[0]
                    d.jugador["posicion"][1] = element[1]-1
                    mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = "X"

                elif d.localitzacions[d.jugador["mapa"]][element[0]][element[1]+1] == " ": #Comprueba si esta libre derecha
                    mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = " "
                    d.jugador["posicion"][0] = element[0]
                    d.jugador["posicion"][1] = element[1]+1
                    mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = "X"

                elif d.localitzacions[d.jugador["mapa"]][element[0]-1][element[1]] == " ": #Comprueba si esta libre arriba
                    mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = " "
                    d.jugador["posicion"][0] = element[0]-1
                    d.jugador["posicion"][1] = element[1]
                    mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = "X"

                elif d.localitzacions[d.jugador["mapa"]][element[0]+1][element[1]] == " ": #Comprueba si esta libre abajo
                    mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = " "
                    d.jugador["posicion"][0] = element[0]+1
                    d.jugador["posicion"][1] = element[1] 
                    mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = "X"


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
            
        if mapaActual[element[0]][element[1]-1] == " ": #Comprueba si esta libre izquierda
            mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = " "
            d.jugador["posicion"][0] = element[0]
            d.jugador["posicion"][1] = element[1]-1
            mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = "X"

        elif mapaActual[element[0]][element[1]+1] == " ": #Comprueba si esta libre derecha
            mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = " "
            d.jugador["posicion"][0] = element[0]
            d.jugador["posicion"][1] = element[1]+1
            mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = "X"

        elif mapaActual[element[0]-1][element[1]] == " ": #Comprueba si esta libre arriba
            mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = " "
            d.jugador["posicion"][0] = element[0]-1
            d.jugador["posicion"][1] = element[1]
            mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = "X"

        elif mapaActual[element[0]+1][element[1]] == " ": #Comprueba si esta libre abajo
            mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = " "
            d.jugador["posicion"][0] = element[0]+1
            d.jugador["posicion"][1] = element[1] 
            mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]] = "X"

#Es lo mismo que la anterior pero limitando el moviemiento a izquierda y derecha.
def moverPersonajeGanon(mapaActual, select, posicionplayer):
    
    
    if select[0:7] == "go left":
        print(posicionplayer[1], posicionplayer[1] - int(select[7:]) )
        if posicionplayer[1] - int(select[7:]) < 0:
            
            return["Invalid action1"], posicionplayer[0], posicionplayer[1]
        else:
            int1 = posicionplayer[1]
            int2 = posicionplayer[1] - int(select[7:])
            diferent = True
           
            for i in range (int1, int2, -1):
                
                if int(select[7:]) == 1:

                    if mapaActual[posicionplayer[0]][i-1] != " ":
                        d.texto_prompt.append("Invalid action")
                        return["Invalid action"], posicionplayer[0], posicionplayer[1]
                    
                    else:

                        mapaActual[posicionplayer[0]][posicionplayer[1] ] = " "
                        mapaActual[posicionplayer[0]][posicionplayer[1] - int(select[7:])] = "X"
                        return mapaActual, posicionplayer[0], posicionplayer[1] - int(select[7:])
                else:

                    if mapaActual[posicionplayer[0]][i-1] != " ":
                        
                        diferent = False
            if diferent == True:

                mapaActual[posicionplayer[0]][posicionplayer[1] ] = " "
                mapaActual[posicionplayer[0]][posicionplayer[1] - int(select[7:])] = "X"
                return mapaActual, posicionplayer[0], posicionplayer[1] - int(select[7:])        
            else:
                d.texto_prompt.append("Invalid action")
                return["Invalid action"], posicionplayer[0], posicionplayer[1]
                       

    elif select[0:8] == "go right":
       
        if posicionplayer[1] + int(select[8:]) > 57:
            

            return["Invalid action1"], posicionplayer[0], posicionplayer[1]
        else:
            int1 = posicionplayer[1]
            int2 = posicionplayer[1] + int(select[8:])
            diferent = True
            for i in range (int2, int1, -1):
                
                if int(select[8:]) == 1:

                    if mapaActual[posicionplayer[0]][i+1] != " ":
                        d.texto_prompt.append("Invalid action")
                        return["Invalid action2"], posicionplayer[0], posicionplayer[1]
                    
                    
                else:

                    if mapaActual[posicionplayer[0]][i+1] != " ":
                        diferent = False
            
            if diferent == True:
       
                mapaActual[posicionplayer[0]][posicionplayer[1] ] = " "
                mapaActual[posicionplayer[0]][posicionplayer[1] + int(select[8:])] = "X"
                return mapaActual, posicionplayer[0], posicionplayer[1] + int(select[8:])
            else:
                d.texto_prompt.append("Invalid action")
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
            descargarGuardadas()
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
                                    d.jugador["id_game"] = int(opc[5])
                                    guardado = True

                                    selectAndChargePartida(int(opc[5]))

                                    salir = True
                                    return True
                            

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

            elif opc.lower() == "consultes":
                limpiar_pantalla()
                print("Elige la consulta que quieres hacer".center(60, "*"))
                print("Jugadores, Partidas, Armas, Alimentos, Blood Moon Media, Blood Moon Max")
                select = input("Que quieres consultar? ")
                
                if select.lower() == "jugadores":
                    consultaJugadores()
                    
                elif select.lower() == "partidas":
                    partidasXJugador()
                    
                elif select.lower() == "armas":
                    ArmasConseguidas()
                    
                elif select.lower() == "alimentos":
                    AlimentosConseguidos()
                    
                elif select.lower() == "blood moon media":
                    MediaBloodMoon()
                    
                elif select.lower() == "blood moon max":
                    maxBloodMoon()
                    
                    

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
                saveInicialGame()
                salir = before_game()
                return True

            elif opc.lower().replace(" ", "").isalnum() and len(opc) >= 3 and len(opc) <= 10:  # Cuando el nombre sea correcto se guarda
                d.jugador["nombre"] = opc # Modificar variable name
                d.texto_prompt.append("Welcome to the game " + d.jugador['nombre'])
                saveInicialGame()
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

#Equipa el arma que le pasemos en el Select.
def equiparArma(Select):
    conteoInventario()
    #armaMenosUsos()
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
                d.inventarioArmas[d.jugador["arma_actual"]]["usos"] -= 1 #cuando atacas con la espda restas 1 de vida a la espada
                d.dades[d.jugador["mapa"]]["T"]["vida"][arbol_encontrado] -= 1 #Cuando atacas con la espda restas 1 de vida al arbol
            elif porcentaje in range(21,41): #Te da un escudo de madera y tiene que salir un mensaje en el promp
                d.texto_prompt.append("You got a Wood shield")
                añadirInventario("Wood Shield",d.inventarioArmas)
                d.inventarioArmas[d.jugador["arma_actual"]]["usos"] -= 1 
                d.dades[d.jugador["mapa"]]["T"]["vida"][arbol_encontrado] -= 1
            elif porcentaje in range(41,81): #Te da una manzana y tiene que salir un mensaje en el promp
                d.texto_prompt.append("You got an apple")
                d.inventarioArmas[d.jugador["arma_actual"]]["usos"] -= 1 
                d.dades[d.jugador["mapa"]]["T"]["vida"][arbol_encontrado] -= 1
                d.inventarioComida["Vegetables"] += 1
            else: #No te da nada y tiene que salir un mensaje en el promp
                d.texto_prompt.append("The tree didn't give you anything")
                d.inventarioArmas[d.jugador["arma_actual"]]["usos"] -= 1 
                d.dades[d.jugador["mapa"]]["T"]["vida"][arbol_encontrado] -= 1
            if d.dades[d.jugador["mapa"]]["T"]["vida"][arbol_encontrado] == 0: #Cuando el arbol llega a 0 se cae y no aparece hasta dentro de 10 movimientos
                d.texto_prompt.append("The tree has fallen") #Este prom lo he añadido yo
                d.dades[d.jugador["mapa"]]["T"]["contador"][arbol_encontrado] = 10

def contador_arbol_mapa(mapaActual): #Cambia los arboles por su numero del contador 
    if d.jugador["mapa"] != "castle":
        for i in range(len(d.dades[d.jugador["mapa"]]["T"]["contador"])): #Busca que arbol tiene la vida al 0 y lo cambia por el numero del contador que tenga en ese momento
            if d.dades[d.jugador["mapa"]]["T"]["contador"][i] != 0:
                mapaActual[d.dades[d.jugador["mapa"]]["T"]["lista"][i][0]][d.dades[d.jugador["mapa"]]["T"]["lista"][i][1]] = str(d.dades[d.jugador["mapa"]]["T"]["contador"][i])

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

def agua(mapaActual): #Interacion con el agua
    agua = False
    if mapaActual[d.jugador["posicion"][0]+1][d.jugador["posicion"][1]] == "~":
        agua = True
    
    elif mapaActual[d.jugador["posicion"][0]-1][d.jugador["posicion"][1]] == "~":
        agua = True
    
    elif mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]+1] == "~":
        agua = True
        
    elif mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]-1] == "~":
        agua = True 
    
    
    if agua == True:
        if d.pesca == True: #Comprueba si ya has conseguido un pez
            d.texto_prompt.append("There are no more fish") #-Este prom lo he añadido yo
        else:
            porcentaje = random.randint(1,100)
            if porcentaje in range(1,21): #Te da un pez, confirma que ya has conseguido un pez y te da un mensaje en el promp
                d.texto_prompt.append("You got a fish")
                d.pesca = True 
                d.inventarioComida["Fish"] += 1
            else: #No te da nada y te escribe en el promp
                d.texto_prompt.append("You didn't get a fish")
    else:
        d.texto_prompt.append("You can't fish here")

def reiniciar_pesca():
    d.pesca = False

def zorro_visivilidad(): #Dice si el zorro sera visible o no
    porcentaje = random.randint(1,100)
    if porcentaje in range(1,51):
        d.visibilidad_zorro = True
        d.vida_zorro = True
        d.texto_prompt.append("You see a Fox")
    else:
        d.visibilidad_zorro = False
        d.texto_prompt.append("You don't see a Fox")
    
def zorro(): #Interacion con el zorro
    if d.visibilidad_zorro == False:
        d.texto_prompt.append("You don't see any fox")
    else:
        if d.jugador["arma_actual"] != " " and d.jugador["arma_actual"] != "":
            if d.vida_zorro == True:
                d.inventarioArmas[d.jugador["arma_actual"]]["usos"] -= 1
                d.texto_prompt.append("You got meat")
                d.inventarioComida["Meat"] += 1
                d.vida_zorro = False
            
            else:
                d.texto_prompt.append("He is dead 💀")
        
        else:
            d.texto_prompt.append("You need a Sword to attack")


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
    saveGame()

def cofre(mapaActual): #Interacion con el cofre
    for j in range(len(d.dades[d.jugador["mapa"]]["M"]["posicion"])):
        if d.jugador["posicion"][0] == d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0] and d.jugador["posicion"][1]+1 == d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]:
            if d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] == True: #comprueba si el cofre ya esta abierto
                d.texto_prompt.append("The chest is now open") #Este prompt lo he puesto yo
            else:
                if d.jugador["mapa"] == ("hyrule" or "gerudo"): #Dependiendo del mapa te dara una espada o un escudo
                    d.texto_prompt.append("You got a sword")
                    d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] = True
                    mapaActual[d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]] = "W"
                    añadirInventario("Sword",d.inventarioArmas)
                else:
                    d.texto_prompt.append("You got a shield")
                    d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] = True
                    mapaActual[d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]] = "W"
                    añadirInventario("Shield",d.inventarioArmas)
        elif d.jugador["posicion"][0] == d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0] and d.jugador["posicion"][1]-1 == d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]:
            if d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] == True: #comprueba si el cofre ya esta abierto
                d.texto_prompt.append("The chest is now open") #Este prompt lo he puesto yo
            else:
                if d.jugador["mapa"] == ("hyrule" or "gerudo"): #Dependiendo del mapa te dara una espada o un escudo
                    d.texto_prompt.append("You got a sword")
                    d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] = True
                    mapaActual[d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]] = "W"
                    añadirInventario("Sword",d.inventarioArmas)
                else:
                    d.texto_prompt.append("You got a shield")
                    d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] = True
                    mapaActual[d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]] = "W"
                    añadirInventario("Shield",d.inventarioArmas)
        elif d.jugador["posicion"][0]+1 == d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0] and d.jugador["posicion"][1] == d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]:
            if d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] == True: #comprueba si el cofre ya esta abierto
                d.texto_prompt.append("The chest is now open") #Este prompt lo he puesto yo
            else:
                if d.jugador["mapa"] == ("hyrule" or "gerudo"): #Dependiendo del mapa te dara una espada o un escudo
                    d.texto_prompt.append("You got a sword")
                    d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] = True
                    mapaActual[d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]] = "W"
                    añadirInventario("Sword",d.inventarioArmas)
                else:
                    d.texto_prompt.append("You got a shield")
                    d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] = True
                    mapaActual[d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]] = "W"
                    añadirInventario("Shield",d.inventarioArmas)
        elif d.jugador["posicion"][0]-1 == d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0] and d.jugador["posicion"][1] == d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]:
            if d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] == True: #comprueba si el cofre ya esta abierto
                d.texto_prompt.append("The chest is now open") #Este prompt lo he puesto yo
            else:
                if d.jugador["mapa"] == ("hyrule" or "gerudo"): #Dependiendo del mapa te dara una espada o un escudo
                    d.texto_prompt.append("You got a sword")
                    d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] = True
                    mapaActual[d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]] = "W"
                    añadirInventario("Sword",d.inventarioArmas)
                else:
                    d.texto_prompt.append("You got a shield")
                    d.dades[d.jugador["mapa"]]["M"]["posicion"][j][2] = True
                    mapaActual[d.dades[d.jugador["mapa"]]["M"]["posicion"][j][0]][d.dades[d.jugador["mapa"]]["M"]["posicion"][j][1]] = "W"
                    añadirInventario("Shield",d.inventarioArmas)

def enemigos(mapaActual): #Interacion con el enemigo
    if d.jugador["arma_actual"] == " " or d.jugador["arma_actual"] == "": #compruba si tienes una espada
        d.texto_prompt.append("I can't attack if you don't have a sword")
    else:
        for i in range(len(d.dades[d.jugador["mapa"]]["E"]["posicion"])):
            enemigo = False
            if d.jugador["posicion"][0] == d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0] and d.jugador["posicion"][1]+1 == d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]:
                enemigo = True
            
            if d.jugador["posicion"][0] == d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0] and d.jugador["posicion"][1]-1 == d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]:
                enemigo = True
            
            if d.jugador["posicion"][0]-1 == d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0] and d.jugador["posicion"][1] == d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]:
                enemigo = True
            
            if d.jugador["posicion"][0]+1 == d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0] and d.jugador["posicion"][1] == d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]:
                enemigo = True
            
            if enemigo == True:  
                if d.dades[d.jugador["mapa"]]["E"]["posicion"][i][3] == 0:
                    d.texto_prompt.append("he is dead 💀")
                
                else:
                    if d.jugador["escudo_actual"] != " " and d.jugador["escudo_actual"] != "":
                        d.inventarioArmas[d.jugador["escudo_actual"]]["usos"] -= 1
                    
                    else:
                        d.jugador["vidas"]-= 1 #Te resta 1 de vida
                    if d.jugador["vidas"] != 0:
                        d.inventarioArmas[d.jugador["arma_actual"]]["usos"] -= 1 #Le quita un uso a la espada
                        d.texto_prompt.append(f"Brave, keep fighting {d.jugador['nombre']}")
                        d.texto_prompt.append(f"Be careful {d.jugador['nombre']}, you only have {d.jugador['vidas']} hearts")

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
                                    if mapaActual[d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]+1] == " ":
                                        mapaActual[d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] = " "
                                        mapaActual[d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]+1] = " "
                                        d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1] += 1
                                        mapaActual[d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] = "E"
                                        salir = True
                                else:
                                    if mapaActual[d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]-1] == " ":
                                        mapaActual[d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] = " "
                                        mapaActual[d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]+1] = " "
                                        d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1] -= 1
                                        mapaActual[d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] = "E"
                                        salir = True
                            else:
                                direccion2= random.randint(1,2)
                                if direccion2 == 1:
                                    if mapaActual[d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]+1][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] == " ":
                                        mapaActual[d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] = " "
                                        mapaActual[d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]+1] = " "
                                        d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0] += 1
                                        mapaActual[d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] = "E"
                                        salir = True
                                else:
                                    if mapaActual[d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]-1][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] == " ":
                                        mapaActual[d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] = " "
                                        mapaActual[d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]+1] = " "
                                        d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0] -= 1
                                        mapaActual[d.dades[d.jugador["mapa"]]["E"]["posicion"][i][0]][d.dades[d.jugador["mapa"]]["E"]["posicion"][i][1]] = "E"
                                        salir = True
    return mapaActual

def vida_ganon():
    if d.jugador["mapa"] != "castle":
        if d.win == False:
            d.ganon["vida"] = 8
            for i in range(8):
                d.localitzacions["castle"][2][46+i+1] = "♥"

def ganon_castillo():
    if d.jugador["posicion"][1] > 18:
        d.jugador["vidas"] -= 1 #Te resta 1 de vida
        d.texto_prompt.append("Gannon attacked you, you lost 1 life")


def pelea_ganon(mapaActual): #Interacion con ganon
    if d.jugador["arma_actual"] == " " or d.jugador["arma_actual"] == "": #compruba si tienes una espada
        d.texto_prompt.append("I can't attack if you don't have a sword")
    else:
        if d.jugador["escudo_actual"] != " " and d.jugador["escudo_actual"] != "":
            d.inventarioArmas[d.jugador["escudo_actual"]]["usos"] -= 1 #Le quita un uso a la espada
        
        else:
            d.jugador["vidas"] -= 1
            
        d.inventarioArmas[d.jugador["arma_actual"]]["usos"] -= 1
        d.texto_prompt.append("You attacked Ganon, Ganon lost 1 life")
        numero = random.randint(0,9)
        d.texto_prompt.append(d.frases_ganon[numero])
        d.ganon["vida"] -= 1 #Le resta 1 de vida al enemigo
        mapaActual[2][47+d.ganon["vida"]] = " "

    return mapaActual
                
def comer(select): #Interaccion de comer #-mirar las direcciones
    if d.jugador["vidas"] == d.jugador["vidas_max"]: #Comprueba si el personaje ya tiene lla vida maxima
        d.texto_prompt.append("You already have your whole life complete")
    else:
        if select.lower() == "eat vegetable": #Comprueba si como un vegetal
            if d.inventarioComida["Vegetables"] < 0: #Comprueba si la comida que quieres esta en el inventario
                d.texto_prompt.append("You have no vegetables left")
            else: #Si tienes entonces te elimina 1 de comida y te añade la vida que necesites
                d.inventarioComida["Vegetables"] -= 1
                d.jugador["vidas"] += 1
                d.texto_prompt.append("You have increased 1 health and spent 1 vegetable")
        elif select.lower() == "eat salad": #Comprueba si como un ensalada
            if d.inventarioComida["Salads"] < 0: #Comprueba si la comida que quieres esta en el inventario
                d.texto_prompt.append("You don't have any salad left")
            else:#Si tienes entonces te elimina 1 de comida y te añade la vida que necesites
                d.inventarioComida["Salads"] -= 1
                for i in range(2): #Para no pasarse de la vida maxima comprueba si ya esta en su maximo de vida o no
                    if not d.jugador["vidas"] == d.jugador["vidas_max"]:
                        d.jugador["vidas"] += 1
                d.texto_prompt.append("You have increased 2 health and spent 1 salad")
        elif select.lower() == "eat pescatarian": #Comprueba si como un pescado
            if d.inventarioComida["Pescatarian"] < 0: #Comprueba si la comida que quieres esta en el inventario
                d.texto_prompt.append("You don't have any pescatarian left")
            else:#Si tienes entonces te elimina 1 de comida y te añade la vida que necesites
                d.inventarioComida["Pescatarian"] -= 1
                for i in range(3): #Para no pasarse de la vida maxima comprueba si ya esta en su maximo de vida o no
                    if not d.jugador["vidas"] == d.jugador["vidas_max"]:
                        d.jugador["vidas"] += 1
                d.texto_prompt.append("You have increased 3 health and spent 1 Pescatarian")
        elif select.lower() == "eat roasted": #Comprueba si como una carne cocinada
            if d.inventarioComida["Roasted"] < 0: #Comprueba si la comida que quieres esta en el inventario
                d.texto_prompt.append("You don't have anything toasted")
            else:#Si tienes entonces te elimina 1 de comida y te añade la vida que necesites
                d.inventarioComida["Roasted"] -= 1
                for i in range(4): #Para no pasarse de la vida maxima comprueba si ya esta en su maximo de vida o no
                    if not d.jugador["vidas"] == d.jugador["vidas_max"]:
                        d.jugador["vidas"] += 1
                d.texto_prompt.append("You have increased 4 health and spent 1 roast")
        else: #Si no existe la comida que ha puesto sale este promp
            d.texto_prompt.append("This food does not exist") #Este promp lo he añadido yo    

#--------------- Cocinar ----------------------
     
def cocinar(receta, inventario, mapaActual): # Funcion para cocinar comida 
    cocinar = False
    if mapaActual[d.jugador["posicion"][0]+1][d.jugador["posicion"][1]] == "C":
        cocinar = True
    
    elif mapaActual[d.jugador["posicion"][0]-1][d.jugador["posicion"][1]] == "C":
        cocinar = True
    
    elif mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]+1] == "C":
        cocinar = True
        
    elif mapaActual[d.jugador["posicion"][0]][d.jugador["posicion"][1]-1] == "C":
        cocinar = True
    
    
    if cocinar == True:
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
    
    else:
        d.texto_prompt.append("You can't cook here")

#Crea el menu inferior en base a lo que haya en el entorno.
def menuInferior():
   
    posicion = d.jugador["posicion"]
    
    menuInferior = "* Exit, Show, Go, Eat"

    if posicion[0] == 10:
        if d.localitzacions[d.jugador["mapa"]][posicion[0]-1][posicion[1]] == "T" or d.localitzacions[d.jugador["mapa"]][posicion[0]][posicion[1]+1]  == "T" or d.localitzacions[d.jugador["mapa"]][posicion[0]][posicion[1]-1]  == "T":

            menuInferior += ", Attack"

    
        if menuInferior.find("Attack") == -1:
        
            if d.localitzacions[d.jugador["mapa"]][posicion[0]-1][posicion[1]][0] in  ("Z","E") or d.localitzacions[d.jugador["mapa"]][posicion[0]][posicion[1]+1][0]  in  ("Z","E") or d.localitzacions[d.jugador["mapa"]][posicion[0]][posicion[1]-1][0]  in  ("Z","E") and d.jugador["arma_actual"] != " ":
                menuInferior += ", Attack"

        if d.localitzacions[d.jugador["mapa"]][posicion[0]-1][posicion[1]][0]  == "~" or d.localitzacions[d.jugador["mapa"]][posicion[0]][posicion[1]+1][0]   == "~" or d.localitzacions[d.jugador["mapa"]][posicion[0]][posicion[1]-1][0]   == "~":
            menuInferior += ", Fish"
        
        if d.localitzacions[d.jugador["mapa"]][posicion[0]-1][posicion[1]][0] in  ("S","M") or d.localitzacions[d.jugador["mapa"]][posicion[0]][posicion[1]+1][0] in  ("S","M") or d.localitzacions[d.jugador["mapa"]][posicion[0]][posicion[1]-1][0] in ("S","M"):
        
            menuInferior += ", Open"
    
    else:
        if d.localitzacions[d.jugador["mapa"]][posicion[0]+1][posicion[1]] == "T" or d.localitzacions[d.jugador["mapa"]][posicion[0]-1][posicion[1]] == "T" or d.localitzacions[d.jugador["mapa"]][posicion[0]][posicion[1]+1]  == "T" or d.localitzacions[d.jugador["mapa"]][posicion[0]][posicion[1]-1]  == "T":

            menuInferior += ", Attack"

    
        if menuInferior.find("Attack") == -1:
        
            if d.localitzacions[d.jugador["mapa"]][posicion[0]+1][posicion[1]][0] in  ("Z","E") or d.localitzacions[d.jugador["mapa"]][posicion[0]-1][posicion[1]][0] in  ("Z","E") or d.localitzacions[d.jugador["mapa"]][posicion[0]][posicion[1]+1][0]  in  ("Z","E") or d.localitzacions[d.jugador["mapa"]][posicion[0]][posicion[1]-1][0]  in  ("Z","E") and d.jugador["arma_actual"] != " ":
                menuInferior += ", Attack"

        if d.localitzacions[d.jugador["mapa"]][posicion[0]+1][posicion[1]][0] == "~" or d.localitzacions[d.jugador["mapa"]][posicion[0]-1][posicion[1]][0]  == "~" or d.localitzacions[d.jugador["mapa"]][posicion[0]][posicion[1]+1][0]   == "~" or d.localitzacions[d.jugador["mapa"]][posicion[0]][posicion[1]-1][0]   == "~":
            menuInferior += ", Fish"
        
        if d.localitzacions[d.jugador["mapa"]][posicion[0]+1][posicion[1]][0] in  ("S","M") or d.localitzacions[d.jugador["mapa"]][posicion[0]-1][posicion[1]][0] in  ("S","M") or d.localitzacions[d.jugador["mapa"]][posicion[0]][posicion[1]+1][0] in  ("S","M") or d.localitzacions[d.jugador["mapa"]][posicion[0]][posicion[1]-1][0] in ("S","M"):
        
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
        if d.jugador["mapa"] == "death" or d.jugador["mapa"] == "gerudo":
            mapaActual = d.localitzacions["hyrule"]
            d.texto_prompt.append("You are now in" + select[6:])
            d.jugador["mapa"] = "hyrule"
            zorro_visivilidad() 
            reiniciar_pesca()
            posicion_player = d.dades["hyrule"]["position"]
            return mapaActual, posicion_player
        
        elif d.jugador["mapa"] == "hyrule":
            d.texto_prompt.append("You already are in " + select[6:])
            return mapaActual, posicionfallo
        
        else:
            d.texto_prompt.append("You can't go to" + select[6:] + " from here")
            return mapaActual, posicionfallo

        
    elif select[6:].lower() == "gerudo":
        if d.jugador["mapa"] == "hyrule" or d.jugador["mapa"] == "necluda":
            mapaActual = d.localitzacions["gerudo"]
            d.texto_prompt.append("You are now in " + select[6:])
            d.jugador["mapa"] = "gerudo"
            zorro_visivilidad() 
            reiniciar_pesca()
            posicion_player = d.dades["gerudo"]["position"]
            return mapaActual, posicion_player

        elif d.jugador["mapa"] == "gerudo":
            d.texto_prompt.append("You already are in " + select[6:])
            return mapaActual, posicionfallo
        
        else:
            d.texto_prompt.append("You can't go to " + select[6:] + " from here")
            return mapaActual, posicionfallo
            
    elif select[6:].lower() == "death mountain":
        if d.jugador["mapa"] == "hyrule" or d.jugador["mapa"] == "necluda":
            mapaActual = d.localitzacions["death"]
            d.texto_prompt.append("You are now in " + select[6:])
            d.jugador["mapa"] = "death"
            zorro_visivilidad()
            reiniciar_pesca() 
            posicion_player = d.dades["death"]["position"]
            return mapaActual, posicion_player
        
        elif d.jugador["mapa"] == "death":
            d.texto_prompt.append("You already are in " + select[6:])
            return mapaActual, posicionfallo
        
        else:
            d.texto_prompt.append("You can't go to " + select[6:] + " from here")
            return mapaActual, posicionfallo
        
    elif select[6:].lower() == "necluda":
        if d.jugador["mapa"] == "death" or d.jugador["mapa"] == "gerudo":
            mapaActual = d.localitzacions["necluda"]
            d.texto_prompt.append("You are now in " + select[6:])
            d.jugador["mapa"] = "necluda"
            zorro_visivilidad() 
            reiniciar_pesca()
            posicion_player = d.dades["necluda"]["position"]
            return mapaActual, posicion_player
        
        elif d.jugador["mapa"] == "necluda":
            d.texto_prompt.append("You already are in " + select[6:])
            return mapaActual, posicionfallo
        
        else:
            d.texto_prompt.append("You can't go to " + select[6:] + " from here")
            return mapaActual, posicionfallo
        
    elif select[6:].lower() == "castle":
        if d.jugador["mapa"] == "hyrule":
            d.mapa_anterior = "hyrule"

        elif d.jugador["mapa"] == "gerudo":
            d.mapa_anterior = "gerudo"

        elif d.jugador["mapa"] == "death":
            d.mapa_anterior = "death"
        
        elif d.jugador["mapa"] == "necluda":
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
def trucos(select):
    if select[0:22].lower() == "cheat rename player to":
        if select[23:].lower().replace(" ", "").isalnum() and len(select[23:]) >= 3 and len(select[23:]) <= 10:
            d.jugador["nombre"] = select[23:]
            d.texto_prompt.append("Cheating:rename player to. Name changed to " + d.jugador["nombre"])

        
        else:
            d.texto_prompt.append("Incorrect name")
    
    elif select.lower() == "cheat add vegetable":
        añadirInventario("Vegetable", d.inventarioComida)
        d.texto_prompt.append("Cheating: add vegetable")
    elif select.lower() == "cheat add fish":
        añadirInventario("Fish", d.inventarioComida)
        d.texto_prompt.append("Cheating: add fish")
    elif select.lower() == "cheat add meat":
        añadirInventario("Meat", d.inventarioComida)
        d.texto_prompt.append("Cheating: add meat")
    elif select.lower() == "cheat cook salad":
        cocinar("cook salad", d.inventarioComida)
        d.texto_prompt.append("Cheating: cook salad")
    elif select.lower() == "cheat cook pescatarian":
        cocinar("cook pescatarian", d.inventarioComida)
        d.texto_prompt.append("Cheating: cook pescatarian")
    elif select.lower() == "cheat cook roasted":
        cocinar("cook roasted", d.inventarioComida)
        d.texto_prompt.append("Cheating: cook roasted")
    elif select.lower() == "cheat add wood sword":
        añadirInventario("Wood Sword", d.inventarioArmas)
        d.texto_prompt.append("Cheating: add wood sword")
    elif select.lower() == "cheat add sword":
        añadirInventario("Sword", d.inventarioArmas)
        d.texto_prompt.append("Cheating: add sword")
    elif select.lower() == "cheat add wood shield":
        añadirInventario("Wood Shield", d.inventarioArmas)
        d.texto_prompt.append("Cheating: add wood shield")
    elif select.lower() == "cheat add shield":
        añadirInventario("Shield", d.inventarioArmas)
        d.texto_prompt.append("Cheating: add shield")
    elif select.lower() == "cheat open sanctuaries":
        lista_mapas = list(d.localitzacions.keys())

        for element in lista_mapas:

            for santuario in d.localitzacions[element]["Santuarios"]["posicion"]:
               
               santuario[3] = True

            d.jugador["vidas_max"] = 10

        d.texto_prompt.append("Cheating: open sanctuaries")
    
    elif select.lower() == "cheat game over":
        d.jugador["vidas"] = 0
        d.texto_prompt.append("Cheating: game over")
    elif select.lower() == "cheat win game":
        d.ganon["vida"] = 0
        d.texto_prompt.append("Cheating: win game")
    else:
        d.texto_prompt.append("Invalid option")
        
        

def imprimir_partidas_guardadas():
    saved_games = [["* Saved games * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"]]
    
    if len(d.datosPartidas) > 1:
        for i in d.datosPartidas:
            saved_games.append(["* {}: {} - {}, {}".format(i[0], i[4], i[1], i[9]).ljust(72) + "♥ {}/{} *".format(i[5], i[6])])
        
        while len(saved_games) != 11:
            saved_games.append(["* ".ljust(78) + "*"]) 
    
    elif len(d.datosPartidas) == 1 and type(d.datosPartidas[0]) == list:
        for i in d.datosPartidas:
            saved_games.append(["* {}: {} - {}, {}".format(i[0], i[4], i[1], i[9]).ljust(72) + "♥ {}/{} *".format(i[5], i[6])])
        
        while len(saved_games) != 11:
            saved_games.append(["* ".ljust(78) + "*"])
    
    else:
        saved_games.append(["* {}".format(d.datosPartidas[0]).ljust(78) + "*"])
        
        while len(saved_games) != 11:
            saved_games.append(["* ".ljust(78) + "*"]) 
        
    saved_games.append(["* Play X, Erase X, Help, Back * * * * * * * * * * * * * * * * * * * * * * * * *"])
    
    imprimirmapa_menu(saved_games)




def atacar(posicionplayer, mapaActual, objeto):
    if posicionplayer[0] != 10 and mapaActual[posicionplayer[0]+1][posicionplayer[1]] == objeto:
        if objeto == "E":
            mapaActual = enemigos(mapaActual)
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
            mapaActual = enemigos(mapaActual)
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
            mapaActual = enemigos(mapaActual)
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
            mapaActual = enemigos(mapaActual)
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

    
#------------------------ Blood moon ----------------
    
def blood_moonn():
    if d.jugador["bloodMoonCoutdown"] == 25:
        d.jugador["bloodMoonCoutdown"] = 0
        d.jugador["totalBloodMoon"] += 1
        d.dades["hyrule"]["E"]["posicion"][0][3] = 1
        d.dades["hyrule"]["E"]["posicion"][1][3] = 9
        d.dades["gerudo"]["E"]["posicion"][0][3] = 1
        d.dades["gerudo"]["E"]["posicion"][1][3] = 2
        d.dades["death"]["E"]["posicion"][0][3] = 2
        d.dades["death"]["E"]["posicion"][1][3] = 2
        d.dades["necluda"]["E"]["posicion"][0][3] = 1
        d.dades["necluda"]["E"]["posicion"][0][3] = 1
    else:
        d.jugador["bloodMoonCoutdown"] += 1




def vida_enemigo(mapaActual):
    if d.jugador["mapa"] != "castle":
        for i in d.dades[d.jugador["mapa"]]["E"]["posicion"]: #Busca que arbol tiene la vida al 0 y lo cambia por el numero del contador que tenga en ese momento
            mapaActual[i[0]][i[1]+1] = str(i[3])
            


#--Consultas menu principal BBDD:

def consultaJugadores():
    cursor = db.cursor()

    cursor.execute("Select distinct  user_name, date_started from game;")
    resultados = cursor.fetchall()

    for element in resultados:
        print(element)

def partidasXJugador():
        cursor = db.cursor()


        cursor.execute("Select user_name, count(*) from game group by user_name;")

        resultados = cursor.fetchall()

        for element in resultados:
            print(element)

def ArmasConseguidas():
        cursor = db.cursor()

        cursor.execute("SELECT g.user_name AS Usuario, w.weapon_name AS Arma, COUNT() AS CantidadObtenida, MAX(g.date_started) AS FechaPartidaMasUsos FROM game g JOIN game_weapons w ON g.game_id = w.game_id GROUP BY g.user_name, w.weapon_name ORDER BY Usuario, CantidadObtenida DESC;")

        resultados = cursor.fetchall()

        for element in resultados:
            print(element)

def AlimentosConseguidos():
        cursor = db.cursor()

        cursor.execute("SELECT  g.user_name AS Usuario, gf.food_name AS Alimento, SUM(gf.quanntity_remaining) AS CantidadObtenida,  max(g.date_started)  as MaxDate FROM game g JOIN game_food gf ON g.game_id = gf.game_id GROUP BY  g.user_name, gf.food_name ORDER BY     Usuario, CantidadObtenida DESC;")
        resultados = cursor.fetchall()

        for element in resultados:
            print(element)

def MediaBloodMoon():

        cursor = db.cursor()

        cursor.execute("Select avg(blood_moon_appearances) from game;")
        resultados = cursor.fetchall()

        for element in resultados:
            print(element)

def maxBloodMoon():

        cursor = db.cursor()

        cursor.execute("Select g.date_started, g.user_name, g.blood_moon_appearances from game g where g.blood_moon_appearances = (select max(g1.blood_moon_appearances)from game g1) ")
        resultados = cursor.fetchall()

        for element in resultados:

            print(element)




def saveInicialGame():

        #Al iniciar la partida guarda la tabla game.
        query = "Insert into game(user_name,date_started,hearts_remaining, blood_moon_countdown,blood_moon_appearances, region, max_live, xpos, ypos ) Values(%s,  NOW(), %s, %s, %s,%s, %s,%s, %s)"
        val = (d.jugador["name"], d.jugador["vidas"], 25,0, "Hyrule", d.jugador["vidas_max"], d.jugador["posicion"][0], d.jugador["posicion"][1])
        cursor.execute(query, val)
        d.jugador["id_game"] = cursor.lastrowid
        print(d.jugador["id_game"])
        db.commit()

        #Y se añaden los enemigos.
        lista_objetos = d.dades.keys()
        for element in lista_objetos:
            for element1 in d.dades[element]["E"]["posicion"]:
                print(element1)
                query = "Insert into game_enemies(game_id, region, num, xpos, ypos, lives_remaining) Values(%s, %s, %s, %s,%s, %s)"
                val = (d.jugador["id_game"],element, element1[2],  element1[0], element1[1], element1[3])
                cursor.execute(query, val)
        db.commit()
       

def saveGame():

    lista_inventario = []

    #Actualizar tabla game.
    query = "UPDATE game SET hearts_remaining = %s, blood_moon_countdown = %s, blood_moon_appearances = %s, region = %s, max_live = %s, xpos = %s, ypos = %s, date_started = NOW() WHERE game_id = %s;"
    val = (d.jugador["vidas"], d.jugador["bloodMoonCoutdown"], d.jugador["totalBloodMoon"], d.jugador["mapa"], d.jugador["vidas_max"], d.jugador["id_game"], d.jugador["posicion"][0], d.jugador["posicion"][1])
    print(d.jugador["id_game"])
    cursor.execute(query, val)
    db.commit()

    #Actualizar enemigos con update.
    lista_inventario = d.dades.keys()
    for element in lista_inventario:
            for element1 in d.dades[element]["E"]["posicion"]:
                print(element1)
                query = "UPDATE game_enemies SET xpos = %s, ypos = %s, lives_remaining = %s WHERE game_id = %s AND region = %s AND num = %s;"
                val = (element1[0], element1[1], element1[3], d.jugador["id_game"],element, element1[2])
                cursor.execute(query, val)
    db.commit()

    #Actualizar o insertar datos en la tabla food
    lista_inventario = list(d.inventarioComida.keys())
    query = "INSERT INTO game_food(game_id, food_name, quanntity_remaining) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE quanntity_remaining = %s;"
    
    for element in lista_inventario:
    
        val = (d.jugador["id_game"], element , d.inventarioComida[element], d.inventarioComida[element])
        cursor.execute(query, val)
    db.commit()

    #Insertamos datos de santuraios. Si ya existe ese santuario en la BBDD no inserta ningun datos.
    
    lista_inventario = d.dades.keys()
    query = "INSERT IGNORE INTO game_sactuaries_opened(game_id, region, num, xpos, ypos) VALUES (%s, %s, %s, %s,%s);"

    for element in lista_inventario:
            for element1 in d.dades[element]["Santuarios"]["posicion"]:
                
                if element1[3] == True:
                    
                    val = (d.jugador["id_game"],element, element1[4],  element1[0], element1[1])
                    cursor.execute(query, val)
    db.commit()
    
    #Actualizar/insertar armas

    lista_inventario = d.inventarioArmas.keys()
    query = "INSERT INTO game_weapons(game_id, weapon_name, lives_remaining, equiped, tipo) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE lives_remaining = %s, equiped = %s;"
    
    for element in lista_inventario:
        
        if d.jugador["arma_actual"] == element or d.jugador["escudo_actual"] == element:
             equiped = True
        else:
             equiped = False

        val = (d.jugador["id_game"], element , d.inventarioArmas[element]["usos"], equiped, d.inventarioArmas[element]["tipo"] , d.inventarioArmas[element]["usos"], equiped  )
        cursor.execute(query, val)
    db.commit()

    #Actualizar, insertar o eliminar(en caso de que se cierre) cofres.

    lista_inventario =  d.dades.keys()

    for element in lista_inventario:
            for element1 in d.dades[element]["M"]["posicion"]:
                print(element1)
                if element1[2] == False:
                    query = "Delete from game_chests_opened where game_id = %s and num = %s;"
                    val = (d.jugador["id_game"], element1[3])
                    cursor.execute(query, val)
                elif element1[2] == True:
                    query = "INSERT IGNORE INTO game_chests_opened(game_id, region, num, xpos, ypos) VALUES (%s, %s, %s, %s,%s);"
                    val = (d.jugador["id_game"], element, element1[3], element1[0], element1[1])
                    cursor.execute(query, val)
    db.commit()

#Descarga los datos de jugador (tabla game) para mostrarlos en el menu de seleccion de partida.
def descargarGuardadas():
    
    query = "Select game_id, user_name, xpos, ypos, date_started, hearts_remaining, max_live,blood_moon_countdown, blood_moon_appearances, region from game limit 8;"
    cursor.execute(query)
    resultados = cursor.fetchall()

    if resultados:
        for element in resultados:
            
            d.datosPartidas.append(element)

    else: d.datosPartidas.append("No hay partidas guardadas, inicia una nueva.")



#Se le pasa el numero de partida que se ha seleccionado.
def selectAndChargePartida(numero):
    datos = []
    for element in d.datosPartidas:
        
        if numero == element[0]:
             
            d.jugador["name"] = element[1]
            d.jugador["posicion"].append(element[2])
            d.jugador["posicion"].append(element[3])
            d.jugador["vidas_max"] = element[6]
            d.jugador["vidas"] = element[5]
            d.jugador["bloodMoonCoutdown"] = element[7]
            d.jugador["mActual"] = element[9]
            d.jugador["id_game"] = element[0]
        
        break

    #Recuperamos la comida
    query = "Select food_name, quanntity_remaining  from game_food where game_id = %s;"
    val=(d.jugador["id_game"],)
    cursor.execute(query,val)
    resultados = cursor.fetchall()

    if resultados:
        for element in resultados:
            
            d.inventarioComida[element[0]] = element[1] 
    
    
    #Recuperamos armas
        
    query = "Select weapon_name, equiped, tipo, lives_remaining from game_weapons where game_id = %s;"
    val=(d.jugador["id_game"],)
    cursor.execute(query,val)
    resultados = cursor.fetchall()

    if resultados:
        for element in resultados:
            
            d.inventarioArmas[element[0]] = {
                
                "tipo" : element[2],
                "usos" : element[3]
                }

            if element[1] == True and "Shield" in element[0]:
                
                d.jugador["escudo_actual"] = element[0]
            
            elif element[1] == True and "Sword" in element[0]: 

                d.jugador["arma_actual"] = element[0]   

    #Recuperamos enemigos
                
    query = "Select region, num, xpos, ypos,lives_remaining from game_enemies where game_id = %s;"
    val=(d.jugador["id_game"],)
    cursor.execute(query,val)
    resultados = cursor.fetchall()

    
    if resultados:
         
         for element in resultados:
            index = resultados.index(element)
            for element1 in d.dades[resultados[index][0]]["E"]["posicion"]:
                index2 = d.dades[resultados[index][0]]["E"]["posicion"].index(element1)
               
                if element[1] == element1[2]:

                    d.dades[resultados[index][0]]["E"]["posicion"][index2][0] = element[2]
                    d.dades[resultados[index][0]]["E"]["posicion"][index2][1] = element[3]
                    d.dades[resultados[index][0]]["E"]["posicion"][index2][3] = element[4]
                    print(d.dades[resultados[index][0]]["E"]["posicion"][index2])
                     
   
    #Recuperamos Santuarios abiertos:
                
    query = "Select region, num from game_sactuaries_opened where game_id = %s;"
    val=(d.jugador["id_game"],)
    cursor.execute(query,val)
    resultados = cursor.fetchall()

    
    if resultados:
         
         for element in resultados:
            index = resultados.index(element)
            for element1 in d.dades[resultados[index][0]]["Santuarios"]["posicion"]:
                index2 = d.dades[resultados[index][0]]["Santuarios"]["posicion"].index(element1)
               
                if element[1] == element1[4]:

                    d.dades[resultados[index][0]]["Santuarios"]["posicion"][index2][3] = True
                    
    #Recuperamos cofes abiertos:
                
    query = "Select region, num from game_chests_opened where game_id = %s;"
    val=(d.jugador["id_game"],)
    cursor.execute(query,val)
    resultados = cursor.fetchall()

    
    if resultados:
         
         for element in resultados:
            index = resultados.index(element)
            for element1 in d.dades[resultados[index][0]]["M"]["posicion"]:
                index2 = d.dades[resultados[index][0]]["M"]["posicion"].index(element1)
               
                if element[1] == element1[3]:

                    d.dades[resultados[index][0]]["M"]["posicion"][index2][2] = True
   

                    



