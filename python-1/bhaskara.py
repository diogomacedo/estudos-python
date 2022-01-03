import math

a=int(input("Informe o valor de A:"))
b=int(input("Informe o valor de B:"))
c=int(input("Informe o valor de C:"))

delta = (b ** 2) - ( 4 * a * c )

if delta < 0:
  print("esta equação não possui raízes reais")
else:
  raizDelta = math.sqrt(delta)
  x1 = (-b + raizDelta) / ( 2 * a )
  x2 = (-b - raizDelta) / ( 2 * a )
  if delta == 0:
    print("a raiz dupla desta equação é", x1)
  else:
    if x1 < x2:
      print("as raízes da equação são", x1, "e", x2)
    else:
      print("as raízes da equação são", x2, "e", x1)