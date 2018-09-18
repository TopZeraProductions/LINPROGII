# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# F. dez
# dados dois inteiros a e b
# retorna True se um dos dois é 10 ou a soma é 10
def dez(a, b):
  if a == 10 or b == 10 or ( a + b ) ==10:
    return True
  return False

def test_ex06():
  print ('Dez')
  assert dez(9, 10) == True
  assert dez(9, 9) == False
  assert dez(1, 9) == True
  assert dez(10, 1) == True
  assert dez(10, 10) == True
  assert dez(8, 2) == True
  assert dez(8, 3) == False
  assert dez(10, 42) == True
  assert dez(12, -2) == True


