def buscaSequencial(lista, item):
  index = -1
  qtdeDeItens = len(lista)
  for i in range(qtdeDeItens):
    if lista[i] == item:
      index = i
      break
  return index

def busca(lista, elemento):
  index = buscaSequencial(lista, elemento)
  if index >= 0:
    return index
  return False