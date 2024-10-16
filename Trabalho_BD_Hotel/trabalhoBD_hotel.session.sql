ALTER TABLE QUARTO DROP FOREIGN KEY CPF_FK;
ALTER TABLE RESERVA DROP FOREIGN KEY NUM_QUARTO_FK;
ALTER TABLE RESERVA DROP FOREIGN KEY CPF_RESERVA_FK;


DROP TABLE IF EXISTS CLIENTE;
DROP TABLE IF EXISTS QUARTO;
DROP TABLE IF EXISTS RESERVA;


CREATE TABLE CLIENTE (
    CPF             VARCHAR(14)         NOT NULL,
    TELEFONE        VARCHAR(18)         NOT NULL,
    NOME            VARCHAR(200)        NOT NULL,
    EMAIL           VARCHAR(100)        NOT NULL,
    DATA_NASCIMENTO DATE                NOT NULL,
    CEP             VARCHAR(9)          NOT NULL,
    PRIMARY KEY (CPF)
);


CREATE TABLE QUARTO (
    NUM_QUARTO      INT                 NOT NULL,
    TIPO_QUARTO     VARCHAR(50)         NOT NULL,
    VALOR_DIARIA    DECIMAL(10, 2)      NOT NULL,
    LIMITE_PESSOAS  INT                 NOT NULL,
    CAFE_INCLUSO    INT                 NOT NULL,
    PRIMARY KEY (NUM_QUARTO)
);


CREATE TABLE RESERVA (
    NUM_RESERVA         INT             NOT NULL,
    DATA_INICIO         DATE            NOT NULL,
    DATA_FINAL          DATE            NOT NULL,
    QUANTIDADE_PESSOAS  INT             NOT NULL,
    VALOR_RESERVA       DECIMAL(10, 2)  NOT NULL,
    PRIMARY KEY (NUM_RESERVA)
);


ALTER TABLE QUARTO ADD CPF VARCHAR(14);


ALTER TABLE RESERVA ADD (
    CPF VARCHAR(14), 
    NUM_QUARTO INT
);


ALTER TABLE QUARTO 
ADD CONSTRAINT CPF_FK 
FOREIGN KEY (CPF) REFERENCES CLIENTE(CPF);

ALTER TABLE RESERVA 
ADD CONSTRAINT CPF_RESERVA_FK
FOREIGN KEY (CPF) REFERENCES CLIENTE(CPF);

ALTER TABLE RESERVA 
ADD CONSTRAINT NUM_QUARTO_FK
FOREIGN KEY (NUM_QUARTO) REFERENCES QUARTO(NUM_QUARTO);