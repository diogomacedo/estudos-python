def encontra_impares(lista):
  qtdeDeItens = len(lista)
  if qtdeDeItens > 1:
    listaItem = [ lista.pop(qtdeDeItens-1) ]
    listaTemp = []
    listaTemp.extend( encontra_impares(lista) )
    listaTemp.extend( encontra_impares(listaItem) )
    return listaTemp
  else:
    if lista[0] % 2 != 0:
      return lista
    return []