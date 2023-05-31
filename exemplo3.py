class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def escreveNome(abc):
        print("Olá, meu nome é",abc.nome,"!")

nome1 = Pessoa("Camila",19)
nome1.escreveNome()

#Aqui eu vou alterar uma variável

nome1.idade = 18
print("Desculpe, a idade correta é",nome1.idade)

