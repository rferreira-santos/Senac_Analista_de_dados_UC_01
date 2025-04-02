nomes = "Rodrigo Ferreira"
nomes_listas = ['Rorigo','Anna', 'Louise']
num = []

for i in range(5):
    num.append(int(input("Informe um valor inteiro:")))

for i in range (len(num)): #comando Len pega a lista     
    print (f"O número {num[i]} esta na posição {i} da lista")

print (num)
print (nomes)
print (nomes_listas)
print (nomes_listas [2])
