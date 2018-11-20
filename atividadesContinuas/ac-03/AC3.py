#-----------------------------------#
# AC1 - Linguagem de Programação II
# João vitor paulino Ra: 1801021
#
#  exercício AC-03 encapsulamento simples (get, set)
#-----------------------------------#

class Pessoa:
    def _init_ (self):
        self.__nome = ""
        self.__idade = 0
        self.__cpf = 0
        self.__profissao = ""

    def setNome (self, arg):
        self.__nome = arg

    def setCpf (self, arg):
        self.__cpf = arg

    def setIdade (self, arg):
        self.__idade = arg

    def setProfissao (self, arg):
        self.__profissao = arg

    def getNome (self):
        return self.__nome

    def getIdade (self):
        return self.__idade
    
    def getCpf (self):
        return self.__cpf

    def getProfissao (self):
        return self.__profissao



nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))
cpf = int(input("Digite seu cpf: "))
profissao = input("Digite sua profissão: ")

pessoa = Pessoa()

pessoa.setNome(nome)
pessoa.setIdade(idade)
pessoa.setCpf(cpf)
pessoa.setProfissao(profissao)

print ("Nome: ",pessoa.getNome())
print ("Idade ",pessoa.getIdade())
print ("Cpf: ",pessoa.getCpf())
print ("Profissão: ",pessoa.getProfissao())
