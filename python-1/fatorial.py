def fatorial(numero):
  if (numero > 0):
    return fatorial(numero-1) * numero
  else:
    return 1

numero=int(input("Digite o valor de n:"))
resultado=fatorial(numero)
print(resultado)