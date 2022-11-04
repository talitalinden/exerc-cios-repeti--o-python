#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes 
#e limitando o fatorial a números inteiros positivos e menores que 16. 

quant = int(input('Insira a quantidade de números que serão calculados: '))

for i in range(1, quant + 1):
    while True:
        num = int(input(f'Insira o {i}º número: '))
        if 0 < num < 16:
            break
        else:
            print('Valor inválido. Tente novamente.')

    resultado = 1
    for n in range(1, num + 1):
        resultado *= n
    print(resultado)