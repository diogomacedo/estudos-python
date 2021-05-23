def computador_escolhe_jogada(n, m):
  #
  result = 0
  #
  if n == m:
    result = m
  elif n < m:
    result = n
  elif m > 1:
    encontrou = False
    valor = m - 1
    while not encontrou and valor > 0:
      if (n - valor) % (m + 1) == 0:
        encontrou = True
        break
      else:
        valor -= 1
    if not encontrou:
      result = m
    else:
      result = valor
  else:
    result = m
  #
  print()
  #
  if result == 1:
    print("O computador tirou uma peça.")
  else:
    print("O computador tirou", result, "peças.")
  #
  return result

def usuario_escolhe_jogada(n, m):
  #
  result = 0
  loop = True
  #
  while loop:
    #
    print()
    #
    qtde = int(input("Quantas peças você vai tirar? "))
    #
    if qtde > 0 and qtde <= n and qtde <= m:
      result = qtde
      loop = False
    else:
      print()
      print("Oops! Jogada inválida! Tente de novo.")
  #
  if result == 1:
    print()
    print("Você tirou uma peça.")
  else:
    print("Voce tirou", result, "peças.")
  #
  return result

def partida ():
  #
  qtdePecas = int(input("Quantas peças? "))
  limitePecas = int(input("Limite de peças por jogada? "))
  #
  """
    jogador = 0 -> sem jogador definido
    jogador = 1 -> jogador começa
    jogador = 2 -> computador começa
  """
  #
  print()
  #
  jogador = 0
  #
  if (qtdePecas % (limitePecas + 1)) == 0:
    jogador = 1
    print("Você começa!")
  else:
    jogador = 2
    print("Computador começa!")
  #
  ganhador = 0
  #
  while qtdePecas > 0:
    #
    valor = 0
    #
    if jogador == 1:
      valor = usuario_escolhe_jogada(qtdePecas, limitePecas)
    else:
      valor = computador_escolhe_jogada(qtdePecas, limitePecas)
    #
    qtdePecas = qtdePecas - valor
    #
    if qtdePecas == 0:
      ganhador = jogador
    #
    if qtdePecas > 1:
      print("Agora restam", qtdePecas, "peças no tabuleiro.")
    elif qtdePecas == 1:
      print("Agora resta apenas uma peça no tabuleiro.")
    #
    if jogador == 1:
      jogador = 2
    else:
      jogador = 1
  #
  if ganhador == 1:
    print("Fim do jogo! Você ganhou!")
  else:
    print("Fim do jogo! O computador ganhou!")
  #
  return ganhador

def campeonato():
  print("Bem-vindo ao jogo do NIM! Escolha:")
  print()
  print("1 - para jogar uma partida isolada")
  #
  opcaoEscolhida = int(input("2 - para jogar um campeonato "))
  #
  print()
  #
  if opcaoEscolhida == 1:
    print("Voce escolheu um partida isolada!")
    print()
    partida()
  else:
    print("Voce escolheu um campeonato!")
    qtdePartidas = 1
    partidasJogador = 0
    partidasComputador = 0
    while qtdePartidas <= 3:
      print()
      print("**** Rodada", qtdePartidas, "****")
      print()
      resultado = partida()
      if resultado == 1:
        partidasJogador += 1
      else:
        partidasComputador += 1
      qtdePartidas += 1
    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você", partidasJogador, "X", partidasComputador, "Computador")

campeonato()
