class Aluno:

    def _init_(self):
        self.__nome = None
        self.__email = None
        self.__ra = None
        self.__celular = None
        self.__desconto = None
        self.__disciplina = None
        self.__listaDisciplina = []

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
        return self.__disciplina


    # métodos
    def add_disciplina(self, Disciplina):
        self.__listaDisciplina.append(Disciplina)

    def aumenta_desconto(self, value):
        self.__desconto = self.__desconto + value

    def diminui_desconto(self, value):
        self.__desconto = self.__desconto - value

        

