def incomodam(n):
  if n > 1:
    return incomodam(1) + incomodam(n-1)
  elif n == 1:
    return 'incomodam '
  else:
    return ''

def elefantes(n, x=2):
  if n > 1 and n >= x:
    result = ''
    if x == 2:
      result = 'Um elefante incomoda muita gente' + '\n' + str(x) + ' elefantes ' + incomodam(x) + 'muito mais' + '\n'
    else:
      temp = x-1
      result = str(temp) + ' elefantes incomodam muita gente' +'\n' + str(x) + ' elefantes ' + incomodam(x) + 'muito mais' +'\n'
    return result + str(elefantes(n, x+1))
  else:
    return ''