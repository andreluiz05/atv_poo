print("=CADASTRO DE USUÁRIO E IDADE=")

user = input("Digite seu nome de usuário: ")

while user == "" or user.isnumeric():
    print("Usuário inválido! Não pode ser vazio ou só números.")
    user = input("Digite seu nome de usuário: ")

print("Usuário aceito!")

idade = input("Digite sua idade: ")

while idade == "" or not idade.isnumeric() or int(idade) <= 0:
    print("Idade inválida! Digite apenas número e maior que zero.")
    idade = input("Digite sua idade corretamente: ")

idade = int(idade)

print("Idade aceita!")
print("Seja bem vindo,", user,"! Você tem", idade,"anos! CADASTRO CONCLUÍDO COM SUCESSO!")
