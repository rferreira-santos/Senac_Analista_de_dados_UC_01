# 1- Escreva um programa que, dados 2 números inteiros (n1 e n2), diga se eles são iguais ou diferentes.
#2- Utilizando a estrutura do programa anterior, some os dois valores se forem diferentes e multiplique-os se forem iguais.

#Entrada de Dados

n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))

#Processamento de dados

if n1 == n2:
    valor = n1 * n2
    print (f"Eles são iguais, e a sua multiplicação é,{valor}")
    # print (f"Eles são iguais, e a sua multiplicação é,{n1 * n2 }") modo utimizado 
else: 
    valor = n1 + n2
    print (f"Eles são diferentes, e a sua soma é,{valor}")