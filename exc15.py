#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
#Faça um programa capaz de gerar a série até o n−ésimo termo.

ntermos = (int(input("Digite a quantidade de termos: ")))
n1, n2 = 0, 1
count = 1
print(n2)

for count in range(ntermos):
    termo = n1 + n2
    n1 = n2
    n2 = termo
    count += 1
    print(termo)