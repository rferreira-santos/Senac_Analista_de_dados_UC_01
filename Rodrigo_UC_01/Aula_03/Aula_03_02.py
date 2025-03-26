#Tendo como dado de entrada à altura (h) de uma pessoa, construa um programa que calcule
#seu peso ideal, utilizando as seguintes fórmulas:
#* Para homens: (72.7*h) - 58
#* Para mulheres: (62.1*h) - 44.7

#Programa Peso Ideal 

#Entrada de Dados

nome = input("Informe o seu nome: ")
altura = float(input(f"Informe a sua altura em metros {nome}:"))
sexo = (input (f"Informe seu sexo, (F) para Feminino e (M) para masculino:"))

#Processamento dos Dados
if sexo == 'm' or sexo == 'M':
    m = (62.1*altura) - 44.7
    print(f"Sr(a) {nome} O seu peso ideal é {m:.2f} Kg.")
elif sexo == 'f' or sexo =='F':
    f = (72.7*altura) - 58
    print(f"Sr(a) {nome} O seu peso ideal é {f:.2f} Kg.")
else:
    print("Verifique o Sexo informado")