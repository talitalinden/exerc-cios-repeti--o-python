#Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0

for i in range(1, 6):
    num = float(input(f'Digite o {i}º número: '))
    soma += num
media = soma / 5

print(f'Soma dos números: {soma:.2f}')
print(f'Média dos números: {media:.2f}')