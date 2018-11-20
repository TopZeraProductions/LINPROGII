#-----------------------------------#
# AC4 - Linguagem de Programação II
# João vitor paulino Ra: 1801021
#
# exercício AC-04 testes - objetivo do exercício é concertar os metodos para que os testes sejam executados corretamente
#-----------------------------------#

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


