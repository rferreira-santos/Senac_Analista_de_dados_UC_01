#O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um programa que leia um conjunto indeterminado de temperaturas, ao final informe a menor e a maior temperatura, bem como a média delas
temperatura = []
resp = "S"
x = 0
#Entrada de Dados
for i in range(0):
    temperatura.append(int(input("Informe a temperatura em Celsius:")))
while resp ==  "S" or resp == "s":
    temperatura.append(int(input("Informe a temperatura em Celsius:")))
    x = x + 1
    resp = str(input("Deseja Continuar (S/N)"))

maior = max (temperatura)
menor = min (temperatura)
media = sum (temperatura) / len (temperatura)

print (f"\nA maior temperatura foi de {maior}ºC. ")
print (f"\nA menor temperatura foi de {menor}ºC. ")
print (f"\nA média da temperatura foi de {media:.2f}ºC. ")

