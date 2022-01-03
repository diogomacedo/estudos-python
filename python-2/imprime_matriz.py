def dimensoes(matriz):
  qtdeDeLinhas = 0
  qtdeDeColunas = 0
  if matriz is not None:
    qtdeDeLinhas = len(matriz)
    auxiliar = matriz[0]
    if auxiliar is not None:
      qtdeDeColunas = len(auxiliar)
  return f'{qtdeDeLinhas}X{qtdeDeColunas}'

def imprime_matriz(matriz):
  dimensao = dimensoes(matriz)
  qtdeDeLinhas = int(dimensao[0])
  qtdeDeColunas = int(dimensao[2])
  for x in range(0, qtdeDeLinhas):
    if qtdeDeColunas > 0:
      for y in range(0, qtdeDeColunas):
        print(matriz[x][y], end='')
        if y != qtdeDeColunas-1:
          print(' ', end='')
      print()
    else:
      print(matriz[x])