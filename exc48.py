##Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.

    #Exemplo:

      #12376489
      #=> 98467321
num = int(input("Digite um número inteiro positivo: "))
num_str = str(num)

print(''.join(reversed(num_str)))