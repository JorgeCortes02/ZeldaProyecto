import mysql.connector

try:
    conexion = mysql.connector.connect(
        user="root",
        host="127.0.0.1",
        database="ZeldaBBDD",
        port="3306",
    )

    micursor = conexion.cursor()

    micursor.execute("SHOW DATABASES")

    consulta = micursor.fetchall()

    for db in consulta:
        print(db)  

    conexion.close() 

except mysql.connector.Error as error:
    print("Error al conectar a la base de datos:", error)
