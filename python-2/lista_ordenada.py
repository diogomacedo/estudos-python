def ordenada(lista):
  qtdeDeItens = len(lista)
  listaOrdenada = True
  menorElemento = None
  for i in range(qtdeDeItens-1):
    menorElemento = lista[i]
    for y in range(i+1, qtdeDeItens):
      if menorElemento > lista[y]:
        listaOrdenada = False
        break
  return listaOrdenada