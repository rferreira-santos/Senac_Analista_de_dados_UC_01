#Faça um programa para uma loja de tintas, que solicite o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 130,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o valor a ser pago

#Entrada de Dados
nome = input("Informe o seu nome: ")
metros = int(input(f" Sr(a) {nome}, Informe a Quantidade de metros quadrados a serem pintados:"))
qtd_latas = 0
#Processamento dos Dados
import math
total_litros = metros / 3
qtd_latas= total_litros / 18
qtd_latas = math.ceil(qtd_latas)
valor_pagar = qtd_latas * 130

#Saída de Dados

print (f"Sr(a) {nome} será necessário comprar {qtd_latas} latas de tinta, e o valor total é de R${valor_pagar:.2f}.")