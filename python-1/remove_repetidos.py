def existe(item, lista):
  result = False
  for i in lista:
    if i == item:
      result = True
      break
  return result

def remove_repetidos(lista):
  listaOrdenada = sorted(lista)
  print(lista)
  print(listaOrdenada)
  tamanhoTotal = len(listaOrdenada)
  contador = 0
  result = []
  for i in listaOrdenada:
    if not existe(i, result):
      result.append(i)
  return result