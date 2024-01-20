import mysql.connector

db = mysql.connector.connect(
    host="172.187.226.29",  # Cambia a tu dirección IP
    user="root2",
    passwd="EsteveTerradas2023.", 
    database="ZeldaBBDD"
)



mitjanaBloodMoon = "Select avg(blood_moon_appearances) from game;"

partidaBloodMoon = "Select g.date_started, g.user_name, g.blood_moon_appearances from game g where g.blood_moon_appearances = (select max(g1.blood_moon_appearances)from game g1) "

# Conectar a la base de datos




def consultasBBDD():
    cursor = db.cursor()
    cursor.execute(partidaBloodMoon)
    resultados = cursor.fetchall()

    for element in resultados:
        print(element)


     





