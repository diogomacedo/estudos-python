import math

def valorRepetido(a, b):
  repetido = False
  for i in a:
    if i == b:
      repetido = True
  return repetido

def obterSoma(lista):
  soma = 0
  for i in lista:
    soma += i
  return soma

def hipotenusaValida(hipotenusa, a, b):
  calculo = math.sqrt( (a ** 2) + (b ** 2) )
  if hipotenusa == calculo:
    return True
  return False

def soma_hipotenusas(n):
  lista = []
  inicio = 1
  fim = n+1
  for hipotenusa in range(1, fim):
    for i in range(inicio, fim):
      for y in range(inicio, fim):
        if hipotenusaValida(hipotenusa, i, y) and not valorRepetido(lista, hipotenusa):
          lista.append(hipotenusa)
  soma = obterSoma(lista)
  return soma
