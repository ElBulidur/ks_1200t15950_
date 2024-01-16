class Automovel:

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca



automovel1 = Automovel()

automovel1.marca = "Gol"

print(automovel1.marca)

