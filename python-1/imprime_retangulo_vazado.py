largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
if altura > 0 and altura > 0:
  for i in range(1, altura+1):
    for y in range(1, largura+1):
      if i == 1 or i == altura:
        print("#", end="")
      elif y == 1 or y == largura:
        print("#", end="")
      else:
        print(" ", end="")
    print("")