def ePrimo(n):
  if n == 1 or n == 2:
    return True
  else:
    qtdeDivisores = 0
    count = 2
    while count <= n:
      if n % count == 0:
        qtdeDivisores += 1
      if qtdeDivisores > 2:
        break
      count += 1
    return qtdeDivisores < 2


def n_primos(n):
  qtde = 0
  if n >= 2:
    for i in range(2, n+1):
      if ePrimo(i):
        qtde += 1
  return qtde