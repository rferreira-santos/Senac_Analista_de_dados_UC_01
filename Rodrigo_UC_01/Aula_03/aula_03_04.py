# Faça um programa que pergunte a uma pessoa, a sua idade, o seu peso e quanto dormiu nas últimas 24 h e diga se ela pode doar ou não sangue de acordo com as seguintes condições
#• Ter entre 16 e 69 anos.
#• Pesar mais de 50 kg.
#• Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas)

#Entrada de Dados

nome = (input("Informe o seu nome: "))
idade = int(input(f"{nome}, informe a sua idade: "))
peso = float(input(f"{nome},Informe o seu peso: "))
horas = int(input(f"{nome}, Informe a Quantidade de horas que dormiu nas últimas 24 Horas: "))

# Processamento de dados

if idade >= 16 and idade <= 69 and peso >50 and horas >=6 :
    print (f"Sr(a) {nome}, pode doar sangue")
elif idade <16 or idade >70:
    print (f"Sr(a) {nome}, para doação a sua idade deverá estar entre 16 e 69 anos")
elif peso < 50:
    print (f"Sr(a) {nome}, para doação o seu peso deverá estar acima de 50 KG")
elif horas < 6:
    print (f"Sr(a) {nome}, para doação deverá ter dormido pelo menos 6 horas")
