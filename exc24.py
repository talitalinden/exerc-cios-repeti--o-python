#Faça um programa que calcule o mostre a média aritmética de N notas. 

notas = int(input("Insira o número total de notas: "))

soma = 0
media = 0

for i in range(1, notas + 1):
    nota = float(input(f'Insira a {i}º nota: '))
    soma += nota
    media += soma / notas

print(f'A média é: {media:.1f}')