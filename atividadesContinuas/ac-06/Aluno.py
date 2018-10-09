#João Vitor Paulino - 1801021 - paulino.joaovitor@yahoo.com.br
#Daniel Roberto - 1800479 - bruce-irom@hotmail.com
#Tiago Beneteli - 1800804 - tiagobeneteli@hotmail.com
#Ramon C. Pires - 1800260 - ramoncavpires@gmail.com

from Pessoa import Pessoa
from Disciplina import Disciplina

class Aluno(Pessoa):
    def __init__(self):
        self.__desconto = None
        super().__init__()

    def aumenta_desconto(self, value):
        self.__desconto = self.__desconto + value

    def diminui_desconto(self, value):
        self.__desconto = self.__desconto - value



#Setor de testes
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

for Disciplina in joao.disciplinas:
    print("> ", Disciplina.nome)