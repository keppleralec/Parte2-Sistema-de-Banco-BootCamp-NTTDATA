menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

--> """
valor_saque = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def sacar(saldo, extrato,valor_saque, limite,numero_saques,LIMITE_SAQUES):
    print("============== SACAR ==============")
    if numero_saques < LIMITE_SAQUES:
        numero_saques += 1
        valor_saque = float(input("Digite o valor para saque: "))
        if valor_saque > saldo:
            print("Operação invalida, valor menor que o Saldo!")
        elif valor_saque > limite:
            print("O limite maximo para saque é de: R$ 500,00")
        else:
            saldo -= valor_saque
            extrato += f"Saque: -R$ {valor_saque}\n"
            print("Valor sacado com sucesso!")
    else:
        print("O limite de saques são 3x ao dia!")
    return saldo, extrato


while True:
    opcao = input(menu)

    if opcao == "1":
        print("=== Deposito ===")
        valor_deposito = float(input("Digite o valor para Deposito: "))
        if valor_deposito <= 0:
            print("Valor invalido, tente novamente!")
        else:
            saldo += valor_deposito
            extrato += f"Depósito: +R$ {valor_deposito}\n"
            print("Valor depositado com sucesso!")

    elif opcao == "2":
        saldo, extrato = sacar(saldo, extrato,valor_saque, limite,numero_saques, LIMITE_SAQUES)
        print(f"Saldo Atual: {saldo}")
        print(f"\nExtrato: \n{extrato}")

    elif opcao == "3":
        print("=== Extrato ===")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("Saldo Atual: ",saldo)
        print("===============")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção invalida, tente novamente!")