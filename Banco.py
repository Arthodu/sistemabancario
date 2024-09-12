menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] sair

=> """

saldo = 0
limite = 500
extrato  = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  opcao = input(menu)

  if opcao == "1":
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
      saldo += valor
      extrato += f"Depósito : R$ {valor:.2f}\n"
    else:
      print("Operação falhou! O valor informado é inválido.")

  elif opcao == "2":
    valor = float(input("Informe o valor do saque:"))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
      print(" Operação falhou! Você não tem salo suficiente.")
    elif excedeu_limite:
      print(" Operação falhou! O valor excede o limite.")
    elif excedeu_saques:
      print("Operação falhou! Numero máximo de saques excedidos.")
    elif  valor > 0:
      saldo -= valor
      extrato += f"Saque: R$ {valor:.2f}\n"
      numero_saques += 1
    else:
      print("Operação falhou! O valor informado é inválido.")
      
  elif opcao == "3":
    print("\n============Extrato============")
    print("Não foram encontradas nenhuma movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========Fim do extrato==========")

  elif opcao == "4":
    break  

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")
