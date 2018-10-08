#João Vitor Paulino - 1801021 - paulino.joaovitor@yahoo.com.br
#Daniel Roberto - 1800479 - bruce-irom@hotmail.com
#Tiago Beneteli - 1800804 - tiagobeneteli@hotmail.com
#Ramon C. Pires - 1800260 - ramoncavpires@gmail.com

from Disciplina import Disciplina
class Aluno:

    def __init__(self):
        self.__nome = None
        self.__email = None
        self.__ra = None
        self.__celular = None
        self.__desconto = None
        self.__lista_disciplinas = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, arg):
        self.__nome = arg

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, arg):
        self.__email = arg

    @property
    def ra(self):
        return self.__ra

    @ra.setter
    def ra(self, arg):
        self.__ra = arg

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, arg):
        self.__celular = arg

    @property
    def desconto(self):
        return self.__desconto

    @desconto.setter
    def desconto(self, arg):
        self.__desconto = arg

    @property
    def disciplinas(self):
        return self.__lista_disciplinas

    # métodos
    def add_disciplina(self, Disciplina):
        self.__lista_disciplinas.append(Disciplina)

    def aumenta_desconto(self, value):
        self.__desconto = self.__desconto + value

    def diminui_desconto(self, value):
        self.__desconto = self.__desconto - value


joao = Aluno()

joao.nome = "Joao"
joao.email = "joao@yahoo.com"
joao.ra = "1111111"
joao.celular = "1111111"
joao.desconto = 1

Disc1 = Disciplina()
Disc1.nome = "História"

Disc2 = Disciplina()
Disc2.nome = "Matemática"

joao.add_disciplina(Disc1)
joao.add_disciplina(Disc2)

print(joao.nome)
print(joao.email)
print(joao.ra)
print(joao.celular)
print(joao.desconto)

for disciplina in joao.disciplinas:
    print("> ", disciplina.nome)