menu = '''
Digite uma das operações abaixo:
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
'''
limite_diario = 3
limite_valor = 500
saldo = 2000
numero_saque = 0
extrato = ""

while True:
    opcao  = input(menu)
    if opcao == "d":
        valor_deposito = float(input("Digite qual valor deseja depositar: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'Depósito: R${valor_deposito:.2f}\n'
            print("Depósito realizado com sucesso")
        else: 
            print("Não é possível realizar a operação, tente novamente")
    elif opcao == "s":
        valor_saque = int(input("Digite o valor para sacar: "))
        if numero_saque<limite_diario and valor_saque<=limite_valor and saldo >= valor_saque and valor_saque > 0:
            saldo -= valor_saque
            numero_saque += 1
            extrato += f'Saque: -R${valor_saque:.2f}\n'
            print(f"Saque realizado com sucesso, você pode realizar mais {limite_diario-numero_saque} saques hoje")
        elif saldo <= valor_saque:
            print("Não é possível realizar a operação, saldo insuficiente")
        elif valor_saque > limite_valor:
            print(f"Não é possível realizar a operação, valor excede o limite de R${limite_valor:.2f}")    
        else:
            print("Não foi possível realizar a operação, tente novamente")
    elif opcao == "e":
        if extrato == "":
             print(f'''
--------EXTRATO-----------
Não foram realizadas movimentações

--------------------------
saldo final: R$ {saldo:.2f}
''')         
        else:
           print(f'''
--------EXTRATO-----------
{extrato} 
--------------------------
saldo final: R$ {saldo:.2f}
''')
    elif opcao == "q":
        break
    else:
        print("Operação inválida, tente novamente")       
                
