#Faça um programa que calcule o valor total investido por um colecionador 
# em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário 
# deverá informar a quantidade de CDs e o valor para em cada um. 

cd = int(input('Digite a quantidade de CDs da sua coleção: '))

valor_total = 0
media = 0

for count in range(1, cd + 1):
    valor = float(input(f'Informe o valor do {count}º CD: '))
    valor_total += valor
    media = valor_total / cd

print(f'O valor total investido foi: R$ {valor_total:.2f}')
print(f'O valor médio gasto em cada CD foi: R$ {media:.2f}')