# Faça um programa que leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é: F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em Celsius;

#Programa Temperatura 

#Entrada de Dados

nome = input("Informe o seu nome: ")
temp = float(input(f"Informe Temperatura {nome}: "))

# Processamento dos Dados
f = (9 * temp + 160) / 5

#Saída de Dados
print (f"{nome} a temperatura em Fahrenheit é: {f}F")