#Crie um programa que calcule a idade de uma pessoa a partir do ano de nascimento dela.

#Importando Biblioteca 
import  datetime #importando biblioteca de data de hora
# Entrada de Dados
nome = input("Informe o seu nome: ")
ano_nasc = int (input(f"Informe a sua data de nascimento, {nome}: "))
data_atual = datetime.date.today()
ano_atual = data_atual.year

#Processamento de Dados
idade = ano_atual - ano_nasc

#Saída de Dados
print (f"{nome} a sua idade é: {idade} anos")