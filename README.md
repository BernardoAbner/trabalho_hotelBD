====================================================================================================
                                 SISTEMA DE GERENCIAMENTO DE HOTEL
====================================================================================================

Este projeto é um sistema de gerenciamento de hotel desenvolvido em Python, utilizando o MySQL como 
banco de dados. Ele permite realizar operações CRUD (Criar, Ler, Atualizar e Excluir) para gerenciar 
entidades como Clientes, Quartos e Reservas, além de gerar relatórios sobre o uso do hotel.

Link para o vídeo de demonstração do código: https://youtu.be/Mjx05IhnHu4?feature=shared

----------------------------------------------------------------------------------------------------
FUNCIONALIDADES
----------------------------------------------------------------------------------------------------

1. Gerenciamento de Clientes:
   - Cadastrar um novo cliente.
   - Listar todos os clientes cadastrados.
   - Atualizar informações de um cliente existente.
   - Excluir um cliente e, se necessário, suas reservas associadas.

2. Gerenciamento de Quartos:
   - Cadastrar novos quartos especificando o tipo, valor da diária e limite de pessoas.
   - Listar todos os quartos cadastrados, indicando se estão livres ou ocupados.
   - Atualizar informações de quartos, caso não estejam ocupados.
   - Excluir quartos e cancelar reservas associadas, se necessário.

3. Gerenciamento de Reservas:

   - Criar novas reservas associando clientes a quartos disponíveis.
   - Listar todas as reservas existentes.
   - Atualizar informações das reservas.
   - Excluir reservas e liberar os quartos para novas reservas.

4. Relatórios:
   - Relatório de quartos, incluindo o total de quartos, número de quartos disponíveis, ocupados 
     e o faturamento total.
   - Relatório de hóspedes, incluindo a quantidade de hóspedes, média de dias alugados e valor médio 
     das reservas.

5. Tela Inicial:
   - Exibição de informações sobre o sistema, como nome, autores, professor e disciplina, além de 
     informações do banco de dados, como o número total de registros em cada tabela.

====================================================================================================
ESTRUTURA DO PROJETO
====================================================================================================

O código é organizado em classes para facilitar a manutenção e expansão do sistema. As classes são:

- DatabaseConnection: Responsável por gerenciar a conexão com o banco de dados MySQL.
- Cliente: Contém métodos para operações CRUD relacionados aos clientes.
- Quarto: Contém métodos para operações CRUD relacionados aos quartos.
- Reserva: Contém métodos para operações CRUD relacionadas às reservas.
- Menus: Funções para exibir os menus e capturar as entradas do usuário..

----------------------------------------------------------------------------------------------------
ESTRUTURA DO BANCO DE DADOS
----------------------------------------------------------------------------------------------------

O sistema utiliza três tabelas no banco de dados:

1. Tabela CLIENTE:
   - Campos: CPF, TELEFONE, NOME, EMAIL, DATA_NASCIMENTO, CEP.

2. Tabela QUARTO:
   - Campos: NUM_QUARTO, TIPO_QUARTO, VALOR_DIARIA, LIMITE_PESSOAS.

3. Tabela RESERVA:
   - Campos: NUM_RESERVA, DATA_INICIO, DATA_FINAL, QUANTIDADE_PESSOAS, VALOR_RESERVA, CPF, 
     NUM_QUARTO, CAFE_INCLUSO.

====================================================================================================
CONFIGURAÇÃO DO AMBIENTE E EXECUÇÃO DO PROJETO
====================================================================================================

Antes de executar o projeto, siga os passos abaixo para configurar o ambiente:

1. Certifique-se de que o Python 3.x está instalado no seu sistema. Para verificar a instalação, 
   execute o comando no terminal:

   $ python3 --version

2. Crie um ambiente virtual para isolar as dependências do projeto:

   $ python3 -m venv nome_da_venv

3. Ative o ambiente virtual:

   - No Linux ou MacOS:

     $ source nome_da_venv/bin/activate

   - No Windows:

     $ nome_da_venv\Scripts\activate

4. Com o ambiente virtual ativado, instale a biblioteca necessária para a conexão com o MySQL:

   $ pip install mysql-connector-python

5. Verifique se a biblioteca foi instalada corretamente listando as bibliotecas instaladas:

   $ pip list

----------------------------------------------------------------------------------------------------
CONFIGURAÇÃO DO BANCO DE DADOS
----------------------------------------------------------------------------------------------------

1. Acesse o MySQL com seu usuário administrativo para configurar o banco de dados:

   $ mysql -u root -p

2. Crie o banco de dados:

   mysql> CREATE DATABASE BDB_hotel;

3. Selecione o banco de dados criado para uso:

   mysql> USE BDB_hotel;

4. Configure as credenciais de conexão no código para acessar o banco de dados, substituindo os 
   valores pelo seu usuário e senha:

   >> python

   def connect():
       return mysql.connector.connect(
           host="localhost",
           user="seu_usuario",
           password="sua_senha",
           database="seu_banco_de_dados",
           auth_plugin='mysql_native_password'
       )

==================================================================================================== 
CLONANDO O REPOSITÓRIO DO GITHUB EM UMA MÁQUINA VIRTUAL LINUX
----------------------------------------------------------------------------------------------------

Acesse a máquina virtual Linux e abra o terminal.

Certifique-se de que o Git está instalado. Para verificar, execute:

$ git --version

Se o Git não estiver instalado, você pode instalá-lo com o comando:

$ sudo apt-get install git

Navegue até o diretório onde deseja clonar o repositório, por exemplo, a pasta home do usuário:

$ cd ~

Clone o repositório do GitHub:

$ git clone https://github.com/BernardoAbner/trabalho_hotelBD

Isso criará uma pasta chamada sistema-de-hotel no diretório atual.

Acesse o diretório do projeto clonado:

$ cd sistema-de-hotel

------------------------------------------------------------------------------------------------------
EXECUTAR O PROGRAMA
------------------------------------------------------------------------------------------------------

1. Com o ambiente virtual ativado e o terminal aberto no diretório raiz do projeto, execute o programa:

   $ python3 main.py

Informações adicionais sobre o sistema, contribuições e estrutura podem ser encontradas no próprio código.
=======================================================================================================
