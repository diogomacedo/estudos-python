lista = []
fim = False
while not fim:
  numero = int(input("Digite um número: "))
  if numero != 0:
    lista.append(numero)
  else:
    fim = True
tamanho = len(lista)
for i in range(tamanho-1, -1, -1):
  print(lista[i])