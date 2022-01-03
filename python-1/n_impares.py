numero=int(input("Digite o valor de n:"))
count=1
lista=[]
while len(lista) < numero:
  if count % 2 != 0:
    lista.append(count)
  count+=1
for x in lista:
  print(x)