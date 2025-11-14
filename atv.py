print("=CADASTRO DE USUÁRIO E IDADE=")

user = input("Digite seu nome de usuário: ")

while user == "" or user.isnumeric():
    print("Usuário inválido! Não pode ser vazio nem só números.")
    user = input("Digite seu nome de usuário: ")

print("Usuário aceito!")

idade = input("Digite sua idade: ")
try:
    idade = int(idade)

    if idade <= 0:
        print("Erro! A idade deve ser maior que zero!")

        while idade <= 0 or idade == "":
            idade = input("Digite sua idade corretamente: ")

            if idade == "":
                print("Erro! Não deixe vazio!")
                

            idade = int(idade)

    print("Idade aceita!")

except:
    print("Erro! Você digitou número inválido ou não inseriu idade!")

    while idade == "" or not idade.isnumeric() or int(idade) <= 0:
        idade = input("Digite sua idade corretamente: ")

    idade = int(idade)

print("Seja bem vindo,", user,"! ""Você tem", idade,"anos !", " CADASTRO CONCLUÍDO COM SUCESSO!")
