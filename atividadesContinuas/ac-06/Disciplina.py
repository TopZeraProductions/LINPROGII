from Professor import Professor

class Disciplina:

    def __init__(self):
        self.__nome = None
        self.__cargaHoraria = None
        self.__mensalidade = None
        self.__professor = Professor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cargaHoraria(self):
        return self.__cargaHoraria

    @cargaHoraria.setter
    def cargaHoraria(self, cargaHoraria):
        self.__cargaHoraria = cargaHoraria

    @property
    def mensalidade(self):
        return self.__mensalidade

    @mensalidade.setter
    def mensalidade(self, mensalidade):
        self.__mensalidade = mensalidade

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, professor):
        self.__professor = professor

    def retorna_valorHora(self):
        return (float(self.__mensalidade) * 6 )/ float(self.__cargaHoraria)
