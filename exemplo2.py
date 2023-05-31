#Aqui eu crio a classe e utilizo a função __init__ para definir nome e idade
class Pessoa:
    def __init__(self,name,age):
        self.name = name
        self.age = age

nome1 = Pessoa("Joaquina",99)
nome2 = Pessoa("Camila",18)

print(nome1.name, nome1.age)
print(nome2.name, nome2.age)
