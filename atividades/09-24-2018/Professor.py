class Professor:

    def __init__(self):
        self.__email = None
        self.__nome = None
        self.__ra = None
        self.__celular = None
        self.__listaDisciplina = []

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_ra(self, ra):
        self.__ra = ra

    def get_ra(self):
        return self.__ra

    def set_celular(self, celular):
        self.__celular = celular

    def get_celular(self):
        return self.__celular

    def add_disciplinas(self, discName):
        self.__listaDisciplina.append(discName)

    def get_disciplinas(self):
        return self.__listaDisciplina




