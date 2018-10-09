#João Vitor Paulino - 1801021 - paulino.joaovitor@yahoo.com.br
#Daniel Roberto - 1800479 - bruce-irom@hotmail.com
#Tiago Beneteli - 1800804 - tiagobeneteli@hotmail.com
#Ramon C. Pires - 1800260 - ramoncavpires@gmail.com

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


x = Disciplina()
x.nome = "Teste"
x.cargaHoraria = 50
x.mensalidade = 150
x.professor.nome = "Tomás Ferreira"
x.professor.email = "tomas@gmail.com"
x.professor.ra = 1800299
x.professor.celular = 11988972762
x.professor.disciplinas = "Ciências"

print(x.nome)
print(x.cargaHoraria)
print(x.mensalidade)
print(x.professor.nome)
print(x.professor.email)
print(x.professor.ra)
print(x.professor.celular)
print(x.professor.disciplinas)
print("carga horaria : ", x.retorna_valorHora())


