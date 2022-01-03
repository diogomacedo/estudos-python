def dimensoes(matriz):
  qtdeDeLinhas = 0
  qtdeDeColunas = 0
  if matriz is not None:
    qtdeDeLinhas = len(matriz)
    auxiliar = matriz[0]
    if auxiliar is not None:
      qtdeDeColunas = len(auxiliar)
  print(qtdeDeLinhas, 'X', qtdeDeColunas, sep='', end='')