import math

x1=int(input("Informe a coordenada x do ponto 1:"))
y1=int(input("Informe a coordenada y do ponto 1:"))

x2=int(input("Informe a coordenada x do ponto 2:"))
y2=int(input("Informe a coordenada y do ponto 2:"))

resultadoSubtracaoXs = x1 - x2
resultadoSubtracaoYs = y1 - y2

resultadoSomaQuadradoXsYs = (resultadoSubtracaoXs ** 2) + (resultadoSubtracaoYs ** 2)

raiz = math.sqrt(resultadoSomaQuadradoXsYs)

resultado = "longe" if raiz >= 10 else "perto"

print(resultado)