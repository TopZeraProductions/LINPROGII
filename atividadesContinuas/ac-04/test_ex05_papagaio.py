#-----------------------------------#
# AC4 - Linguagem de Programação II
# João vitor paulino Ra: 1801021
#
# exercício AC-04 testes - objetivo do exercício é concertar os metodos para que os testes sejam executados corretamente
#-----------------------------------#

def papagaio(falando, hora):
  if hora < 7 or hora > 20:
    if falando:
      return True
    else:
      return False

  return False

def test_ex05():
  print ('Papagaio')
  assert papagaio(True, 6) == True
  assert papagaio(True, 7) == False
  assert papagaio(False, 6) == False
  assert papagaio(True, 21) == True
  assert papagaio(False, 21) == False
  assert papagaio(True, 23) == True
  assert papagaio(True, 20) == False

