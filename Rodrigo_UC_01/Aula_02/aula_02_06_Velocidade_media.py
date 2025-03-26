#Escreva um programa que calcule a velocidade média de um veículo com base na distância percorrida e no tempo em que uma viagem foi realizada.
#Com base nos dados obtidos no programa anterior e sabendo que o veículo usado consome 12 Km/l, construa um programa que determine a quantidade de combustível gasto nessa viagem.

#Programa Velocidade Média 

#Entrada de Dados

dist = float(input(f"Informe a distância percorrida em KM:"))
temp = float(input(f"Informe o tempo percorrido em Horas:"))

# Processamento dos Dados
vel_med = dist / temp
Cons = dist / 12

#Saída de Dados
print (f"A Velocidade percorrida foi: {vel_med}KM/h e o seu consumo foi de: {Cons:.1f} Litros de combustível")
