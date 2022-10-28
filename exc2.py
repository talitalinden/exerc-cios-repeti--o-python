#Faça um programa que leia um nome de usuário e a sua senha e 
# não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações. 

#Faça um programa que leia um nome de usuário e a sua senha e 
# não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações. 

nome = str(input("Digite o seu nome: "))
senha = input("Digite a sua senha: ")

while nome != senha:
    print("A senha está correta.")
    if nome == senha:
        print("A senha deve ser diferente do seu nome.")
    break
else:
    print ("Digite a sua senha novamente: ")

