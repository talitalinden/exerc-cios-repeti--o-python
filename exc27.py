#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça 
#a quantidade de turmas e a quantidade de alunos para cada turma. 
#As turmas não podem ter mais de 40 alunos. 

turma = int(input('Digite a quantidade de turmas: '))

soma_alunos = 0
media = 0

for i in range(1, turma + 1):
    while True:
        alunos = int(input(f'Insira a quantidade de alunos da {i}ª turma: '))
        if alunos <= 40:
            break
        else:
            print('As turmas não podem ter mais de 40 alunos.')
            print('Tente novamente.')
    soma_alunos += alunos
    media = soma_alunos / turma

print(f'O número médio de alunos por turma é: {media:.2f}')