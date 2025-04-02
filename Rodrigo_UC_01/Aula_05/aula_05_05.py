#Faça um programa que armazene em vetores o nome, a média e a situação de um grupo de 10 alunos. Ao final mostre o nome de cada aluno com sua respectiva situação.

# Entrada de Dados
nome = []
media = []
situacao = []
n = 1

# Processamento dos Dados

for i in range(5):
    nome.append(input(f"Informe a resposta da {n} Pessoa: "))
    media.append(input(f"Informe a média da {n} Pessoa"))
    situacao.append(input(f"Informe a situação da {n} Pessoa"))
    n+=1

# Saída de Dados
print (nome)
print (media)
print (situacao)