from Aluno import Aluno

def createAluno():
    objAluno = object.__new__(Aluno)
    objAluno.__init__()
    return objAluno

def test_name():
    objTeste = createAluno()

    objTeste.nome = "joao"
    assert (objTeste.nome == "joao")
    objTeste.nome = "maria"
    assert (objTeste.nome == "maria")
    objTeste.nome = "Jose"
    assert (objTeste.nome == "Jose")

def test_email():
    objTeste = createAluno()

    objTeste.email = "teste@teste"
    assert (objTeste.email == "teste@teste")
    objTeste.email = "maria@teste.com"
    assert (objTeste.email == "maria@teste.com")
    objTeste.email = "Jose@jose.com.br"
    assert (objTeste.email == "Jose@jose.com.br")

def test_ra():
    objTeste = createAluno()

    objTeste.ra = "123456"
    assert (objTeste.ra == "123456")
    objTeste.ra = "654321"
    assert (objTeste.ra == "654321")
    objTeste.ra = "6543255"
    assert (objTeste.ra == "6543255")

def test_celular():
    objTeste = createAluno()

    objTeste.celular = "12443456"
    assert (objTeste.celular == "12443456")
    objTeste.celular = "654321"
    assert (objTeste.celular == "654321")
    objTeste.celular = "6543255"
    assert (objTeste.celular == "6543255")

def test_desconto_methods():
    objTeste = createAluno()
    objTeste.desconto = 5

    objTeste.aumenta_desconto(5)
    assert(objTeste.desconto == 10)

    objTeste.diminui_desconto(5)
    assert(objTeste.desconto == 5)


def test_lista_disciplinas_methods():
    objTeste = createAluno()

    objTeste.add_disciplina("Arg")

    assert (len(objTeste.disciplinas) > 0)
    assert (objTeste.disciplinas[0] == "Arg")
