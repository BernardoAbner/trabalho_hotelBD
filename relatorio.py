from DatabaseConnection import DatabaseConnection

class Relatorio:
    @staticmethod
    def relatorio_quartos():
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM QUARTO")
        total_quartos = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM QUARTO WHERE CPF IS NULL")
        quartos_disponiveis = cursor.fetchone()[0]

        quartos_alugados = total_quartos - quartos_disponiveis

        cursor.execute("SELECT SUM(VALOR_RESERVA) FROM RESERVA")
        faturamento_total = cursor.fetchone()[0] or 0

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

        cursor.close()
        db.close_connection()

    @staticmethod
    def relatorio_hospedes():
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(DISTINCT CPF) FROM RESERVA")
        total_hospedes = cursor.fetchone()[0]

        cursor.execute("SELECT AVG(DATEDIFF(DATA_FINAL, DATA_INICIO)) FROM RESERVA")
        media_dias_alugados = cursor.fetchone()[0] or 0

        cursor.execute("SELECT AVG(VALOR_RESERVA) FROM RESERVA")
        media_valor_reserva = cursor.fetchone()[0] or 0

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
        db.close_connection()
