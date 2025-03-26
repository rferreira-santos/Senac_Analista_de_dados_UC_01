#Faça um programa que obtenha o valor para a variável HT (horas trabalhadas no mês), obtenha o valor para a variável VH (valor hora trabalhada), obtenha o valor para a variável PD (percentual de desconto) e calcule o salário bruto => SB = HT * VH, mais o total de desconto => TD = (PD/100)*SB e o salário líquido => SL = SB – TD. Apresentando ao final o Salário Liquido

#Entrada de Dados
nome = input("Informe o seu nome: ")
ht = float(input(f"Informe as horas trabalhadas no mês:"))
vh = float(input(f"Informe o valor das horas trabalhadas no mês:"))
pd = float(input(f"Informe o percentual de desconto:"))

#Processamento dos Dados

SB = ht * vh
TD = (pd/100)*SB
SL = SB - TD

# Saída dos Dados
print(f"O Salário Líquido é de R$: {SL:.2f}")