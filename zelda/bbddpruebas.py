import mysql.connector
import funciones.datos as d


def saveInicialGame():

        #Al iniciar la partida guarda la tabla game.
        query = "Insert into game(user_name,date_started,hearts_remaining, blood_moon_countdown,blood_moon_appearances, region, max_live, xpos, ypos ) Values(%s, CURRENT_TIMESTAMP, %s, %s, %s,%s, %s,%s, %s)"
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
    query = "UPDATE game SET hearts_remaining = %s, blood_moon_countdown = %s, blood_moon_appearances = %s, region = %s, max_live = %s WHERE game_id = %s, xpos = %s, ypos = %s;"
    val = (d.jugador["vidas"], d.jugador["bloodMoonCoutdown"], d.jugador["totalBloodMoon"], d.jugador["mActual"], d.jugador["vidas_max"], d.jugador["id_game"], d.jugador["posicion"][0], d.jugador["posicion"][1])
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

        val = (d.jugador["id_game"], element , d.inventarioArmas[element]["usos"], equiped, d.inventarioArmas[element]["usos"], equiped,d.inventarioArmas[element]["tipo"]  )
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
    
    query = "Select game_id, user_name, xpos, ypos, date_started, hearts_remaining, max_lives ,blood_moon_countdown, blood_moon_appearances, region from game limit 8;"
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

   
# Conectar a la base de datos
db = mysql.connector.connect(
    host="172.187.226.29",  # Cambia a tu dirección IP
    user="root2",
    passwd="EsteveTerradas2023.", 
    database="ZeldaBBDD"
)






     





# Crear un cursor
cursor = db.cursor()

selectAndChargePartida(3)


