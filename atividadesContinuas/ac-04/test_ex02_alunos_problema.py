#-----------------------------------#
# AC4 - Linguagem de Programação II
# João vitor paulino Ra: 1801021
#
# exercício AC-04 testes - objetivo do exercício é concertar os metodos para que os testes sejam executados corretamente
#-----------------------------------#

def alunos_problema(a_sorri, b_sorri):
  if a_sorri == b_sorri:
    return True
  else:
    return False


def test_ex02():
  print ('Alunos problema')
  assert alunos_problema(True, True)    == True
  assert alunos_problema(False, False)  == True
  assert alunos_problema(True, False)   == False
  assert alunos_problema(False, True)   == False

