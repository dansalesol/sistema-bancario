menu = """
======== SISTEMA BANCÁRIO ========
[d] Depositar
[s] Sacar
[e] Extrato
[t] Transferência
[q] Sair
==================================
=> """

saldo = 0
limite_saque = 1000
limite_transferencia = 800
extrato = ""
numero_saques = 0
numero_transferencias = 0
LIMITE_SAQUES = 3
LIMITE_TRANSFERENCIA = 2

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_saque

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "t":
        valor = float(input("Informe o valor a ser transferido: "))
        numero_conta_transferencia = input("Informe o número da conta a ser transferido: ")

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_transferencia

        excedeu_transferencias = numero_transferencias >= LIMITE_TRANSFERENCIA

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor da transferência excede o limite permitido por transação.")

        elif excedeu_transferencias:
            print("Operação falhou! Número máximo de transferências excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Transferência: R$ {valor:.2f} para conta {numero_conta_transferencia}\n"
            numero_transferencias += 1

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")