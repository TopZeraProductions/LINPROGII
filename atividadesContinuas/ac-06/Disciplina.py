"""

    João Vitor Paulino - 1801021 - paulino.joaovitor@yahoo.com.br
    Daniel Roberto - 1800479 - bruce-irom@hotmail.com
    Tiago Beneteli - 1800804 - tiagobeneteli@hotmail.com
    Ramon C. Pires - 1800260 - ramoncavpires@gmail.com

"""

from Professor import Professor

class Disciplina:

    def __init__(self):
        self.__nome = None
        self.__carga_horaria = None
        self.__mensalidade = None
        self.__professor = Professor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, carga_horaria):
        self.__carga_horaria = carga_horaria

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
    def professor(self, Professor):
        self.__professor = Professor

    def retorna_valor_Hora(self):
        return (float(self.__mensalidade) * 6 )/ float(self.__carga_horaria)