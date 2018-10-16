"""

    João Vitor Paulino - 1801021 - paulino.joaovitor@yahoo.com.br
    Daniel Roberto - 1800479 - bruce-irom@hotmail.com
    Tiago Beneteli - 1800804 - tiagobeneteli@hotmail.com
    Ramon C. Pires - 1800260 - ramoncavpires@gmail.com

"""

from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self):
        self.__desconto = int(0)
        super().__init__()

    @property
    def desconto(self):
        return self.__desconto

    @desconto.setter
    def desconto(self, value):
        self.__desconto = value

    def aumenta_desconto(self, value):
        self.desconto += int(value)

    def diminui_desconto(self, value):
        self.desconto -= int(value)