class Triangulo:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
  def perimetro(self):
    return self.a + self.b + self.c
  def tipo_lado(self):
    count = 0
    if self.a == self.b:
      count += 1
    if self.a == self.c:
      count += 1
    if self.b == self.c:
      count += 1
    if count == 3:
      return 'equilátero'
    elif count == 2:
      return 'isósceles'
    else:
      return 'escaleno'