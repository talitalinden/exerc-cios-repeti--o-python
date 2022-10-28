#Faça um programa que leia um nome de usuário e a sua senha e 
# não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações. 

nome = (input("Digite o seu nome: "))
senha = float(input("Digite a sua senha: "))
while senha == nome:
    senha = float(input("Senha não permitida. Digite novamente"))
print("Senha permitida.")