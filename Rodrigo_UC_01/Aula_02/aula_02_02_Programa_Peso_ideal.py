#Tendo como dado de entrada à altura (h) de uma pessoa, construa um programa que calcule
#seu peso ideal, utilizando as seguintes fórmulas:
#* Para homens: (72.7*h) - 58
#* Para mulheres: (62.1*h) - 44.7

#Programa Peso Ideal 

#Entrada de Dados

nome = input("Informe o seu nome: ")
altura = float(input(f"Informe a sua altura em metros {nome}"))

#Processamento dos Dados
h = (72.7*altura) - 58
m = (62.1*altura) - 44.7

# Saída dos Dados
print(f"O Peso ideal para homens é {h:.0f} Kg.")
print(f"O Peso ideal para Mulheres é {m:.0f} Kg.")        