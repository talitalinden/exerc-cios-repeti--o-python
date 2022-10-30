#Faça um programa que leia 5 números e informe o maior número. 

num = int(input(f'Digite um número de 1 a 5: '))
maior = 0

for num in range(1, 6):
    print(num)
if num > maior:
    print(f'{num} é o maior número.')