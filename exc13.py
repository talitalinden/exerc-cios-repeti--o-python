#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
#Não utilize a função de potência da linguagem. 

base = int(input("Digite um número base: "))
expo = int(input("Digite um número expoente: "))

potencia = 1
for count in range(expo):
    count += 1
    potencia *= base

print(potencia)