import mysql.connector
import datetime
import random

# Conectar ao banco de dados
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="trabalhobd_hotel",
        auth_plugin='mysql_native_password'
    )

def formatar_data(data):
    return data.strftime("%d-%m-%Y") if isinstance(data, datetime.date) else data


# Funções CRUD para CLIENTE
def create_cliente():
    cpf = input("Informe o CPF: ")
    telefone = input("Informe o Telefone: ")
    nome = input("Informe o Nome: ")
    email = input("Informe o Email: ")

    while True:
        data_nascimento = input("Informe a Data de Nascimento (DD-MM-YYYY): ")
        try:
            data_nascimento = datetime.datetime.strptime(data_nascimento, "%d-%m-%Y").date()
            data_nascimento = data_nascimento.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Data inválida. Tente novamente.")

    cep = input("Informe o CEP: ")

    db = connect()
    cursor = db.cursor()
    cursor.execute("INSERT INTO CLIENTE (CPF, TELEFONE, NOME, EMAIL, DATA_NASCIMENTO, CEP) VALUES (%s, %s, %s, %s, %s, %s)", 
                   (cpf, telefone, nome, email, data_nascimento, cep))
    db.commit()
    cursor.close()
    db.close()
    print("Cliente criado com sucesso!")


def read_clientes():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT CPF, TELEFONE, NOME, EMAIL, DATA_NASCIMENTO, CEP FROM CLIENTE")
    
    clientes = cursor.fetchall()
    if not clientes:
        print("Não há clientes cadastrados.")
    else:
        print("+" + "-" * 110 + "+")
        print("|{:^15}|{:^15}|{:^20}|{:^30}|{:^15}|{:^10}|".format("CPF", "Telefone", "Nome", "Email", "Data Nasc.", "CEP"))
        print("+" + "-" * 110 + "+")
        
        for cliente in clientes:
            print("|{:^15}|{:^15}|{:^20}|{:^30}|{:^15}|{:^10}|".format(
                cliente[0], cliente[1], cliente[2], cliente[3], formatar_data(cliente[4]), cliente[5]))
            print("+" + "-" * 110 + "+")
    
    cursor.close()
    db.close()


def update_cliente():
    cpf = input("Informe o CPF do cliente que deseja atualizar: ")
    
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM CLIENTE WHERE CPF = %s", (cpf,))
    cliente = cursor.fetchone()

    if not cliente:
        print("Cliente não encontrado.")
        cursor.close()
        db.close()
        return  
    
    telefone = input("Informe o novo Telefone: ")
    nome = input("Informe o novo Nome: ")
    email = input("Informe o novo Email: ")

    while True:
        data_nascimento = input("Informe a nova Data de Nascimento (DD-MM-YYYY): ")
        try:
            data_nascimento = datetime.datetime.strptime(data_nascimento, "%d-%m-%Y").date()
            data_nascimento = data_nascimento.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Data inválida. Tente novamente.")

    cep = input("Informe o novo CEP: ")

    cursor.execute("UPDATE CLIENTE SET TELEFONE = %s, NOME = %s, EMAIL = %s, DATA_NASCIMENTO = %s, CEP = %s WHERE CPF = %s", 
                   (telefone, nome, email, data_nascimento, cep, cpf))
    db.commit()
    cursor.close()
    db.close()
    print("Cliente atualizado com sucesso!")



def delete_cliente():
    cpf = input("Informe o CPF do Cliente que deseja deletar: ")

    db = connect()
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM CLIENTE WHERE CPF = %s", (cpf,))
    cliente = cursor.fetchone()

    if not cliente:
        print("Cliente não encontrado.")
        cursor.close()
        db.close()
        return

    cursor.execute("SELECT * FROM RESERVA WHERE CPF = %s", (cpf,))
    reserva = cursor.fetchone()

    if reserva:
        confirmar = input("Este cliente tem reservas ativas. Deseja realmente deletá-lo? Isso cancelará a reserva (s/n): ").lower()
        if confirmar != 's':
            print("Operação cancelada. O cliente não foi deletado.")
            cursor.close()
            db.close()
            return
        

        cursor.execute("DELETE FROM RESERVA WHERE CPF = %s", (cpf,)) 


        cursor.execute("UPDATE QUARTO SET CPF = NULL WHERE CPF = %s", (cpf,)) 


    cursor.execute("DELETE FROM CLIENTE WHERE CPF = %s", (cpf,))
    db.commit()
    cursor.close()
    db.close()
    print("Cliente deletado com sucesso!")




# Funções CRUD para QUARTO
def create_quarto():
    num_quarto = int(input("Informe o Número do Quarto: "))
    print("Tipos de quarto:\n1. Standard\n2. Deluxe\n3. Suíte")
    while True:
        tipoQuarto = int(input("Informe o Tipo de Quarto: "))
        if tipoQuarto == 1:
            tipo_quarto = "Standard"
            break
        elif tipoQuarto == 2:
            tipo_quarto = "Deluxe"
            break
        elif tipoQuarto == 3:
            tipo_quarto = "Suíte"
            break
        else:
            print("Tipo de quarto inválido!")
        
    while True:
        valor_diaria_str = input("Informe o Valor da Diária: ").replace(",", ".")
        try:
            valor_diaria = float(valor_diaria_str)
            break
        except ValueError:
            print("Valor inválido! Informe um número válido para a diária.")
    limite_pessoas = int(input("Informe o Limite de Pessoas: "))
    
    db = connect()
    cursor = db.cursor()
    cursor.execute("INSERT INTO QUARTO (NUM_QUARTO, TIPO_QUARTO, VALOR_DIARIA, LIMITE_PESSOAS) VALUES (%s, %s, %s, %s)", 
                   (num_quarto, tipo_quarto, valor_diaria, limite_pessoas))
    db.commit()
    cursor.close()
    db.close()
    print("Quarto criado com sucesso!")


def read_quartos():
    db = connect()
    cursor = db.cursor()

    cursor.execute("SELECT NUM_QUARTO, TIPO_QUARTO, VALOR_DIARIA, CPF FROM QUARTO")
    quartos = cursor.fetchall()

    if not quartos:
        print("Nenhum quarto encontrado.")
        return
    
    print("+" + "-" * 50 + "+")
    print("|{:^10}|{:^15}|{:^12}|{:^10}|".format("Nº Quarto", "Tipo", " Diária (R$)", "Situação"))
    print("+" + "-" * 50 + "+")

    for quarto in quartos:
        num_quarto = quarto[0]
        tipo_quarto = quarto[1]
        valor_diaria = quarto[2]
        cpf_cliente = quarto[3]

        situacao = "Ocupado" if cpf_cliente else "Livre"

        print("|{:^10}|{:^15}|{:^12.2f}|{:^10}|".format(num_quarto, tipo_quarto, valor_diaria, situacao))

    print("+" + "-" * 50 + "+")

    cursor.close()
    db.close()


def update_quarto():
    num_quarto = int(input("Informe o Número do Quarto que deseja atualizar: "))
    
    db = connect()
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM QUARTO WHERE NUM_QUARTO = %s", (num_quarto,))
    quarto = cursor.fetchone()

    if not quarto:
        print("Quarto não encontrado.")
        cursor.close()
        db.close()
        return 

    if quarto[3] is not None: 
        print("Não é possível atualizar este quarto porque ele está ocupado.")
        cursor.close()
        db.close()
        return 

    print("Tipos de quarto:\n1. Standard\n2. Deluxe\n3. Suíte")
    while True:
        tipoQuarto = int(input("Informe o novo Tipo de Quarto: "))
        if tipoQuarto == 1:
            tipo_quarto = "Standard"
            break
        elif tipoQuarto == 2:
            tipo_quarto = "Deluxe"
            break
        elif tipoQuarto == 3:
            tipo_quarto = "Suíte"
            break
        else:
            print("Tipo de quarto inválido!")
    
    valor_diaria = float(input("Informe o novo Valor da Diária: "))
    limite_pessoas = int(input("Informe o novo Limite de Pessoas: "))

    cursor.execute("UPDATE QUARTO SET TIPO_QUARTO = %s, VALOR_DIARIA = %s, LIMITE_PESSOAS = %s WHERE NUM_QUARTO = %s", 
                   (tipo_quarto, valor_diaria, limite_pessoas, num_quarto))
    db.commit()
    cursor.close()
    db.close()
    print("Quarto atualizado com sucesso!")


def delete_quarto():
    num_quarto = int(input("Informe o Número do Quarto que deseja deletar: "))
    
    db = connect()
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM QUARTO WHERE NUM_QUARTO = %s", (num_quarto,))
    quarto = cursor.fetchone()

    if not quarto:
        print("Quarto não encontrado.")
        cursor.close()
        db.close()
        return 
    

    if quarto[3] is not None:  
        confirmar = input("Este quarto está ocupado. Deseja realmente deletá-lo? Isso cancelará a reserva (s/n): ").lower()
        if confirmar != 's':
            print("Operação cancelada. O quarto não foi deletado.")
            cursor.close()
            db.close()
            return
        

        cursor.execute("DELETE FROM RESERVA WHERE NUM_QUARTO = %s", (num_quarto,)) 

    cursor.execute("DELETE FROM QUARTO WHERE NUM_QUARTO = %s", (num_quarto,))
    db.commit()
    cursor.close()
    db.close()
    print("Quarto deletado e reserva cancelada com sucesso!")




# Funções CRUD para RESERVA
def create_reserva():
    num_reserva = random.randint(0, 100)
    
    db = connect()
    cursor = db.cursor()

    cursor.execute("SELECT CPF, NOME FROM CLIENTE WHERE CPF NOT IN (SELECT CPF FROM QUARTO WHERE CPF IS NOT NULL)")
    clientes = cursor.fetchall()
    if not clientes:
        print("Não há clientes disponíveis para reserva.")
        return
    
    print("Clientes disponíveis:")
    read_clientes()
    
    cpf_cliente = input("Informe o CPF do cliente: ")

    cursor.execute("SELECT * FROM CLIENTE WHERE CPF = %s", (cpf_cliente,))
    if not cursor.fetchone():
        print("Cliente não encontrado.")
        return
    
    cursor.execute("SELECT NUM_QUARTO, TIPO_QUARTO, VALOR_DIARIA, LIMITE_PESSOAS FROM QUARTO WHERE CPF IS NULL")
    quartos = cursor.fetchall()
    if not quartos:
        print("Não há quartos disponíveis para reserva.")
        return
    
    print("Quartos disponíveis:")
    read_quartos()
    
    num_quarto = int(input("Informe o número do quarto: "))
    

    cursor.execute("SELECT * FROM QUARTO WHERE NUM_QUARTO = %s AND CPF IS NULL", (num_quarto,))
    quarto_selecionado = cursor.fetchone()
    if not quarto_selecionado:
        print("Quarto não disponível para reserva.")
        return
    
    limite_pessoas = quarto_selecionado[3] 

    while True:
        data_inicio = input("Informe a Data de Início (DD-MM-YYYY): ")
        try:
            data_inicio = datetime.datetime.strptime(data_inicio, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Data inválida. Tente novamente.")
    
    while True:
        data_final = input("Informe a Data de Fim (DD-MM-YYYY): ")
        try:
            data_final = datetime.datetime.strptime(data_final, "%d-%m-%Y").date()
            if data_final <= data_inicio:
                print("A data de fim deve ser posterior à data de início.")
            else:
                break
        except ValueError:
            print("Data inválida. Tente novamente.")
    

    quantidade_pessoas = int(input("Informe a Quantidade de Pessoas: "))
    

    if quantidade_pessoas > limite_pessoas:
        print(f"Não é possível reservar. O limite máximo de pessoas para este quarto é {limite_pessoas}.")
        return 
    
    cafe_incluso = input("Café da manhã incluso? (S/N): ").strip().upper()
    cafe_incluso = 1 if cafe_incluso == "S" else 0
    
    num_dias = (data_final - data_inicio).days
    valor_reserva = quarto_selecionado[2] * num_dias 
    if cafe_incluso == 1:
        valor_reserva += 60

    cursor.execute(
        "INSERT INTO RESERVA (NUM_RESERVA, DATA_INICIO, DATA_FINAL, QUANTIDADE_PESSOAS, VALOR_RESERVA, CPF, NUM_QUARTO, CAFE_INCLUSO) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
        (num_reserva, data_inicio, data_final, quantidade_pessoas, valor_reserva, cpf_cliente, num_quarto, cafe_incluso)
    )
    

    cursor.execute("UPDATE QUARTO SET CPF = %s WHERE NUM_QUARTO = %s", (cpf_cliente, num_quarto))
    
    db.commit()
    cursor.close()
    db.close()

    print(f"\nReserva número {num_reserva} criada com sucesso! Valor total: R${valor_reserva:.2f} para {num_dias} dias.")


def read_reservas():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT NUM_RESERVA, DATA_INICIO, DATA_FINAL, QUANTIDADE_PESSOAS, VALOR_RESERVA, CPF, NUM_QUARTO, CAFE_INCLUSO FROM RESERVA")
    
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
                reserva[0], formatar_data(reserva[1]), formatar_data(reserva[2]), reserva[3], 
                reserva[4], reserva[5], reserva[6], "Sim" if reserva[7] == 1 else "Não"))
            print("+" + "-" * 101 + "+")
    
    cursor.close()
    db.close()


def update_reserva():
    num_reserva = int(input("Informe o Número da Reserva que deseja atualizar: "))

    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM RESERVA WHERE NUM_RESERVA = %s", (num_reserva,))
    reserva = cursor.fetchone()

    if not reserva:
        print("Reserva não encontrada.")
        cursor.close()
        db.close()
        return

    print("Clientes cadastrados:")
    read_clientes()  
    cpf = input("Informe o novo CPF do cliente: ")

    cursor.execute("SELECT * FROM CLIENTE WHERE CPF = %s", (cpf,))
    if not cursor.fetchone():
        print("Cliente não encontrado.")
        cursor.close()
        db.close()
        return

    print("Quartos cadastrados:")
    read_quartos() 
    num_quarto = int(input("Informe o novo Número do Quarto: "))

    cursor.execute("SELECT * FROM QUARTO WHERE NUM_QUARTO = %s", (num_quarto,))
    quarto_selecionado = cursor.fetchone()
    if not quarto_selecionado:
        print("Quarto não encontrado.")
        cursor.close()
        db.close()
        return


    while True:
        data_inicio = input("Informe a nova Data de Início (DD-MM-YYYY): ")
        try:
            data_inicio = datetime.datetime.strptime(data_inicio, "%d-%m-%Y").date()
            data_inicio = data_inicio.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Data inválida. Tente novamente.")

    while True:
        data_final = input("Informe a nova Data de Fim (DD-MM-YYYY): ")
        try:
            data_final = datetime.datetime.strptime(data_final, "%d-%m-%Y").date()
            data_final = data_final.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Data inválida. Tente novamente.")


    cursor.execute("""
        SELECT * FROM RESERVA 
        WHERE NUM_QUARTO = %s AND (
            (DATA_INICIO <= %s AND DATA_FINAL >= %s) OR
            (DATA_INICIO <= %s AND DATA_FINAL >= %s) OR
            (DATA_INICIO >= %s AND DATA_FINAL <= %s)
        )
    """, (num_quarto, data_final, data_final, data_inicio, data_inicio, data_inicio, data_final))

    if cursor.fetchone():
        print("O quarto não está disponível nas novas datas.")
        cursor.close()
        db.close()
        return

    cafe_incluso = input("Café da manhã incluso? (S/N): ").strip().upper()
    cafe_incluso = 1 if cafe_incluso == "S" else 0


    data_inicio_dt = datetime.datetime.strptime(data_inicio, "%Y-%m-%d").date()
    data_final_dt = datetime.datetime.strptime(data_final, "%Y-%m-%d").date()
    dias_reserva = (data_final_dt - data_inicio_dt).days
    valor_reserva = quarto_selecionado[2] * dias_reserva
    
    if cafe_incluso == 1:
        valor_reserva += 60
    
    quantidade_pessoas = int(input("Informe a nova Quantidade de Pessoas: "))


    cursor.execute(
        "UPDATE RESERVA SET DATA_INICIO = %s, DATA_FINAL = %s, QUANTIDADE_PESSOAS = %s, VALOR_RESERVA = %s, CPF = %s, NUM_QUARTO = %s, CAFE_INCLUSO = %s "
        "WHERE NUM_RESERVA = %s",
        (data_inicio, data_final, quantidade_pessoas, valor_reserva, cpf, num_quarto, cafe_incluso, num_reserva)
    )


    cursor.execute("UPDATE QUARTO SET CPF = %s WHERE NUM_QUARTO = %s", (cpf, num_quarto))

    db.commit()
    cursor.close()
    db.close()
    print("Reserva e CPF do quarto atualizados com sucesso!")



def delete_reserva():
    num_reserva = int(input("Informe o Número da Reserva que deseja deletar: "))
    
    db = connect()
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM RESERVA WHERE NUM_RESERVA = %s", (num_reserva,))
    reserva = cursor.fetchone()

    if not reserva:
        print("Reserva não encontrada.")
        cursor.close()
        db.close()
        return  
    
    num_quarto = reserva[7] 
    

    cursor.execute("DELETE FROM RESERVA WHERE NUM_RESERVA = %s", (num_reserva,))
    

    cursor.execute("UPDATE QUARTO SET CPF = NULL WHERE NUM_QUARTO = %s", (num_quarto,))

    db.commit()
    cursor.close()
    db.close()
    print("Reserva deletada e quarto liberado com sucesso!")

def relatorio_quartos():
    db = connect()
    cursor = db.cursor()

    # Relatório de quartos
    cursor.execute("SELECT COUNT(*) FROM QUARTO")
    total_quartos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM QUARTO WHERE CPF IS NULL")
    quartos_disponiveis = cursor.fetchone()[0]

    quartos_alugados = total_quartos - quartos_disponiveis

    cursor.execute("SELECT SUM(VALOR_RESERVA) FROM RESERVA")
    faturamento_total = cursor.fetchone()[0] or 0  # Se não houver reservas, faturamento será zero

    cursor.execute("SELECT AVG(VALOR_RESERVA / QUANTIDADE_PESSOAS) FROM RESERVA WHERE QUANTIDADE_PESSOAS > 0")
    media_pago_por_pessoa = cursor.fetchone()[0] or 0  # Evitar divisão por zero

    # Exibir o relatório com bordas e formatação
    print("\n+" + "-"*60 + "+")
    print("|{:^60}|".format("RELATÓRIO DE QUARTOS"))
    print("+" + "-"*60 + "+")
    print("| {:<30} | {:>25} |".format("Número total de quartos", total_quartos))
    print("+" + "-"*60 + "+")
    print("| {:<30} | {:>25} |".format("Quartos disponíveis", quartos_disponiveis))
    print("+" + "-"*60 + "+")
    print("| {:<30} | {:>25} |".format("Quartos alugados", quartos_alugados))
    print("+" + "-"*60 + "+")
    print("| {:<30} | R${:>23.2f} |".format("Faturamento total", faturamento_total))
    print("+" + "-"*60 + "+")
    print("| {:<30} | R${:>23.2f} |".format("Média paga por pessoa", media_pago_por_pessoa))
    print("+" + "-"*60 + "+")

    cursor.close()
    db.close()

def relatorio_hospedes():
    db = connect()
    cursor = db.cursor()

    # Relatório de hóspedes
    cursor.execute("SELECT COUNT(DISTINCT CPF) FROM RESERVA")
    total_hospedes = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(DATEDIFF(DATA_FINAL, DATA_INICIO)) FROM RESERVA")
    media_dias_alugados = cursor.fetchone()[0] or 0

    cursor.execute("SELECT AVG(VALOR_RESERVA) FROM RESERVA")
    media_valor_reserva = cursor.fetchone()[0] or 0

    # Exibir o relatório com bordas e formatação
    print("\n+" + "-"*60 + "+")
    print("|{:^60}|".format("RELATÓRIO DE HÓSPEDES"))
    print("+" + "-"*60 + "+")
    print("| {:<30} | {:>25} |".format("Quantidade de hóspedes", total_hospedes))
    print("+" + "-"*60 + "+")
    print("| {:<30} | {:>25.2f} |".format("Média de dias alugados", media_dias_alugados))
    print("+" + "-"*60 + "+")
    print("| {:<30} | R${:>23,.2f} |".format("Valor médio da reserva", media_valor_reserva))
    print("+" + "-"*60 + "+")

    cursor.close()
    db.close()


def menu_relatorios():
    while True:
        print("\n" + "="*47)
        print(" "*15 + "MENU RELATÓRIOS")
        print("="*47)

        print("\nSelecione uma opção:")
        print("-"*47)
        print("| 1. 📊  Relatório de Quartos                 |")
        print("-"*47)
        print("| 2. 📈  Relatório de Hóspedes                |")
        print("-"*47)
        print("| 3. 📝  Tela Inicial (Menu de Criação)       |")  
        print("-"*47)
        print("| 4. 🔙  Voltar                               |")
        print("="*47)

        escolha = input("\nDigite sua opção: ")

        if escolha == '1':
            relatorio_quartos()
        elif escolha == '2':
            relatorio_hospedes()
        elif escolha == '3':
            menu_de_criacao() 
        elif escolha == '4':
            break
        else:
            print("\nOpção inválida. Tente novamente.")



# Menus organizados em submenus
def menu():
    while True:
        print("\n"+"="*47)
        print(" "*9 + "SISTEMA DE GESTÃO DE HOTEL")
        print("="*47)

        print("\nSelecione uma opção:")
        print("-"*47)
        print("| 1. 🧑  Clientes                             |")
        print("-"*47)
        print("| 2. 🏨  Quartos                              |")
        print("-"*47)
        print("| 3. 📅  Reservas                             |")
        print("-"*47)
        print("| 4. 📊  Relatórios                           |")
        print("-"*47)
        print("| 5. ❌  Sair                                 |")
        print("="*47)

        escolha = input("\nDigite sua opção: ")

        if escolha == '1':
            menu_cliente()
        elif escolha == '2':
            menu_quarto()
        elif escolha == '3':
            menu_reserva()
        elif escolha == '4':
            menu_relatorios()
        elif escolha == '5':
            print("\nSaindo... Obrigado por utilizar o sistema!")
            print("="*47)
            break
        else:
            print("\nOpção inválida. Tente novamente.")

def menu_cliente():
    while True:
        print("\n" + "="*47)
        print(" "*15 + "MENU DE CLIENTE")
        print("="*47)

        print("\nSelecione uma opção:")
        print("-"*47)
        print("| 1. ➕  Cadastrar Cliente                    |")
        print("-"*47)
        print("| 2. 📜  Ler Clientes                         |")
        print("-"*47)
        print("| 3. ✏️   Atualizar Cliente                    |")
        print("-"*47)
        print("| 4. 🗑️   Excluir Cliente                      |")
        print("-"*47)
        print("| 5. 🔙  Voltar                               |")
        print("="*47)

        escolha = input("\nDigite sua opção: ")

        if escolha == '1':
            create_cliente()
        elif escolha == '2':
            read_clientes()
        elif escolha == '3':
            update_cliente()
        elif escolha == '4':
            delete_cliente()
        elif escolha == '5':
            break
        else:
            print("\nOpção inválida. Tente novamente.")

def menu_quarto():
    while True:
        print("\n" + "="*47)
        print(" "*15 + "MENU DE QUARTO")
        print("="*47)

        print("\nSelecione uma opção:")
        print("-"*47)
        print("| 1. ➕  Cadastrar Quarto                     |")
        print("-"*47)
        print("| 2. 📜  Ler Quartos                          |")
        print("-"*47)
        print("| 3. ✏️   Atualizar Quarto                     |")
        print("-"*47)
        print("| 4. 🗑️   Excluir Quarto                       |")
        print("-"*47)
        print("| 5. 🔙  Voltar                               |")
        print("="*47)

        escolha = input("\nDigite sua opção: ")

        if escolha == '1':
            create_quarto()
        elif escolha == '2':
            read_quartos()
        elif escolha == '3':
            update_quarto()
        elif escolha == '4':
            delete_quarto()
        elif escolha == '5':
            break
        else:
            print("\nOpção inválida. Tente novamente.")


def menu_reserva():
    while True:
        print("\n" + "="*47)
        print(" "*14 + "MENU DE RESERVA")
        print("="*47)

        print("\nSelecione uma opção:")
        print("-"*47)
        print("| 1. ➕  Cadastrar Reserva                    |")
        print("-"*47)
        print("| 2. 📜  Ler Reservas                         |")
        print("-"*47)
        print("| 3. ✏️   Atualizar Reserva                    |")
        print("-"*47)
        print("| 4. 🗑️   Excluir Reserva                      |")
        print("-"*47)
        print("| 5. 🔙  Voltar                               |")
        print("="*47)

        escolha = input("\nDigite sua opção: ")

        if escolha == '1':
            create_reserva()
        elif escolha == '2':
            read_reservas()
        elif escolha == '3':
            update_reserva()
        elif escolha == '4':
            delete_reserva()
        elif escolha == '5':
            break
        else:
            print("\nOpção inválida. Tente novamente.")

def menu_de_criacao():
    # Informações do sistema
    system_name = "Sistema de Gerenciamento de Hotel"
    created_by = (
        "Aidhan Freitas, Henrique Volpini, Samuel Lucas           |\n"
        "| Bernardo Abner, Rafael Barcelos, Lucas Xavier"
    )
    professor = "HOWARD ROATTI"
    disciplina = "Banco de Dados"
    semestre = "2024/2"
    coracao = "❤️"

    # Conectar ao banco de dados para contar os registros
    db = connect()
    cursor = db.cursor()

    # Contar os registros nas tabelas
    cursor.execute("SELECT COUNT(*) FROM CLIENTE")
    total_clientes = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM QUARTO")
    total_quartos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM RESERVA")
    total_reservas = cursor.fetchone()[0]

    cursor.close()
    db.close()

    # Exibir a tela inicial com bordas e formatação organizada
    print("\n" + "="*60)
    print(f"{system_name:^60}")
    print("="*60)
    print("TOTAL DE REGISTROS:")
    print("-"*60)
    print(f"| 1. Número de Clientes:                             {str(total_clientes).rjust(5)} |")
    print("-"*60)
    print(f"| 2. Número de Quartos:                              {str(total_quartos).rjust(5)} |")
    print("-"*60)
    print(f"| 3. Número de Reservas:                             {str(total_reservas).rjust(5)} |")
    print("="*60)
    print("CRIADO POR:")
    print("-"*60)
    print(f"| {created_by:<80}            |")
    print("="*60)
    print("PROFESSOR:")
    print("-"*60)
    print(f"| {professor:<53} {coracao:<3} |")
    print("="*60)
    print("DISCIPLINA:")
    print("-"*60)
    print(f"| {disciplina:<49} {semestre:<1} |")
    print("="*60)

if __name__ == "__main__":
    menu_de_criacao()  # Exibe a tela inicial antes de iniciar o menu
    menu()  # Chama o menu principal

