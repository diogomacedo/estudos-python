def soma_lista(lista):
  qtdeDeItens = len(lista)
  if qtdeDeItens > 1:
    return soma_lista(lista[qtdeDeItens-1:]) + soma_lista(lista[:qtdeDeItens-1])
  return lista[qtdeDeItens-1]