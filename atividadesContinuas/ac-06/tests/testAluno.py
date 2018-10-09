#João Vitor Paulino - 1801021 - paulino.joaovitor@yahoo.com.br
#Daniel Roberto - 1800479 - bruce-irom@hotmail.com
#Tiago Beneteli - 1800804 - tiagobeneteli@hotmail.com
#Ramon C. Pires - 1800260 - ramoncavpires@gmail.com

import sys
sys.path.append("../")
import Aluno

def createAluno():
    return Aluno

def test_name():
    objTeste = createAluno()
    objTeste.nome = "joao"
    return (objTeste.nome == "joao")

print(test_name())