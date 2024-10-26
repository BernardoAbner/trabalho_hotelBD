from DatabaseConnection import DatabaseConnection

class Reserva:
    def __init__(self, num_reserva=None, data_inicio=None, data_final=None,
                 quantidade_pessoas=None, valor_reserva=None, cpf=None,
                 num_quarto=None, cafe_incluso=0):
        self._num_reserva = num_reserva
        self._data_inicio = data_inicio
        self._data_final = data_final
        self._quantidade_pessoas = quantidade_pessoas
        self._valor_reserva = valor_reserva
        self._cpf = cpf
        self._num_quarto = num_quarto
        self._cafe_incluso = cafe_incluso

    # Getters and Setters
    @property
    def num_reserva(self):
        return self._num_reserva

    @num_reserva.setter
    def num_reserva(self, value):
        self._num_reserva = value

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, value):
        self._data_inicio = value

    @property
    def data_final(self):
        return self._data_final

    @data_final.setter
    def data_final(self, value):
        self._data_final = value

    @property
    def quantidade_pessoas(self):
        return self._quantidade_pessoas

    @quantidade_pessoas.setter
    def quantidade_pessoas(self, value):
        self._quantidade_pessoas = value

    @property
    def valor_reserva(self):
        return self._valor_reserva

    @valor_reserva.setter
    def valor_reserva(self, value):
        self._valor_reserva = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @property
    def num_quarto(self):
        return self._num_quarto

    @num_quarto.setter
    def num_quarto(self, value):
        self._num_quarto = value

    @property
    def cafe_incluso(self):
        return self._cafe_incluso

    @cafe_incluso.setter
    def cafe_incluso(self, value):
        self._cafe_incluso = value

    # Operações CRUD
    def create_reserva(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO RESERVA (NUM_RESERVA, DATA_INICIO, DATA_FINAL, QUANTIDADE_PESSOAS, "
            "VALOR_RESERVA, CPF, NUM_QUARTO, CAFE_INCLUSO) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (self.num_reserva, self.data_inicio, self.data_final, self.quantidade_pessoas,
             self.valor_reserva, self.cpf, self.num_quarto, self.cafe_incluso)
        )
        connection.commit()
        cursor.close()
        db.close_connection()
        print(f"Reserva número {self.num_reserva} criada com sucesso!")

    @staticmethod
    def read_reservas():
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT NUM_RESERVA, DATA_INICIO, DATA_FINAL, QUANTIDADE_PESSOAS, "
            "VALOR_RESERVA, CPF, NUM_QUARTO, CAFE_INCLUSO FROM RESERVA"
        )
        reservas = cursor.fetchall()
        if not reservas:
            print("Não há reservas cadastradas.")
        else:
            print("+" + "-" * 101 + "+")
            print("|{:^12}|{:^15}|{:^15}|{:^10}|{:^12}|{:^12}|{:^10}|{:^8}|".format(
                "Nº Reserva", "Início", "Fim", "Pessoas", "Valor (R$)", "CPF", "Quarto", "Café"))
            print("+" + "-" * 101 + "+")
            for reserva in reservas:
                print("|{:^12}|{:^15}|{:^15}|{:^10}|{:^12.2f}|{:^12}|{:^10}|{:^8}|".format(
                    reserva[0], reserva[1].strftime("%d-%m-%Y"), reserva[2].strftime("%d-%m-%Y"),
                    reserva[3], reserva[4], reserva[5], reserva[6],
                    "Sim" if reserva[7] == 1 else "Não"))
                print("+" + "-" * 101 + "+")
        cursor.close()
        db.close_connection()

    def update_reserva(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE RESERVA SET DATA_INICIO = %s, DATA_FINAL = %s, QUANTIDADE_PESSOAS = %s, "
            "VALOR_RESERVA = %s, CPF = %s, NUM_QUARTO = %s, CAFE_INCLUSO = %s "
            "WHERE NUM_RESERVA = %s",
            (self.data_inicio, self.data_final, self.quantidade_pessoas,
             self.valor_reserva, self.cpf, self.num_quarto, self.cafe_incluso, self.num_reserva)
        )
        connection.commit()
        cursor.close()
        db.close_connection()
        print("Reserva atualizada com sucesso!")

    def delete_reserva(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM RESERVA WHERE NUM_RESERVA = %s", (self.num_reserva,))
        connection.commit()
        cursor.close()
        db.close_connection()
        print("Reserva deletada com sucesso!")

    @staticmethod
    def reserva_exists(num_reserva):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM RESERVA WHERE NUM_RESERVA = %s", (num_reserva,))
        reserva = cursor.fetchone()
        cursor.close()
        db.close_connection()
        return reserva is not None
