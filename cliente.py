import datetime
from DatabaseConnection import DatabaseConnection

class Cliente:
    def __init__(self, cpf=None, telefone=None, nome=None, email=None, data_nascimento=None, cep=None):
        self._cpf = cpf
        self._telefone = telefone
        self._nome = nome
        self._email = email
        self._data_nascimento = data_nascimento
        self._cep = cep
        
    # Getters and Setters
    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, value):
        self._telefone = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, value):
        self._data_nascimento = value

    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, value):
        self._cep = value

    # Operações CRUD
    def create_cliente(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO CLIENTE (CPF, TELEFONE, NOME, EMAIL, DATA_NASCIMENTO, CEP) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (self.cpf, self.telefone, self.nome, self.email, self.data_nascimento, self.cep)
        )
        connection.commit()
        cursor.close()
        db.close_connection()
        print("Cliente criado com sucesso!")

    @staticmethod
    def read_clientes():
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT CPF, TELEFONE, NOME, EMAIL, DATA_NASCIMENTO, CEP FROM CLIENTE")
        clientes = cursor.fetchall()
        if not clientes:
            print("Não há clientes cadastrados.")
        else:
            print("+" + "-" * 110 + "+")
            print("|{:^15}|{:^15}|{:^20}|{:^30}|{:^15}|{:^10}|".format(
                "CPF", "Telefone", "Nome", "Email", "Data Nasc.", "CEP"))
            print("+" + "-" * 110 + "+")
            for cliente in clientes:
                print("|{:^15}|{:^15}|{:^20}|{:^30}|{:^15}|{:^10}|".format(
                    cliente[0], cliente[1], cliente[2], cliente[3], cliente[4].strftime("%d-%m-%Y"), cliente[5]))
                print("+" + "-" * 110 + "+")
        cursor.close()
        db.close_connection()

    def update_cliente(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE CLIENTE SET TELEFONE = %s, NOME = %s, EMAIL = %s, DATA_NASCIMENTO = %s, CEP = %s WHERE CPF = %s",
            (self.telefone, self.nome, self.email, self.data_nascimento, self.cep, self.cpf)
        )
        connection.commit()
        cursor.close()
        db.close_connection()
        print("Cliente atualizado com sucesso!")

    def delete_cliente(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM CLIENTE WHERE CPF = %s", (self.cpf,))
        connection.commit()
        cursor.close()
        db.close_connection()
        print("Cliente deletado com sucesso!")

    @staticmethod
    def cliente_exists(cpf):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM CLIENTE WHERE CPF = %s", (cpf,))
        cliente = cursor.fetchone()
        cursor.close()
        db.close_connection()
        return cliente is not None
