def dimensoes(matriz):
  qtdeDeLinhas = 0
  qtdeDeColunas = 0
  if matriz is not None:
    qtdeDeLinhas = len(matriz)
    auxiliar = matriz[0]
    if auxiliar is not None:
      qtdeDeColunas = len(auxiliar)
  return f'{qtdeDeLinhas}X{qtdeDeColunas}'

def somar(m1, m2, dimensao):
  qtdeDeLinhas = int(dimensao[0])
  qtdeDeColunas = int(dimensao[2])
  m3 = []
  for x in range(0, qtdeDeLinhas):
    linha = []
    for y in range(0, qtdeDeColunas):
      soma = m1[x][y] + m2[x][y]
      linha.append(soma)
    m3.append(linha)
  return m3

def soma_matrizes(m1, m2):
  dimensaoM1 = dimensoes(m1)
  dimensaoM2 = dimensoes(m2)
  if dimensaoM1 == dimensaoM2:
    return somar(m1, m2, dimensaoM1)
  else:
    return False
