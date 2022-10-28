#Faça um programa que leia e valide as seguintes informações:
    #Nome: maior que 3 caracteres;
    #Idade: entre 0 e 150;
    #Salário: maior que zero;
    #Sexo: 'f' ou 'm';
    #Estado Civil: 's', 'c', 'v', 'd'; 

nome = str(input("Digite o seu nome: "))
if len(nome) < 3:
    print("Nome inválido")
else:
    print("Nome válido")

idade = int(input("Digite a sua idade: "))
if 0 < idade < 150:
    print("Idade correta")
else:
    print("Idade não correta")

salario = float(input("Digite o seu salário: "))
if salario > 0:
    print("Salário correto.")
else:
    print("Salário inválido")

sexo = str(input('Sexo (F-Feminino, M-Masculino): ')).upper()
if sexo in 'FM':
    print("Informação válida")
else:
    print('informação inválida')

estado_civil = str(input("Seu estado civil ( S-solteiro, C-casado, V-viúvo, D-divorciado): ")).upper()
if estado_civil in 'SCVD':
    print("Informação válida")
else:
    print("Informação inválida")
