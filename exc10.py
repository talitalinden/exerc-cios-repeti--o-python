#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles. 

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
  for i in range(num2 + 1, num1, 1):
    print(i)
else:
  for y in range(num1 + 1, num2,1):
    print(y)
