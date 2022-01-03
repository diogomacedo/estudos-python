def maiusculas(frase):
  lista = ''
  caracteresMaiusculos = []
  for i in range(65, 91):
    caracteresMaiusculos.append(chr(i))
  for i in frase:
    for x in caracteresMaiusculos:
      if i == x:
        lista = lista + i
  return lista