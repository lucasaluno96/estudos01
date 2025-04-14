#exemplo de saldo em banco
senha = ""
saldo = 0

# Primeiro: verificação da senha
while senha != "1234":
    senha = input("Digite a senha para acessar sua conta: ")

print("Bem-vindo ao caixa eletrônico!")

# Menu principal
opcao = ""

while opcao != "4":
    print("\nMenu:")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Seu saldo atual é: R$ {saldo}")
    elif opcao == "2":
        valor = float(input("Digite o valor para depositar: "))
        saldo += valor
        print(f"Depósito de R$ {valor} realizado com sucesso.")
    elif opcao == "3":
        valor = float(input("Digite o valor para sacar: "))
        if valor <= saldo:
            saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")
    elif opcao == "4":
        print("Saindo... obrigado por usar nosso banco.")
    else:
        print("Opção inválida. Tente novamente.")
