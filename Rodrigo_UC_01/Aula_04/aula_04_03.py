# Faça um programa que receba do usuário o nome e a idade de 10 pessoas. Ao final mostre a soma e a média das idades.
# Utilizando a estrutura do programa anterior, identifique o nome da pessoa mais velha e a pessoa mais nova

# Entrda de Dados 
soma = 0
maior_idade = 0
menor_idade = 200

# Processamento dos dados - Estrutura de repetição
for i in range (3):
    nome = input("Informe o nome do usuário: ")
    idade = int(input("Informe a sua idade: "))
    soma = soma + idade
    
    if idade > maior_idade:
        velho = nome
        maior_idade = idade

        
    if idade < menor_idade:
        novo = nome
        menor_idade = idade 


   
#Saída dos dados
print (f"A soma das idades foi: {soma} ")
print (f"A média das idades foi {(soma/ (i+1)):.2f}")
print (f"A pessoa mais velha é: {velho}")
print (f"A pessoa mais nova é: {novo}")