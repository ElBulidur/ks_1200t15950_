# MÓDULOS
# import random as rn
# from random import random, randint

# num1 = random() # Numero real aleatorio.

# num2 = randint(1, 10)

# print(num1)
# print(num2)

from calculadora import *


opt, numero1, numero2 = menu_inicial()


if opt == "+":
    soma(numero1, numero2)
elif opt == "-":
    subtracao(numero1, numero2)
elif opt == "/":
    divisao(numero1, numero2)
elif opt == "*":
    multiplicao(numero1, numero2)
else:
    print("Coloque um operador válido!")









