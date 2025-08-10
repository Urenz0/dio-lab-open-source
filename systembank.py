import time
saldo = 0.0
limite = 500.0
extrato = []
Menu ="""
--------------------- Sistema Bancário ---------------------
    1 -> Depositar
    2 -> Sacar
    3 -> Visualizar extrato
    4 -> Sair
    Escolha uma opção: 
"""
while True:
    print(Menu)
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        valor = float(input("Digite o valor para depositar: "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
            time.sleep(1)
        else:
            print("Valor inválido para depósito.")
            time.sleep(1)
    elif opcao == "2":
        valor = float(input("Digite o valor a sacar: "))
        if valor > limite:
            print(f"Valor excede o limite de saque diário R${limite:.2f}.")
            time.sleep(1)
            continue
        if valor <= 0:
            print("Valor inválido para saque.")
            time.sleep(1)
            continue
        if valor > saldo:
            print("Saldo insuficiente para realizar o saque.")
            time.sleep(1)
        else:
            saldo -= valor
            limite -= valor
            extrato.append(f"Saque: R${valor:.2f}")
            print(f"Saque no valor de R${valor:.2f} realizado com sucesso.")
            time.sleep(1)
            
    elif opcao == "3":
        print("\n--------------------- Extrato Bancário ---------------------")
        if extrato:
            for item in extrato:
                print("  ", item)
        else:
            print("Não foram realizadas movimentações.")
        print("\n----------------- Saldo Atual -----------------")
        print(f"Saldo atual: R${saldo:.2f}")
        time.sleep(2)
    elif opcao == "4":
        print("Finalizando Operação. Até logo!")
        time.sleep(1)
        break
    else:
        print("Opção inválida. Tente novamente.")
        time.sleep(1)