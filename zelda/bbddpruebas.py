import mysql.connector
import funciones.datos as d


def saveInicialGame():

        #Al iniciar la partida guarda la tabla game.
        query = "Insert into game(user_name,date_started,hearts_remaining, blood_moon_countdown,blood_moon_appearances, region, max_live ) Values(%s, CURRENT_TIMESTAMP, %s, %s, %s,%s, %s)"
        val = (d.jugador["name"], d.jugador["vidas"], 25,0, "Hyrule", d.jugador["vidas_max"])
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
    query = "UPDATE game SET hearts_remaining = %s, blood_moon_countdown = %s, blood_moon_appearances = %s, region = %s, max_live = %s WHERE game_id = %s;"
    val = (d.jugador["vidas"], d.jugador["bloodMoonCoutdown"], d.jugador["totalBloodMoon"], d.jugador["mActual"], d.jugador["vidas_max"], d.jugador["id_game"])
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
    query = "INSERT INTO game_weapons(game_id, weapon_name, lives_remaining, equiped) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE lives_remaining = %s, equiped = %s;"
    
    for element in lista_inventario:
        
        if d.jugador["arma_actual"] == element or d.jugador["escudo_actual"] == element:
             equiped = True
        else:
             equiped = False

        val = (d.jugador["id_game"], element , d.inventarioArmas[element]["usos"], equiped, d.inventarioArmas[element]["usos"], equiped )
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

print("hola1")
# Conectar a la base de datos
db = mysql.connector.connect(
    host="172.187.226.29",  # Cambia a tu dirección IP
    user="root2",
    passwd="EsteveTerradas2023.", 
    database="ZeldaBBDD"
)

# Crear un cursor
cursor = db.cursor()


saveGame()




