class Pessoa:
    def _init_ (self,nome,cpf,idade,profissao):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.idade = idade
        self.profissao =profissao

    def setNome (self,nome):
        self.nome = nome

    def setCpf (self,cpf):
        self.cpf = cpf

    def setIdade (self,idade):
        self.idade = idade

    def setProfissao (self,profissao):
        self.profissao = profissao

    def getNome (self, idade):
        return self.nome

    def getIdade (self, idade):
        return self.idade
    
    def getCpf (self, cpf):
        return self.cpf

    def getProfissao (self, profissao):
        return self.profissao




nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))
cpf = int(input("Digite seu cpf: "))
profissao = input("Digite sua profissão: ")  

pessoa.setNome(nome)
pessoa.setIdade(idade)
pessoa.setCpf(cpf)
pessoa.setProfissao(profissao)


pessoa = Pessoa ("","","","")

print ("Nome: ",pessoa.getNome())
print ("Idade ",pessoa.getIdade())
print ("Cpf: ",pessoa.getCpf())
print ("Profissão: ",pessoa.getProfissao())
