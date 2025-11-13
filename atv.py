print("=CADASTRO DE USUÁRIO E IDADE=")

user = str(input("Digite seu nome de usuário: "))
if user == "" or user.isnumeric():
    print("Usuário com número ou vazio! Preencha corretamente!")
   
while user == "" or user.isnumeric():
        user = str(input("Digite seu nome de usuário: "))

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
                continue

            idade = int(idade)

    print("Idade aceita!")

except:
    print("Erro! Você digitou número inválido ou não inseriu idade!")

    while idade == "" or not idade.isnumeric() or int(idade) <= 0:
        idade = input("Digite sua idade corretamente: ")

    idade = int(idade)

print("Seja bem vindo,", user,"! ""Você tem", idade,"anos !", " CADASTRO CONCLUÍDO COM SUCESSO!")
