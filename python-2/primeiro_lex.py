def primeiro_lex(lista):
  tamanho = len(lista)
  primeiroElemento = None
  for i in range(0, tamanho):
    if primeiroElemento == None:
      primeiroElemento = lista[i]
    else:
      if lista[i] < primeiroElemento:
        primeiroElemento = lista[i]
  return primeiroElemento