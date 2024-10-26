import mysql.connector

class DatabaseConnection:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="trabalhobd_hotel",
            auth_plugin='mysql_native_password'
        )

    def get_connection(self):
        return self.connection

    def close_connection(self):
        self.connection.close()
