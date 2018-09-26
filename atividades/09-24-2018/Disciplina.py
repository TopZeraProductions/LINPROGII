import Professor

class Disciplina:
    def __init__(self):
        self.__nome = None
        self.__cargaHoraria = None
        self.__mensalidade = None
        self.__professor = Professor

    def set_nome(self, nome):
        self.__nome = nome

    def set_cargaHoraria(self, cargaHoraria):
        self.__cargaHoraria = cargaHoraria

    def set_mensalidade(self, mensalidade):
        self.__mensalidade = mensalidade

    def set_Professor(self, professor):
        self.__professor = Professor

    def get_nome(self):
        return self.__nome

    def get_cargaHoraria(self):
        return self.__cargaHoraria

    def get_mensalidade(self):
        return self.__mensalidade

    def get_Professor(self):
        return self.__Professor

    def retornaValorHora(self, value):
        return self.__value



