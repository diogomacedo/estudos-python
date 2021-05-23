numero=int(input("Digite um número inteiro:"))
count=1
qtde=0
while count > 0 and count <= numero:
  if numero % count == 0:
    qtde+=1
  count+=1
  if qtde > 2:
    break
if qtde == 2:
  print("primo")
else:
  print("não primo")