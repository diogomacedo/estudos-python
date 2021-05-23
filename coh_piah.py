import re

class Palavra:
  def __init__(self, valor):
    self.valor = valor
    self.qtde = 1
  def registrarOcorrencia(self):
    self.qtde = self.qtde + 1

class Similaridade:
  def __init__(self):
    self.qtdeTotalDePalavras = 0
    self.palavras = []
    self.palavrasDiferentes = []
  def adicionarPalavra(self, palavra):
    qtdeLimite = len(self.palavras)
    if qtdeLimite > 0:
      achou = False
      posicao = 0
      while not achou and posicao < qtdeLimite:
        item = self.palavras[posicao];
        if item.valor == palavra:
          item.registrarOcorrencia()
          achou = True
        else:
          posicao = posicao + 1
      if not achou:
        novaPalavra = Palavra(palavra)
        self.palavras.append(novaPalavra)
    else:
      novaPalavra = Palavra(palavra)
      self.palavras.append(novaPalavra)
    if palavra not in self.palavrasDiferentes:
      self.palavrasDiferentes.append(palavra)
    self.qtdeTotalDePalavras = self.qtdeTotalDePalavras + 1
  def obterQtdeDePalavrasUnicas(self):
    qtde = 0
    for i in self.palavras:
      if i.qtde == 1:
        qtde = qtde + 1
    return qtde

def calcularTamanhoMedioDeSentencas(sentencas):
  qtdeTotalDeSentencas = 0
  qtdeTotalDeCaracteresDasSentencas = 0
  for sentenca in sentencas:
#    sentencaTratada = sentenca.strip()
    qtdeTotalDeSentencas = qtdeTotalDeSentencas + 1
    qtdeTotalDeCaracteresDasSentencas = qtdeTotalDeCaracteresDasSentencas + len(sentenca)
  tamanhoMedioDasSentencas = qtdeTotalDeCaracteresDasSentencas / qtdeTotalDeSentencas
  return tamanhoMedioDasSentencas

def calcularComplexidadeMediaDeSentencas(sentencas):
  qtdeDeSentencas = len(sentencas)
  qtdeTotalDeFrasesDasSentencas = 0
  for sentenca in sentencas:
    sentencaTratada = sentenca.strip()
    frases = separa_frases(sentencaTratada)
    qtdeTotalDeFrasesDasSentencas = qtdeTotalDeFrasesDasSentencas + len(frases)
  complexidade = qtdeTotalDeFrasesDasSentencas / qtdeDeSentencas
  return complexidade

def calcularTamanhoMedioDeFrases(sentencas):
  qtdeTotalDeFrasesDasSentencas = 0
  qtdeTotalDeCaracteresDasFrases = 0
  for sentenca in sentencas:
    #sentencaTratada = sentenca.strip()
    frases = separa_frases(sentenca)
    qtdeTotalDeFrasesDasSentencas = qtdeTotalDeFrasesDasSentencas + len(frases)
    for frase in frases:
      #fraseTratada = frase.strip()
      qtdeTotalDeCaracteresDasFrases = qtdeTotalDeCaracteresDasFrases + len(frase)
  tamanhoMedioDasFrases = qtdeTotalDeCaracteresDasFrases / qtdeTotalDeFrasesDasSentencas
  return tamanhoMedioDasFrases

def calcularTamanhoMedioDePalavras(sentencas):
  qtdeTotalDePalavras = 0
  qtdeTotalDeCaracteresDasPalavras = 0
  for sentenca in sentencas:
    sentencaTratada = sentenca.strip()
    frases = separa_frases(sentencaTratada)
    for frase in frases:
      fraseTratada = frase.strip()
      palavras = separa_palavras(fraseTratada)
      for palavra in palavras:
        palavraTratada = palavra.strip()
        qtdeTotalDePalavras = qtdeTotalDePalavras + 1
        qtdeTotalDeCaracteresDasPalavras = qtdeTotalDeCaracteresDasPalavras + len(palavraTratada)
  tamanhoMedioDePalavras = qtdeTotalDeCaracteresDasPalavras / qtdeTotalDePalavras
  return tamanhoMedioDePalavras

def calcularRelacaoTypeToken(sentencas):
  qtdeTotalDePalavras = 0
  palavrasDiferentes = []
  for sentenca in sentencas:
    sentencaTratada = sentenca.strip()
    frases = separa_frases(sentencaTratada)
    for frase in frases:
      fraseTratada = frase.strip()
      palavras = separa_palavras(fraseTratada)
      for palavra in palavras:
        palavraTratada = palavra.strip()
        palavraTratada = palavraTratada.lower()
        qtdeTotalDePalavras = qtdeTotalDePalavras + 1
        if palavraTratada not in palavrasDiferentes:
          palavrasDiferentes.append(palavraTratada)
  relacaoTypeToken = len(palavrasDiferentes) / qtdeTotalDePalavras
  return relacaoTypeToken

def calcularRazaoHapaxLegomana(sentencas):
  similaridade = Similaridade()
  for sentenca in sentencas:
    sentencaTratada = sentenca.strip()
    frases = separa_frases(sentencaTratada)
    for frase in frases:
      fraseTratada = frase.strip()
      palavras = separa_palavras(fraseTratada)
      for palavra in palavras:
        palavraTratada = palavra.strip()
        palavraTratada = palavraTratada.lower()
        similaridade.adicionarPalavra(palavraTratada)
  qtdeTotalDePalavras = similaridade.qtdeTotalDePalavras
  qtdePalavrasUnicas = similaridade.obterQtdeDePalavrasUnicas()
  razaoHapaxLegomana = qtdePalavrasUnicas / qtdeTotalDePalavras
  return razaoHapaxLegomana

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    # Assinatura A
    wal_a = as_a[0]
    ttr_a = as_a[1]
    hlr_a = as_a[2]
    sal_a = as_a[3]
    sac_a = as_a[4]
    pal_a = as_a[5]
    # Assinatura B
    wal_b = as_b[0]
    ttr_b = as_b[1]
    hlr_b = as_b[2]
    sal_b = as_b[3]
    sac_b = as_b[4]
    pal_b = as_b[5]
    # Diferencas
    wal_diff = abs(wal_a - wal_b)
    ttr_diff = abs(ttr_a - ttr_b)
    hlr_diff = abs(hlr_a - hlr_b)
    sal_diff = abs(sal_a - sal_b)
    sac_diff = abs(sac_a - sac_b)
    pal_diff = abs(pal_a - pal_b)
    # Total
    somaDaDiff = wal_diff + ttr_diff + hlr_diff + sal_diff + sac_diff + pal_diff
    # Grau de similaridade
    grauDeSimilaridade = somaDaDiff / 6
    return grauDeSimilaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    # Tamanho médio das sentenças
    sal = calcularTamanhoMedioDeSentencas(sentencas)
    # Complexidade média das sentenças
    sac = calcularComplexidadeMediaDeSentencas(sentencas)
    # Tamanho médio de frase
    pal = calcularTamanhoMedioDeFrases(sentencas)
    # Tamanho médio de palavra
    wal = calcularTamanhoMedioDePalavras(sentencas)
    # Relação Type-Token
    ttr = calcularRelacaoTypeToken(sentencas)
    # Razão Hapax Legomana
    hlr = calcularRazaoHapaxLegomana(sentencas)
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    similaridades = []
    # Navegar / percorrer textos
    for texto in textos:
      # Obter assinatura do texto selecionado
      assinaturaTexto = calcula_assinatura(texto)
      # Obter grau de similaridade
      grauDeSimilaridade = compara_assinatura(ass_cp, assinaturaTexto)
      similaridades.append(grauDeSimilaridade)
    menorSimilaridade = min(similaridades)
    posicao = similaridades.index(menorSimilaridade)
    return posicao + 1
