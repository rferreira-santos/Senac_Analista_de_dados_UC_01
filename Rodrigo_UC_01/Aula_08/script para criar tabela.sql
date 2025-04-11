CREATE TABLE pedidos(
    numero integer NOT NULL,
    data DATE NOT NULL,
    status varchar(30) NOT NULL,
    cpf varchar(14) NOT NULL,
    cnpj varchar(14) NOT NULL,
    codigo integer NOT NULL,
    PRIMARY KEY (numero, cpf, cnpj, codigo),
    FOREIGN KEY (cpf) REFERENCES clientes(cpf),
    FOREIGN KEY (cnpj) REFERENCES fornecedores(cnpj),
    FOREIGN KEY (codigo) REFERENCES equipamento(codigo)
    );