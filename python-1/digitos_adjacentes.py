numeroStr=input("Digite um número inteiro:")
qtde=0
count=0
tamanho=len(numeroStr)
if tamanho == 0 or tamanho == 1:
  print("não")
else:
  while qtde == 2 or count < tamanho-1:
    valor=numeroStr[count]
    valorPosterior=numeroStr[count+1]
    if valor == valorPosterior:
      qtde+=1
      break
    count+=1
if qtde == 0:
  print("não")
else:
  print("sim")