import mysql.connector


partidasxJugador = "Select user_name, count(*) from game group by user_name;"

ArmasUsuarios = "SELECT g.user_name AS Usuario, w.weapon_name AS Arma, COUNT(*) AS CantidadObtenida, MAX(g.date_started) AS FechaPartidaMasUsos FROM game g JOIN game_weapons w ON g.game_id = w.game_id GROUP BY g.user_name, w.weapon_name ORDER BY Usuario, CantidadObtenida DESC;"


# Conectar a la base de datos
db = mysql.connector.connect(
    host="172.187.226.29",  # Cambia a tu dirección IP
    user="root2",
    passwd="EsteveTerradas2023.", 
    database="ZeldaBBDD"
)



def consultasBBDD():

    jugadores = "Select distinct  user_name, date_started from game;"

    cursor.execute(ArmasUsuarios)
    resultados = cursor.fetchall()

    for element in resultados:
        print(element)


     





# Crear un cursor
cursor = db.cursor()
consultasBBDD()