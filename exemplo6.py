#Mesma coisa do exemplo anterior porém de outra forma

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def escreve(self):
        print(self.nome, self.idade)

class Estudante(Pessoa):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)

        #Aqui eu estou adicionando um novo item a classe
        self.graduacao = 2024
x = Estudante("Jô",21)
x.escreve()
print(x.graduacao)

