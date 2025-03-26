# Programa Média

# Entrada de Dados
nome = input("Informe o Nome do Estudante: ") # entrada de dados
n1 = float(input(f"Informe a Nota 1 do estudante {nome}: ")) # entrada de dados, float transforma a string em números decimais 
n2 = float(input(f"Informe a Nota 2 do estudante {nome}: "))
n3 = float(input(f"Informe a Nota 3 do estudante {nome}: "))

# Processamento dos Dados
media = (n1+n2+n3)/3

# Saída dos Dados
print(f"Sr(a) {nome}, a sua média foi{media:.2f}")