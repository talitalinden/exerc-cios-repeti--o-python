#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
#Faça um programa que gere a série até que o valor seja maior que 500.

termos = int(input("Digite a quantidade de termos: "))
n1, n2 = 0, 1
count = 500
print(n2)

for count in range(termos):
    termo = n1 + n2
    n1 = n2
    n2 = termo
    count += 500
    print(termo)