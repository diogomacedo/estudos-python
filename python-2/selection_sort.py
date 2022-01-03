def ordena(lista):
  qtdeDeItens = len(lista)
  for i in range(qtdeDeItens-1):
    indiceMenorElemento = i
    for y in range(i+1, qtdeDeItens):
      if lista[indiceMenorElemento] > lista[y]:
        indiceMenorElemento = y
    lista[i], lista[indiceMenorElemento] = lista[indiceMenorElemento], lista[i]
  return lista