def fizzbuzz(numero):
  if numero % 3 == 0 and numero % 5 != 0:
    return "Fizz"
  else:
    if numero % 3 != 0 and numero % 5 == 0:
      return "Buzz"
    else:
      if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
      else:
        return numero