def removeEspacosEmBranco(palavra):
  while palavra.find(' ') > -1:
    palavra = palavra.strip()
  palavra = palavra.lower()
  return palavra

def menor_nome(nomes):
  menorNome = None
  for nome in nomes:
    nomeAux = removeEspacosEmBranco(nome)
    if menorNome == None or len(menorNome) > len(nomeAux):
      menorNome = nomeAux
  menorNome=menorNome.capitalize()
  return menorNome