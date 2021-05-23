numero=int(input("Por favor, informe um número:"))
resultado="FizzBuzz" if numero % 3 == 0 and numero % 5 == 0 else str(numero)
print(resultado)