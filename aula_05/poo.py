

# ABSTRAÇÃO => OBJETO => METODOS E ATRIBUTOS(PROPRIEDADES)

# ABSTRAÇÃO
class Copo: 
    def __init__(self, tipo):
        # Atributo
        self.tipo = tipo
        self.status = "vazio"
    
    # Metodo
    def encher_copo(self, porcentagem):
        self.status = f"Cheio {porcentagem}%"


# OBJETO
copo_americano = Copo("Americano") #stanciamento
taca = Copo("taca")

# print(Copo)
# print(copo_americano)
print(copo_americano.status) # vazio
print(taca.status)

taca.encher_copo(80)
copo_americano.encher_copo(30)

print(taca.status) #Cheio 80%
print(copo_americano.status) #Cheio 30%
