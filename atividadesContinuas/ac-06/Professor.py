#João Vitor Paulino - 1801021 - paulino.joaovitor@yahoo.com.br
#Daniel Roberto - 1800479 - bruce-irom@hotmail.com
#Tiago Beneteli - 1800804 - tiagobeneteli@hotmail.com
#Ramon C. Pires - 1800260 - ramoncavpires@gmail.com

from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self):
        super().__init__()

x = Professor()
x.nome = "Tomás Ferreira"
x.email = "tomas@gmail.com"
x.ra = 1800299
x.celular = 11988972762
x.add_disciplinas = "Ciências"
print(x.nome)
print(x.email)
print(x.ra)
print(x.celular)
print(x.add_disciplinas)
