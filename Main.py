import datetime
import random
from cliente import Cliente
from quarto import Quarto
from reserva import Reserva
from relatorio import Relatorio  # Importação da classe Relatorio
from DatabaseConnection import DatabaseConnection

def formatar_data(data):
    return data.strftime("%d-%m-%Y") if isinstance(data, datetime.date) else data

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
            Cliente.read_clientes()
        elif escolha == '3':
            update_cliente()
        elif escolha == '4':
            delete_cliente()
        elif escolha == '5':
            break
        else:
            print("\nOpção inválida. Tente novamente.")

def create_cliente():
    cpf = input("Informe o CPF: ")
    telefone = input("Informe o Telefone: ")
    nome = input("Informe o Nome: ")
    email = input("Informe o Email: ")

    while True:
        data_nascimento = input("Informe a Data de Nascimento (DD-MM-YYYY): ")
        try:
            data_nascimento_dt = datetime.datetime.strptime(data_nascimento, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Data inválida. Tente novamente.")

    cep = input("Informe o CEP: ")

    cliente = Cliente(cpf, telefone, nome, email, data_nascimento_dt, cep)
    cliente.create_cliente()

def update_cliente():
    cpf = input("Informe o CPF do cliente que deseja atualizar: ")

    if not Cliente.cliente_exists(cpf):
        print("Cliente não encontrado.")
        return

    telefone = input("Informe o novo Telefone: ")
    nome = input("Informe o novo Nome: ")
    email = input("Informe o novo Email: ")

    while True:
        data_nascimento = input("Informe a nova Data de Nascimento (DD-MM-YYYY): ")
        try:
            data_nascimento_dt = datetime.datetime.strptime(data_nascimento, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Data inválida. Tente novamente.")

    cep = input("Informe o novo CEP: ")

    cliente = Cliente(cpf, telefone, nome, email, data_nascimento_dt, cep)
    cliente.update_cliente()

def delete_cliente():
    cpf = input("Informe o CPF do Cliente que deseja deletar: ")

    if not Cliente.cliente_exists(cpf):
        print("Cliente não encontrado.")
        return

    confirmar = input("Tem certeza que deseja deletar este cliente? (s/n): ").lower()
    if confirmar != 's':
        print("Operação cancelada.")
        return

    cliente = Cliente(cpf=cpf)
    cliente.delete_cliente()

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
            Quarto.read_quartos()
        elif escolha == '3':
            update_quarto()
        elif escolha == '4':
            delete_quarto()
        elif escolha == '5':
            break
        else:
            print("\nOpção inválida. Tente novamente.")

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

    quarto = Quarto(num_quarto, tipo_quarto, valor_diaria, limite_pessoas)
    quarto.create_quarto()

def update_quarto():
    num_quarto = int(input("Informe o Número do Quarto que deseja atualizar: "))

    if not Quarto.quarto_exists(num_quarto):
        print("Quarto não encontrado.")
        return

    if Quarto.is_quarto_ocupado(num_quarto):
        print("Não é possível atualizar este quarto porque ele está ocupado.")
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

    quarto = Quarto(num_quarto, tipo_quarto, valor_diaria, limite_pessoas)
    quarto.update_quarto()

def delete_quarto():
    num_quarto = int(input("Informe o Número do Quarto que deseja deletar: "))

    if not Quarto.quarto_exists(num_quarto):
        print("Quarto não encontrado.")
        return

    if Quarto.is_quarto_ocupado(num_quarto):
        confirmar = input("Este quarto está ocupado. Deseja realmente deletá-lo? Isso cancelará a reserva (s/n): ").lower()
        if confirmar != 's':
            print("Operação cancelada.")
            return
        else:
            # Aqui você pode adicionar a lógica para deletar a reserva associada
            pass

    quarto = Quarto(num_quarto=num_quarto)
    quarto.delete_quarto()

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
            Reserva.read_reservas()
        elif escolha == '3':
            update_reserva()
        elif escolha == '4':
            delete_reserva()
        elif escolha == '5':
            break
        else:
            print("\nOpção inválida. Tente novamente.")

def create_reserva():
    num_reserva = random.randint(0, 100)

    Cliente.read_clientes()
    cpf_cliente = input("Informe o CPF do cliente: ")

    if not Cliente.cliente_exists(cpf_cliente):
        print("Cliente não encontrado.")
        return

    Quarto.read_quartos()
    num_quarto = int(input("Informe o número do quarto: "))

    if not Quarto.quarto_exists(num_quarto):
        print("Quarto não encontrado.")
        return

    if Quarto.is_quarto_ocupado(num_quarto):
        print("Quarto já está ocupado.")
        return

    while True:
        data_inicio = input("Informe a Data de Início (DD-MM-YYYY): ")
        try:
            data_inicio_dt = datetime.datetime.strptime(data_inicio, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Data inválida. Tente novamente.")

    while True:
        data_final = input("Informe a Data de Fim (DD-MM-YYYY): ")
        try:
            data_final_dt = datetime.datetime.strptime(data_final, "%d-%m-%Y").date()
            if data_final_dt <= data_inicio_dt:
                print("A data de fim deve ser posterior à data de início.")
            else:
                break
        except ValueError:
            print("Data inválida. Tente novamente.")

    quantidade_pessoas = int(input("Informe a Quantidade de Pessoas: "))

    cafe_incluso_opcao = input("Café incluso? (1 para Sim, 2 para Não): ").strip()
    if cafe_incluso_opcao == '1':
        cafe_incluso = 1
    else:
        cafe_incluso = 0

    num_dias = (data_final_dt - data_inicio_dt).days
    valor_reserva = calcular_valor_reserva(num_quarto, num_dias, cafe_incluso)

    reserva = Reserva(num_reserva, data_inicio_dt, data_final_dt, quantidade_pessoas,
                      valor_reserva, cpf_cliente, num_quarto, cafe_incluso)
    reserva.create_reserva()

    # Atualizar o quarto como ocupado usando o método atualizar_cpf()
    quarto = Quarto(num_quarto=num_quarto, cpf=cpf_cliente)
    quarto.atualizar_cpf()

    print(f"\nReserva número {num_reserva} criada com sucesso! Valor total: R${valor_reserva:.2f} para {num_dias} dias.")

def calcular_valor_reserva(num_quarto, num_dias, cafe_incluso):
    db = DatabaseConnection()
    connection = db.get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT VALOR_DIARIA FROM QUARTO WHERE NUM_QUARTO = %s", (num_quarto,))
    valor_diaria = cursor.fetchone()[0]
    cursor.close()
    db.close_connection()

    valor_total = valor_diaria * num_dias
    if cafe_incluso == 1:
        valor_total += 60

    return valor_total

def update_reserva():
    num_reserva = int(input("Informe o Número da Reserva que deseja atualizar: "))

    if not Reserva.reserva_exists(num_reserva):
        print("Reserva não encontrada.")
        return

    Cliente.read_clientes()
    cpf_cliente = input("Informe o novo CPF do cliente: ")

    if not Cliente.cliente_exists(cpf_cliente):
        print("Cliente não encontrado.")
        return

    Quarto.read_quartos()
    num_quarto = int(input("Informe o novo número do quarto: "))

    if not Quarto.quarto_exists(num_quarto):
        print("Quarto não encontrado.")
        return

    while True:
        data_inicio = input("Informe a nova Data de Início (DD-MM-YYYY): ")
        try:
            data_inicio_dt = datetime.datetime.strptime(data_inicio, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Data inválida. Tente novamente.")

    while True:
        data_final = input("Informe a nova Data de Fim (DD-MM-YYYY): ")
        try:
            data_final_dt = datetime.datetime.strptime(data_final, "%d-%m-%Y").date()
            if data_final_dt <= data_inicio_dt:
                print("A data de fim deve ser posterior à data de início.")
            else:
                break
        except ValueError:
            print("Data inválida. Tente novamente.")

    quantidade_pessoas = int(input("Informe a nova Quantidade de Pessoas: "))

    cafe_incluso_opcao = input("Café incluso? (1 para Sim, 2 para Não): ").strip()
    if cafe_incluso_opcao == '1':
        cafe_incluso = 1
    else:
        cafe_incluso = 0

    num_dias = (data_final_dt - data_inicio_dt).days
    valor_reserva = calcular_valor_reserva(num_quarto, num_dias, cafe_incluso)

    reserva = Reserva(num_reserva, data_inicio_dt, data_final_dt, quantidade_pessoas,
                      valor_reserva, cpf_cliente, num_quarto, cafe_incluso)
    reserva.update_reserva()

def delete_reserva():
    num_reserva = int(input("Informe o Número da Reserva que deseja deletar: "))

    if not Reserva.reserva_exists(num_reserva):
        print("Reserva não encontrada.")
        return

    confirmar = input("Tem certeza que deseja deletar esta reserva? (s/n): ").lower()
    if confirmar != 's':
        print("Operação cancelada.")
        return

    reserva = Reserva(num_reserva=num_reserva)
    reserva.delete_reserva()

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
        print("| 3. 🔙  Voltar                               |")
        print("="*47)

        escolha = input("\nDigite sua opção: ")

        if escolha == '1':
            Relatorio.relatorio_quartos()
        elif escolha == '2':
            Relatorio.relatorio_hospedes()
        elif escolha == '3':
            break
        else:
            print("\nOpção inválida. Tente novamente.")

def menu_de_criacao():
    system_name = "Sistema de Gerenciamento de Hotel"
    created_by = (
        "Aidhan Freitas, Henrique Volpini, Samuel Lucas           |\n"
        "| Bernardo Abner, Rafael Barcelos, Lucas Xavier"
    )
    professor = "HOWARD ROATTI"
    disciplina = "Banco de Dados"
    semestre = "2024/2"
    coracao = "❤️"

    db = DatabaseConnection()
    connection = db.get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM CLIENTE")
    total_clientes = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM QUARTO")
    total_quartos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM RESERVA")
    total_reservas = cursor.fetchone()[0]

    cursor.close()
    db.close_connection()

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
    menu_de_criacao()
    menu()
