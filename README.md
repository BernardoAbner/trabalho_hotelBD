# trabalho_hotelBD
# Sistema de Gerenciamento de Hotel

Este é um projeto de sistema de gerenciamento de hotel desenvolvido em Python, utilizando o MySQL como banco de dados. O sistema permite realizar operações de CRUD (Criar, Ler, Atualizar e Excluir) para entidades como Clientes, Quartos e Reservas, além de gerar relatórios sobre o uso do hotel.

## Funcionalidades

O sistema inclui as seguintes funcionalidades:

1. *Gerenciamento de Clientes*:
   - Cadastrar novo cliente.
   - Listar todos os clientes cadastrados.
   - Atualizar informações de um cliente existente.
   - Excluir um cliente e, se necessário, suas reservas associadas.

2. *Gerenciamento de Quartos*:
   - Cadastrar novos quartos com tipo, valor da diária e limite de pessoas.
   - Listar todos os quartos cadastrados e suas situações (livre ou ocupado).
   - Atualizar informações dos quartos, caso estejam livres.
   - Excluir quartos e cancelar reservas associadas.

3. *Gerenciamento de Reservas*:
   - Criar novas reservas associando clientes a quartos disponíveis.
   - Listar todas as reservas feitas.
   - Atualizar informações das reservas.
   - Excluir reservas e liberar os quartos.

4. *Relatórios*:
   - Gerar relatórios de quartos (total de quartos, disponíveis, ocupados e faturamento).
   - Gerar relatórios de hóspedes (quantidade de hóspedes, média de dias alugados, valor médio das reservas).

5. *Tela Inicial com Informações do Sistema*:
   - Tela inicial que exibe o nome do sistema, informações dos criadores, professor e disciplina, e o número total de registros no banco de dados.

## Estrutura do Projeto

O projeto está organizado em classes para facilitar a manutenção e a expansão:

- *DatabaseConnection*: Classe responsável por gerenciar a conexão com o banco de dados MySQL.
- *Cliente*: Classe com métodos para as operações CRUD relacionadas aos clientes.
- *Quarto*: Classe com métodos para as operações CRUD relacionadas aos quartos.
- *Reserva*: Classe com métodos para as operações CRUD relacionadas às reservas.
- *Menus*: Funções para exibir os menus e capturar as entradas do usuário, organizando as funcionalidades do sistema.

## Requisitos

- Python 3.x
- Biblioteca mysql-connector-python para conectar o Python ao MySQL.
- Servidor MySQL para hospedar o banco de dados.

## Instalação

1. *Clonar o repositório*:
   ```bash
   git clone https://github.com/BernardoAbner/trabalho_hotelBD.git
   cd sistema-de-hotel