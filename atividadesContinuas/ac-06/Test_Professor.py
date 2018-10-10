from Professor import Professor

def create_obj():
    obj = object.__new__(Professor)
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

def test_email():
    objTeste = create_obj()

    objTeste.email = "teste@teste"
    assert (objTeste.email == "teste@teste")
    objTeste.email = "maria@teste.com"
    assert (objTeste.email == "maria@teste.com")
    objTeste.email = "Jose@jose.com.br"
    assert (objTeste.email == "Jose@jose.com.br")

def test_ra():
    objTeste = create_obj()

    objTeste.ra = "123456"
    assert (objTeste.ra == "123456")
    objTeste.ra = "654321"
    assert (objTeste.ra == "654321")
    objTeste.ra = "6543255"
    assert (objTeste.ra == "6543255")

def test_celular():
    objTeste = create_obj()

    objTeste.celular = "12443456"
    assert (objTeste.celular == "12443456")
    objTeste.celular = "654321"
    assert (objTeste.celular == "654321")
    objTeste.celular = "6543255"
    assert (objTeste.celular == "6543255")

def test_lista_disciplinas_methods():
    objTeste = create_obj()

    objTeste.add_disciplina("Arg")

    assert (len(objTeste.disciplinas) > 0)
    assert (objTeste.disciplinas[0] == "Arg")
