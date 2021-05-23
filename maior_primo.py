def ePrimo(numero):
  qtde = 0
  count = 1
  while count > 0 and count <= numero:
    if numero % count == 0:
      qtde+=1
    count+=1
    if qtde > 2:
      break
  return qtde == 2

def maior_primo(numero):
  if numero >= 2:
    count = 1
    lista = []
    while count <= numero:
      resultado = ePrimo(count)
      if resultado:
        lista.append(count)
      count+=1
    tamanho = len(lista)
    if tamanho > 0:
      return lista[tamanho-1]