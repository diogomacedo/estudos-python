def insertion_sort(lista):
  qtdeDeItens = len(lista)
  for i in range(1, qtdeDeItens):
    posicao = i
    itemAtual = lista[i]
    while posicao > 0 and lista[posicao-1] > itemAtual:
      lista[posicao] = lista[posicao-1]
      posicao = posicao-1
    lista[posicao] = itemAtual
  return lista