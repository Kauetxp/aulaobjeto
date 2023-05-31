#Esse código faz a mesma coisa do exemplo 4, porém de outra forma

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def escreve(self):
        print(self.nome, self.idade)

class Estudante(Pessoa):
    def __init__(self, nome, idade):
        Pessoa.__init__(self,nome,idade)

x = Estudante("Jô",21)
x.escreve()

