def eVogal(letra):
  letraAux = letra.lower()
  if letraAux == 'a' or letraAux == 'e' or letraAux == 'i' or letraAux == 'o' or letraAux == 'u':
    return True
  return False

def contarVogais(frase):
  fraseAux = frase.replace(" ", "")
  qtde = 0
  for i in fraseAux:
    if eVogal(i):
      qtde += 1
  return qtde

def contarConsoantes(frase):
  fraseAux = frase.replace(" ", "")
  qtde = 0
  for i in fraseAux:
    if not eVogal(i):
      qtde += 1
  return qtde

def conta_letras(frase, contar="vogais"):
  if contar == "consoantes":
    return contarConsoantes(frase)
  return contarVogais(frase)