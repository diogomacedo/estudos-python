numeroStr=input("Digite um número inteiro:")
tamanho=len(numeroStr)
count=0
soma=0
while tamanho > 0:
  valorStr=numeroStr[count]
  valorInt=int(valorStr)
  soma+=valorInt
  count+=1
  tamanho-=1
print(soma)