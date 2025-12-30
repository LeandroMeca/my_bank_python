menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
quantidade_saques = 0
QUANTIDADE_LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            if saldo < 0:
                 taxa = abs(saldo) * 0.01
                 print(f"Sua conta está negativa em R$ {saldo:.2f}.")
                 print(f"Taxa de 1% sobre a dívida: R$ {taxa:.2f}")
                 
                 transacao_limite = input("Deseja continuar? [s/n]: ")
                 
                 if transacao_limite.lower() == "s":
                     valor_liquido = valor - taxa
                     saldo += valor_liquido
                     extrato += f"Depósito: R$ {valor:.2f} (- Taxa dívida: R$ {taxa:.2f})\n"
                     print(f"Depósito realizado! Saldo atual: R$ {saldo:.2f}")
                 else:
                     print("Operação cancelada.")
            else:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("Depósito realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_limite = valor > limite
        excedeu_saques = quantidade_saques >= QUANTIDADE_LIMITE_SAQUES
        
        if excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
        
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários excedido.")
            
        elif valor > 0:
            if valor > saldo:
                print("Saldo insuficiente. Você entrará no cheque especial.")
                op = input("Tem certeza que deseja continuar? [s/n]: ")
                
                if op.lower() == "s":
                    saldo -= valor
                    extrato += f"Saque (Cheque Esp.): R$ {valor:.2f}\n"
                    quantidade_saques += 1
                    print("Saque realizado (Cheque Especial).")
                else:
                    print("Saque cancelado.")
            
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                quantidade_saques += 1
                print("Saque realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")