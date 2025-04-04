#Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, aqual coletaram os seguintes dados referentes a cada habitante para serem analisados:
#- sexo (masculino e feminino)
#- cor dos olhos (azuis, verdes ou castanhos)
#- cor dos cabelos (louros, castanhos, pretos)
#- idade
#Faça um programa que determine e escreva:
#a) a maior idade dos habitantes;
#b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
#c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros;

#Entrada de Dados
idade = []
sexo = []
olhos = []
cabelos = []
maior = 0
ind_fem = 0
individuos = 0
# Processamento dos dados

for i in range(3):
    idade.append(int(input("Informe a idade da Pessoa: ")))
    #if idade[i] >= 18 and idade[i] <=35:
    #    maior = maior +1
    #else:
    #    maior = maior 
    sexo.append(input("Informe o sexo da pessoa: (F) para Feminino e (M) para masculino "))
    if sexo [i] == "F" and idade[i] >= 18 and idade[i] <=35:
        ind_fem = ind_fem + 1
    else:
        ind_fem = ind_fem
    olhos.append(input("escolha a cor dos olhos: Azuis, verdes ou castanhos: "))
    cabelos.append(input("escolha a cor dos cabelos: Louros, castalhos ou pretos: "))
    if olhos[i] == "verdes" and cabelos[i] == "louros":
        individuos = individuos + 1
    else:
        individuos = individuos

maior = max (idade)

#Saída dos dados
print (f"\nA maior idade dos intrevistados é: {maior} anos.")
print (f"\nO Total de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos é de: {ind_fem} ")
print (f"\nO Total de indivíduos que tenham olhos verdes e cabelos louros é de: {individuos} ")