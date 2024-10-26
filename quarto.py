
from DatabaseConnection import DatabaseConnection

class Quarto:
    def __init__(self, num_quarto=None, tipo_quarto=None, valor_diaria=None,
                 limite_pessoas=None, cpf=None):
        self._num_quarto = num_quarto
        self._tipo_quarto = tipo_quarto
        self._valor_diaria = valor_diaria
        self._limite_pessoas = limite_pessoas
        self._cpf = cpf

    # Getters and Setters
    @property
    def num_quarto(self):
        return self._num_quarto

    @num_quarto.setter
    def num_quarto(self, value):
        self._num_quarto = value

    @property
    def tipo_quarto(self):
        return self._tipo_quarto

    @tipo_quarto.setter
    def tipo_quarto(self, value):
        self._tipo_quarto = value

    @property
    def valor_diaria(self):
        return self._valor_diaria

    @valor_diaria.setter
    def valor_diaria(self, value):
        self._valor_diaria = value

    @property
    def limite_pessoas(self):
        return self._limite_pessoas

    @limite_pessoas.setter
    def limite_pessoas(self, value):
        self._limite_pessoas = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    # Método para criar um quarto
    def create_quarto(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO QUARTO (NUM_QUARTO, TIPO_QUARTO, VALOR_DIARIA, LIMITE_PESSOAS, CPF) "
            "VALUES (%s, %s, %s, %s, %s)",
            (self.num_quarto, self.tipo_quarto, self.valor_diaria,
             self.limite_pessoas, self.cpf)
        )
        connection.commit()
        cursor.close()
        db.close_connection()
        print("Quarto criado com sucesso!")

    # Método para ler quartos
    @staticmethod
    def read_quartos():
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT NUM_QUARTO, TIPO_QUARTO, VALOR_DIARIA, CPF FROM QUARTO")
        quartos = cursor.fetchall()
        if not quartos:
            print("Nenhum quarto encontrado.")
        else:
            print("+" + "-" * 50 + "+")
            print("|{:^10}|{:^15}|{:^12}|{:^10}|".format(
                "Nº Quarto", "Tipo", "Diária (R$)", "Situação"))
            print("+" + "-" * 50 + "+")
            for quarto in quartos:
                num_quarto = quarto[0]
                tipo_quarto = quarto[1]
                valor_diaria = quarto[2]
                cpf_cliente = quarto[3]
                situacao = "Ocupado" if cpf_cliente else "Livre"
                print("|{:^10}|{:^15}|{:^12.2f}|{:^10}|".format(
                    num_quarto, tipo_quarto, valor_diaria, situacao))
            print("+" + "-" * 50 + "+")
        cursor.close()
        db.close_connection()

    # Método para atualizar um quarto
    def update_quarto(self):
        if None in (self.tipo_quarto, self.valor_diaria, self.limite_pessoas, self.num_quarto):
            print("Erro: Todos os campos devem ser preenchidos para atualizar o quarto.")
            return
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE QUARTO SET TIPO_QUARTO = %s, VALOR_DIARIA = %s, LIMITE_PESSOAS = %s WHERE NUM_QUARTO = %s",
            (self.tipo_quarto, self.valor_diaria, self.limite_pessoas, self.num_quarto)
        )
        connection.commit()
        cursor.close()
        db.close_connection()
        print("Quarto atualizado com sucesso!")

    # Método para deletar um quarto
    def delete_quarto(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM QUARTO WHERE NUM_QUARTO = %s", (self.num_quarto,))
        connection.commit()
        cursor.close()
        db.close_connection()
        print("Quarto deletado com sucesso!")

    # Método para verificar se um quarto existe
    @staticmethod
    def quarto_exists(num_quarto):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM QUARTO WHERE NUM_QUARTO = %s", (num_quarto,))
        quarto = cursor.fetchone()
        cursor.close()
        db.close_connection()
        return quarto is not None

    # Método para verificar se um quarto está ocupado
    @staticmethod
    def is_quarto_ocupado(num_quarto):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT CPF FROM QUARTO WHERE NUM_QUARTO = %s", (num_quarto,))
        result = cursor.fetchone()
        cursor.close()
        db.close_connection()
        return result[0] is not None

    # Método para atualizar apenas o CPF do quarto
    def atualizar_cpf(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE QUARTO SET CPF = %s WHERE NUM_QUARTO = %s",
            (self.cpf, self.num_quarto)
        )
        connection.commit()
        cursor.close()
        db.close_connection()
        print("CPF do quarto atualizado com sucesso!")
