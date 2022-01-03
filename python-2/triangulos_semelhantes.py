import math

class Triangulo:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
  def perimetro(self):
    return self.a + self.b + self.c
  def tipo_lado(self):
    if self.a == self.b and self.b == self.c:
      return 'equilátero'
    if (self.a == self.b and self.b != self.c) or (self.a == self.c and self.a != self.b) or (self.b == self.c and self.b != self.a):
      return 'isósceles'
    else:
      return 'escaleno'
  def retangulo(self):
    quadradoA = self.a ** 2
    quadradoB = self.b ** 2
    quadradoC = self.c ** 2
    if self.a == math.sqrt( quadradoB + quadradoC ) or self.b == math.sqrt( quadradoA + quadradoC ) or self.c == math.sqrt( quadradoA + quadradoB ):
      return True
    else:
      return False
  def calcularRazao(self, triangulo):
    lista = [triangulo.a, triangulo.b, triangulo.c]
    lista.sort()
    razaoAB = lista[0] / lista[1]
    razaoBC = lista[1] / lista[2]
    razaoAC = lista[0] /lista[2]
    return [razaoAB, razaoBC,razaoAC]
  def semelhantes(self, triangulo):
    razaoSelf = self.calcularRazao(self)
    razaoTriangulo = self.calcularRazao(triangulo)
    if razaoSelf[0] == razaoTriangulo[0] and razaoSelf[1] == razaoTriangulo[1] and razaoSelf[2] == razaoTriangulo[2]:
      return True
    else:
      return False