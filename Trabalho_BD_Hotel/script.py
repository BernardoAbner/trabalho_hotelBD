import mysql.connector
from mysql.connector import Error

# Inicializa a variável connection
connection = None

try:
    connection = mysql.connector.connect(
        host='localhost', 
        database='trabalhobd_hotel',
        user='root',  
        password='1234'  
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Conectado ao servidor MySQL versão ", db_info)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("Conectado ao banco de dados: ", record)

except Error as e:
    print("Erro ao conectar ao MySQL:", e)

finally:
    if connection is not None and connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão com o MySQL foi encerrada")
