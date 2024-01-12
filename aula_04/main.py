
import random as rd

#GERENCIADOR DE PACOTES => PIP
# import tqdm as tq
from tqdm import tqdm

# for _ in tqdm(range(1000000000), "Contando até 1.000.000.000 =>"):
#     pass

# for _ in range(5):
#     print("*")

# VIRTUAL ENV


# PROCEDURAL

num1 = 10
num2 = 12

print(num1 + num2)

# FUNCIONAL

def soma(num1, num2): print(num1 + num2)

soma(10, 12)

# PROGRAMAÇÃO ORIENTADA A OBJETO

class Soma:
    def imprimir(self, num1, num2):
        print(num1 + num2)


imprimir_soma = Soma()

imprimir_soma.imprimir(10, 12)






