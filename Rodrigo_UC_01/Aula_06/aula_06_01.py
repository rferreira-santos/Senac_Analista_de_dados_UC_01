#1- Faça um programa que pergunte quanto um funcionário recebe por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário, sabendo que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#a) salário bruto.
#b) Quanto pagou ao IRRF.
#c) quanto pagou ao INSS.
#d) quanto pagou ao sindicato.
#e) o salário líquido.

#Entrada de Dados
nome = input("Informe o seu nome: ")
VH = float(input(f" Sr(a) {nome},Qual o valor da hora trabalhada:"))
HT = float(input(f"Sr(a) {nome},Informe a quantidade de horas trabalhadas no mês:"))

#Processamento dos Dados

SB = HT * VH
IRRF = (SB *  11)/100 
INSS = (SB * 8)/100
SIND = (SB * 5)/100
SL = (SB) - (IRRF) - (SIND)

# Saída dos Dados
print(f"\nSr(a) {nome} O Salário Bruto é de R$: {SB:.2f}")
print(f"\nSr(a) {nome} O Desconto do IRRF foi de  R$: {IRRF:.2f}")
print(f"\nSr(a) {nome} O Desconto do INSS foi de  R$: {INSS:.2f}")
print(f"\nSr(a) {nome} O Desconto do Sindicato foi de R$: {SIND:.2f}")
print(f"\nSr(a) {nome}O Salário Líquido é de R$: {SL:.2f}")
