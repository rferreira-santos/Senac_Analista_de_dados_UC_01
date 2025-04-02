#Faça um programa que verifique a quantidade de acertos de uma prova com cinco questões, sabendo que serão fornecidos pelo usuário as letras assinaladas em cada questão. Para isso será criado um vetor chamado GABARITO com as seguintes respostas: A, B, B, D, E.

# Entrda de Dados 

gabarito = ['A','B','B','D','E']
cartao = []
n = 1
acerto = 0
erro = 0
for i in range(5):
    cartao.append(input(f"Informe a resposta da {n}a questão: "))
    n+=1
   
for i in range(len(cartao)):
    if cartao[i].upper()== gabarito[i]:
        acerto +=1
    else:
        erro +=1
print('\nAs alternativas informadas foram')
print(cartao)
print('\nAs alternativas corretão são')
print(gabarito)
print(f"\nPortanto, você acertou {acerto} questão(s) e errou {erro} questão(s)")