#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
#Valide a entrada e permita repetir a operação. 

pais_a = float(input("Digite a população total do país A: "))
while pais_a < 1:
    print("Valor inválido. Tente novamente.")
taxa_a = float(input("Digite a taxa de crescimento anual do país A: "))
while taxa_a <= 0:
    print("Valor inválido. Tente novamente.")

pais_b = float(input("Informe a população total do país B: "))
while pais_b < pais_a:
    print("Valor inválido. Tente novamente.")
taxa_b = float(input("Digite a taxa de crescimento anual do país B: "))
while taxa_b > taxa_a:
    print("Valor inválido. tente novamente.")
while pais_a <= pais_b:
    pais_a = (pais_a * taxa_a / 100) + pais_a
    pais_b = (pais_b * taxa_b / 100) + pais_b
    anos += 1

print(f'A população do país A será maior que a população do país B em {anos} anos.')
