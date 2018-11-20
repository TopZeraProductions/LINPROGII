#-----------------------------------#
# AC4 - Linguagem de Programação II
# João vitor paulino Ra: 1801021
#
# exercício AC-04 testes - objetivo do exercício é concertar os metodos para que os testes sejam executados corretamente
#-----------------------------------#
def soma_dobro(a, b):
  if a == b:
    return 2 * (a + b )

  else:
    return a + b

def test_ex03():
  print ('Soma dobro')
  assert soma_dobro(1, 2)  == 3
  assert soma_dobro(3, 2)  == 5
  assert soma_dobro(2, 2)  == 8
  assert soma_dobro(-1, 0) == -1
  assert soma_dobro(0, 0)  == 0
  assert soma_dobro(0, 1)  == 1

