import random

def lista_grande(n):
  lista = []
  for i in range(n):
    numero = random.randrange(1000)
    lista.append(numero)
  return lista