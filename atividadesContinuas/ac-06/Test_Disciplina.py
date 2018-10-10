from Disciplina import Disciplina

def create_obj():
    obj = object.__new__(Disciplina)
    obj.__init__()
    return obj

    self.__nome = None
    self.__cargaHoraria = None
    self.__mensalidade = None
    self.__professor = Professor



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