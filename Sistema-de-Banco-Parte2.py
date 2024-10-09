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

def sacar(*,saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    print("============== SACAR ==============")
    if numero_saques < LIMITE_SAQUES:
        valor_saque = float(input("Digite o valor para saque: "))
        if valor_saque > saldo:
            print("Operação invalida, valor maior que o Saldo!")
        elif valor_saque > limite:
            print("O LIMITE MAXIMO DE SAQUE É: R$ 500,00")
        else:
            numero_saques += 1
            saldo -= valor_saque
            extrato += f"Saque: -R$ {valor_saque}\n"
            print("Valor sacado com sucesso!")
    else:
        print("O LIMITE DE SAQUES SÃO 3x AO DIA!!!!")
    return saldo, extrato, numero_saques

def depositar(saldo,extrato, /):
    print("=== Deposito ===")
    valor_deposito = float(input("Digite o valor para Deposito: "))
    if valor_deposito <= 0:
        print("Valor invalido, tente novamente!")
    else:
        saldo += valor_deposito
        extrato += f"Depósito: +R$ {valor_deposito}\n"
        print("Valor depositado com sucesso!")
    return saldo, extrato

def mostrarExtrato(saldo,*,extrato):
    print("=== Extrato ===")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("Saldo Atual: ",saldo)
    print("===============")
    return saldo, extrato

while True:
    opcao = input(menu)

    if opcao == "1":
        saldo, extrato = depositar(0,"")
        print(f"Saldo Atual: {saldo}")
        

    elif opcao == "2":
        saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, limite=limite,numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
        print(f"Saldo Atual: {saldo}")
        

    elif opcao == "3":
        mostrarExtrato(saldo,extrato=extrato)

    elif opcao == "4":
        print("Programa Finalizado!")
        exit()
    else:
        print("Opção invalida, tente novamente!")