#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
#Ex.: 5!=5.4.3.2.1=120

num = int(input("Insira um número inteiro: "))

resultado = 1

for n in range(1, num + 1):
    resultado *= n

print(f'{num}! = {resultado}')
