def maior_elemento(lista):
  maiorElemento = None
  for i in lista:
    if maiorElemento == None or maiorElemento < i:
      maiorElemento = i
  return maiorElemento