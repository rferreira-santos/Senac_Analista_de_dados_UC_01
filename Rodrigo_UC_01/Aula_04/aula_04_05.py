#Utilizando apenas o conceito de repetição, faça um programa para ler 2 valores e se o segundo valor informado for ZERO, deve ser lido um novo valor, pois o segundo valor não pode ser igual a zero. Ao final imprimir o resultado da divisão do primeiro valor pelo segundo valor.

# Entrda de Dados 
divisao = 0
for i in range (2):
    n1 = int(input(f"Informe o primeiro número: "))
    n2 = int(input(f"Informe o segundo número: "))
    if n2 == 0:
        n2 = int(input(f"O valor informado não pode ser Zero, informe um novo valor: "))
    divisao = n1/n2
    print (f"A divisão do primeiro valor sobre o segundo é {divisao:.2f}")

    ## Entrada de Dados
#n1 = int(input("Digite o primeiro valor: "))
#n2 = int(input("Digite o segundo valor: "))

# Processamento dos Dados
#while n2 == 0:
#    n2 = int(input("Digite o segundo valor: "))

# Saída de Dados
#print(f"O resultado da divisão de {n1} por {n2} é: {(n1 / n2):.2f}")