#-----------------------------------#
# AC4 - Linguagem de Programação II
# João vitor paulino Ra: 1801021
#
# exercício AC-04 testes - objetivo do exercício é concertar os metodos para que os testes sejam executados corretamente
#-----------------------------------#

def dormir(dia_semana, feriado):
  if (feriado or not dia_semana):
      return True
  elif (dia_semana and not feriado):
      return False
  elif (not dia_semana and feriado):
      return True 
  else:
      return True    


def test_ex01():
  print ('Oba! Hoje vou ficar dormindo!')
  assert dormir(False, False) == True
  assert dormir(True, False)  == False
  assert dormir(False, True)  == True
  assert dormir(True, True)   == True


