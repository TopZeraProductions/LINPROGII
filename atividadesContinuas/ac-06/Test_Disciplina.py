"""

    João Vitor Paulino - 1801021 - paulino.joaovitor@yahoo.com.br
    Daniel Roberto - 1800479 - bruce-irom@hotmail.com
    Tiago Beneteli - 1800804 - tiagobeneteli@hotmail.com
    Ramon C. Pires - 1800260 - ramoncavpires@gmail.com

"""

from Disciplina import Disciplina

def create_obj():
    obj = object.__new__(Disciplina)
    obj.__init__()
    return obj

def test_name():
    objTeste = create_obj()

    objTeste.nome = "joao"
    assert (objTeste.nome == "joao")
    objTeste.nome = "maria"
    assert (objTeste.nome == "maria")
    objTeste.nome = "Jose"
    assert (objTeste.nome == "Jose")

def test_carga_horaria():
    objTeste = create_obj()

    objTeste.carga_horaria = 30
    assert (objTeste.carga_horaria == 30)

def test_mensalidade():
    objTeste = create_obj()

    objTeste.mensalidade = 200
    assert (objTeste.mensalidade == 200)

def test_retorna_valor_Hora_method():
    objTeste = create_obj()

    objTeste.carga_horaria = 30
    objTeste.mensalidade = 200
    teste = objTeste.retorna_valor_Hora()
    assert (teste == float(40.0))
