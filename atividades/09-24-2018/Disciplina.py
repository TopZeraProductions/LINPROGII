import Professor

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

    @property
    def retornaValorHora(self, value):
        return self.__value

x = Disciplina()
x.nome = "Teste"
x.cargaHoraria = "50 horas"
x.mensalidade = "R$ 150,00"
x.professor = Professor()

print(x.nome)
print(x.cargaHoraria)
print(x.mensalidade)
print(x.professor.nome)

