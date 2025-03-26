#CONSTRUA UM PROGRAMA PARA LIBERAR ACESSO PARA MAIORES DE 18 ANOS

#Entrada de Dados

idade = int(input("Informe a sua Idade"))

#Processamento e saída de Dados

if idade < 18:
    print("você é menor de Idade")
elif idade == 18:
    print("Você tem exatos 18 anos - Acesso Liberado")
elif idade >= 18 and idade <65:
    print("Você tem mais de 65 anos - Acesso Liberado com Cautela")
else:
    print("Acesso Liberado")
