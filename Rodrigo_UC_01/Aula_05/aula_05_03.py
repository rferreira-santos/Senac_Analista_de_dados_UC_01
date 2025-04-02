#Construa um programa que armazene 10 números inteiros em um vetor. Ao final informe quantos números são pares e quantos são ímpares e mostre o vetor principal na ordem inversa e depois na ordem crescente

num = []
calculo = 0
par = 0
impar = 0
num_par =[]
num_imp = []
for i in range(10):
    num.append(int(input("Informe um valor inteiro:")))
    calculo = num[i] % 2  
    if calculo == 0:
        num_par.append(num[i])
        par = par + 1
    else:
        num_imp.append(num[i])
        impar = impar + 1
        
print(f"\nO total de Números Pares é {par}")
print(num_par)
print(f"\nO total de Números Impares é {impar}")
print(num_imp)
num.sort(reverse=True)
print('\nLista em Ordem Reversa')
print(num)
print('\nLista em Ordem Crescente')
num.sort()
print (num)
print('\n')