"""

    João Vitor Paulino - 1801021 - paulino.joaovitor@yahoo.com.br
    Daniel Roberto - 1800479 - bruce-irom@hotmail.com
    Tiago Beneteli - 1800804 - tiagobeneteli@hotmail.com
    Ramon C. Pires - 1800260 - ramoncavpires@gmail.com

"""

class Pessoa:
    def __init__(self):
        self.__nome = None
        self.__email = None
        self.__ra = None
        self.__celular = None
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

    # metodos
    def add_disciplina(self, Disciplina):
        self.__lista_disciplinas.append(Disciplina)