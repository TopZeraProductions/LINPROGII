# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# E. papagaio
# temos um papagaio que fala alto
# hora é um parâmetro entre 0 e 23
# temos problemas se o papagaio estiver falando
# antes da 7 ou depois das 20
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

