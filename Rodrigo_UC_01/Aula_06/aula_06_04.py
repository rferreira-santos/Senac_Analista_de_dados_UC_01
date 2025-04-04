#Crie um programa que:
#1- Peça ao usuário para digitar dez números inteiros e os armazene em uma lista.
#2- Exiba a lista completa.
#3- Exiba o maior e o menor número da lista.
#4- Exiba a soma e a média de todos os números.

#Entrada de Dados
num = []

# Processamento dos dados
for i in range(10):
    num.append(int(input("Informe um valor inteiro:")))

soma = sum (num)
maior = max (num)
menor = min (num)
#Saída dos dados
print (num)
print (f"\nO maior número foi o: {maior}")
print (f"\nO menor número foi o: {menor}")
print (f"\nA soma de todos os números foi: {soma}")


