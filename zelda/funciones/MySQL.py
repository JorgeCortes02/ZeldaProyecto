import mysql.connector
print("hola1")
# Conectar a la base de datos
db = mysql.connector.connect(
    host="172.187.226.29",  # Cambia a tu dirección IP
    user="root2",
    passwd="EsteveTerradas2023.",  # root
 
    database="ZeldaBBDD"
)
print("hola2")
# Crear un cursor
cursor = db.cursor()
print("hola3")
# Consulta para obtener información sobre las columnas de la tabla 'game'
query = "Show columns from game;"
print("hola")
# Ejecutar la consulta
cursor.execute(query)

# Imprimir los resultados
for x in cursor:
    print(x)
# Cerrar el cursor y la conexión
cursor.close()
db.close()

