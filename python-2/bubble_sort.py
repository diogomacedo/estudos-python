def bubble_sort(lista):
  qtdeDeItens = len(lista)
  for i in range(qtdeDeItens-1, 0, -1):
    for y in range(i):
      if lista[y] > lista[y+1]:
        lista[y], lista[y+1]=lista[y+1], lista[y]
        print(lista)
  return lista