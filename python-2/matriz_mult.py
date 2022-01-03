def dimensoes(matriz):
  qtdeDeLinhas = 0
  qtdeDeColunas = 0
  if matriz is not None:
    qtdeDeLinhas = len(matriz)
    auxiliar = matriz[0]
    if auxiliar is not None:
      qtdeDeColunas = len(auxiliar)
  return f'{qtdeDeLinhas}X{qtdeDeColunas}'


def sao_multiplicaveis(m1, m2):
  dimensaoM1 = dimensoes(m1)
  dimensaoM2 = dimensoes(m2)
  qtdeDeLinhasM1 = int(dimensaoM1[0])
  qtdeDeColunasM1 = int(dimensaoM1[2])
  qtdeDeLinhasM2 = int(dimensaoM2[0])
  qtdeDeColunasM2 = int(dimensaoM2[2])
  if qtdeDeColunasM1 == qtdeDeLinhasM2:
    return True
  else:
    return False