C1 = int(1)
C2 = int(2)
C1nom = "John Doe"
C1senha = "123"
C1saldo = float(0)
C2nom = "Jane Dow"
C2senha = "123"
C2saldo = float(100)

contaCard = int()
senhaCard = int()

def inserirCard():
  global contaCard
  contaCard = int(input("Insira o número da conta: "))
  senhaCard = input("Insira a senha do cartao: ")

  if (contaCard != C1 and contaCard != C2 and isinstance(contaCard, int)):
    print("Número de conta invalido")
    return inserirCard()
  elif(senhaCard != C1senha and senhaCard != C2senha and not senhaCard):
    print("Senha da conta incorreta")
    return inserirCard()
  return chamarSubMenuCard()

def adicionarSaldo(contaDestino, valorTransferencia):
  global C1saldo
  global C2saldo
  if (contaDestino == C1):
    C1saldo = C1saldo + valorTransferencia
  elif(contaDestino == C2):
    C2saldo = C2saldo + valorTransferencia
  print("Deposito realizado com sucesso!")
  return chamarMenu()

def Deposito():
  contaDestino = int(input("Insira o número da conta: "))
  valorTransf = float(input("Insira o valor do depósito: R$ "))

  if (contaDestino == C1 or contaDestino == C2):
    return adicionarSaldo(contaDestino, valorTransf)
  else :
    return Deposito()

def Saldo():
  if (contaCard == C1):
    print("Senhor(a) {}, seu saldo atual é: R$ {}".format(C1nom, C1saldo))
  elif(contaCard == C2):
    print("Senhor(a) {}, seu saldo atual é: R$ {}".format(C2nom, C2saldo))
  return chamarSubMenuCard()

def Saque():
  global contaCard
  global C1saldo
  global C2saldo

  valorSaque = float(input("Insira o valor de saque: "))
  
  if(valorSaque <= 0):
    print("Valor de saque precisa ser maior que zero")
    return chamarSubMenuCard()

  if contaCard == C1:
    if (valorSaque > C1saldo):
      print("Conta nao tem saldo suficiente para saque")
      return chamarSubMenuCard()

    print("Seu saldo é: R$ ", C1saldo)
    print("Valor de saque: R$ ", valorSaque)
    print("Saldo restante na conta apos saque: R$ ",(C1saldo - valorSaque))
    resposta = int(input("Para confirmar digite 1: "))

    if (resposta == 1):
      C1saldo = C1saldo - valorSaque
      print("Saque realizado com sucesso")
      return chamarSubMenuCard()
    else :
      print("Saque nao realizado")
      return chamarSubMenuCard()
  
  elif contaCard == C2:
    if (valorSaque > C2saldo):
      print("Conta nao tem saldo suficiente para saque")
      return chamarSubMenuCard()
    print("Seu saldo é: R$ ", C2saldo)
    print("Valor de saque: R$ ", valorSaque)
    print("Saldo restante na conta apos saque: R$ ",(C2saldo - valorSaque))
    resposta = int(input("Para confirmar digite 1"))

    if (resposta == 1):
      C2saldo = C2saldo - valorSaque
      print("Saque realizado")
      return chamarSubMenuCard()
    else :
      print("Saque nao realizado")
      return chamarSubMenuCard()
  return

def Transferencia():
  global contaCard
  global C1saldo
  global C2saldo

  contaDestino = int(input("Digite o numero da conta destino: "))
  valorTransf = float(input("Digite o valor a ser transferido: "))
  
  if (contaDestino != C1 and contaDestino != C2 and isinstance(contaDestino, int)):
      print("Número de conta invalido")
      return chamarSubMenuCard()
  elif (valorTransf <= 0):
    print("Valor inválido")
    return chamarSubMenuCard()
  
  if ((contaCard == C1 and valorTransf > C1saldo) or (contaCard == C2 and valorTransf > C2saldo)):
    print("Conta nao tem saldo suficiente para transferencia")
    return chamarSubMenuCard()

  if (contaCard == C1 and contaDestino == C2):
    print("Seu saldo é: R$ ", C1saldo)
    print("Valor de transferência: R$ ", valorTransf)
    print("Saldo restante na conta apos transferência: R$ ",(C1saldo - valorTransf))

    resposta = int(input("Para confirmar digite 1"))
    if (resposta == 1):
      C1saldo = C1saldo - valorTransf
      C2saldo = C2saldo + valorTransf
      print("Transferência realizada")
      return chamarSubMenuCard()
    else :
      print("Transferência não realizada")
      return chamarSubMenuCard()
  elif (contaCard == C2 and contaDestino == C1):
    print("Seu saldo é: R$ ", C2saldo)
    print("Valor de transferência: R$ ", valorTransf)
    print("Saldo restante na conta apos transferência: R$ ",(C2saldo - valorTransf))

    resposta = int(input("Para confirmar digite 1"))
    if (resposta == 1):
      C2saldo = C2saldo - valorTransf
      C1saldo = C1saldo + valorTransf
      print("Transferência realizada")
      return chamarSubMenuCard()
    else :
      print("Transferência não realizada")
      return chamarSubMenuCard()
  else:
    print("Transferência não realidada, tente novamente!")
    return chamarSubMenuCard()

def chamarSubMenuCard():
  menu = int(
    input(
      "4 - Saque \n5 - Transferencia\n6 - Saldo \n0 - Voltar menu anterior\n"
    ))
  if (menu == 4):
    return Saque()
  if (menu == 5):
    return Transferencia()
  if (menu == 6):
    return Saldo()
  if (menu == 0):
    return chamarMenu()
  return

def Desligar():
  print(chr(27) + "[2J")
  print("Relatorio final\n")
  print("== Conta 1 ==")
  print("Num: ", C1)
  print("Nome do titular: ", C1nom)
  print("Saldo em conta: ", C1saldo)
  print("== Conta 2 ==")
  print("Num: ", C2)
  print("Nome do titular: ", C2nom)
  print("Saldo em conta: ", C2saldo)
  
  menu = int(input("\nPressione 1 para desligar\n"))
  if (menu == 1):
    return
  else:
    return chamarMenu()

def chamarMenu():
  menu = int(input("1 - Inserir Cartão \n2 - Depósito \n3 - Desligar\n"))
  if (menu == 1):
    return inserirCard()
  if (menu == 2):
    return Deposito()
  if (menu == 3):
    return Desligar()
  else :
    print("Opção selecionada inválida")
    return chamarMenu()

chamarMenu()