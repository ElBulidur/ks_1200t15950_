

class Pessoa():
    def __init__(self):
        self.nome = input("Coloque o nome: ")
        self.idade = input("Coloque a idade: ")
        self.peso = input("Coloque o peso: ")
        self.altura = input("Coloque a altura: ")
        
        self.apelido = None

    def criar_apelido(self, apelido):
        
        self.apelido = apelido



pessoa1 = Pessoa()

# pessoa1.criar_apelido("Zé Leitão")

if pessoa1.apelido:
    print(f"O apelido do {pessoa1.nome} é {pessoa1.apelido}")
else:
    print(f"O {pessoa1.nome} não tem apelido!")


# print(f"O {pessoa1.nome}, tem a idade de {pessoa1.idade} anos, peso de {pessoa1.peso}kl e altura de {pessoa1.altura}")